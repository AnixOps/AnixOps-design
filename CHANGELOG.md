# Changelog

All notable changes to the AnixOps Design System. Versions follow
[Semantic Versioning](https://semver.org/) on token names and asset paths.

## 1.0.0 - 2026-10-01 (DRAFT — pending owner approval; not tagged)

### Added

- Brand spec `brand/brand.md`: the AnixOps mark redrawn as geometric SVG from
  the Control Center app icon (24-unit grid, hexagon ring, hub and spokes),
  clear space and minimum size, versions, wordmark lockup, palette, type,
  do and don't.
- Assets in `brand/assets/`: `mark.svg` (gradient tile), `mark-mono-white.svg`,
  `mark-mono-black.svg`, `mark-glyph.svg` (`currentColor`), `wordmark.svg`
  (live text; to be outlined before release), `favicon.svg` (16 px-safe).
- Design tokens `tokens/tokens.json` (W3C Design Tokens format): colour for
  light and dark (pure black dark background), seven-step type scale,
  spacing, sizes, radius, shadow, motion, z-index, breakpoints. Generated
  `tokens/css/tokens.css` with system, light and dark theme selectors.
- `scripts/build-tokens.py` (CSS generator with `--check`) and
  `scripts/contrast.py` (WCAG contrast table with `--check`), both
  dependency free.
- Guidelines: principles (including the legal limits on Apple fonts, SF
  Symbols and assets), colour with the computed contrast table, typography,
  layout, motion, iconography (Lucide, 1.5 px), voice and tone with a glossary
  seed, accessibility.
- `LICENSE` (MIT, code) and `LICENSE-BRAND.md` (name, mark and wordmark: all
  rights reserved, AnixOps products only).
