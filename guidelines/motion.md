# Motion

Motion explains a change of state: something opened, closed, moved or loaded.
It never decorates. AnixOps products are tools that show live data, so most
of what changes on screen changes **without** animation; motion is kept for
what the user did and for where things went.

Rules are numbered (`M1`, …) like those in [`actions.md`](actions.md):
a number is never reused or renumbered, so a review can cite it.

## Tokens

| Token | Value | Use |
|---|---|---|
| `--dur-micro` | 120 ms | Hover, press, switch thumb |
| `--dur-toggle` | 200 ms | Segmented control, expand/collapse, tab change |
| `--dur-overlay` | 280 ms | Dialogs, sheets, drawers |
| `--dur-page` | 240 ms | Page change: fade in + 8 px rise |
| `--ease-standard` | `cubic-bezier(.25,.1,.25,1)` | Most transitions |
| `--ease-emphasized` | `cubic-bezier(.2,.8,.2,1)` | Entering overlays |
| `--ease-exit` | `cubic-bezier(.4,0,1,1)` | Leaving overlays |

## 1. Basics

- **M1** Animate `opacity` and `transform` only. Never animate layout
  (width, height, margins) on a list or a table.
- **M2** No infinite loops; loading uses skeletons, not spinners on large
  areas (a small inline spinner in a busy button is fine).
- **M3** `prefers-reduced-motion: reduce` (and the matching system setting on
  every native platform): remove translation and scale; keep opacity changes
  of 100 ms or less.
- **M4** No scroll-driven parallax.
- **M5** Every transition can be interrupted. Input is never blocked while
  something animates: a second click, a key press or a new selection takes
  effect at once and the animation jumps to its end.
- **M6** Leaving is faster than entering. An overlay enters in
  `--dur-overlay` with `--ease-emphasized` and leaves in `--dur-toggle` with
  `--ease-exit`.
- **M7** Only the four durations above are used. A product does not add a
  fifth, and nothing in a tool window lasts longer than 280 ms.

## 2. What moves and what does not

| Change | Motion |
|---|---|
| Hover, press, focus ring | `--dur-micro`; the pressed state shows within 100 ms of the press |
| Switch, segmented control, disclosure, tab | `--dur-toggle`, `--ease-standard` |
| Dialog, sheet, drawer, popover, menu | M6 |
| Page or sidebar section change | `--dur-page` on the web; none in a desktop client window (M9) |
| Selecting a row, moving the selection with arrow keys | None |
| Sorting, filtering, searching, changing columns | None |
| Rows arriving from a live stream (requests, connections, logs) | None |
| A number that updates (speed, traffic, latency, counters) | None; the digits are replaced |
| A row the user added, removed or reordered | `--dur-toggle` fade; the neighbours do not slide in a table |
| Status dot or pill changing state | `--dur-toggle` cross-fade of colour |
| Toast | Enters and leaves like an overlay; never pushes content |

- **M8** Live data does not animate. Rows that arrive from a stream are
  simply there; numbers do not count up, flash or change colour because they
  changed. Colour on a number means status
  ([`color.md`](color.md)), never "this just updated".
- **M9** In a desktop client window, changing page, tab or inspector content
  is immediate: the user switches between them many times a minute. Phone
  navigation uses the system push and pop.
- **M10** Selection is immediate. The highlight follows the pointer or the
  arrow key in the same frame, and the detail pane shows the new item
  without a transition.
- **M11** A live list follows its newest row only while the user is at that
  end. Once they scroll away the list stops following and shows a quiet
  "N 条新记录 / N new" control that jumps back; the row under the pointer
  never moves because new rows arrived.
- **M12** Live values update at a steady rhythm: text at most twice a second,
  charts once a second with the line extended, not redrawn. Faster updates
  are averaged, not shown.
- **M13** Nothing appears, disappears or moves under the pointer because of
  hover ([`actions.md`](actions.md) V3). Row actions that show on hover fade
  in place, in space that was already reserved.

## 3. Feedback timing

- **M14** A press is acknowledged within 100 ms by the control itself
  (pressed state, then busy state in place; `actions.md` V3, F1).
- **M15** A busy indicator or skeleton appears only if the work has taken
  300 ms, and once shown stays for at least 400 ms, so quick work does not
  flicker.
- **M16** A state that takes more than 2 s says what it is doing in words
  ("正在连接…", "正在测速 12 / 40"), and offers cancel if one exists
  (`actions.md` V5). Work with a known length shows progress, not a spinner.
- **M17** Success is shown by the new state, not by an animation: the button
  returns from busy with its new label, the status dot changes. No check
  marks that draw themselves, no confetti, no bouncing.
- **M18** A "copied" confirmation swaps the control's icon or label in place
  for 1.5 s and then returns; it needs no toast.
- **M19** Tooltips appear after 500 ms of rest and at once when the pointer
  moves to a neighbouring control; they leave without a fade.
- **M20** Haptics (phones) mark only the result of the hero action
  (connected, failed) and a destructive confirmation. Lists, tabs and
  switches use the system's own feedback and add none.

## 4. Native platforms

- **M21** Use the system's own transition for system containers: navigation
  push, sheets, alerts, menus, popovers, window resize. Do not replace their
  duration or curve. The tokens govern only the transitions a product
  defines itself.
- **M22** Where a product does define one, it uses the tokens:

  | Token | SwiftUI | WinUI 3 | GTK 4 / libadwaita |
  |---|---|---|---|
  | `--dur-micro` | `.easeOut(duration: 0.12)` | `0:0:0.12` | 120 ms |
  | `--dur-toggle` | `.easeInOut(duration: 0.2)` | `0:0:0.2` | 200 ms |
  | `--dur-overlay` | system | system | system |
  | `--dur-page` | system | none (M9) | none (M9) |

- **M23** `withAnimation`, implicit animations and their equivalents are
  never wrapped around a data refresh. Animate the one property that the
  user changed, not the view that redraws.

## 5. Review checklist

1. Does anything animate that the user did not cause? (M8)
2. Does selection, sorting or switching a tab wait for a transition? (M9, M10)
3. Can every transition be interrupted? (M5)
4. Does quick work flicker a spinner? (M15)
5. Does anything move under the pointer? (M11, M13)
6. Is reduced motion honoured? (M3)
