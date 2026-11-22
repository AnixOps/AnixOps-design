"""Sampler: plays the nearest recorded note, resampled to pitch.

Samples: VSCO 2 Community Edition (CC0), https://github.com/sgossner/VSCO-2-CE, not stored in this repository.
"""
import re, wave
from pathlib import Path
import numpy as np

PC = {n: i for i, n in enumerate('C C# D D# E F F# G G# A A# B'.split())}
# track → [(glob, octave offset)]: VSCO strings name middle C "C3", the harp names it "C4"
SETS = {
    'lead': 'piano',
    'arp': [('Strings/Harp/KSHarp_*.wav', 1)],
    'pad': [('Strings/Cello Section/susvib/*_v1_1.wav', 2), ('Strings/Viola Section/susvib/*_v1_1.wav', 2),
            ('Strings/Violin Section/susVib/*_v1.wav', 2)],
    'bass': [('Strings/Solo Contrabass/Pizz/*_v1_rr1.wav', 2)],
}


def read(path):
    w = wave.open(str(path)); sw, ch = w.getsampwidth(), w.getnchannels(); raw = w.readframes(w.getnframes())
    if sw == 3:
        a = np.frombuffer(raw, np.uint8).reshape(-1, 3).astype(np.int32)
        x = a[:, 0] | a[:, 1] << 8 | a[:, 2] << 16
        x = np.where(x >= 1 << 23, x - (1 << 24), x) / 2 ** 23
    else:
        x = np.frombuffer(raw, '<i2') / 32768
    x = x.reshape(-1, ch).T if ch == 2 else np.vstack([x, x])
    start = max(0, np.argmax(np.abs(x).max(0) > 0.02 * np.abs(x).max()) - 64)  # skip leading silence
    return x[:, start:] / np.abs(x).max()


class Sampler:
    def __init__(self, root):
        self.root, self.maps, self.cache = Path(root), {}, {}
        for track, spec in SETS.items():
            m = {}
            if spec == 'piano':  # the piano is numbered by its mapping chart
                chart = dict(l.split('=') for l in (self.root / 'Keys/Upright Piano/MappingChart.txt').read_text().split() if '=' in l and l[0].isdigit())
                for f in (self.root / 'Keys/Upright Piano').glob('Player_dyn2_rr1_*.wav'):
                    m[int(chart[f.stem[-3:]])] = f
            else:
                for pattern, off in spec:  # later sets win where ranges overlap: violins on top, cellos below
                    for f in self.root.glob(pattern):
                        n = re.search(r'_([A-G]#?)(-?\d)_?', f.name)
                        m[12 * (int(n[2]) + off) + PC[n[1]]] = f
            self.maps[track] = m

    def __contains__(self, track):
        return track in self.maps

    def __call__(self, track, midi, k):
        """(2, k) stereo: the nearest sample, resampled to the target pitch."""
        src = min(self.maps[track], key=lambda s: (abs(s - midi), s))
        f = self.maps[track][src]
        x = self.cache.get(f)
        if x is None: x = self.cache[f] = read(f)
        pos = np.arange(k) * 2 ** ((midi - src) / 12)
        return np.vstack([np.interp(pos, np.arange(x.shape[1]), c, right=0) for c in x])
