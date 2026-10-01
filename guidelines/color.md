# Colour

> DRAFT — pending owner approval. Values live in
> [`../tokens/tokens.json`](../tokens/tokens.json); this page explains them.

## Rules

1. **Neutrals carry the interface.** Large areas are `--bg`, `--bg-elevated`
   and `--bg-grouped`; text is `--label-1/2/3`. Colour is the exception.
2. **One accent.** `--accent` marks what is interactive or selected: links,
   the primary button, focus rings, the selected item. Never decoration.
3. **Status colours only for status.** Success, warning and danger appear on
   badges, inline alerts, chart thresholds and destructive actions, and always
   with a word or icon (never colour alone).
4. **The brand gradient only for brand moments**: logo tile, login backdrop,
   user home hero numbers. Never on controls or text.
5. **Filled controls use `-fill` tokens.** `--accent-fill` and
   `--danger-fill` exist because the dark text colours (`#818CF8`, `#FF453A`)
   are too light for white text.
6. **Dark mode is pure black** (`#000`) with `#1C1C1E` cards; layers are
   separated by a 1px highlight edge, not heavier shadows.
7. **Charts** use `--chart-1` … `--chart-8` in order; every series colour is at
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
| light | label-2 `#6E6E73` | bg `#FBFBFD` | 4.91:1 | 4.5:1 | pass |
| light | label-2 `#6E6E73` | bg-elevated `#FFFFFF` | 5.07:1 | 4.5:1 | pass |
| light | label-2 `#6E6E73` | bg-grouped `#F5F5F7` | 4.66:1 | 4.5:1 | pass |
| light | label-3 `#86868B` | bg `#FBFBFD` | 3.51:1 | 3.0:1 | pass |
| light | label-3 `#86868B` | bg-elevated `#FFFFFF` | 3.62:1 | 3.0:1 | pass |
| light | label-3 `#86868B` | bg-grouped `#F5F5F7` | 3.33:1 | 3.0:1 | pass |
| light | accent `#4F5BE8` | bg `#FBFBFD` | 5.09:1 | 4.5:1 | pass |
| light | accent `#4F5BE8` | bg-elevated `#FFFFFF` | 5.26:1 | 4.5:1 | pass |
| light | accent `#4F5BE8` | bg-grouped `#F5F5F7` | 4.83:1 | 4.5:1 | pass |
| light | success `#1A7F37` | bg `#FBFBFD` | 4.91:1 | 4.5:1 | pass |
| light | success `#1A7F37` | bg-elevated `#FFFFFF` | 5.08:1 | 4.5:1 | pass |
| light | success `#1A7F37` | bg-grouped `#F5F5F7` | 4.66:1 | 4.5:1 | pass |
| light | warning `#B25000` | bg `#FBFBFD` | 5.03:1 | 4.5:1 | pass |
| light | warning `#B25000` | bg-elevated `#FFFFFF` | 5.20:1 | 4.5:1 | pass |
| light | warning `#B25000` | bg-grouped `#F5F5F7` | 4.77:1 | 4.5:1 | pass |
| light | danger `#D70015` | bg `#FBFBFD` | 5.21:1 | 4.5:1 | pass |
| light | danger `#D70015` | bg-elevated `#FFFFFF` | 5.38:1 | 4.5:1 | pass |
| light | danger `#D70015` | bg-grouped `#F5F5F7` | 4.94:1 | 4.5:1 | pass |
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
| dark | accent `#818CF8` | bg `#000000` | 7.04:1 | 4.5:1 | pass |
| dark | accent `#818CF8` | bg-elevated `#1C1C1E` | 5.70:1 | 4.5:1 | pass |
| dark | accent `#818CF8` | bg-grouped `#111113` | 6.32:1 | 4.5:1 | pass |
| dark | success `#30D158` | bg `#000000` | 10.39:1 | 4.5:1 | pass |
| dark | success `#30D158` | bg-elevated `#1C1C1E` | 8.42:1 | 4.5:1 | pass |
| dark | success `#30D158` | bg-grouped `#111113` | 9.33:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | bg `#000000` | 10.22:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | bg-elevated `#1C1C1E` | 8.28:1 | 4.5:1 | pass |
| dark | warning `#FF9F0A` | bg-grouped `#111113` | 9.18:1 | 4.5:1 | pass |
| dark | danger `#FF453A` | bg `#000000` | 6.16:1 | 4.5:1 | pass |
| dark | danger `#FF453A` | bg-elevated `#1C1C1E` | 4.99:1 | 4.5:1 | pass |
| dark | danger `#FF453A` | bg-grouped `#111113` | 5.54:1 | 4.5:1 | pass |
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
| light | `#FFFFFF` | accent `#4F5BE8` | 5.26:1 | 4.5:1 | pass |
| dark | `#FFFFFF` | accent `#818CF8` | 2.98:1 | — | info only |
| dark | `#000000` | accent `#818CF8` | 7.04:1 | — | info only |
| light | brand.gradient-start `#38BDF8` | `#FFFFFF` | 2.14:1 | — | info only |
| light | brand.gradient-end `#6366F1` | `#FFFFFF` | 4.47:1 | — | info only |
| light | `#FFFFFF` | brand.gradient-start `#38BDF8` | 2.14:1 | — | info only |
| light | `#FFFFFF` | brand.gradient-end `#6366F1` | 4.47:1 | — | info only |
| light | brand.purple `#8B5CF6` | `#FFFFFF` | 4.23:1 | 3.0:1 | pass |
| light | brand.amber `#F59E0B` | `#FFFFFF` | 2.15:1 | — | info only |
| dark | brand.purple `#8B5CF6` | `#000000` | 4.96:1 | 3.0:1 | pass |
| dark | brand.amber `#F59E0B` | `#000000` | 9.78:1 | 3.0:1 | pass |
| light | `#1E8E3E` | `#FFFFFF` | 4.21:1 | — | info only |

### Pairs below 4.5:1 and where they are allowed

| Pair | Ratio | Allowed use |
|---|---|---|
| `--label-3` on light backgrounds | 3.33–3.62:1 | Non-essential text ≥ 14 px only (placeholders, secondary timestamps) |
| Chart colours, `--accent-fill` as a boundary | 3.26–5.26:1 vs 3:1 target | Graphics and control boundaries, not text |
| White on `#38BDF8` / `#6366F1` | 2.14 / 4.47:1 | The logo only (logotypes are exempt) |
| White on dark `#818CF8` | 2.98:1 | Not used: dark filled buttons use `--accent-fill` `#5B63E6` |
| Amber `#F59E0B` on white | 2.15:1 | Illustrations in dark contexts only |
| `#1E8E3E` on white | 4.21:1 | Not used: replaced by `#1A7F37` |
