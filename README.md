# AnixOps Design

The brand, visual identity and design tokens shared by every AnixOps product.
AnixOps Control (panel, Control Center web and mobile) is the first consumer;
every other AnixOps app, CLI and site adopts the same mark, palette, type and
rules.

> **Status: 1.0.0 DRAFT, pending owner approval.** The brand palette is not
> final. Do not tag `v1.0.0` until the owner has approved `brand/brand.md` and
> `guidelines/color.md`.

## Contents

| Path | What it holds |
|---|---|
| [`brand/brand.md`](brand/brand.md) | The brand spec: mark, construction, versions, palette, typography, do and don't |
| [`brand/assets/`](brand/assets/) | SVG mark (gradient tile, mono white, mono black, `currentColor` glyph), wordmark lockup, favicon |
| [`tokens/tokens.json`](tokens/tokens.json) | Source of truth: colour (light and dark), type scale, spacing, size, radius, shadow, motion, z-index, breakpoints, in [W3C Design Tokens](https://design-tokens.github.io/community-group/format/) format |
| [`tokens/css/tokens.css`](tokens/css/tokens.css) | Generated CSS custom properties. Do not edit by hand |
| [`scripts/build-tokens.py`](scripts/build-tokens.py) | Generates `tokens.css` from `tokens.json` (Python 3, no dependencies) |
| [`scripts/contrast.py`](scripts/contrast.py) | Computes the WCAG contrast table for every colour pair we use |
| [`guidelines/`](guidelines/) | Principles, colour, typography, layout, motion, iconography, voice and tone, accessibility |

## Using it in a product

**Web (CSS, Vue, React).** Copy or vendor `tokens/css/tokens.css` and use only
the variables: `color: var(--label-1)`, `border-radius: var(--radius-md)`. The
file follows the system theme and honours a manual override on the root
element:

```html
<html data-theme="dark">   <!-- or "light"; remove the attribute to follow the system -->
```

Copy the SVGs from `brand/assets/`. `favicon.svg` is the browser tab icon;
`mark-glyph.svg` uses `currentColor`, so inline it to inherit text colour.

**Flutter, native, CLIs.** Read `tokens/tokens.json` (stable keys, hex values)
and generate the platform's theme from it. Terminal tools map status colours
to the nearest ANSI colours and never rely on colour alone.

**Rule for every product:** components reference tokens, never literal colours.
When the palette changes, regenerating `tokens.css` updates every screen.

## Working on it

```bash
python3 scripts/build-tokens.py          # regenerate tokens/css/tokens.css
python3 scripts/build-tokens.py --check  # CI: fail if tokens.css is stale
python3 scripts/contrast.py --check      # CI: fail if a pair misses its WCAG target
```

Change `tokens.json`, regenerate, run the contrast check, update
`guidelines/color.md` if a number moved, and add a `CHANGELOG.md` entry.

## Versioning

[Semantic Versioning](https://semver.org/) on the token names and asset paths:

- **Major**: a token is renamed or removed, or an asset path changes.
- **Minor**: a token, asset or guideline is added.
- **Patch**: a value is tuned within the same intent (for example a contrast fix).

Products pin a version and upgrade deliberately. Planned: 1.1 or 2.0 brings the
Vue component library, first built inside anix-control.

## License

Code (tokens, scripts, CSS) is MIT: see [`LICENSE`](LICENSE). The AnixOps name,
mark, wordmark and favicon are **not** covered by the MIT license; see
[`LICENSE-BRAND.md`](LICENSE-BRAND.md).
