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
ALL = json.loads((ROOT / "tokens" / "tokens.json").read_text(encoding="utf-8"))
TOKENS = ALL["color"]
TERMINAL = {k: v for k, v in ALL["terminal"].items() if not k.startswith("$")}


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


def gradient_at(t):
    """Brand gradient colour at position t (0 = start, 1 = end)."""
    a, b = TOKENS["brand"]["gradient-start"]["$value"], TOKENS["brand"]["gradient-end"]["$value"]
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(ca[i] * (1 - t) + cb[i] * t):02X}" for i in range(3))


# The white glyph on the tile must stay at 3:1 (UI graphics) wherever it sits. The gradient
# runs at 135 degrees, so t = (x + y) / 2 in tile units; the glyph box is 56.25 % of the tile,
# centred, and its lightest point is the ring's top-left vertex (3.5, 7.25) on the 24 grid.
GLYPH_T = (0.21875 + 3.5 / 24 * 0.5625 + 0.21875 + 7.25 / 24 * 0.5625) / 2
PAIRS.append(("light", "#FFFFFF", gradient_at(GLYPH_T), 3.0))


def xterm256(index):
    """Hex value of an xterm-256 colour in the 6x6x6 cube (16-231) or grey ramp (232-255)."""
    if index >= 232:
        v = 8 + 10 * (index - 232)
        return f"#{v:02X}{v:02X}{v:02X}"
    levels = [0, 95, 135, 175, 215, 255]
    i = index - 16
    return "#" + "".join(f"{levels[n]:02X}" for n in (i // 36, i // 6 % 6, i % 6))


def nearest256(hex_colour):
    """Nearest xterm-256 index by redmean distance (the method used to pick the tokens)."""
    def rgb(h):
        return [int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    a = rgb(hex_colour)

    def dist(index):
        b = rgb(xterm256(index))
        r = (a[0] + b[0]) / 2
        d = [a[i] - b[i] for i in range(3)]
        return (2 + r / 256) * d[0] ** 2 + 4 * d[1] ** 2 + (2 + (255 - r) / 256) * d[2] ** 2
    return min(range(16, 256), key=dist)


# Terminal backgrounds: light terminals are close to white, dark ones to black or #1C1C1E.
TERM_BGS = {"light": ["#FFFFFF"], "dark": ["#000000", "#1C1C1E"]}


def terminal_table():
    failures = 0
    print()
    print("| Role | Terminal | Colour | Background | Ratio | Target | Result |")
    print("|---|---|---|---|---|---|---|")
    for role, spec in TERMINAL.items():
        target = 0 if role.startswith("brand") else 4.5
        for theme in ("light", "dark"):
            truecolor = spec[theme]["$value"]
            index = spec[f"ansi256-{theme}"]["$value"]
            if index != nearest256(truecolor):
                print(f"{role} ansi256-{theme} is {index}, nearest to {truecolor} is {nearest256(truecolor)}",
                      file=sys.stderr)
                failures += 1
            for label, colour in ((f"{theme} truecolor", truecolor), (f"{theme} 256 ({index})", xterm256(index))):
                for bg in TERM_BGS[theme]:
                    r = ratio(colour, bg)
                    result = "info only" if target == 0 else ("pass" if r >= target else "FAIL")
                    failures += result == "FAIL"
                    print(f"| {role} | {label} | `{colour}` | `{bg}` | {r:.2f}:1 | "
                          f"{'—' if target == 0 else f'{target}:1'} | {result} |")
    return failures


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
    failures += terminal_table()
    if "--check" in sys.argv and failures:
        print(f"{failures} pair(s) below target", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
