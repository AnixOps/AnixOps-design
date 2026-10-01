#!/usr/bin/env python3
"""Print the WCAG 2.x contrast table for the colour pairs in tokens/tokens.json.

Dependency free. Run from the repository root:

    python3 scripts/contrast.py            # Markdown table
    python3 scripts/contrast.py --check    # exit 1 if a pair misses its target
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))["color"]


def luminance(hex_colour):
    h = hex_colour.lstrip("#")
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def tok(theme, name):
    if name.startswith("#"):
        return name
    if name.startswith("brand."):
        return TOKENS["brand"][name[6:]]["$value"]
    return TOKENS[theme][name]["$value"]


# (foreground, background, target, use). Target 4.5 = body text, 3.0 = large
# text / UI graphics, 0 = informative only (brand moments, logo: exempt).
TEXT_BGS = ["bg", "bg-elevated", "bg-grouped"]
PAIRS = []
for theme in ("light", "dark"):
    for fg, target in [("label-1", 4.5), ("label-2", 4.5), ("label-3", 3.0), ("accent", 4.5),
                       ("success", 4.5), ("warning", 4.5), ("danger", 4.5)]:
        for bg in TEXT_BGS:
            PAIRS.append((theme, fg, bg, target))
    PAIRS += [
        (theme, "on-accent", "accent-fill", 4.5),
        (theme, "on-accent", "accent-fill-hover", 4.5),
        (theme, "on-danger", "danger-fill", 4.5),
        (theme, "accent-fill", "bg-elevated", 3.0),
    ]
    for i in range(1, 9):
        PAIRS.append((theme, f"chart-{i}", "bg-elevated", 3.0))
PAIRS += [
    ("light", "#FFFFFF", "accent", 4.5),
    ("dark", "#FFFFFF", "accent", 0),
    ("dark", "#000000", "accent", 0),
    ("light", "brand.gradient-start", "#FFFFFF", 0),
    ("light", "brand.gradient-end", "#FFFFFF", 0),
    ("light", "#FFFFFF", "brand.gradient-start", 0),
    ("light", "#FFFFFF", "brand.gradient-end", 0),
    ("light", "brand.purple", "#FFFFFF", 3.0),
    ("light", "brand.amber", "#FFFFFF", 0),
    ("dark", "brand.purple", "#000000", 3.0),
    ("dark", "brand.amber", "#000000", 3.0),
    ("light", "#1E8E3E", "#FFFFFF", 0),
]


def main():
    failures = 0
    print("| Theme | Foreground | Background | Ratio | Target | Result |")
    print("|---|---|---|---|---|---|")
    for theme, fg, bg, target in PAIRS:
        fv, bv = tok(theme, fg), tok(theme, bg)
        r = ratio(fv, bv)
        if target == 0:
            result = "info only"
        elif r >= target:
            result = "pass"
        else:
            result = "FAIL"
            failures += 1
        label = lambda n, v: f"`{v}`" if n.startswith("#") else f"{n} `{v}`"
        print(f"| {theme} | {label(fg, fv)} | {label(bg, bv)} | {r:.2f}:1 | "
              f"{'—' if target == 0 else f'{target}:1'} | {result} |")
    if "--check" in sys.argv and failures:
        print(f"{failures} pair(s) below target", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
