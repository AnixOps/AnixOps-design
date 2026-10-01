# Layout

## Spacing

4 pt scale: `--space-0-5` 2 · `--space-1` 4 · `--space-2` 8 · `--space-3` 12 ·
`--space-4` 16 · `--space-5` 20 · `--space-6` 24 · `--space-8` 32 ·
`--space-10` 40 · `--space-12` 48 · `--space-16` 64 · `--space-20` 80.

- Card padding 24 (phone 16). Section gap 48–64. Form field gap 20.
- Page side gutter: 16 on phones, 24 on tablets, 32+ on desktop.

## Widths and breakpoints

| Token | Value | Use |
|---|---|---|
| `--size-content-user` | 980 px | User-facing pages |
| `--size-content-admin` | 1280 px | Admin pages |
| `--size-content-wide` | 1440 px | Wide tables |
| `--size-content-read` | 692 px | Articles |

Breakpoints, used literally (CSS variables cannot appear in media queries):
`sm 640`, `md 834`, `lg 1068`, `xl 1440`. No others.

## Controls

Heights: 44 (touch, `--size-control-lg`), 36 (default), 28 (inside tables).
Touch targets are never smaller than 44 × 44 on phones.

## Radius

`--radius-xs` 6 (badges) · `--radius-sm` 10 (inputs, buttons) ·
`--radius-md` 14 (cards) · `--radius-lg` 20 (dialogs, large cards) ·
`--radius-pill` 980 (pill buttons, segmented controls, chips).

## Elevation

| Token | Use |
|---|---|
| `--shadow-1` | Resting cards (with a hairline border) |
| `--shadow-2` | Hover, menus, popovers |
| `--shadow-3` | Dialogs and sheets |

Dark mode keeps shadows faint and adds a 1 px `--highlight` edge.
Separators are 1 px hairlines (`--separator`), 0.5 px on high-density
screens; no thick borders.

Frosted material for top bars, sidebars and menus:

```css
background: var(--bg);                       /* fallback */
@supports (backdrop-filter: blur(1px)) {
  background: var(--material);
  backdrop-filter: saturate(180%) blur(20px);
}
```

## Z-index

`--z-base 0 · --z-sticky 10 · --z-dropdown 100 · --z-drawer 200 ·
--z-modal 300 · --z-toast 400 · --z-tooltip 500`.

## Page templates

List (header, toolbar, table, bulk bar, side sheet) · Detail (back link,
title and status, segmented sections, grouped lists) · Settings (left list,
grouped rows, sticky save bar when dirty) · Dashboard (3–4 metrics, one main
chart, alerts and activity) · Wizard (steps, form, back/next).
