#!/usr/bin/env python3
"""Generate a theme for every product major release that has none yet, and refuse duplicate themes.

  update.py --work DIR --samples VSCO_DIR   clone each product, generate missing themes into brand/assets/audio
  update.py --check                         exit 1 if two themes share every musical parameter

A major is vX.0.0, or v0.X.0 while a product is on 0.x; only majors newer than the product's latest theme
(or, for a product with none, its latest major) are generated. Its range starts at the last tag of the previous major
(or the first commit). Run by .github/workflows/themes.yml.
"""
import argparse, json, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIO = HERE.parent.parent / 'brand/assets/audio'
REPOS = {'control': 'AnixOps/anix-control', 'core': 'AnixOps/networkcore_anixops', 'agent': 'AnixOps/anix-agent',
         'net': 'AnixOps/anixops-net', 'ssh': 'AnixOps/EasySSH'}
TAG = re.compile(r'^v(\d+)\.(\d+)\.(\d+)$')
SKIP = {'stats', 'bars', 'major'}  # not heard: the key already carries the major


def major(v):
    return (v[0],) if v[0] else (0, v[1])


def fingerprint(meta):
    return json.dumps({k: v for k, v in meta.items() if k not in SKIP}, sort_keys=True)


def check():
    seen = {}
    for f in sorted(AUDIO.glob('*.json')):
        fp = fingerprint(json.loads(f.read_text()))
        if fp in seen:
            sys.exit(f'{f.name} has the same musical parameters as {seen[fp]}: change the generator or the range')
        seen[fp] = f.name
    print(f'{len(seen)} themes, all distinct')


def update(work, samples):
    have = {(m['product'], tuple(m['major'])) for m in (json.loads(f.read_text()) for f in AUDIO.glob('*.json'))}
    token = os.environ.get('THEME_REPO_TOKEN', '')
    auth = f'x-access-token:{token}@' if token else ''
    for product, repo in REPOS.items():
        path = Path(work) / product
        if not path.exists():
            subprocess.run(['git', 'clone', '-q', '--filter=blob:none', f'https://{auth}github.com/{repo}', str(path)], check=True)
        tags = sorted((tuple(map(int, m.groups())), t) for t in subprocess.run(
            ['git', '-C', str(path), 'tag'], capture_output=True, text=True, check=True).stdout.split() if (m := TAG.match(t)))
        firsts = [(i, v, tag) for i, (v, tag) in enumerate(tags) if not v[2] and not (v[0] and v[1])]  # first release of each major
        latest = max((mj for p, mj in have if p == product), default=None)
        for i, v, tag in firsts[-1:] if latest is None else [f for f in firsts if major(f[1]) > latest]:
            prev = [t for w, t in tags[:i] if major(w) != major(v)]
            frm = prev[-1] if prev else 'root'
            print(f'{product}: {frm}..{tag}', flush=True)
            subprocess.run([sys.executable, str(HERE / 'theme.py'), '--repo', str(path), '--from', frm, '--to', tag,
                            '--product', product, '--samples', samples, '--out', str(AUDIO)], check=True)
            have.add((product, major(v)))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true'); ap.add_argument('--work'); ap.add_argument('--samples')
    o = ap.parse_args()
    if not o.check: update(o.work, o.samples)
    check()
