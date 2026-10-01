# Motion

Motion explains a change of state: something opened, closed, moved or loaded.
It never decorates.

| Token | Value | Use |
|---|---|---|
| `--dur-micro` | 120 ms | Hover, press, switch thumb |
| `--dur-toggle` | 200 ms | Segmented control, expand/collapse, tab change |
| `--dur-overlay` | 280 ms | Dialogs, sheets, drawers |
| `--dur-page` | 240 ms | Page change: fade in + 8 px rise |
| `--ease-standard` | `cubic-bezier(.25,.1,.25,1)` | Most transitions |
| `--ease-emphasized` | `cubic-bezier(.2,.8,.2,1)` | Entering overlays |
| `--ease-exit` | `cubic-bezier(.4,0,1,1)` | Leaving overlays |

Rules:

- Animate `opacity` and `transform` only.
- No infinite loops; loading uses skeletons, not spinners on large areas
  (a small inline spinner in a busy button is fine).
- `prefers-reduced-motion: reduce`: remove translation and scale; keep
  opacity changes of 100 ms or less.
- No scroll-driven parallax.
