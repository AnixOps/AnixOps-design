# Changelog

All notable changes to AnixOps Design. Versions follow
[Semantic Versioning](https://semver.org/) on token names and asset paths.

## Unreleased

### Added

- `legal/terms.zh-CN.md` 2.2.0: section 1 gains 「提供地区」. The AnixOps
  Net client is not offered in mainland China: no official builds, updates,
  store listings or promotion there, and the download channels we run do
  not answer requests from mainland China. The software is not built to
  evade any country's or region's network rules. A new clause (minor
  version), so clients do not ask for consent again; every product
  repository copies the new common terms.
- `guidelines/density.md` section 4, N28–N34, grouped and nested lists:
  one grouping dimension at a time with a "Group by" control, group
  headers with a count and a folded one-line summary, rows that unfold one
  level only, parent rows that state what they hold, search and filters
  that reach folded rows, the worst status shown on a folded group, and
  one role pill per row. The review checklist is now section 5. Prompted
  by the AnixOps Net mesh member list (regions, gateways with subnets,
  hosts with virtual machines).
- `guidelines/voice-and-tone.md` glossary: the mesh terms (组网, 成员,
  地区, 边界, 网关, 宿主, 接入端, 通告子网, 中转, 跨区, 途经点 and the path
  states).
- `guidelines/voice-and-tone.md` W1–W7, formal register: no second person,
  no colloquial words or contractions, no exclamation marks, hints say what
  and not why or how, no explanatory connectives, at most two sentences per
  string. `guidelines/formal-copy.json` lists the forbidden words for
  products to check their string tables in CI.
- `guidelines/density.md` N25–N27: a budget for the settings first screen
  (8 sections, 16 rows, two viewports; advanced and diagnostic items on
  detail pages), user-added lists fold after five rows, and a master switch
  gets its own section. Products check them in CI. Prompted by the AnixOps
  Net settings page growing past what most people read, and the HTTPS
  decryption switch sitting among the plugin rows.

### Changed

- AnixOps Net product icon: the single arc between two nodes read as a
  stick at small sizes, so the symbol is now a route that forks in two, the
  chosen branch ending at the slate dot (traffic split by rules). Same tile,
  colours and stroke range; every `assets/products/net/` file regenerated.
- Text colours now hold 4.5:1 on the translucent fills they sit on, not only
  on the three backgrounds (`guidelines/color.md` rule 7): light `label-2`
  `#6E6E73` → `#656569`, `accent`/`info` `#4F5BE8` → `#4753E8`, `success`
  `#1A7F37` → `#1A7537`, `warning` `#B25000` → `#A24F00`, `danger` `#D70015`
  → `#CF0015`; dark `accent`/`info` `#818CF8` → `#8994F8`, `danger` `#FF453A`
  → `#FF6D62`. `accent-fill`, `danger-fill`, the soft fills, chart colours
  and the terminal palette are unchanged. Found by the AnixOps Net desktop
  axe check: secondary text in the sidebar, success pills and a danger
  status in a selected row were 3.7–4.4:1. `scripts/contrast.py` now
  composites every fill over every background and checks those pairs too.

### Added

- Version themes (`brand/brand.md` 2.7): a generated piece of music per
  product major release for the website, from a fixed product motif varied
  by the release's git history. Generator `scripts/theme/` (own MIDI writer,
  sampler and mixer; samples from VSCO 2 CE, CC0, not stored). First set in
  `brand/assets/audio/`: Control 5.0.0, Agent 5.0.0, Core 0.2.0,
  Net 0.3.0-beta.10, SSH 2.4.0.
  `.github/workflows/themes.yml` generates themes for new majors and opens
  a pull request; CI checks that no two themes are identical.
- Product icons (`brand/brand.md` 2.6): one icon per product, AnixOps
  Control, Core, Agent, Net and SSH, under `brand/assets/products/<id>/`
  (rounded and full-bleed SVG, PNG 16–1024, ICO, ICNS). The symbol names the
  product, the tile colour names the product line. New tokens
  `color.brand.line-tools-start` / `line-tools-end` for the tools line.

- `guidelines/terminology.md` (`T1`–`T8`): neutral terminology for every
  product (服务商 / provider, 网络干扰, 服务可用性 and the terms they replace),
  with the machine-readable list `guidelines/neutral-terms.json` and the
  checker `scripts/neutral_terms.py` that product repositories copy into CI.
  AnixOps Net added to the product table in `guidelines/naming.md`.
- `legal/terms.zh-CN.md` 2.1.2: section 5 now says 「核查」 for checking
  third-party content. Wording
  only; no change to rights or obligations, no new consent needed.
- `guidelines/motion.md` rewritten as numbered rules (`M1`–`M23`): live data
  does not animate, selection and page changes in client windows are
  immediate, feedback timing (100 ms press, 300 ms before a busy indicator,
  400 ms minimum), interruptible transitions, native platform mapping. The
  motion tokens are unchanged.
- `guidelines/keyboard.md` (`K1`–`K22`): keyboard principles, the command
  palette, and the reserved shortcuts every product shares on macOS, Windows
  and Linux.
- `guidelines/density.md` (`N1`–`N24`): two density tiers chosen by
  page type (comfortable, compact), the rules for compact tables with the
  node table as the reference, and for comfortable pages.

- `--font-app` and `--font-app-mono` (`font.family.app`, `app-mono`): system
  font stacks for installed client applications (Segoe UI Variable with
  Microsoft YaHei UI on Windows, the desktop font on Linux, the platform font
  on Apple and Android), without Inter. Web products keep `--font-sans` and
  `--font-mono`. See `guidelines/typography.md`, "Client applications".
- `legal/`: baseline user agreement, acceptable use policy and disclaimer
  (`terms.zh-CN.md`, terms version 1.0.0) and how each product repository
  adopts it as `TERMS.md` with a product supplement. Draft, not legal advice.
- `legal/terms.zh-CN.md` 2.0.0: governing law and courts are now England
  and Wales (section 13), keeping local mandatory consumer protection.
- `legal/terms.zh-CN.md` 2.0.1: abuse reports go to abuse@anixops.com
  (section 11).
- `legal/terms.zh-CN.md` 2.1.0: section 4 now covers packet capture as well
  as HTTPS decryption: capture and decrypt only traffic you are entitled to
  see (your own devices, or apps, devices and networks you are authorised to
  debug); connect other devices to capture only with their owner's consent;
  products ask once more the first time HTTPS decryption is turned on;
  captures stay on the device and are redacted before export.
- `legal/terms.zh-CN.md` 2.1.1: the “不构成法律意见” notes at the top and at the end
  of the terms are removed (wording only; no clause changes).

## 1.2.0 - 2026-11-11

### Added

- Organisation mark (`brand/brand.md` 2.5): a bold A whose crossbar is a dot,
  for the GitHub organisation and other AnixOps accounts, as
  `brand/assets/social/org-avatar.svg` and `.png`. Products keep the orbit A.
- `guidelines/actions.md`: the UI/UX rules every product follows on iOS,
  macOS, Windows, Linux and the web panels. Four emphasis levels (primary,
  secondary, quiet, destructive) mapped to tokens and to each platform's
  controls; scope levels (app, page, section, row, selection, dialog) and
  where each sits; order and spacing; destructive actions with four
  confirmation tiers (undo, confirm, typed, system); showing only what
  applies; information hierarchy; dialogs, sheets and forms; feedback;
  per-platform placement; worked examples; a review checklist; and how
  products adopt and change the rules. Rules are numbered (`A`, `S`, `O`,
  `D`, `V`, `H`, `C`, `F`, `P`) and the numbers are stable so reviews can
  cite them.

## 1.1.0 - 2026-11-08

### Changed

- New mark: the orbit A. Two legs meet under an apex node, and a tilted
  orbit with a satellite node passes behind the legs at the top and in front
  at the bottom, with cut gaps so the weave reads in one colour. Replaces the
  hexagon-and-hub mark; geometry in `brand/brand.md` 2.1, owner decision in
  section 7.
- Tile: slate `#0F172A` (`brand.slate-900`) with the brand gradient on the
  glyph and a white hairline at 8 % for edge definition on black, instead of
  a gradient tile with a white glyph. The glyph is at least 4.00:1 on the tile
  (was 3.36:1); `scripts/contrast.py --check` now checks the gradient on
  slate.
- Favicon variant: no satellite, heavier strokes for 16 px.
- Android adaptive icon: gradient glyph over a slate background; iOS icon
  flattened onto slate.
- ASCII mark redrawn as the orbit A, so `anixops.Banner` (Go) and
  `term::ASCII_MARK` (Rust) change their first three lines.
- Every brand asset regenerated. Asset paths and token names are unchanged;
  token values are unchanged.

### Added

- `brand/assets/app-icon-monochrome.svg`: white glyph for Android themed
  icons (previously the white foreground doubled as the monochrome layer).

### Fixed

- `scripts/build-assets.mjs` loads the Inter fonts from the exact file bytes.
  Passing `Buffer.buffer` broke on newer Node versions, where it can be a
  shared pool with an offset; output is byte-identical.

## 1.0.2 - 2026-10-01

### Changed

- Mark: the hub circle grows from radius 2.25 to 2.75 (the favicon already
  used 2.75). At 2.25 the arcs left between the spokes were thin slivers that
  showed as notches in large renders; the hub now reads as a clear node.
- Brand gradient start deepened from `#38BDF8` to `#0EA5E9`
  (`--brand-gradient-start`, terminal `brand-start`, xterm-256 75 → 38). The
  white glyph is now at least 3.36:1 wherever it sits on the tile (was
  2.78:1 at its top-left vertex); `scripts/contrast.py --check` enforces 3:1.
- Every brand asset regenerated.

## 1.0.1 - 2026-10-01

### Changed

- Naming: EasySSH and AnixOps-ssh merge into one product, AnixOps SSH.
- Naming: AnixOps Studio is the maker of AnixOps products, not a product
  name; it is not yet a legal entity, so legal text names the owner.
- `LICENSE` and `LICENSE-BRAND.md`: copyright holder is now
  "kalijerry (AnixOps Studio)" instead of "AnixOps", which is not a legal
  entity.

## 1.0.0 - 2026-10-01

First release. Palette and scope approved by the owner on 2026-10-01.

### Brand

- Brand spec `brand/brand.md`: the AnixOps mark redrawn as geometric SVG from
  the Control Center app icon (24-unit grid, hexagon ring, hub and spokes),
  clear space and minimum size, versions, wordmark lockup, palette, type,
  do and don't, and the owner's decisions.
- One accent for every product: `#4F5BE8` light, `#818CF8` dark (`#5B63E6`
  dark fill). Replaces the earlier primaries, including anix-control's
  `#0064FA`. No sub-brand accents.
- Assets in `brand/assets/`, all generated by `scripts/build-assets.mjs`:
  `mark.svg`, `mark-mono-white.svg`, `mark-mono-black.svg`, `mark-glyph.svg`
  (`currentColor`), `favicon.svg` (16 px-safe), `wordmark.svg` and
  `wordmark-on-dark.svg` (text outlined in Inter), full-bleed app icon
  sources, and raster sets: `favicon/` (ICO 16/32/48, apple-touch 180, PWA
  192/512 and maskable), `app-icon/` (1024 iOS, Android adaptive foreground,
  background and monochrome), `tauri/` (PNG, ICO, ICNS), `social/og-image`
  (1200 × 630) and `banner/readme-banner-{light,dark}`. `--product` generates
  lockups, banners and OG images for any product.
- `brand/assets/ascii-mark.txt`: three-line ASCII mark for terminals.

### Tokens

- `tokens/tokens.json` (W3C Design Tokens format): colour for light and dark
  (pure black dark background), terminal palette (truecolor, xterm-256 and
  ANSI 16), seven-step type scale, spacing, sizes, radius, shadow, motion,
  z-index, breakpoints.
- Generated by `scripts/build-tokens.py` (dependency free, `--check` for CI):
  `css/tokens.css` (system, light and dark selectors), `tailwind/preset.cjs`
  (v3), `tailwind/theme.css` (v4), `element-plus/element-plus.css`,
  `flutter/anixops_tokens.dart` (ThemeData, ColorScheme, ThemeExtension, type
  scale), `go/anixops` (Go module with UI colours, terminal palette,
  `ColorEnabled` for `NO_COLOR`, and `Banner`), `rust/anixops_tokens.rs`.
- `scripts/contrast.py`: WCAG contrast tables for UI and terminal colours,
  and a check that every xterm-256 fallback is the nearest colour.
- Light success corrected from `#1E8E3E` (4.21:1 on white) to `#1A7F37`.

### Fonts

- Self-hosted Inter (variable, Latin subset) in `fonts/inter/` with
  `@font-face` CSS; Chinese uses system fonts.

### Guidelines

- Principles (including the legal limits on Apple fonts, SF Symbols and
  assets), colour with the computed contrast tables, typography, layout,
  motion, iconography (Lucide, 1.5 px), voice and tone with a glossary seed,
  accessibility.
- New: naming (canonical "AnixOps <Product>" names, including AnixOps SSH and
  AnixOps ToDo), terminal (palette, `NO_COLOR` and `--color` policy, banner),
  platforms (per-stack setup and assets), adoption (each product's divergence
  from the 2026-10 audit and its migration).

### Licensing

- `LICENSE` (MIT, code) and `LICENSE-BRAND.md` (name, mark, wordmark and
  every brand asset: all rights reserved, AnixOps products only).
