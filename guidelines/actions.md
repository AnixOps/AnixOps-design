# Actions and hierarchy

Every AnixOps screen, on every platform, follows these rules for buttons, for
where they sit, and for the hierarchy of the content around them. They apply
to the iOS, macOS, Windows and Linux clients, to the web panels (user and
admin) and to any future AnixOps app.

A reader must be able to tell, without reading a label, which action is the
main one, what each action will affect, and which ones are dangerous. Two
buttons that differ in importance or in what they affect never sit side by
side looking the same.

Each rule has a number so a review can cite it (`A3`, `S2`, …). Numbers are
stable: a rule is never renumbered and a retired number is never reused.
"Must" rules are the numbered ones; everything else on this page explains
them.

| Prefix | Section |
|---|---|
| `A` | 1. Emphasis levels |
| `S` | 2. Scope levels |
| `O` | 3. Order and spacing |
| `D` | 4. Destructive and irreversible actions |
| `V` | 5. Show what applies |
| `H` | 6. Information hierarchy |
| `C` | 7. Dialogs, sheets and forms |
| `F` | 8. Feedback |
| `P` | 9. Platforms |

## 1. Emphasis levels

An action has exactly one level. The level decides how it looks.

| Level | Meaning | Look | Web (tokens) |
|---|---|---|---|
| **E1 Primary** | The one thing this view is for | Filled accent | `--accent-fill` background, `--on-accent` text, `--accent-fill-hover` on hover |
| **E2 Secondary** | A useful alternative to the primary | Bezel: neutral fill, no accent | `--fill-1` background (`--fill-2` on hover), `--label-1` text |
| **E3 Quiet** | Frequent but minor: refresh, copy, open, "全部 ›" | Text or icon only | No background at rest, `--fill-1` on hover; `--accent` text, or `--label-2` for icons |
| **E4 Destructive** | Removes data, or cannot be taken back | Red text; filled red only inside its own confirmation | `--danger` text; in the confirmation `--danger-fill` background, `--on-danger` text |

All four share one shape (`--radius-pill`) and the control heights in
[`layout.md`](layout.md): 44 on touch, 36 by default, 28 inside tables.
Section 9 gives the native control for each level on every platform.

- **A1** A view (a page, a dialog, a card) has at most **one** E1. If two
  actions both look primary, one of them is wrong.
- **A2** Buttons in one group differ by at most one level, and at most one of
  them is the strongest. E1 with E2 is a group; E1 with E3 icons and an E4 is
  not.
- **A3** An icon-only button is always E3. An action that matters enough to be
  E1 or E2 has a text label.
- **A4** Navigation ("全部 ›", "连接记录 ›") is not an action. It is E3 with a
  trailing chevron and never shares a group with buttons that change something.
- **A5** A toggle that takes effect immediately is a switch, not a button. A
  choice between two to four exclusive modes is a segmented control.
- **A6** There are four looks and no others. No outlined-accent buttons, no
  gradient buttons, no buttons coloured by status (green "start", amber
  "retry"). The brand gradient is never on a control
  ([`color.md`](color.md) rule 4).
- **A7** One action has one level, one label and one icon wherever it appears
  in a product and across products. "更新订阅" is not E1 on one page and an
  icon on the next, unless the page is that action's home (S2).
- **A8** Size does not add a level. Within a group every button has the same
  height; a larger button is allowed only for the single hero action (H2).
- **A9** Every icon-only button has a tooltip on pointer platforms and an
  accessibility label everywhere, using the same words as the labelled form
  of that action.

How to choose a level:

1. Is it the reason the view exists (connect, save, import, create)? E1, and
   only one.
2. Does it remove something or change something that cannot be taken back?
   E4, and read section 4.
3. Is it a real alternative to the primary, or the main action of a section
   that has no E1? E2.
4. Everything else is E3, or belongs in a "more" menu.

## 2. Scope levels

An action sits at the level of the thing it changes, and only there.

| Scope | What it changes | Where it sits |
|---|---|---|
| **S1 App** | The whole product: connect, import, proxy mode; in a panel the account, language, theme, current tenant | Sidebar foot, hero, menu bar, tray, tab bar; in a panel the top bar. Never in a page toolbar |
| **S2 Page** | Everything the page shows: search, filter, test all, refresh all, create | Page toolbar, next to the title |
| **S3 Section** | One card or list | The card header, trailing edge |
| **S4 Row** | One item | The row's trailing edge |

Two more places hold actions, and each is its own scope:

| Scope | What it changes | Where it sits |
|---|---|---|
| **Selection** | The rows that are selected | A bulk bar that appears with the selection (S5) |
| **Dialog** | What the dialog, sheet or form is about | Its footer (C1) |

- **S1** Actions of different scopes never share a group, a toolbar segment or
  a row. A page toolbar holds only S2 actions; the app's own controls keep
  their fixed place on every page.
- **S2** One action lives in one place. Do not repeat a page action inside a
  card, or an app action on a page, unless the page is that action's home
  (an empty state may offer the first step, such as "导入订阅").
- **S3** A row shows at most **one labelled action and one icon action**.
  Everything else for that row goes into a "more" menu (`⋯`, labelled
  "更多 / More"). The row's main action is the labelled one.
- **S4** A section header shows at most two actions; further ones go into the
  same kind of menu.
- **S5** Actions on a selection appear only while something is selected, in a
  bulk bar that states the count ("已选 3 项"). The bar replaces or covers
  the page toolbar; it never mixes with it. It holds at most one E2, quiet
  actions and a "more" menu; a destructive bulk action follows D1 and D6.
- **S6** A page toolbar holds at most one E1 (usually "create" or "import"),
  at most two other labelled actions, then icons and a "more" menu. Search
  and filters are inputs, not buttons, and sit on the leading side.
- **S7** If clicking a row opens or selects the item, that is the row's
  default action and needs no button. The row may then show one more
  labelled action at most (S3 still counts it).

## 3. Order and spacing

- **O1** Within a group the strongest action is at the trailing edge (right in
  left-to-right layouts): quiet, then secondary, then primary. Dialogs follow
  the platform: cancel before confirm on Apple and the web, the platform order
  on Windows system dialogs.
- **O2** Buttons of one group are 8 px apart (`--space-2`). Different groups
  are at least 16 px apart (`--space-4`) or have a hairline separator
  (`--separator`) between them.
- **O3** Inside a "more" menu: everyday items first, then a separator, then
  destructive items last.
- **O4** A toolbar reads, from the leading edge: title, search and filters,
  then quiet actions, the "more" menu, secondary, and the primary last.
- **O5** On a phone, a group that does not fit in one line stacks at full
  width with the primary on top and cancel at the bottom. It does not shrink
  labels into icons to fit.
- **O6** The order of a group is the same on every screen of a product.
  Buttons do not change places between states; a state change swaps the
  label in place (V1, V3).

## 4. Destructive and irreversible actions

An action is destructive when it removes the user's data or configuration,
affects other people (a panel admin banning a user), or cannot be reversed by
one more click. Disconnecting, stopping or pausing something that can be
started again is **not** destructive; it is the other half of a switch or an
ordinary E2 or E3.

- **D1** A destructive action is never the strongest control in a group and
  never sits directly beside the primary action. Its default home is the
  "more" menu, last, after a separator, in red.
- **D2** It asks for confirmation that names the thing: "删除订阅 Example？",
  with the consequence in one sentence. The confirming button repeats the verb
  ("删除"), never "确定 / OK".
- **D3** Actions that change the system (install a driver, a service, a root
  certificate, change system proxy settings) say so before they run and state
  what will be changed. They are E2 at most.
- **D4** Where it is cheap, prefer undo over confirmation (remove a rule, close
  a connection).
- **D5** The confirmation matches the damage. Use the lowest tier that fits:

  | Tier | When | How |
  |---|---|---|
  | **T0 Undo** | One item, restorable by the app (remove a rule, a node from a group, a log filter) | Act at once; a toast names what happened and offers "撤销 / Undo" for at least 5 s |
  | **T1 Confirm** | Not restorable, one item, the user's own data (delete a subscription, a profile, a plugin) | Dialog per D2 with a filled red confirm button |
  | **T2 Typed** | Many items, other people's data, or anything money or access depends on (delete a user, a node in use, reset all traffic, revoke every key) | Dialog per D2 that also lists what is affected with counts; the confirm button stays disabled until the user types the object's name or the stated word |
  | **T3 System** | Changes outside the app (D3) | Explain first in our own sheet, then let the operating system ask for its own authorisation; never hide or pre-empt the system prompt |

- **D6** In a destructive confirmation, cancel is always present, is the
  default for Enter and has the initial focus; Esc cancels. The red button is
  never the default. Clicking outside a T1 dialog cancels; a T2 dialog closes
  only by its buttons.
- **D7** A bulk destructive action states the count in the title ("删除 12 个
  节点？") and names the items, or the first few and "等 12 项". It is at
  least T1, and T2 when it touches other people's data.
- **D8** After a destructive action, a toast confirms what was done by name.
  The view does not jump: the list keeps its scroll position and focus moves
  to the next item.
- **D9** A destructive action is never triggered by a single keystroke, a
  hover, or a gesture alone without T0 undo or a confirmation. Full-swipe to
  delete is allowed only at T0.
- **D10** Red is reserved. `--danger` on a control means E4 and nothing else;
  errors and expired states use badges and inline messages (H4, F3), not red
  buttons.

## 5. Show what applies

- **V1** Offer only the actions that make sense in the current state. A
  service that is not installed shows "安装"; a stopped one shows "启动"; a
  running one shows "停止". Do not line up install, start and stop together.
- **V2** Hide what cannot apply; disable what applies but is temporarily
  unavailable (busy, nothing selected), and give the reason in a tooltip or
  hint when it is not obvious.
- **V3** While an action runs, its own control shows progress and stays in
  place. Controls do not appear or move while the pointer is over them.
- **V4** An action the user has no permission for is hidden, not disabled,
  unless seeing it explains how to get it (an upgrade, an administrator
  setting); then it is disabled with the reason.
- **V5** A running action cannot be started twice: its control is busy until
  the result arrives. If it can be cancelled, the same control becomes
  "取消 / Cancel" in place.

## 6. Information hierarchy

Actions follow the hierarchy of the content they belong to, so the content
needs one too.

- **H1** Four text levels and no more on a screen: page title, section title,
  row label or value, hint. Sizes and weights come from
  [`typography.md`](typography.md); never invent a fifth level with colour or
  weight alone.
- **H2** One hero per page at most: the single most important state and its
  one primary action. Everything else is a section.
- **H3** A section has a title, optionally one sentence, then its content.
  Titles are nouns ("订阅"); buttons are verbs ("更新").
- **H4** Status is shown by a dot or a pill beside the value, with the status
  colours from [`color.md`](color.md), never by colouring a button.
- **H5** Advanced or rarely used settings are grouped at the bottom or behind
  "更多 / More", never mixed among everyday ones.
- **H6** A page reads in one order: what state am I in, what can I do about
  it, then the details. State and the primary action are visible without
  scrolling at the smallest supported window size.
- **H7** A card or panel is about one object or one question, and its title
  says which. Do not group by technology ("TUN", "gRPC") what the user sees
  as one thing ("连接").
- **H8** A card shows one key value at the largest size it uses; supporting
  values are row-level text. Numbers are tabular
  ([`typography.md`](typography.md)) and carry their unit.
- **H9** Nesting stops at three: page, section, row. A card does not contain
  cards. Detail deeper than a row opens a detail page, a side sheet or a
  dialog.
- **H10** Colour and weight follow the level, not the wish to be noticed:
  `--label-1` for titles and values, `--label-2` for labels and supporting
  text, `--label-3` for hints and disabled text. `--accent` marks only what
  is interactive or selected.

The four levels map to the type scale like this:

| Level | Token | Colour |
|---|---|---|
| Page title | `--type-title-1-*` (desktop client windows may use `--type-title-2-*`) | `--label-1` |
| Section title | `--type-title-3-*` | `--label-1` |
| Row label or value | `--type-body-*` | `--label-1` for the value, `--label-2` for its label |
| Hint | `--type-callout-*`; `--type-caption-*` inside badges and timestamps | `--label-2` or `--label-3` |

`--type-display-*` is for the one hero value of H2 and for login.

## 7. Dialogs, sheets and forms

- **C1** A dialog, sheet or form footer holds only its own actions: one E1
  (or one filled red button for a confirmation), cancel as E2 or E3, and at
  most one further E3 on the leading edge ("了解更多"). No page or app
  actions inside.
- **C2** Use the lightest container that works: inline edit for one field, a
  popover or menu for a choice, a side sheet for details and editing beside a
  list, a dialog only when the user must decide before going on. Dialogs do
  not open dialogs, except a confirmation.
- **C3** Settings that are safe to apply take effect at once, with switches
  and pickers and no save button. A form that must be applied together has
  one "保存 / Save" (E1) and one "取消 / Cancel" in a footer or a sticky
  save bar that appears when the form is dirty; never both models on one
  page.
- **C4** Leaving a dirty form asks once: "放弃更改？", with "放弃 / Discard"
  (E4) and "继续编辑 / Keep editing" as the default.
- **C5** The title of a dialog is the question or the task ("删除订阅
  Example？", "添加节点"), and the primary button answers it with the same
  verb. "确定 / OK" and "是 / 否" are not button labels
  ([`voice-and-tone.md`](voice-and-tone.md)).
- **C6** Enter triggers the E1 of a dialog or form unless it is destructive
  (D6); Esc cancels. Both work on every desktop platform and in the panels.
- **C7** A wizard shows "上一步 / Back" (E2 or E3) and "下一步 / Next" (E1)
  in fixed places; the last step renames Next to the verb that finishes the
  task ("导入", "创建").

## 8. Feedback

- **F1** The result of an action appears where the action was: the row
  updates, the button returns from busy. A toast is added only when the
  result is not visible in place.
- **F2** Use one channel per kind of message:

  | Message | Channel |
  |---|---|
  | Done, nothing to decide | Toast, 4 s, no button or one "撤销 / Undo" |
  | A field is wrong | Inline under the field, `--danger` text with an icon |
  | A section failed to load or act | Inline in the section, with "重试 / Retry" (E2) |
  | A condition that lasts and affects the page or app (offline, expired, update required) | Banner at the top of the page or app, with at most one action |
  | The user must decide before going on | Dialog |

- **F3** An error says what happened and what to do, and offers the fix as
  its one action. Technical detail is behind "技术详情 / Details".
- **F4** Banners and toasts follow the same levels: at most one action each,
  E3 in a toast, E2 in a banner, never E1.
- **F5** Empty, loading and error are designed states of every list and
  card. Empty says what will appear and offers the first step, which may be
  the page's E1 (S2); loading uses a skeleton
  ([`motion.md`](motion.md)); error follows F2.

## 9. Platforms

The rules are the same everywhere; the control that carries them is the
platform's own.

### Levels

| Level | SwiftUI (iOS, macOS) | Desktop web UI (Windows, Linux; React) | Panels (Vue, Element Plus) | Flutter |
|---|---|---|---|---|
| E1 | `.borderedProminent` | Filled accent button | `type="primary"` | `FilledButton` |
| E2 | `.bordered` | Bezel button | default `el-button` | `FilledButton.tonal` |
| E3 | `.borderless`, `.plain`; `Link` for A4 | Text or icon button | `text` or `link` | `TextButton`, `IconButton` |
| E4 | `role: .destructive` | Red text button, red menu item | `type="danger"` with `text`; filled only in the confirmation | `TextButton` in the error colour |
| "More" menu | `Menu` with `ellipsis` | `⋯` button with a menu | `el-dropdown` on a `⋯` button | `PopupMenuButton` |

Each product wraps these once in its own button components and uses only
those; screens do not style buttons by hand.

### Scopes

| Scope | iOS, iPadOS | macOS | Windows, Linux | Web panels |
|---|---|---|---|---|
| S1 App | Tab bar; the home hero | Sidebar foot; menu bar item | Sidebar foot; tray menu | Top bar and sidebar |
| S2 Page | Navigation bar, trailing | Window toolbar | Page title bar tools | Page header, trailing |
| S3 Section | Section header, trailing | Section or card header | Card header | Card header or table toolbar |
| S4 Row | Tap for the default action; swipe and context menu for the rest | Trailing edge on hover; context menu | Trailing edge; `⋯`; right-click | "操作" column: one text action and `⋯` |
| Selection (S5) | Bottom toolbar in edit mode | Toolbar while selected | Bulk bar over the page tools | Bulk bar above the table |
| Dialog (C1) | Sheet with navigation bar buttons, or alert | Sheet or alert | In-app dialog | `el-dialog`, side sheet (`el-drawer`) |

- **P1** Use the platform's own control and place for a scope before
  inventing one. Where a platform guideline and this page disagree about
  *look*, the platform wins on Apple systems; about *level, scope and
  destructive handling*, this page wins everywhere.
- **P2** iOS: a navigation bar shows at most two trailing items; more go
  into a `⋯` menu. Leading swipe is for non-destructive actions, trailing
  swipe ends with the destructive one. Every swipe or context-menu action is
  also reachable without the gesture (detail page or edit mode).
- **P3** iOS: the hero action and form submit sit in the thumb zone at the
  bottom, full width, 44 pt or taller. Alerts use the system alert with a
  destructive-role button for T1; T2 uses a sheet with a text field.
- **P4** macOS: the main window follows the same levels; the menu bar item
  and its menu hold S1 actions only, plus "打开主窗口" and "退出". Every S1
  and S2 action also has a menu-bar command, with the standard shortcut where
  one exists.
- **P5** Windows and Linux share one UI and therefore one layout. Tray menus
  hold S1 actions only. Row actions that appear on hover on macOS are always
  visible here if the window may be used by touch; nothing is reachable by
  right-click alone.
- **P6** Panels: a table row has one text action and a `⋯` menu in its
  action column (S3); several text links in a row are a violation. The admin
  panel may be denser ([`principles.md`](principles.md)), but density changes
  spacing and row height, not the number of visible actions per row.
- **P7** Panels on phones follow the iOS rules for stacking (O5) and touch
  size; table row actions collapse into the `⋯` menu entirely.
- **P8** Every action reachable by pointer is reachable by keyboard and by a
  screen reader, with the level announced by role and label, not by colour
  ([`accessibility.md`](accessibility.md)).
- **P9** Terminal apps (TUI) keep the same levels in the key hint bar: the
  primary key first, destructive keys last and confirmed by typing
  ([`terminal.md`](terminal.md)).

## 10. Examples

A subscription row.

```text
Wrong   Example  128 GB · 30 天   [更新] [编辑] [复制链接] [测速] [删除]
Right   Example  128 GB · 30 天                          [更新]  ⋯
                                    ⋯ → 编辑 · 复制链接 · 测速 ── 删除
```

Five equal buttons break A2, S3 and D1. One labelled action stays; the rest
go into the menu, delete last and red.

A page toolbar.

```text
Wrong   代理   [连接] [导入订阅] [全部测速] [刷新] [删除全部]
Right   代理   [搜索…]                         ↻  ⋯  [全部测速] [导入订阅]
```

"连接" is S1 and lives in the sidebar foot (S1). "刷新" is an icon (A3).
"删除全部" moves into `⋯` (D1) and is T2 (D5). One E1 remains (A1, S6).

A system service card.

```text
Wrong   系统服务   [安装] [启动] [停止] [卸载]
Right   系统服务   ● 运行中                              [停止]  ⋯
                                                 ⋯ → 重新安装 ── 卸载
```

Only the action for the current state is shown (V1); status is a dot and a
word (H4); uninstall is destructive and a system change (D1, D3, T3).

A delete confirmation (T1).

```text
删除订阅 Example？
其中的 42 个节点会一并移除，此操作无法撤销。
                                      [取消]  [删除]
```

Cancel has the focus and answers Enter (D6); the red button repeats the verb
(D2, C5).

## 11. Review checklist

Before a screen ships, on every platform:

1. Is there at most one filled button in each view? (A1)
2. Does every group hold neighbouring levels only, with one strongest? (A2)
3. Does every toolbar, header and row hold actions of one scope? (S1)
4. Does any row show more than one labelled and one icon action? (S3)
5. Is every destructive action in a menu or clearly apart, red, confirmed by
   name? (D1, D2)
6. Are only applicable actions shown for the current state? (V1)
7. Can the four text levels be told apart at a glance? (H1)
8. Does each destructive action use the right tier, with cancel as the
   default? (D5, D6)
9. Does every button use one of the four looks, through the product's own
   button components? (A6, section 9)
10. Are state and the primary action visible without scrolling? (H6)
11. Do dialogs and forms hold only their own actions, labelled with verbs?
    (C1, C5)
12. Are empty, loading and error states designed? (F5)

## 12. Adopting and changing these rules

- Each product keeps a short mapping document in its own repository: which of
  its components carries each level and scope, and any exception with its
  reason. Its agent and contributor instructions point to this page.
- A pull request that adds or changes a screen states that the checklist was
  run, and cites the rule number for anything a reviewer asks about.
- A change that breaks a rule either fixes the screen or changes this document
  first, in the same way a token change starts in `tokens.json`. An exception
  that two products need is a missing rule: add it here.
- Adding a rule is a minor version of AnixOps Design; changing the meaning of
  an existing rule is a major one and is listed in
  [`CHANGELOG.md`](../CHANGELOG.md).
