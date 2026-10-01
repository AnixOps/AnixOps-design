# Platforms: using the tokens and assets

Every file below is generated from [`../tokens/tokens.json`](../tokens/tokens.json)
by `python3 scripts/build-tokens.py` (tokens) or `node scripts/build-assets.mjs`
(assets). Copy or vendor the files for your stack and pin the AnixOps Design
version you copied from. Never edit a copy: change `tokens.json` here and
regenerate.

| Stack | Products today | Use |
|---|---|---|
| Vue 3 / any web, hand-written CSS | anix-control, Prompt-To-Website, Blog (Hono SSR), AnixOps-network (Flask) | `tokens/css/tokens.css` |
| Tailwind CSS v3 | control-center web, node-platform | `tokens/tailwind/preset.cjs` |
| Tailwind CSS v4 | new projects | `tokens/tailwind/theme.css` |
| Element Plus | website, ToDoList | `tokens/element-plus/element-plus.css` |
| React + shadcn/ui | node-platform, NetworkCore, AnixOps SSH (Tauri, AnixOps-ssh) | `tokens.css` + the mapping below |
| Flutter (Material 3) | control-center mobile | `tokens/flutter/anixops_tokens.dart` |
| Go (lipgloss, bubbletea, cobra) | control-center TUI, anix-agent | `tokens/go/anixops` module, see [terminal](terminal.md) |
| Rust (egui, ratatui) | AnixOps SSH (egui, EasySSH) | `tokens/rust/anixops_tokens.rs` |

## Web: CSS

```html
<link rel="stylesheet" href="/fonts/inter/inter.css">   <!-- copy fonts/inter/ -->
<link rel="stylesheet" href="/tokens.css">
<html data-theme="dark">  <!-- optional: "light" or "dark"; omit to follow the system -->
```

Use only the variables (`color: var(--label-1)`). Layer frosted bars with
`background: var(--material); backdrop-filter: saturate(180%) blur(20px)` and
fall back to `--bg` when `backdrop-filter` is unsupported or
`prefers-reduced-transparency` is set.

## Tailwind CSS

**v3**: `presets: [require('./anixops/preset.cjs')]` in `tailwind.config.js`, and
load `tokens.css` before Tailwind's layers. **v4**: import `tailwindcss`,
then `tokens.css`, then `theme.css`.

Utilities are named after the tokens: `bg-bg-elevated`, `text-label-2`,
`bg-accent-fill hover:bg-accent-fill-hover text-on-accent`, `text-title-1`,
`rounded-md`, `shadow-2`, `ease-emphasized duration-overlay`,
`max-w-content-admin`, `z-modal`, `bg-brand-gradient`. Every colour is a CSS
variable, so themes switch without `dark:` variants; do not add them. The
spacing scale is Tailwind's default, which already equals `--space-*`.
Breakpoints are replaced by ours (`sm` 640, `md` 834, `lg` 1068, `xl` 1440).

Colour opacity modifiers (`bg-accent/50`) do not work on variables in v3; use
the `-soft` tokens instead.

## Element Plus

Load `element-plus/dist/index.css`, then `tokens.css`, then
`element-plus.css`. Do not import Element Plus's `dark/css-vars.css` and do not
toggle `html.dark`: the overrides follow the system theme and `data-theme`
like everything else. Primary maps to `--accent-fill`; the `light-3` to
`light-9` and `dark-2` steps are mixed at build time against the card colour of
each theme.

## React + shadcn/ui

shadcn/ui (Tailwind v4 setup) defines its own colour variables in `:root`
and `.dark`, then maps them with `@theme inline { --color-*: var(--…) }`.
Delete its `:root` and `.dark` colour blocks (tokens.css replaces them; never
redefine `--accent` or other AnixOps variables) and point the `@theme inline`
mapping at the AnixOps tokens instead. Import order: `tailwindcss`,
`tokens.css`, `theme.css`, then this block, so shadcn's names win:

```css
@theme inline {
  --color-background: var(--bg);
  --color-foreground: var(--label-1);
  --color-card: var(--bg-elevated);
  --color-card-foreground: var(--label-1);
  --color-popover: var(--bg-elevated);
  --color-popover-foreground: var(--label-1);
  --color-primary: var(--accent-fill);
  --color-primary-foreground: var(--on-accent);
  --color-secondary: var(--fill-1);
  --color-secondary-foreground: var(--label-1);
  --color-muted: var(--fill-1);
  --color-muted-foreground: var(--label-2);
  --color-accent: var(--fill-2);            /* shadcn's "accent" is a hover fill */
  --color-accent-foreground: var(--label-1);
  --color-destructive: var(--danger-fill);
  --color-border: var(--separator);
  --color-input: var(--separator-strong);
  --color-ring: var(--accent);
}
```

In these apps the `accent` utility (`bg-accent`) means shadcn's hover fill;
for the AnixOps accent use `text-(--accent)` for text and `bg-accent-fill`
for filled controls; `var(--accent)` itself is untouched. Set shadcn's `--radius` to
`var(--radius-sm)`. Projects still on the older HSL setup
(`hsl(var(--primary))`) move to the v4 style first.

## Flutter

Copy `anixops_tokens.dart` into `lib/theme/`. Needs Dart 3 (Flutter 3.10+).

```dart
MaterialApp(
  theme: anixOpsTheme(Brightness.light),
  darkTheme: anixOpsTheme(Brightness.dark),
);
final c = Theme.of(context).extension<AnixOpsColors>()!;   // c.success, c.label2, ...
```

Inter: add `fonts/inter/` (as TTF, or use `google_fonts`) under the family
name `Inter`, or call `anixOpsTheme(b, fontFamily: null)` on iOS/macOS to keep
the platform font. Chinese falls back to PingFang SC / Microsoft YaHei / Noto
Sans SC.

App icons with `flutter_launcher_icons`:

```yaml
flutter_launcher_icons:
  image_path: "assets/icon/app-icon-1024.png"                   # brand/assets/app-icon/
  adaptive_icon_foreground: "assets/icon/app-icon-foreground-1024.png"
  adaptive_icon_background: "assets/icon/app-icon-background-1024.png"
  adaptive_icon_monochrome: "assets/icon/app-icon-monochrome-1024.png"
  remove_alpha_ios: true
  web: { generate: true, image_path: "assets/icon/app-icon-1024.png" }
```

## Go and Rust

See [terminal](terminal.md). The Go module also exports the UI colours
(`anixops.UIAccent.Light`, …) for server-rendered pages. The Rust file has
`light`, `dark`, `brand`, `term`, `space`, `radius`, `size` and `duration`
modules; for egui use
`egui::Color32::from_rgba_unmultiplied(c.r, c.g, c.b, c.a)`.

## Assets per platform

| Need | File in `brand/assets/` |
|---|---|
| Browser tab | `favicon.svg` (modern browsers) + `favicon/favicon.ico` (16/32/48) |
| iOS home screen | `favicon/apple-touch-icon.png` (180, full bleed; iOS rounds it) |
| PWA manifest | `favicon/icon-192.png`, `favicon/icon-512.png`, `favicon/icon-maskable-512.png` (`"purpose": "maskable"`) |
| iOS / Android app | `app-icon/` (1024 source, adaptive foreground, background, monochrome) |
| Tauri | `tauri/` → copy into `src-tauri/icons/` (`32x32.png`, `128x128.png`, `128x128@2x.png`, `icon.png`, `icon.ico`, `icon.icns`) |
| Link previews | `social/og-image.png` (1200 × 630) |
| README header | `banner/readme-banner-light.png` and `-dark.png`, with `<picture>` |
| UI chrome next to text | `mark-glyph.svg` inline (`currentColor`) |
| Logo with name | `wordmark.svg` / `wordmark-on-dark.svg` (outlined; no font needed) |

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:image" content="https://<domain>/og-image.png">
<meta name="theme-color" content="#FBFBFD" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
```

```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/readme-banner-dark.png">
  <img alt="AnixOps Control Center" src="brand/readme-banner-light.png">
</picture>
```

**Product lockups, banners and OG images** with the product name:

```bash
npm install
node scripts/build-assets.mjs --product "Control Center" --out ./out
# wordmark-control-center.svg, -on-dark.svg, readme-banner-control-center-{light,dark}.{svg,png},
# og-image-control-center.{svg,png}
```

Use the canonical product names from [naming](naming.md).
