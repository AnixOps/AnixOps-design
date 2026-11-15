# Keyboard

A professional tool is driven from the keyboard. Every AnixOps product that
runs on a computer (the desktop clients, the web panels, the TUI) follows
these rules; phone and tablet apps follow them when a hardware keyboard is
attached.

Rules are numbered (`K1`, …) like those in [`actions.md`](actions.md):
a number is never reused or renumbered.

In the tables, **Mod** is `⌘` on macOS and `Ctrl` on Windows, Linux and the
web panels on those systems. A panel opened on a Mac uses `⌘`.

## 1. Principles

- **K1** Every action reachable by pointer is reachable by keyboard
  ([`actions.md`](actions.md) P8), and the keyboard route is discoverable:
  the shortcut is shown in the menu item, in the tooltip (A9) and in the
  command palette. A shortcut that is written down nowhere does not exist.
- **K2** A platform's own shortcut always wins. A product never rebinds
  copy, paste, undo, select all, find, close window, quit, minimise, full
  screen, or the system's text-editing keys.
- **K3** One command has one shortcut in every AnixOps product, from the
  reserved list in section 3. A product may leave a reserved shortcut unused;
  it may not use it for something else.
- **K4** Single-letter shortcuts without a modifier are allowed only where no
  text field can have the focus (a list, a table, a tree, the TUI), and never
  while a field is focused. `/` to focus search is the one exception on the
  web.
- **K5** A destructive command is never one keystroke away from done
  (`actions.md` D9): its shortcut opens the confirmation or acts with undo.
- **K6** Focus is always visible ([`accessibility.md`](accessibility.md)) and
  always somewhere sensible: opening a page focuses its list or its first
  field; closing an overlay returns focus to the control that opened it;
  removing a row moves focus to the next row (D8).
- **K7** Tab moves between regions and controls; arrow keys move inside one
  (a list, a table, a tree, a menu, a segmented control, tabs). A list is one
  Tab stop, not one per row.
- **K8** Shortcuts are layout-independent where the platform allows: they
  follow the character on the key, and every command that uses a punctuation
  key also sits in a menu or the palette.
- **K22** No shortcut on Windows or Linux uses `Ctrl+Alt`: on many keyboard
  layouts that is AltGr and types a character. Use `Ctrl+Shift` for the
  second layer.
- **K9** The product's shortcuts are listed in one place the user can open
  (`Mod` `/` or the Help menu), generated from the same table the code uses.

## 2. Command palette

Desktop clients and panels have one command palette, opened with `Mod` `K`.

- **K10** The palette lists every S1 and S2 action of the product
  (`actions.md` section 2), every page, and the objects the user would
  otherwise find by navigating (nodes, groups, subscriptions, rules; in a
  panel users, nodes, plans). It is not a second place for settings forms.
- **K11** A command's name is the same verb and noun as its button or menu
  item (A7), shown with its shortcut. Names in both interface languages
  match, and pinyin initials match Chinese names.
- **K12** Order: an exact match first, then recently used, then the rest by
  page. With an empty query the palette shows what applies to the current
  page and the last five commands.
- **K13** Only commands that apply now are offered (V1). A command that needs
  a selection acts on the current selection and says so ("测速：已选 3 个
  节点").
- **K14** `↑` `↓` move, `Enter` runs, `Esc` closes and returns focus. Running
  a command closes the palette; a command that needs one more choice (pick a
  node) continues inside the palette, not in a new dialog.
- **K15** A destructive command run from the palette goes through the same
  confirmation tier as from its button (D5).
- **K16** The palette opens within 100 ms and filters on every key press
  without a spinner; it searches what is already loaded.

## 3. Reserved shortcuts

### App and window

| Command | macOS | Windows, Linux |
|---|---|---|
| Command palette | `⌘K` | `Ctrl+K` |
| Shortcut list | `⌘/` | `Ctrl+/` |
| Settings | `⌘,` | `Ctrl+,` |
| Go to page 1–9 (sidebar order) | `⌘1` … `⌘9` | `Ctrl+1` … `Ctrl+9` |
| Back, forward (where there is history) | `⌘[`, `⌘]` | `Alt+←`, `Alt+→` |
| Toggle the main switch (connect, start) | `⇧⌘C` | `Ctrl+Shift+C` |
| Import or add (the product's first step) | `⌘I` | `Ctrl+I` |
| New item on this page | `⌘N` | `Ctrl+N` |
| Refresh this page | `⌘R` | `Ctrl+R`, `F5` |
| Find or filter on this page | `⌘F` | `Ctrl+F` |
| Show or hide the sidebar | `⌃⌘S` | `Ctrl+B` |
| Show or hide the inspector or detail pane | `⌥⌘I` | `Ctrl+Shift+I` |
| Close window (the app keeps running) | `⌘W` | `Ctrl+W` |
| Quit | `⌘Q` | `Ctrl+Q` |

### Lists, tables and trees

| Command | macOS | Windows, Linux |
|---|---|---|
| Move | `↑` `↓` | `↑` `↓` |
| First, last | `⌥↑`, `⌥↓` | `Home`, `End` |
| Page | `Page Up`, `Page Down` | `Page Up`, `Page Down` |
| Extend the selection | `⇧↑` `⇧↓`, `⇧`-click, `⌘`-click | `Shift+↑` `Shift+↓`, `Shift`-click, `Ctrl`-click |
| Select all | `⌘A` | `Ctrl+A` |
| Open, or run the row's default action (S7) | `Return` | `Enter` |
| Peek without leaving the list (inspector, quick look) | `Space` | `Space` |
| Expand, collapse a tree row | `→`, `←` | `→`, `←` |
| Expand, collapse with everything inside | `⌥→`, `⌥←` | `Shift+→`, `Shift+←` |
| Copy the row's main value | `⌘C` | `Ctrl+C` |
| Row menu ("more") | `⌃Return` or the menu key | `Shift+F10` or the menu key |
| Rename or edit | `Return` on a name that edits in place, otherwise `⌘E` | `F2`, otherwise `Ctrl+E` |
| Remove (D5, K5) | `⌘⌫` | `Delete` |
| Clear the selection, close the inspector, leave search | `Esc` | `Esc` |

### Panes, tabs and overlays

| Command | macOS | Windows, Linux |
|---|---|---|
| Next, previous tab in a pane | `⌃Tab`, `⌃⇧Tab` | `Ctrl+Tab`, `Ctrl+Shift+Tab` |
| Next, previous region (sidebar, list, inspector) | `Tab`, `⇧Tab`; `F6` | `F6`, `Shift+F6` |
| Confirm a dialog or form (C6) | `Return`; `⌘Return` in a multi-line field | `Enter`; `Ctrl+Enter` |
| Cancel, close an overlay | `Esc` | `Esc` |
| Save a dirty form (C3) | `⌘S` | `Ctrl+S` |
| Undo the last T0 action (D5) | `⌘Z` | `Ctrl+Z` |

### Capture and inspection tools

Products that show live traffic (the client's debug pages) also reserve:

| Command | macOS | Windows, Linux |
|---|---|---|
| Pause, resume the live list | `⇧⌘P` | `Ctrl+Shift+P` |
| Clear the list (T0: undo while the data is still held) | `⇧⌘K` | `Ctrl+Shift+K` |
| Next, previous item while the inspector has the focus | `⌘↓`, `⌘↑` | `Alt+↓`, `Alt+↑` |

Going to the last row (`⌥↓`, `End`) resumes following the newest row
([`motion.md`](motion.md) M11). Less frequent commands (copy as cURL, export,
replay) have no reserved shortcut; they are in the row menu and the palette.

## 4. Platforms

- **K17** macOS: every S1 and S2 action is a menu-bar command
  (`actions.md` P4) and gets its shortcut there; the menu is the shortcut
  list. Standard menus (Edit, View, Window, Help) keep their standard items.
- **K18** Windows and Linux: shortcuts are shown in menus and tooltips;
  `Alt` shows access keys where the toolkit provides them; `F10` focuses the
  menu or the title bar tools. `Ctrl+Q` quits; closing the window follows the
  product's tray setting.
- **K19** Web panels never take a shortcut the browser needs to keep the user
  safe or oriented (`Mod+W`, `Mod+T`, `Mod+L`, `Mod+R`, `Mod+N`, back and
  forward). In a panel, refresh is a button, "new" is `N` on a focused list
  (K4), and history belongs to the browser.
- **K20** iPad with a keyboard follows the macOS column; holding `⌘` shows
  the system's shortcut overlay, so commands are declared to the system and
  grouped by page.
- **K21** The TUI follows [`terminal.md`](terminal.md); where a command
  exists in both, the letter is the same as the desktop shortcut without its
  modifier (`r` refresh, `n` new, `/` search, `?` shortcut list).

## 5. Review checklist

1. Can the whole screen be used without a pointer, in a sensible Tab order?
   (K1, K7)
2. Is every shortcut shown in a menu, a tooltip or the palette? (K1)
3. Does any shortcut differ from the reserved list, or reuse one? (K2, K3)
4. Does a single key do something destructive? (K5)
5. After closing an overlay or removing a row, is focus where the user
   expects? (K6)
6. Is every page action in the command palette under the same name? (K10,
   K11)
