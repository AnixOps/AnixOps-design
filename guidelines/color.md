# Colour

> Approved 1.0.0 (2026-10-01). Values live in
> [`../tokens/tokens.json`](../tokens/tokens.json); this page explains them.

## Rules

1. **Neutrals carry the interface.** Large areas are `--bg`, `--bg-elevated`
   and `--bg-grouped`; text is `--label-1/2/3`. Colour is the exception.
2. **One accent, for every product.** `--accent` marks what is interactive or
   selected: links, the primary button, focus rings, the selected item. Never
   decoration. Products do not get their own accent.
3. **Status colours only for status.** Success, warning and danger appear on
   badges, inline alerts, chart thresholds and destructive actions, and always
   with a word or icon (never colour alone).
4. **The brand gradient only for brand moments**: the logo glyph, login
   backdrop, user home hero numbers. Never on controls or text.
5. **Filled controls use `-fill` tokens.** `--accent-fill` and
   `--danger-fill` exist because the dark text colours (`#8994F8`, `#FF6D62`)
   are too light for white text.
6. **Dark mode is pure black** (`#000`) with `#1C1C1E` cards; layers are
   separated by a 1px highlight edge, not heavier shadows.
7. **Text holds on every fill.** Text sits on more than the three
   backgrounds: on a selected row (`--accent-soft`), a badge or status pill
   (its own `-soft` fill), a control or a sidebar (`--fill-1`, `--fill-2`).
   `--label-1/2`, `--accent` and the status colours reach 4.5:1 on each of
   these fills over each background; the table below checks every pair.
8. **Charts** use `--chart-1` … `--chart-8` in order; every series colour is at
   least 3:1 against the card.

## Theme switching

`tokens.css` puts light values on bare `:root`; dark values apply under
`prefers-color-scheme: dark` unless `<html data-theme="light">`, and always
under `data-theme="dark"`. Products offer 跟随系统 / 浅色 / 深色 (System /
Light / Dark) and store the choice locally.

## Contrast table

Computed by `python3 scripts/contrast.py` (WCAG 2.x relative luminance).
Targets: 4.5:1 for text, 3:1 for large text, UI boundaries and chart marks.
"info only" rows are not used as text and are listed to show why.

| Theme | Foreground | Background | Ratio | Target | Result |
|---|---|---|---|---|---|
| light | label-1 `#1D1D1F` | bg `#FBFBFD` | 16.28:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | bg-elevated `#FFFFFF` | 16.83:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | bg-grouped `#F5F5F7` | 15.46:1 | 4.5:1 | pass |
| light | label-2 `#656569` | bg `#FBFBFD` | 5.61:1 | 4.5:1 | pass |
| light | label-2 `#656569` | bg-elevated `#FFFFFF` | 5.80:1 | 4.5:1 | pass |
| light | label-2 `#656569` | bg-grouped `#F5F5F7` | 5.33:1 | 4.5:1 | pass |
| light | label-3 `#86868B` | bg `#FBFBFD` | 3.51:1 | 3.0:1 | pass |
| light | label-3 `#86868B` | bg-elevated `#FFFFFF` | 3.62:1 | 3.0:1 | pass |
| light | label-3 `#86868B` | bg-grouped `#F5F5F7` | 3.33:1 | 3.0:1 | pass |
| light | accent `#4753E8` | bg `#FBFBFD` | 5.54:1 | 4.5:1 | pass |
| light | accent `#4753E8` | bg-elevated `#FFFFFF` | 5.72:1 | 4.5:1 | pass |
| light | accent `#4753E8` | bg-grouped `#F5F5F7` | 5.25:1 | 4.5:1 | pass |
| light | success `#1A7537` | bg `#FBFBFD` | 5.58:1 | 4.5:1 | pass |
| light | success `#1A7537` | bg-elevated `#FFFFFF` | 5.76:1 | 4.5:1 | pass |
| light | success `#1A7537` | bg-grouped `#F5F5F7` | 5.29:1 | 4.5:1 | pass |
| light | warning `#A24F00` | bg `#FBFBFD` | 5.56:1 | 4.5:1 | pass |
| light | warning `#A24F00` | bg-elevated `#FFFFFF` | 5.75:1 | 4.5:1 | pass |
| light | warning `#A24F00` | bg-grouped `#F5F5F7` | 5.28:1 | 4.5:1 | pass |
| light | danger `#CF0015` | bg `#FBFBFD` | 5.55:1 | 4.5:1 | pass |
| light | danger `#CF0015` | bg-elevated `#FFFFFF` | 5.73:1 | 4.5:1 | pass |
| light | danger `#CF0015` | bg-grouped `#F5F5F7` | 5.26:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | fill-1/bg `#F1F1F3` | 14.92:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | fill-1/bg-elevated `#F4F4F5` | 15.31:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | fill-1/bg-grouped `#EBEBED` | 14.14:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | fill-2/bg `#EBEBEE` | 14.15:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | fill-2/bg-elevated `#EFEFF0` | 14.65:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | fill-2/bg-grouped `#E6E6E9` | 13.51:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | accent-soft/bg `#EAEBFB` | 14.25:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | accent-soft/bg-elevated `#EDEFFD` | 14.72:1 | 4.5:1 | pass |
| light | label-1 `#1D1D1F` | accent-soft/bg-grouped `#E4E6F6` | 13.58:1 | 4.5:1 | pass |
| light | label-2 `#656569` | fill-1/bg `#F1F1F3` | 5.14:1 | 4.5:1 | pass |
| light | label-2 `#656569` | fill-1/bg-elevated `#F4F4F5` | 5.28:1 | 4.5:1 | pass |
| light | label-2 `#656569` | fill-1/bg-grouped `#EBEBED` | 4.87:1 | 4.5:1 | pass |
| light | label-2 `#656569` | fill-2/bg `#EBEBEE` | 4.88:1 | 4.5:1 | pass |
| light | label-2 `#656569` | fill-2/bg-elevated `#EFEFF0` | 5.05:1 | 4.5:1 | pass |
| light | label-2 `#656569` | fill-2/bg-grouped `#E6E6E9` | 4.66:1 | 4.5:1 | pass |
| light | label-2 `#656569` | accent-soft/bg `#EAEBFB` | 4.91:1 | 4.5:1 | pass |
| light | label-2 `#656569` | accent-soft/bg-elevated `#EDEFFD` | 5.08:1 | 4.5:1 | pass |
| light | label-2 `#656569` | accent-soft/bg-grouped `#E4E6F6` | 4.68:1 | 4.5:1 | pass |
| light | accent `#4753E8` | fill-1/bg `#F1F1F3` | 5.07:1 | 4.5:1 | pass |
| light | accent `#4753E8` | fill-1/bg-elevated `#F4F4F5` | 5.21:1 | 4.5:1 | pass |
| light | accent `#4753E8` | fill-1/bg-grouped `#EBEBED` | 4.81:1 | 4.5:1 | pass |
| light | accent `#4753E8` | fill-2/bg `#EBEBEE` | 4.81:1 | 4.5:1 | pass |
| light | accent `#4753E8` | fill-2/bg-elevated `#EFEFF0` | 4.98:1 | 4.5:1 | pass |
| light | accent `#4753E8` | fill-2/bg-grouped `#E6E6E9` | 4.59:1 | 4.5:1 | pass |
| light | accent `#4753E8` | accent-soft/bg `#EAEBFB` | 4.84:1 | 4.5:1 | pass |
| light | accent `#4753E8` | accent-soft/bg-elevated `#EDEFFD` | 5.00:1 | 4.5:1 | pass |
| light | accent `#4753E8` | accent-soft/bg-grouped `#E4E6F6` | 4.62:1 | 4.5:1 | pass |
| light | success `#1A7537` | fill-1/bg `#F1F1F3` | 5.11:1 | 4.5:1 | pass |
| light | success `#1A7537` | fill-1/bg-elevated `#F4F4F5` | 5.24:1 | 4.5:1 | pass |
| light | success `#1A7537` | fill-1/bg-grouped `#EBEBED` | 4.84:1 | 4.5:1 | pass |
| light | success `#1A7537` | fill-2/bg `#EBEBEE` | 4.84:1 | 4.5:1 | pass |
| light | success `#1A7537` | fill-2/bg-elevated `#EFEFF0` | 5.02:1 | 4.5:1 | pass |
| light | success `#1A7537` | fill-2/bg-grouped `#E6E6E9` | 4.63:1 | 4.5:1 | pass |
| light | success `#1A7537` | accent-soft/bg `#EAEBFB` | 4.88:1 | 4.5:1 | pass |
| light | success `#1A7537` | accent-soft/bg-elevated `#EDEFFD` | 5.04:1 | 4.5:1 | pass |
| light | success `#1A7537` | accent-soft/bg-grouped `#E4E6F6` | 4.65:1 | 4.5:1 | pass |
| light | success `#1A7537` | success-soft/bg `#E4EFE9` | 4.89:1 | 4.5:1 | pass |
| light | success `#1A7537` | success-soft/bg-elevated `#E8F2EB` | 5.03:1 | 4.5:1 | pass |
| light | success `#1A7537` | success-soft/bg-grouped `#DFE9E4` | 4.64:1 | 4.5:1 | pass |
| light | warning `#A24F00` | fill-1/bg `#F1F1F3` | 5.09:1 | 4.5:1 | pass |
| light | warning `#A24F00` | fill-1/bg-elevated `#F4F4F5` | 5.23:1 | 4.5:1 | pass |
| light | warning `#A24F00` | fill-1/bg-grouped `#EBEBED` | 4.83:1 | 4.5:1 | pass |
| light | warning `#A24F00` | fill-2/bg `#EBEBEE` | 4.83:1 | 4.5:1 | pass |
| light | warning `#A24F00` | fill-2/bg-elevated `#EFEFF0` | 5.00:1 | 4.5:1 | pass |
| light | warning `#A24F00` | fill-2/bg-grouped `#E6E6E9` | 4.61:1 | 4.5:1 | pass |
| light | warning `#A24F00` | accent-soft/bg `#EAEBFB` | 4.86:1 | 4.5:1 | pass |
| light | warning `#A24F00` | accent-soft/bg-elevated `#EDEFFD` | 5.03:1 | 4.5:1 | pass |
| light | warning `#A24F00` | accent-soft/bg-grouped `#E4E6F6` | 4.64:1 | 4.5:1 | pass |
| light | warning `#A24F00` | warning-soft/bg `#F4EAE4` | 4.85:1 | 4.5:1 | pass |
| light | warning `#A24F00` | warning-soft/bg-elevated `#F7EEE6` | 5.01:1 | 4.5:1 | pass |
| light | warning `#A24F00` | warning-soft/bg-grouped `#EEE4DE` | 4.59:1 | 4.5:1 | pass |
| light | danger `#CF0015` | fill-1/bg `#F1F1F3` | 5.08:1 | 4.5:1 | pass |
| light | danger `#CF0015` | fill-1/bg-elevated `#F4F4F5` | 5.21:1 | 4.5:1 | pass |
| light | danger `#CF0015` | fill-1/bg-grouped `#EBEBED` | 4.81:1 | 4.5:1 | pass |
| light | danger `#CF0015` | fill-2/bg `#EBEBEE` | 4.82:1 | 4.5:1 | pass |
| light | danger `#CF0015` | fill-2/bg-elevated `#EFEFF0` | 4.99:1 | 4.5:1 | pass |
| light | danger `#CF0015` | fill-2/bg-grouped `#E6E6E9` | 4.60:1 | 4.5:1 | pass |
| light | danger `#CF0015` | accent-soft/bg `#EAEBFB` | 4.85:1 | 4.5:1 | pass |
| light | danger `#CF0015` | accent-soft/bg-elevated `#EDEFFD` | 5.01:1 | 4.5:1 | pass |
| light | danger `#CF0015` | accent-soft/bg-grouped `#E4E6F6` | 4.63:1 | 4.5:1 | pass |
| light | danger `#CF0015` | danger-soft/bg `#F8E7EA` | 4.81:1 | 4.5:1 | pass |
| light | danger `#CF0015` | danger-soft/bg-elevated `#FCEBEC` | 4.98:1 | 4.5:1 | pass |
| light | danger `#CF0015` | danger-soft/bg-grouped `#F3E1E5` | 4.56:1 | 4.5:1 | pass |
| light | on-accent `#FFFFFF` | accent-fill `#4F5BE8` | 5.26:1 | 4.5:1 | pass |
| light | on-accent `#FFFFFF` | accent-fill-hover `#4350DD` | 6.12:1 | 4.5:1 | pass |
| light | on-danger `#FFFFFF` | danger-fill `#D70015` | 5.38:1 | 4.5:1 | pass |
| light | accent-fill `#4F5BE8` | bg-elevated `#FFFFFF` | 5.26:1 | 3.0:1 | pass |
| light | chart-1 `#4F5BE8` | bg-elevated `#FFFFFF` | 5.26:1 | 3.0:1 | pass |
| light | chart-2 `#0891B2` | bg-elevated `#FFFFFF` | 3.68:1 | 3.0:1 | pass |
| light | chart-3 `#8B5CF6` | bg-elevated `#FFFFFF` | 4.23:1 | 3.0:1 | pass |
| light | chart-4 `#DB2777` | bg-elevated `#FFFFFF` | 4.60:1 | 3.0:1 | pass |
| light | chart-5 `#EA580C` | bg-elevated `#FFFFFF` | 3.56:1 | 3.0:1 | pass |
| light | chart-6 `#A16207` | bg-elevated `#FFFFFF` | 4.92:1 | 3.0:1 | pass |
| light | chart-7 `#16A34A` | bg-elevated `#FFFFFF` | 3.30:1 | 3.0:1 | pass |
| light | chart-8 `#8E8E93` | bg-elevated `#FFFFFF` | 3.26:1 | 3.0:1 | pass |
| dark | label-1 `#F5F5F7` | bg `#000000` | 19.29:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | bg-elevated `#1C1C1E` | 15.63:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | bg-grouped `#111113` | 17.32:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | bg `#000000` | 8.16:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | bg-elevated `#1C1C1E` | 6.61:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | bg-grouped `#111113` | 7.33:1 | 4.5:1 | pass |
| dark | label-3 `#8E8E93` | bg `#000000` | 6.44:1 | 3.0:1 | pass |
| dark | label-3 `#8E8E93` | bg-elevated `#1C1C1E` | 5.22:1 | 3.0:1 | pass |
| dark | label-3 `#8E8E93` | bg-grouped `#111113` | 5.78:1 | 3.0:1 | pass |
| dark | accent `#8994F8` | bg `#000000` | 7.66:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | bg-elevated `#1C1C1E` | 6.20:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | bg-grouped `#111113` | 6.88:1 | 4.5:1 | pass |
| dark | success `#30D158` | bg `#000000` | 10.39:1 | 4.5:1 | pass |
| dark | success `#30D158` | bg-elevated `#1C1C1E` | 8.42:1 | 4.5:1 | pass |
| dark | success `#30D158` | bg-grouped `#111113` | 9.33:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | bg `#000000` | 10.22:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | bg-elevated `#1C1C1E` | 8.28:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | bg-grouped `#111113` | 9.18:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | bg `#000000` | 7.62:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | bg-elevated `#1C1C1E` | 6.17:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | bg-grouped `#111113` | 6.84:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | fill-1/bg `#131314` | 17.05:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | fill-1/bg-elevated `#2B2B2E` | 12.96:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | fill-1/bg-grouped `#212124` | 14.75:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | fill-2/bg `#1D1D1F` | 15.46:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | fill-2/bg-elevated `#323236` | 11.72:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | fill-2/bg-grouped `#2A2A2D` | 13.14:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | accent-soft/bg `#17192D` | 15.89:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | accent-soft/bg-elevated `#2E3045` | 11.87:1 | 4.5:1 | pass |
| dark | label-1 `#F5F5F7` | accent-soft/bg-grouped `#25273C` | 13.45:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | fill-1/bg `#131314` | 7.22:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | fill-1/bg-elevated `#2B2B2E` | 5.49:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | fill-1/bg-grouped `#212124` | 6.24:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | fill-2/bg `#1D1D1F` | 6.54:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | fill-2/bg-elevated `#323236` | 4.96:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | fill-2/bg-grouped `#2A2A2D` | 5.56:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | accent-soft/bg `#17192D` | 6.73:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | accent-soft/bg-elevated `#2E3045` | 5.02:1 | 4.5:1 | pass |
| dark | label-2 `#A1A1A6` | accent-soft/bg-grouped `#25273C` | 5.69:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | fill-1/bg `#131314` | 6.77:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | fill-1/bg-elevated `#2B2B2E` | 5.15:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | fill-1/bg-grouped `#212124` | 5.85:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | fill-2/bg `#1D1D1F` | 6.14:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | fill-2/bg-elevated `#323236` | 4.65:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | fill-2/bg-grouped `#2A2A2D` | 5.22:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | accent-soft/bg `#17192D` | 6.31:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | accent-soft/bg-elevated `#2E3045` | 4.71:1 | 4.5:1 | pass |
| dark | accent `#8994F8` | accent-soft/bg-grouped `#25273C` | 5.34:1 | 4.5:1 | pass |
| dark | success `#30D158` | fill-1/bg `#131314` | 9.18:1 | 4.5:1 | pass |
| dark | success `#30D158` | fill-1/bg-elevated `#2B2B2E` | 6.98:1 | 4.5:1 | pass |
| dark | success `#30D158` | fill-1/bg-grouped `#212124` | 7.94:1 | 4.5:1 | pass |
| dark | success `#30D158` | fill-2/bg `#1D1D1F` | 8.32:1 | 4.5:1 | pass |
| dark | success `#30D158` | fill-2/bg-elevated `#323236` | 6.31:1 | 4.5:1 | pass |
| dark | success `#30D158` | fill-2/bg-grouped `#2A2A2D` | 7.08:1 | 4.5:1 | pass |
| dark | success `#30D158` | accent-soft/bg `#17192D` | 8.56:1 | 4.5:1 | pass |
| dark | success `#30D158` | accent-soft/bg-elevated `#2E3045` | 6.39:1 | 4.5:1 | pass |
| dark | success `#30D158` | accent-soft/bg-grouped `#25273C` | 7.24:1 | 4.5:1 | pass |
| dark | success `#30D158` | success-soft/bg `#08210E` | 8.42:1 | 4.5:1 | pass |
| dark | success `#30D158` | success-soft/bg-elevated `#1F3927` | 6.21:1 | 4.5:1 | pass |
| dark | success `#30D158` | success-soft/bg-grouped `#16301E` | 7.04:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | fill-1/bg `#131314` | 9.03:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | fill-1/bg-elevated `#2B2B2E` | 6.87:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | fill-1/bg-grouped `#212124` | 7.81:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | fill-2/bg `#1D1D1F` | 8.19:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | fill-2/bg-elevated `#323236` | 6.21:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | fill-2/bg-grouped `#2A2A2D` | 6.96:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | accent-soft/bg `#17192D` | 8.42:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | accent-soft/bg-elevated `#2E3045` | 6.29:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | accent-soft/bg-grouped `#25273C` | 7.12:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | warning-soft/bg `#291902` | 8.28:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | warning-soft/bg-elevated `#40311B` | 6.11:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | warning-soft/bg-grouped `#372812` | 6.93:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | fill-1/bg `#131314` | 6.73:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | fill-1/bg-elevated `#2B2B2E` | 5.12:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | fill-1/bg-grouped `#212124` | 5.82:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | fill-2/bg `#1D1D1F` | 6.10:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | fill-2/bg-elevated `#323236` | 4.63:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | fill-2/bg-grouped `#2A2A2D` | 5.19:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | accent-soft/bg `#17192D` | 6.28:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | accent-soft/bg-elevated `#2E3045` | 4.69:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | accent-soft/bg-grouped `#25273C` | 5.31:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | danger-soft/bg `#290B09` | 6.65:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | danger-soft/bg-elevated `#402322` | 5.14:1 | 4.5:1 | pass |
| dark | danger `#FF6D62` | danger-soft/bg-grouped `#371919` | 5.79:1 | 4.5:1 | pass |
| dark | on-accent `#FFFFFF` | accent-fill `#5B63E6` | 4.80:1 | 4.5:1 | pass |
| dark | on-accent `#FFFFFF` | accent-fill-hover `#5058DC` | 5.57:1 | 4.5:1 | pass |
| dark | on-danger `#FFFFFF` | danger-fill `#E0242F` | 4.71:1 | 4.5:1 | pass |
| dark | accent-fill `#5B63E6` | bg-elevated `#1C1C1E` | 3.54:1 | 3.0:1 | pass |
| dark | chart-1 `#818CF8` | bg-elevated `#1C1C1E` | 5.70:1 | 3.0:1 | pass |
| dark | chart-2 `#22D3EE` | bg-elevated `#1C1C1E` | 9.42:1 | 3.0:1 | pass |
| dark | chart-3 `#A78BFA` | bg-elevated `#1C1C1E` | 6.25:1 | 3.0:1 | pass |
| dark | chart-4 `#F472B6` | bg-elevated `#1C1C1E` | 6.42:1 | 3.0:1 | pass |
| dark | chart-5 `#FB923C` | bg-elevated `#1C1C1E` | 7.52:1 | 3.0:1 | pass |
| dark | chart-6 `#FACC15` | bg-elevated `#1C1C1E` | 11.11:1 | 3.0:1 | pass |
| dark | chart-7 `#4ADE80` | bg-elevated `#1C1C1E` | 9.76:1 | 3.0:1 | pass |
| dark | chart-8 `#8E8E93` | bg-elevated `#1C1C1E` | 5.22:1 | 3.0:1 | pass |
| light | `#FFFFFF` | accent `#4753E8` | 5.72:1 | 4.5:1 | pass |
| dark | `#FFFFFF` | accent `#8994F8` | 2.74:1 | — | info only |
| dark | `#000000` | accent `#8994F8` | 7.66:1 | — | info only |
| light | brand.gradient-start `#0EA5E9` | `#FFFFFF` | 2.77:1 | — | info only |
| light | brand.gradient-end `#6366F1` | `#FFFFFF` | 4.47:1 | — | info only |
| light | `#FFFFFF` | brand.gradient-start `#0EA5E9` | 2.77:1 | — | info only |
| light | `#FFFFFF` | brand.gradient-end `#6366F1` | 4.47:1 | — | info only |
| light | brand.purple `#8B5CF6` | `#FFFFFF` | 4.23:1 | 3.0:1 | pass |
| light | brand.amber `#F59E0B` | `#FFFFFF` | 2.15:1 | — | info only |
| dark | brand.purple `#8B5CF6` | `#000000` | 4.96:1 | 3.0:1 | pass |
| dark | brand.amber `#F59E0B` | `#000000` | 9.78:1 | 3.0:1 | pass |
| light | `#1E8E3E` | `#FFFFFF` | 4.21:1 | — | info only |
| dark | `#0EA5E9` | brand.slate-900 `#0F172A` | 6.44:1 | 3.0:1 | pass |
| dark | `#3886ED` | brand.slate-900 `#0F172A` | 4.93:1 | 3.0:1 | pass |
| dark | `#6366F1` | brand.slate-900 `#0F172A` | 4.00:1 | 3.0:1 | pass |

### Terminal

Truecolor values and their xterm-256 fallbacks on typical terminal backgrounds
([terminal](terminal.md)). The check also fails if a 256 index is not the
nearest one to its truecolor value.

| Role | Terminal | Colour | Background | Ratio | Target | Result |
|---|---|---|---|---|---|---|
| accent | light truecolor | `#4F5BE8` | `#FFFFFF` | 5.26:1 | 4.5:1 | pass |
| accent | light 256 (62) | `#5F5FD7` | `#FFFFFF` | 5.12:1 | 4.5:1 | pass |
| accent | dark truecolor | `#818CF8` | `#000000` | 7.04:1 | 4.5:1 | pass |
| accent | dark truecolor | `#818CF8` | `#1C1C1E` | 5.70:1 | 4.5:1 | pass |
| accent | dark 256 (105) | `#8787FF` | `#000000` | 6.94:1 | 4.5:1 | pass |
| accent | dark 256 (105) | `#8787FF` | `#1C1C1E` | 5.62:1 | 4.5:1 | pass |
| success | light truecolor | `#1A7F37` | `#FFFFFF` | 5.08:1 | 4.5:1 | pass |
| success | light 256 (29) | `#00875F` | `#FFFFFF` | 4.53:1 | 4.5:1 | pass |
| success | dark truecolor | `#30D158` | `#000000` | 10.39:1 | 4.5:1 | pass |
| success | dark truecolor | `#30D158` | `#1C1C1E` | 8.42:1 | 4.5:1 | pass |
| success | dark 256 (41) | `#00D75F` | `#000000` | 10.89:1 | 4.5:1 | pass |
| success | dark 256 (41) | `#00D75F` | `#1C1C1E` | 8.82:1 | 4.5:1 | pass |
| warning | light truecolor | `#B25000` | `#FFFFFF` | 5.20:1 | 4.5:1 | pass |
| warning | light 256 (130) | `#AF5F00` | `#FFFFFF` | 4.71:1 | 4.5:1 | pass |
| warning | dark truecolor | `#FF9F0A` | `#000000` | 10.22:1 | 4.5:1 | pass |
| warning | dark truecolor | `#FF9F0A` | `#1C1C1E` | 8.28:1 | 4.5:1 | pass |
| warning | dark 256 (214) | `#FFAF00` | `#000000` | 11.38:1 | 4.5:1 | pass |
| warning | dark 256 (214) | `#FFAF00` | `#1C1C1E` | 9.22:1 | 4.5:1 | pass |
| danger | light truecolor | `#D70015` | `#FFFFFF` | 5.38:1 | 4.5:1 | pass |
| danger | light 256 (160) | `#D70000` | `#FFFFFF` | 5.40:1 | 4.5:1 | pass |
| danger | dark truecolor | `#FF453A` | `#000000` | 6.16:1 | 4.5:1 | pass |
| danger | dark truecolor | `#FF453A` | `#1C1C1E` | 4.99:1 | 4.5:1 | pass |
| danger | dark 256 (203) | `#FF5F5F` | `#000000` | 7.05:1 | 4.5:1 | pass |
| danger | dark 256 (203) | `#FF5F5F` | `#1C1C1E` | 5.72:1 | 4.5:1 | pass |
| muted | light truecolor | `#6E6E73` | `#FFFFFF` | 5.07:1 | 4.5:1 | pass |
| muted | light 256 (242) | `#6C6C6C` | `#FFFFFF` | 5.25:1 | 4.5:1 | pass |
| muted | dark truecolor | `#8E8E93` | `#000000` | 6.44:1 | 4.5:1 | pass |
| muted | dark truecolor | `#8E8E93` | `#1C1C1E` | 5.22:1 | 4.5:1 | pass |
| muted | dark 256 (246) | `#949494` | `#000000` | 6.92:1 | 4.5:1 | pass |
| muted | dark 256 (246) | `#949494` | `#1C1C1E` | 5.61:1 | 4.5:1 | pass |
| brand-start | light truecolor | `#0EA5E9` | `#FFFFFF` | 2.77:1 | — | info only |
| brand-start | light 256 (38) | `#00AFD7` | `#FFFFFF` | 2.59:1 | — | info only |
| brand-start | dark truecolor | `#0EA5E9` | `#000000` | 7.58:1 | — | info only |
| brand-start | dark truecolor | `#0EA5E9` | `#1C1C1E` | 6.14:1 | — | info only |
| brand-start | dark 256 (38) | `#00AFD7` | `#000000` | 8.11:1 | — | info only |
| brand-start | dark 256 (38) | `#00AFD7` | `#1C1C1E` | 6.57:1 | — | info only |
| brand-end | light truecolor | `#6366F1` | `#FFFFFF` | 4.47:1 | — | info only |
| brand-end | light 256 (63) | `#5F5FFF` | `#FFFFFF` | 4.60:1 | — | info only |
| brand-end | dark truecolor | `#6366F1` | `#000000` | 4.70:1 | — | info only |
| brand-end | dark truecolor | `#6366F1` | `#1C1C1E` | 3.81:1 | — | info only |
| brand-end | dark 256 (63) | `#5F5FFF` | `#000000` | 4.57:1 | — | info only |
| brand-end | dark 256 (63) | `#5F5FFF` | `#1C1C1E` | 3.70:1 | — | info only |

### Pairs below 4.5:1 and where they are allowed

| Pair | Ratio | Allowed use |
|---|---|---|
| `--label-3` on light backgrounds | 3.33–3.62:1 | Non-essential text ≥ 14 px only (placeholders, secondary timestamps) |
| Chart colours, `--accent-fill` as a boundary | 3.26–5.26:1 vs 3:1 target | Graphics and control boundaries, not text |
| White on `#0EA5E9` / `#6366F1` | 2.77 / 4.47:1 | Not used for text. Since 1.1.0 the logo puts the gradient on the glyph over slate `#0F172A`, checked at ≥ 3:1 (the last three rows of the table above) |
| White on dark `#8994F8` | 2.74:1 | Not used: dark filled buttons use `--accent-fill` `#5B63E6` |
| Amber `#F59E0B` on white | 2.15:1 | Illustrations in dark contexts only |
| `#1E8E3E` on white | 4.21:1 | Not used: replaced by `#1A7537` |
