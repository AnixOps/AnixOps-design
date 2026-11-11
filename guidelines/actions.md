# Actions and hierarchy

Every AnixOps screen, on every platform, follows these rules for buttons and
for where they sit. A reader must be able to tell, without reading a label,
which action is the main one, what each action will affect, and which ones
are dangerous. Two buttons that differ in importance or in what they affect
never sit side by side looking the same.

Each rule has a number so a review can cite it (`A3`, `S2`, …).

## 1. Emphasis levels

An action has exactly one level. The level decides how it looks.

| Level | Meaning | Look | Web (tokens) | SwiftUI |
|---|---|---|---|---|
| **E1 Primary** | The one thing this view is for | Filled accent | `--primary` fill, `--on-primary` text | `.borderedProminent` |
| **E2 Secondary** | A useful alternative to the primary | Bezel: neutral fill, hairline | `--fill-1` or surface with `--separator` | `.bordered` |
| **E3 Quiet** | Frequent but minor: refresh, copy, open, "全部 ›" | Text or icon only, accent or secondary text colour | no background until hover | `.link`, `.plain`, `.borderless` |
| **E4 Destructive** | Removes data or cuts a connection for good | Red text; filled red only inside its own confirmation | `--danger` | `role: .destructive` |

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

## 2. Scope levels

An action sits at the level of the thing it changes, and only there.

| Scope | What it changes | Where it sits |
|---|---|---|
| **S1 App** | The whole client: connect, import, proxy mode | Sidebar foot, hero, menu bar, tray. Never in a page toolbar |
| **S2 Page** | Everything the page shows: search, test all, refresh all | Page toolbar, next to the title |
| **S3 Section** | One card or list | The card header, trailing edge |
| **S4 Row** | One item | The row's trailing edge |

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

## 3. Order and spacing

- **O1** Within a group the strongest action is at the trailing edge (right in
  left-to-right layouts): quiet, then secondary, then primary. Dialogs follow
  the platform: cancel before confirm on Apple and the web, the platform order
  on Windows system dialogs.
- **O2** Buttons of one group are 8 px apart. Different groups are at least
  16 px apart or have a hairline separator between them.
- **O3** Inside a "more" menu: everyday items first, then a separator, then
  destructive items last.

## 4. Destructive and irreversible actions

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

## 5. Show what applies

- **V1** Offer only the actions that make sense in the current state. A
  service that is not installed shows "安装"; a stopped one shows "启动"; a
  running one shows "停止". Do not line up install, start and stop together.
- **V2** Hide what cannot apply; disable what applies but is temporarily
  unavailable (busy, nothing selected), and give the reason in a tooltip or
  hint when it is not obvious.
- **V3** While an action runs, its own control shows progress and stays in
  place. Controls do not appear or move while the pointer is over them.

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

## 7. Review checklist

Before a screen ships, on every platform:

1. Is there at most one filled button in each view? (A1)
2. Does every group hold neighbouring levels only, with one strongest? (A2)
3. Does every toolbar, header and row hold actions of one scope? (S1)
4. Does any row show more than one labelled and one icon action? (S3)
5. Is every destructive action in a menu or clearly apart, red, confirmed by
   name? (D1, D2)
6. Are only applicable actions shown for the current state? (V1)
7. Can the four text levels be told apart at a glance? (H1)

A change that breaks a rule either fixes the screen or changes this document
first, in the same way a token change starts in `tokens.json`.
