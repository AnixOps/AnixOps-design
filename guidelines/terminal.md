# Terminal: CLIs and TUIs

AnixOps Agent, the Control Center TUI and every other command-line tool share
one palette, one colour policy and one banner. Values live in the `terminal`
group of [`../tokens/tokens.json`](../tokens/tokens.json); Go and Rust
programs import the generated files instead of copying numbers.

## Palette

Each role has a truecolor value for light and for dark terminal backgrounds,
the nearest xterm-256 colour for each (computed by redmean distance, checked by
`scripts/contrast.py`), and a basic ANSI index that the user's terminal theme
remaps.

| Role | Light truecolor | Dark truecolor | 256 light | 256 dark | ANSI 16 | Use |
|---|---|---|---|---|---|---|
| accent | `#4F5BE8` | `#818CF8` | 62 | 105 | 4 blue | Selection, prompts, links, the focused pane |
| success | `#1A7F37` | `#30D158` | 29 | 41 | 2 green | `✓ done`, healthy status |
| warning | `#B25000` | `#FF9F0A` | 130 | 214 | 3 yellow | Degraded, deprecated flags |
| danger | `#D70015` | `#FF453A` | 160 | 203 | 1 red | Errors, failed checks, destructive prompts |
| muted | `#6E6E73` | `#8E8E93` | 242 | 246 | 8 bright black | Hints, timestamps, secondary columns |
| brand-start | `#0EA5E9` | `#0EA5E9` | 38 | 38 | 6 cyan | Banner gradient only |
| brand-end | `#6366F1` | `#6366F1` | 63 | 63 | 5 magenta | Banner gradient only |

Every text role, truecolor and 256 fallback alike, is at least 4.5:1 on white
(light) and on `#000000` and `#1C1C1E` (dark); see the terminal table printed
by `python3 scripts/contrast.py`. The brand colours are not text colours.

Pick the light or dark value from the terminal background (lipgloss
`AdaptiveColor` does this; otherwise default to dark). Use the 256 value when
`COLORTERM` is not `truecolor`/`24bit`, and the ANSI 16 index when the
terminal only reports 16 colours.

## Colour policy

1. **`NO_COLOR`**: if set to any non-empty value, print no colour, ever
   ([no-color.org](https://no-color.org)).
2. **`--color=auto|always|never`** on every CLI; `auto` is the default.
   Flags win over the environment, except that `NO_COLOR` beats `always`.
3. **`auto`** means colour only when the stream is a terminal and `TERM` is
   not `dumb`. `FORCE_COLOR` (non-empty, not `0`) turns it on for CI logs.
4. **Never colour alone.** Status words or symbols always accompany colour:
   `✓ ok`, `! warning`, `✗ failed`. Output must be complete with colour off.
5. **No background fills** except the selected row in a TUI list
   (`accent` background, white text in truecolor and 256 modes only).
6. **Machine output** (`--json`, `--output yaml`, piped tables) never contains
   ANSI codes.

Go: `anixops.ColorEnabled(isTerminal)` implements rules 1 and 3.

## Banner and `--version`

The three-line ASCII mark ([`../brand/assets/ascii-mark.txt`](../brand/assets/ascii-mark.txt))
stands in for the logo in terminals. Plain ASCII, so it survives every font
and log viewer:

```text
  ___
 / o \   AnixOps Agent
 \___/   1.4.2
```

- `--version` prints the banner on a terminal and a single line
  (`anixops-agent 1.4.2 (commit abc1234, 2026-10-01)`) when piped.
- Interactive TUIs may show the banner on the start screen; long-running
  daemons print the single line only.
- With colour on, the mark may use `brand-start` (top line) to `brand-end`
  (bottom line); the product name uses the default foreground, the version
  `muted`.

Go: `anixops.Banner("AnixOps Agent", version)`. Rust: `term::ASCII_MARK`.

## Using the tokens

**Go (lipgloss, bubbletea, cobra)**: `go get github.com/AnixOps/AnixOps-design/tokens/go/anixops`
(module tag `tokens/go/anixops/v1.0.0`).

```go
import (
	"strconv"

	"github.com/charmbracelet/lipgloss"
	"github.com/AnixOps/AnixOps-design/tokens/go/anixops"
)

func adaptive(c anixops.TermColor) lipgloss.CompleteAdaptiveColor {
	return lipgloss.CompleteAdaptiveColor{
		Light: lipgloss.CompleteColor{TrueColor: c.Light, ANSI256: strconv.Itoa(int(c.ANSI256Light)), ANSI: strconv.Itoa(int(c.ANSI16))},
		Dark:  lipgloss.CompleteColor{TrueColor: c.Dark, ANSI256: strconv.Itoa(int(c.ANSI256Dark)), ANSI: strconv.Itoa(int(c.ANSI16))},
	}
}

var accent = lipgloss.NewStyle().Foreground(adaptive(anixops.TermAccent))
```

The Control Center TUI today uses 256-colour indexes 62/57, 86 and 241: map
them to `TermAccent`, `TermSuccess` and `TermMuted`.

**Rust (ratatui, clap, egui)**: copy
[`../tokens/rust/anixops_tokens.rs`](../tokens/rust/anixops_tokens.rs) into
the crate. `Color::Rgb(c.r, c.g, c.b)` for truecolor, `Color::Indexed(n)` for
256, and check `NO_COLOR` yourself (or use a crate such as `anstream` that
does).
