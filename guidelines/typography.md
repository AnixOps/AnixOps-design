# Typography

## Font stacks

```css
--font-sans: -apple-system, BlinkMacSystemFont, Inter, "Segoe UI", "PingFang SC",
             "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", system-ui, sans-serif;
--font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
```

- Apple devices render their system font through `-apple-system`; nothing is
  bundled.
- **Inter** is self-hosted from [`../fonts/inter/`](../fonts/inter/) (variable WOFF2, Latin subset only,
  `font-display: swap`, `unicode-range` limited to Latin) so non-Apple
  platforms get a close, neutral sans.
- **Chinese** always comes from the system: PingFang SC (Apple), Microsoft
  YaHei (Windows), Noto Sans SC (Linux, Android). No CJK web font.

## Scale

| Token | Size / line | Weight | Tracking | Use |
|---|---|---|---|---|
| `--type-display-*` | 48 / 1.08 (below 834 px: 34) | 700 | −0.015em | User home headline, login |
| `--type-title-1-*` | 32 / 1.125 (below 834 px: 28) | 700 | −0.01em | Page H1, one per page |
| `--type-title-2-*` | 24 / 1.17 | 600 | −0.005em | Section heading |
| `--type-title-3-*` | 19 / 1.26 | 600 | 0 | Card, sheet and dialog titles |
| `--type-body-*` | 15 / 1.47 | 400 | 0 | Body, tables, form values |
| `--type-callout-*` | 13 / 1.38 | 400 | 0 | Labels, table headers, help text |
| `--type-caption-*` | 12 / 1.33 | 500 | 0 | Badges, timestamps |

Only these seven sizes. Form inputs are at least 16 px on phones to stop iOS
zooming.

## Rules

- `font-variant-numeric: tabular-nums` on every number: tables, traffic,
  money, dates, counters.
- Chinese paragraphs: line height 1.6, no letter spacing, full-width
  punctuation. A space between a number and its unit (`128.4 GB`); no manual
  spaces between Chinese and Latin words.
- Line length: 692 px maximum for reading text.
- Weight carries hierarchy before colour: title 600–700, body 400; avoid
  more than two weights in one component.
- Never use all caps for Chinese; for Latin sidebar group titles use
  small caps size (caption) with +0.04em tracking.
