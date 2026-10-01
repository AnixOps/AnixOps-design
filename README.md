<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/assets/banner/readme-banner-dark.png">
  <img alt="AnixOps" src="brand/assets/banner/readme-banner-light.png">
</picture>

# AnixOps Design

The brand, visual identity and design tokens shared by every AnixOps product:
AnixOps Control, AnixOps Control Center (web, mobile and TUI), AnixOps Agent
and every other AnixOps app, CLI and site use the same mark, palette, type and
rules.

**Version 1.0.1** (2026-10-01). See [`CHANGELOG.md`](CHANGELOG.md).

## Contents

| Path | What it holds |
|---|---|
| [`brand/brand.md`](brand/brand.md) | The brand spec: mark, construction, versions, palette, typography, do and don't, decisions |
| [`brand/assets/`](brand/assets/) | Mark (gradient tile, mono white and black, `currentColor` glyph), small-size favicon, outlined wordmarks, app icon sources, and the raster sets: favicon, PWA, iOS/Android, Tauri, OG image, README banners, ASCII mark |
| [`tokens/tokens.json`](tokens/tokens.json) | Source of truth in [W3C Design Tokens](https://design-tokens.github.io/community-group/format/) format: colour (light and dark), terminal palette, type scale, spacing, size, radius, shadow, motion, z-index, breakpoints |
| [`tokens/`](tokens/) | Generated per platform: `css/`, `tailwind/` (v3 preset, v4 theme), `element-plus/`, `flutter/`, `go/anixops/` (Go module), `rust/`. Do not edit by hand |
| [`fonts/inter/`](fonts/inter/) | Self-hosted Inter (variable, Latin subset) with `@font-face` CSS; SIL OFL 1.1 |
| [`guidelines/`](guidelines/) | Principles, colour, typography, layout, motion, iconography, voice and tone, accessibility, naming, terminal, platforms, adoption |
| [`scripts/`](scripts/) | `build-tokens.py` (tokens → every platform), `contrast.py` (WCAG table), `build-assets.mjs` (SVG and raster assets) |

## Using it in a product

[`guidelines/platforms.md`](guidelines/platforms.md) has the steps for each
stack. In short:

| Stack | Copy |
|---|---|
| Any web page | `tokens/css/tokens.css` and `fonts/inter/` |
| Tailwind CSS | v3 `tokens/tailwind/preset.cjs`, v4 `tokens/tailwind/theme.css` (plus `tokens.css`) |
| Element Plus | `tokens/element-plus/element-plus.css` (plus `tokens.css`) |
| React + shadcn/ui | `tokens.css` and the mapping in platforms.md |
| Flutter | `tokens/flutter/anixops_tokens.dart`: `anixOpsTheme(Brightness.light)` |
| Go CLI / TUI | `go get github.com/AnixOps/AnixOps-design/tokens/go/anixops` |
| Rust (egui, ratatui) | `tokens/rust/anixops_tokens.rs` |
| Icons, banners, OG | `brand/assets/` |

The CSS follows the system theme and honours a manual override on the root
element:

```html
<html data-theme="dark">   <!-- or "light"; remove the attribute to follow the system -->
```

**Rule for every product:** components reference tokens, never literal
colours. When a value changes, regenerating the platform files updates every
screen. [`guidelines/adoption.md`](guidelines/adoption.md) lists what each
existing product changes to adopt 1.0.0.

## Working on it

```bash
python3 scripts/build-tokens.py          # regenerate every file under tokens/ (no dependencies)
python3 scripts/contrast.py              # print the WCAG contrast tables
npm install && node scripts/build-assets.mjs   # regenerate brand/assets/ (sharp, opentype.js, Inter)
node scripts/build-assets.mjs --product "Control Center" --out ./out   # one product's lockups, banners, OG image

npm run check                            # what CI runs: stale outputs, contrast targets, missing assets
```

Change `tokens.json`, regenerate, run the checks, update
`guidelines/color.md` if a number moved, and add a `CHANGELOG.md` entry.

## Versioning

[Semantic Versioning](https://semver.org/) on token names and asset paths:

- **Major**: a token is renamed or removed, or an asset path changes.
- **Minor**: a token, asset, platform output or guideline is added.
- **Patch**: a value is tuned within the same intent (for example a contrast fix).

Releases are tagged `vX.Y.Z`; the Go module is also tagged
`tokens/go/anixops/vX.Y.Z`. Products pin a version and upgrade deliberately.
Planned: 1.1 or 2.0 brings the Vue component library, first built inside
anix-control.

## License

Code (tokens, generated platform files, scripts) is MIT: see
[`LICENSE`](LICENSE). The AnixOps name, mark, wordmark and every file in
`brand/assets/` are **not** covered by the MIT license; see
[`LICENSE-BRAND.md`](LICENSE-BRAND.md). Inter in `fonts/inter/` is under the
SIL Open Font License 1.1 ([`fonts/inter/OFL.txt`](fonts/inter/OFL.txt)).
