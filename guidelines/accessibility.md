# Accessibility

Target: **WCAG 2.2 AA** in both themes, on desktop and phone.

- **Contrast**: text ≥ 4.5:1, large text and UI graphics ≥ 3:1. Guaranteed at
  the token level; `scripts/contrast.py --check` fails CI otherwise. See
  [`color.md`](color.md).
- **Focus**: every interactive element shows a 2 px `--accent` ring with a
  2 px offset on `:focus-visible`. Never remove outlines without a replacement.
- **Keyboard**: everything reachable with Tab; `Esc` closes overlays; dialogs
  trap focus and return it; `⌘K`/`Ctrl+K` opens the command palette; `/`
  focuses search; arrow keys move within tables, menus and segmented controls.
- **Semantics**: one H1 per page and continuous heading levels; landmarks
  (`header`, `nav`, `main`); dialogs with `role="dialog"`, `aria-modal` and
  `aria-labelledby`; form fields with a visible top label, help and error
  text tied by `aria-describedby`.
- **Not colour alone**: status badges carry a word and/or icon; charts offer
  a table view.
- **Motion**: honour `prefers-reduced-motion`; honour `prefers-contrast: more`
  by strengthening separators (`--separator-strong`) and secondary text.
- **Touch**: targets ≥ 44 × 44 px; inputs ≥ 16 px font on phones; respect
  `env(safe-area-inset-*)`.
- **Language**: set `lang` (`zh-CN`, `en`); never put text in images.
- **Testing**: axe (serious and critical = 0) on every page in both themes;
  manual screen-reader pass on login, user home and one admin list.
