# Typography

## Font stacks

```css
--font-sans: -apple-system, BlinkMacSystemFont, Inter, "Segoe UI", "PingFang SC",
             "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", system-ui, sans-serif;
--font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
```

These two are for **web products** (panel, sites, documentation).

- Apple devices render their system font through `-apple-system`; nothing is
  bundled.
- **Inter** is self-hosted from [`../fonts/inter/`](../fonts/inter/) (variable WOFF2, Latin subset only,
  `font-display: swap`, `unicode-range` limited to Latin) so non-Apple
  platforms get a close, neutral sans.
- **Chinese** always comes from the system: PingFang SC (Apple), Microsoft
  YaHei (Windows), Noto Sans SC (Linux, Android). No CJK web font.

### Client applications

Installed clients (desktop and mobile apps, whether native or in a web view)
use the platform's own interface font and do not load Inter:

```css
--font-app: -apple-system, BlinkMacSystemFont, "Segoe UI Variable Text", "Segoe UI Variable",
            "Segoe UI", system-ui, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI",
            "Microsoft YaHei", "Noto Sans CJK SC", "Noto Sans SC", sans-serif;
--font-app-mono: ui-monospace, "SF Mono", "Cascadia Mono", "JetBrains Mono", Menlo, Consolas,
                 "DejaVu Sans Mono", monospace;
```

- A client is read next to the system's own applications, and its text is
  mostly Chinese. Inter has no Chinese glyphs, so it would sit beside a
  system Chinese font whose weight and baseline do not match; the platform
  pairs (San Francisco with PingFang SC, Segoe UI Variable with Microsoft
  YaHei UI, Roboto with Noto Sans) are designed together.
- Native toolkits (SwiftUI, WinUI, GTK, Compose) already default to these
  fonts: leave the default. A web-view client sets `--font-app` and
  `--font-app-mono` in place of `--font-sans` and `--font-mono`.
- Sizes, weights and the rules below are the same as on the web.

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
