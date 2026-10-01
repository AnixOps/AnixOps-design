// Package anixops holds the AnixOps design tokens for Go programs: the UI
// colours, the brand colours and the terminal palette for CLIs and TUIs.
//
// The values in tokens.go are generated from tokens/tokens.json; this file
// holds the types and helpers. With lipgloss:
//
//	accent := lipgloss.CompleteAdaptiveColor{
//		Light: lipgloss.CompleteColor{TrueColor: anixops.TermAccent.Light, ANSI256: strconv.Itoa(int(anixops.TermAccent.ANSI256Light)), ANSI: strconv.Itoa(int(anixops.TermAccent.ANSI16))},
//		Dark:  lipgloss.CompleteColor{TrueColor: anixops.TermAccent.Dark, ANSI256: strconv.Itoa(int(anixops.TermAccent.ANSI256Dark)), ANSI: strconv.Itoa(int(anixops.TermAccent.ANSI16))},
//	}
package anixops

import (
	"os"
	"strings"
)

// Color is a UI colour with a value for each theme.
type Color struct {
	Light, Dark string
}

// TermColor is a terminal colour: truecolor hex values for light and dark
// terminal backgrounds, the nearest xterm-256 indexes, and the basic ANSI
// index (0-15), which the user's terminal theme remaps.
type TermColor struct {
	Light, Dark               string
	ANSI256Light, ANSI256Dark uint8
	ANSI16                    uint8
}

// ColorEnabled reports whether a program may write colour to a stream.
// It returns false when NO_COLOR is set to any non-empty value
// (https://no-color.org), when TERM is "dumb", or when the stream is not a
// terminal. FORCE_COLOR (non-empty, not "0") overrides the terminal check but
// never NO_COLOR. Flags such as --color=never are the caller's to apply first.
func ColorEnabled(isTerminal bool) bool {
	if os.Getenv("NO_COLOR") != "" {
		return false
	}
	if f := os.Getenv("FORCE_COLOR"); f != "" && f != "0" {
		return true
	}
	return isTerminal && os.Getenv("TERM") != "dumb"
}

// Banner returns the ASCII mark with the product name on the second line and
// the version on the third, for --version output and startup banners:
//
//	 ___
//	/ o \   AnixOps Agent
//	\___/   1.4.2
//
// product should be the full product name, for example "AnixOps Agent".
func Banner(product, version string) string {
	text := []string{"", product, version}
	var b strings.Builder
	for i, line := range ASCIIMark {
		b.WriteString(line)
		if i < len(text) && text[i] != "" {
			b.WriteString(strings.Repeat(" ", 7-len(line)+2))
			b.WriteString(text[i])
		}
		b.WriteByte('\n')
	}
	return b.String()
}
