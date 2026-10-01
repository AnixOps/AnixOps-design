package anixops

import (
	"regexp"
	"strings"
	"testing"
)

var hex = regexp.MustCompile(`^#[0-9A-F]{6}$`)

func TestTermPalette(t *testing.T) {
	for name, c := range map[string]TermColor{
		"accent": TermAccent, "success": TermSuccess, "warning": TermWarning,
		"danger": TermDanger, "muted": TermMuted, "brand-start": TermBrandStart, "brand-end": TermBrandEnd,
	} {
		if !hex.MatchString(c.Light) || !hex.MatchString(c.Dark) {
			t.Errorf("%s: bad hex %q / %q", name, c.Light, c.Dark)
		}
		if c.ANSI256Light < 16 || c.ANSI256Dark < 16 {
			t.Errorf("%s: ANSI256 fallbacks must come from the 6x6x6 cube or grey ramp", name)
		}
		if c.ANSI16 > 15 {
			t.Errorf("%s: ANSI16 %d out of range", name, c.ANSI16)
		}
	}
}

func TestColorEnabled(t *testing.T) {
	t.Setenv("FORCE_COLOR", "")
	t.Setenv("TERM", "xterm-256color")
	t.Setenv("NO_COLOR", "")
	if !ColorEnabled(true) {
		t.Error("terminal without NO_COLOR should allow colour")
	}
	if ColorEnabled(false) {
		t.Error("non-terminal should not get colour")
	}
	t.Setenv("FORCE_COLOR", "1")
	if !ColorEnabled(false) {
		t.Error("FORCE_COLOR should enable colour")
	}
	t.Setenv("NO_COLOR", "1")
	if ColorEnabled(true) {
		t.Error("NO_COLOR must win over FORCE_COLOR")
	}
	t.Setenv("NO_COLOR", "")
	t.Setenv("FORCE_COLOR", "")
	t.Setenv("TERM", "dumb")
	if ColorEnabled(true) {
		t.Error("TERM=dumb should disable colour")
	}
}

func TestBanner(t *testing.T) {
	got := Banner("AnixOps Agent", "1.4.2")
	want := "  ___\n / o \\   AnixOps Agent\n \\___/   1.4.2\n"
	if got != want {
		t.Errorf("Banner:\n%s\nwant:\n%s", got, want)
	}
	if strings.ContainsAny(got, "\x1b") {
		t.Error("banner must be plain text")
	}
}
