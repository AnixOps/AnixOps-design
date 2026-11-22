#!/usr/bin/env python3
"""Version theme generator: a fixed motif per product, varied by the release's own git history.

The data sets the skeleton (mode, tempo, densities, form); the release commit hash picks only the details that
carry no meaning (progression, rhythm offsets, arpeggio order, voicing), so every major sounds different.
No randomness: the same release always gives the same piece. See brand/brand.md section 2.7.

Usage: theme.py --repo PATH --from TAG|root --to TAG --product control --samples VSCO_DIR [--out DIR]
Writes <product>-<to>.mp3 (needs ffmpeg), .mid and .json (the statistics and the derived parameters).
"""
import argparse, hashlib, itertools, json, math, re, subprocess, tempfile, wave
from pathlib import Path
import numpy as np
from sampler import Sampler

SR, TPB = 44100, 480  # sample rate, MIDI ticks per beat

# Product motifs: (scale degree, length in 16ths), two bars each. Degrees follow the mode, so the
# contour and rhythm stay recognisable in every key.
MOTIFS = {
    'control': [(0, 6), (4, 2), (3, 4), (4, 4), (7, 6), (6, 2), (4, 8)],                                 # rise a fifth, settle: a command
    'agent':   [(0, 2), (0, 2), (4, 4), (0, 2), (0, 2), (5, 4), (4, 4), (2, 4), (1, 8)],                 # repeated pulse: a heartbeat
    'core':    [(0, 2), (2, 2), (4, 2), (7, 2), (4, 2), (2, 2), (4, 4), (5, 2), (4, 2), (2, 4), (0, 8)],  # arpeggio: a loop
    'net':     [(0, 4), (7, 4), (6, 2), (4, 2), (5, 4), (9, 8), (7, 8)],                                 # wide leaps: a long route
    'ssh':     [(0, 2), (0, 2), (2, 2), (0, 2), (4, 4), (3, 2), (2, 2), (1, 4), (0, 12)],                # key taps: a terminal
}
# Fixed tempo per product tier: server side is steady and slow, clients medium, UI showcase fast.
TIER = {'control': 'server', 'core': 'server', 'agent': 'server', 'net': 'client', 'ssh': 'showcase'}
BPM = {'server': 86, 'client': 104, 'showcase': 126}
# Modes from dark to bright, picked by insertions / (insertions + deletions): a clean-up release is
# darker, an expansion brighter.
MODES = [('aeolian', [0, 2, 3, 5, 7, 8, 10]), ('dorian', [0, 2, 3, 5, 7, 9, 10]),
         ('mixolydian', [0, 2, 4, 5, 7, 9, 10]), ('ionian', [0, 2, 4, 5, 7, 9, 11]),
         ('lydian', [0, 2, 4, 6, 7, 9, 11])]
# Details picked by the release commit hash
PROGRESSIONS = [[0, 5, 3, 4], [0, 3, 5, 4], [0, 5, 1, 4], [0, 2, 5, 3], [0, 4, 5, 3], [5, 3, 0, 4], [0, 3, 1, 4], [3, 4, 2, 5]]
VOICINGS = [(2, 4, 6, 8), (4, 6, 8, 9), (2, 6, 8, 11)]  # chord tones above the root, in degrees; the root is the bass's
ARP_ORDERS = list(itertools.permutations((0, 4, 6, 8)))
NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()
GROUPS = {'backend': {'go', 'rs', 'py', 'c', 'h', 'sql'}, 'frontend': {'vue', 'js', 'ts', 'tsx', 'css', 'dart', 'html'},
          'config': {'json', 'yaml', 'yml', 'toml', 'nft', 'sh', 'conf'}}


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, check=True).stdout


def stats(repo, a, b):
    rng = f'{a}..{b}'
    subjects = git(repo, 'log', '--format=%s', rng).splitlines()
    types = {}
    for s in subjects:
        m = re.match(r'([a-z]+)', s)
        if m: types[m[1]] = types.get(m[1], 0) + 1
    ins = dele = 0
    lang = {k: 0 for k in [*GROUPS, 'other']}
    for line in git(repo, '-c', 'diff.renameLimit=0', 'diff', '--numstat', rng).splitlines():
        x, y, f = line.split('\t', 2)
        if x == '-': continue
        ins += int(x); dele += int(y)
        ext = f.rsplit('.', 1)[-1].lower() if '.' in f else ''
        lang[next((g for g, s in GROUPS.items() if ext in s), 'other')] += int(x) + int(y)
    t0, t1 = (int(git(repo, 'log', '-1', '--format=%ct', t)) for t in (a, b))
    commit = git(repo, 'rev-list', '-n1', b).strip()
    tot = sum(lang.values()) or 1
    return {'from': a, 'to': b, 'commit': commit, 'commits': len(subjects), 'insertions': ins, 'deletions': dele,
            'days': max(1, round((t1 - t0) / 86400)), 'types': types,
            'lang': {k: round(v / tot, 3) for k, v in lang.items()}}


def euclid(k, rot=0, n=16):
    """k hits spread as evenly as possible over n steps, rotated by rot."""
    return [((i + rot) * k) % n < k for i in range(n)]


def compose(st, product, major_key):
    grow = st['insertions'] / max(1, st['insertions'] + st['deletions'])
    mode_name, scale = MODES[min(4, int(grow * 5))]
    major = major_key[-1]
    tonic = 50 + (major * 7) % 12 - (12 if (major * 7) % 12 > 6 else 0)  # each major moves one step round the circle of fifths
    T, L, n = st['types'], st['lang'], max(1, st['commits'])
    feat, fix = T.get('feat', 0), T.get('fix', 0)
    tidy = T.get('refactor', 0) + T.get('chore', 0) + T.get('test', 0)
    arp_hits = min(12, 4 + round(st['commits'] / st['days'] * 0.8))  # commits per day → arpeggio density
    ornaments = min(6, round(feat / n * 10))                          # share of feat → ornaments in B
    kick = 2 + round(L['backend'] * 4)                                # backend share → kick
    hat = min(12, 4 + round(fix / n * 24))                            # share of fix → hi-hat
    bass_hits = 3 + round(L['config'] * 10)                           # config and ops share → bass groove
    invert = tidy > feat * 0.35                                       # tidy-up release → A' inverted, else reversed
    h = hashlib.sha256(st['commit'].encode()).digest()
    prog, voicing = PROGRESSIONS[h[0] % 8], VOICINGS[h[1] % 3]
    arp_rot, hat_rot, arp_order = h[2] % 16, h[3] % 16, ARP_ORDERS[h[4] % 24]

    def pitch(deg, octave=0):
        o, d = divmod(deg, 7)
        return tonic + 12 * (o + octave) + scale[d]

    motif = MOTIFS[product]
    var = []  # B: upper neighbour notes on the longest notes, then the whole line a third higher
    longest = sorted(range(len(motif)), key=lambda i: -motif[i][1])[:ornaments]
    for i, (d, ln) in enumerate(motif):
        var += [(d + 1, 2), (d, ln - 2)] if i in longest and ln >= 4 else [(d, ln)]
    var = [(d + 2, ln) for d, ln in var]
    mirror = [(-d + 4, ln) for d, ln in motif] if invert else motif[::-1]
    coda = [(d, ln * 2) for d, ln in motif[:3]] + [(0, 16)]

    full = {'pad', 'arp', 'bass', 'drums'}
    # The motif starts on beat one; drums enter in B, drop out in A', return, and the coda is strings only.
    sections = [('A', motif, {'pad', 'arp'}), ('B', var, full), ('A2', mirror, {'pad', 'bass'}),
                ('A', motif, full), ('coda', coda, {'pad'})]
    notes = {k: [] for k in ('lead', 'arp', 'pad', 'bass', 'drums')}  # (start16, len16, midi, velocity)

    def put(track, s, ln, m, v):  # deterministic feel: off-beat swing, small timing and velocity drift
        i = len(notes[track])
        s += 0.12 * (s % 2 == 1) + 0.04 * math.sin(i * 2.399)
        notes[track].append((s, ln, m, max(1, min(127, round(v * (1 + 0.08 * math.sin(i * 1.618)))))))

    t = 0
    for name, mel, parts in sections:
        bars = max(2, math.ceil(sum(ln for _, ln in mel) / 16))
        p = t
        for d, ln in mel:
            put('lead', p, ln, pitch(d, 1), 100 if p % 16 == 0 else 86 if p % 4 == 0 else 76); p += ln
        for b in range(bars):
            root = prog[(b + (name == 'B') * 2) % 4]
            s = t + b * 16
            for k in voicing:  # seventh and ninth chords as degrees, so the progression takes the colour of the mode
                notes['pad'].append((s, 16, pitch(root + k), 48))
            if 'arp' in parts:
                for i, on in enumerate(euclid(arp_hits, arp_rot)):
                    if on: put('arp', s + i, 1, pitch(root + arp_order[i % 4], 1), 64 - 12 * (i % 2))
            if 'bass' in parts:
                for i, on in enumerate(euclid(bass_hits)):
                    if on: put('bass', s + i, 2, pitch(root, -1), 92 - 10 * (i % 4 != 0))
            if 'drums' in parts:
                for i in range(16):
                    if euclid(kick)[i]: put('drums', s + i, 1, 36, 110)
                    if euclid(hat, hat_rot)[i]: put('drums', s + i, 1, 42, 70 + 20 * (i % 4 == 0))
                    if i in (4, 12): put('drums', s + i, 1, 39, 80)
                if b == 0: notes['drums'].append((s, 1, 49, 100))  # a cymbal where the drums come in
        t += bars * 16
    meta = {'product': product, 'key': f'{NOTE_NAMES[tonic % 12]} {mode_name}', 'tier': TIER[product],
            'bpm': BPM[TIER[product]], 'growth_ratio': round(grow, 3), 'arp_hits': arp_hits, 'ornaments': ornaments,
            'kick_hits': kick, 'hat_hits': hat, 'bass_hits': bass_hits, 'A2': 'inversion' if invert else 'retrograde',
            'progression': prog, 'voicing': voicing, 'arp_rotation': arp_rot, 'hat_rotation': hat_rot,
            'arp_order': arp_order, 'major': major_key, 'bars': t // 16, 'stats': st}
    return notes, meta


def write_midi(notes, bpm, path):
    def vlq(n):
        out = [n & 0x7F]
        while n > 0x7F: n >>= 7; out.insert(0, (n & 0x7F) | 0x80)
        return bytes(out)

    def track(events):
        events.sort(key=lambda e: (e[0], e[1][0] & 0xF0 == 0x90))  # note-off before note-on at the same tick
        data, last = b'', 0
        for tick, ev in events: data += vlq(tick - last) + bytes(ev); last = tick
        data += b'\x00\xff\x2f\x00'
        return b'MTrk' + len(data).to_bytes(4, 'big') + data

    us = round(60_000_000 / bpm)
    tracks = [track([(0, [0xFF, 0x51, 3, *us.to_bytes(3, 'big')])])]
    # General MIDI: piano, harp, string ensemble, contrabass, drums
    for ch, (name, prog) in enumerate([('lead', 0), ('arp', 46), ('pad', 48), ('bass', 43), ('drums', None)]):
        ch = 9 if name == 'drums' else ch
        ev = [] if prog is None else [(0, [0xC0 | ch, prog])]
        for s, ln, m, v in notes[name]:
            ev += [(round(s * TPB / 4), [0x90 | ch, m, v]), (round((s + ln) * TPB / 4), [0x80 | ch, m, 0])]
        tracks.append(track(ev))
    Path(path).write_bytes(b'MThd' + (6).to_bytes(4, 'big') + bytes([0, 1, 0, len(tracks), TPB >> 8, TPB & 0xFF]) + b''.join(tracks))


def render(notes, meta, smp):
    """Sampled piano, harp, strings and bass; synthesised drums; sidechain, ping-pong delay, stereo reverb."""
    step = 60 / meta['bpm'] / 4
    total = int((meta['bars'] * 16 * step + 4) * SR)
    dry, pump, dly, rev = (np.zeros((2, total)) for _ in range(4))  # direct / ducked by the kick / delay send / reverb send

    def env(n, a, r):
        e = np.ones(n); a, r = min(a, n), min(r, n)
        e[:a] = np.linspace(0, 1, a); e[n - r:] *= np.linspace(1, 0, r)
        return e

    def add(bus, start, sig, gain, pan=0.0, d=0.0, r=0.0):
        i = int(start * step * SR); sig = sig[..., :total - i] * gain
        th = (pan + 1) * math.pi / 4
        for c, g in enumerate((math.cos(th), math.sin(th))):
            x = g * (sig[c] if sig.ndim == 2 else sig)
            bus[c, i:i + len(x)] += x
            dly[c, i:i + len(x)] += d * x
            rev[c, i:i + len(x)] += r * x

    def noise(k, seed):  # deterministic noise
        return np.sin(np.arange(k) * 12.9898 + seed) * 43758.5453 % 1 * 2 - 1

    for j, (s, ln, m, v) in enumerate(notes['lead']):
        k = int((ln * step + 0.8) * SR)
        add(dry, s, smp('lead', m, k) * env(k, 1, int(0.4 * SR)), 0.42 * v / 127, 0.1 * math.sin(j * 0.7), d=0.15, r=0.4)
    for j, (s, ln, m, v) in enumerate(notes['arp']):
        k = int(1.5 * SR)
        add(pump, s, smp('arp', m, k) * env(k, 1, int(0.6 * SR)), 0.13 * v / 127, 0.4 if j % 2 else -0.4, d=0.3, r=0.4)
    for s, ln, m, v in notes['pad']:
        k = int((ln * step + 1.2) * SR)
        add(pump, s, smp('pad', m, k) * env(k, int(0.4 * SR), int(1.2 * SR)), 0.14 * v / 127, (m % 5 - 2) * 0.25, r=0.45)
    for s, ln, m, v in notes['bass']:
        k = int((ln * step + 0.6) * SR)
        add(pump, s, smp('bass', m, k) * env(k, 1, int(0.3 * SR)), 0.42 * v / 127, r=0.1)
    sc = np.ones(total)  # kick sidechain: strings, harp and bass breathe with the kick
    for j, (s, ln, m, v) in enumerate(notes['drums']):
        k = int((2.0 if m == 49 else 0.5) * SR); t = np.arange(k) / SR; nz = noise(k, m + j % 7)
        if m == 36:
            i = int(s * step * SR); w = min(k, total - i)
            sc[i:i + w] = np.minimum(sc[i:i + w], 1 - 0.45 * np.exp(-t[:w] * 9))
            add(dry, s, np.sin(2 * np.pi * (48 + 70 * np.exp(-t * 35)) * t) * np.exp(-t * 7), 0.28 * v / 127)
        elif m == 42:
            add(dry, s, np.diff(nz, prepend=0) * np.exp(-t * 70), 0.07 * v / 127, 0.35, r=0.1)
        elif m == 39:  # clap: three short noise bursts
            sig = sum(np.roll(nz * np.exp(-t * 40), int(o * SR)) for o in (0, 0.011, 0.023))
            add(dry, s, np.diff(sig, prepend=0), 0.10 * v / 127, -0.15, r=0.6)
        else:
            add(dry, s, np.diff(nz, prepend=0) * np.exp(-t * 2.2), 0.05 * v / 127, 0, r=0.4)
    mix = dry + pump * sc
    d, src = int(3 * step * SR), dly.sum(0)  # dotted-eighth delay, echoes alternate left and right
    for i in range(1, 6):
        mix[i % 2, d * i:] += 0.45 ** i * src[:total - d * i]
    # Stereo reverb: one decorrelated decaying-noise impulse response per side, low cut, 25 ms pre-delay
    k = int(3.2 * SR); t = np.arange(k) / SR; nfft = 1 << (total + k).bit_length()
    for c in range(2):
        ir = np.diff(noise(k, 7 + c * 31), prepend=0) * np.exp(-t * 2.2); ir[:int(0.025 * SR)] = 0
        mix[c] += 0.35 * np.fft.irfft(np.fft.rfft(rev[c], nfft) * np.fft.rfft(ir / np.abs(ir).sum() * 40, nfft), nfft)[:total]
    mix *= env(total, 1, int(3 * SR))
    return np.tanh(1.4 * mix / np.abs(mix).max()) / np.tanh(1.4) * 0.89  # soft limiter


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True); ap.add_argument('--from', dest='a', required=True)
    ap.add_argument('--to', dest='b', required=True); ap.add_argument('--product', choices=MOTIFS, required=True)
    ap.add_argument('--samples', required=True, help='VSCO-2-CE checkout'); ap.add_argument('--out', default='.')
    o = ap.parse_args()
    nums = [int(x) for x in re.findall(r'\d+', o.b)[:2]]
    major_key = nums[:1] if nums[0] else nums  # 0.x products use the minor version
    if o.a == 'root': o.a = git(o.repo, 'rev-list', '--max-parents=0', o.b).split()[-1]
    notes, meta = compose(stats(o.repo, o.a, o.b), o.product, major_key)
    stem = Path(o.out) / f'{o.product}-{o.b}'
    stem.parent.mkdir(parents=True, exist_ok=True)
    write_midi(notes, meta['bpm'], f'{stem}.mid')
    pcm = (render(notes, meta, Sampler(o.samples)).T * 32767).astype('<i2')
    with tempfile.NamedTemporaryFile(suffix='.wav') as tmp:
        with wave.open(tmp.name, 'wb') as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', tmp.name, '-b:a', '192k', f'{stem}.mp3'], check=True)
    Path(f'{stem}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in meta.items() if k != 'stats'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
