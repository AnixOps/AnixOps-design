# Density

How much a screen shows per unit of area is decided by what the page is for,
not by taste and not by a user setting. There are two tiers.

Rules are numbered (`N1`, …) like those in [`actions.md`](actions.md):
a number is never reused or renumbered.

## 1. The two tiers

| | **Comfortable** | **Compact** |
|---|---|---|
| For | Pages the user reads or decides on: overview, settings, forms, onboarding, account, empty states, every user-facing panel page | Pages the user scans and compares: nodes, connections, requests, logs, rules, DNS records, admin tables |
| Row height (pointer) | 44 | 28 |
| Row height (touch) | 44 or taller | 44 or taller, two lines |
| Row text | `--type-body-*` (15) | `--type-callout-*` (13) |
| Secondary text | `--type-callout-*` under or beside the value | Same size, `--label-2`, in its own column |
| Cell padding, horizontal | `--space-4` (16) | `--space-2` (8); `--space-3` (12) at the table's edges |
| Control height inside a row | 36 | 28 ([`layout.md`](layout.md)) |
| Container | Cards with `--space-6` padding, `--space-12` between sections | Edge to edge in the content area; one hairline between rows; no card around a table |
| Section header | `--type-title-3-*` | `--type-callout-*`, `--label-2`, sticky |
| Icons | 20 | 16 |

- **N1** A page has one tier. The page type picks it (the table above);
  a product lists the tier of every page in its mapping document
  (`actions.md` section 12). There is no third tier.
- **N2** The tier is not a user preference in the clients. An admin
  panel table may offer a row-height switch (comfortable 40, compact 32)
  because its users sit in it all day on very different screens
  ([`principles.md`](principles.md)); the choice is remembered per table.
- **N3** A compact page may contain a comfortable part and the reverse
  only as a separate pane with its own purpose: a compact request list with
  a comfortable inspector summary, a comfortable overview with one compact
  "recent" table. Tiers never mix inside one list.
- **N4** Density changes spacing, row height and text size. It never
  changes the number of text levels (H1), the emphasis levels (A6), the
  number of actions a row shows (S3, P6) or the contrast targets.
- **N5** On touch, compact means more information per row, not smaller
  targets: the row stays 44 or taller and carries a second line
  (`--type-callout-*`, `--label-2`) with the two or three values that matter
  most. Columns that do not fit are in the detail page.
- **N6** The smallest text on any page is `--type-caption-*` (12), used
  for badges and timestamps only. Compact does not go below 13 for values.
- **N7** Platform metrics win where the platform has them: a macOS
  table uses the system's row heights nearest to the tier (medium 28 for
  compact, large for comfortable), Windows and GTK use the toolkit's compact
  and standard list densities. Sizes follow the user's system text size.

## 2. Compact tables

These apply to every compact table; the node table is the reference case.

- **N8** Column order is fixed: what it is (name, with its status dot),
  what kind (type, group, region), how it is doing (latency, speed, traffic,
  time), then the row's actions at the trailing edge (S3). Selection
  checkboxes, where used, lead.
- **N9** One column is flexible, the name; it takes the spare width and
  truncates. Every other column has a fixed or content width with a stated
  minimum, so numbers never jump sideways when data changes.
- **N10** Numbers are right-aligned, tabular
  ([`typography.md`](typography.md)) and share one unit per column, named in
  the header when it never changes ("延迟 ms") and beside the value when it
  scales ("1.2 MB/s"). Text is left-aligned. Headers align with their
  column.
- **N11** Identifiers the user compares or copies (hosts, addresses,
  ports, hashes, paths) are in the monospace face (`--font-app-mono` or
  `--font-mono`); names and labels are not.
- **N12** Truncation: names cut at the end, hosts and paths in the
  middle so the end stays readable. A truncated cell shows the full value in
  a tooltip and copies the full value.
- **N13** An absent value is the placeholder "—" in
  `--label-3`, never "0", "N/A" or an empty cell. A value still loading is a
  skeleton of the column's usual width ([`motion.md`](motion.md) M15).
- **N14** Status is a dot before the name or a word in its own column
  (H4). A metric is coloured only by documented thresholds, which the
  product writes down once (for latency: good, fair, poor, timed out), and
  a failed measurement is a word ("超时"), not a red number.
- **N15** Rows are separated by one hairline (`--separator`), with no
  zebra stripes and no vertical rules. Hover is `--fill-1`; the selected row
  is `--accent-soft` (the system selection colour on native tables), and
  stays readable when the table loses focus.
- **N16** The header is sticky and is the sort control: a click sorts,
  a second click reverses, an arrow shows the state. Sorting is stable, is
  remembered per table, and a live table that is sorted keeps its order as
  values change only when the user asks (a "排序已固定" state), so rows do
  not jump while being read (M8, M11).
- **N17** Column widths, order and visibility are the user's to change
  (drag, and a header context menu that is also in the page's "more" menu),
  remembered per table, with "恢复默认 / Reset" in the same menu. The name
  column cannot be hidden.
- **N18** Grouping (by subscription, by region, by host) uses sticky
  group rows in the section-header style with a count; a group collapses
  with its disclosure and by keyboard ([`keyboard.md`](keyboard.md)).
- **N19** A table that can hold more than a few hundred rows is
  virtualised and keeps scrolling at the display's frame rate; filtering and
  sorting 10 000 rows shows its result within 100 ms.
- **N20** The filter bar above a compact table is one line: search
  first, then filter chips, then the count of what is shown ("128 / 2 040");
  S2 actions sit at its trailing edge (O4). It does not wrap into a second
  line; filters that do not fit go into a "筛选 / Filters" menu.
- **N21** Detail belongs beside the table, not inside it: a row opens
  an inspector pane or a side sheet (C2), the table stays visible and keeps
  its selection, and the split position is remembered. Rows do not expand in
  place into forms.

The node table, as an example:

```text
  名称                     类型      地区   延迟 ms   速度        流量
● 香港 01                  ANX       HK        38    12.4 MB/s   1.2 GB    ⋯
● 东京 02 · IPLC           SS-2022   JP        71     8.1 MB/s   640 MB    ⋯
○ 洛杉矶 03                VLESS     US       超时        —        —       ⋯
```

One flexible column (N9), numbers right-aligned with the unit in the header
where it is constant (N10), a word for the failed test (N14), a placeholder
for absent values (N13), one "more" menu per row (S3).

## 3. Comfortable pages

- **N22** A comfortable page keeps line length readable: content is
  capped at `--size-content-user` (forms and settings at 692 px,
  `--size-content-read`) and centred or leading-aligned as the platform
  does; it does not stretch rows across a wide window.
- **N23** Settings are grouped lists: a row is a label, an optional
  one-line hint under it, and one control at the trailing edge. A row has
  one control; a setting that needs more opens a detail page or sheet.
- **N24** A comfortable page shows at most one compact table, and only
  a short one (ten rows or fewer, with "全部 ›" per A4).
- **N25** A settings page's first screen holds the settings most people
  change: at most 8 sections and 16 rows, and no taller than two
  viewports at the reference size (phone 393 × 852, desktop window
  1100 × 760). Advanced and rarely used settings go to a "高级 / Advanced"
  detail page, privacy and diagnostics to "隐私与诊断 / Privacy &
  Diagnostics" (H5, N23). A footer on the first screen is one sentence;
  longer explanations live on the detail page.
- **N26** A list of things the user adds (plugins, scripts, rules, Wi-Fi
  rules, hosts) on a comfortable page shows at most five rows. Beyond
  five it folds in place behind "显示全部 N 个 / Show all N" (which turns
  into "收起 / Show less"), or opens a detail page with "全部 ›" (A4).
  The add action stays visible below the folded list.
- **N27** A master switch that turns a feature on or off sits in its own
  section, above the content it governs, never as one row among the
  items it controls (H7).

## 4. Grouped and nested lists

A list of things that belong to something else (members of a network by
region, virtual machines on a host, devices behind a gateway, nodes by
subscription) shows that structure instead of one long flat list. The
network member list of AnixOps Net is the reference case.

- **N28** A list that can pass about twenty rows is grouped by one
  dimension at a time. The product names the default dimension and offers
  at most three others, plus "不分组 / None", in one "分组 / Group by"
  control at page scope (S2). Groups never nest inside groups.
- **N29** A group header states the group's name and its count
  ("欧洲 · 9 台"), is sticky, and folds its rows. A folded header becomes
  a one-line summary: the count, the worst status inside it (N33) and the
  one metric that matters for the group. The group the user is in, or
  the one that needs attention, opens unfolded; the rest open folded.
  What the user folds or unfolds is remembered per list.
- **N30** A row may unfold in place to show the things it stands for,
  one level only (H9). The children are rows in the same columns,
  indented once, on the `--fill-1` background, without actions of their
  own beyond the default one (S7). Anything deeper opens the detail page
  or the inspector. On pointer platforms the disclosure control unfolds
  and a click on the row selects it; on touch a tap unfolds, and the
  unfolded part ends with a link to the detail page (A4).
- **N31** A parent row summarises what it holds while folded: the count
  with its noun ("5 台虚拟机", "2 个子网") in `--label-2` after the name.
  Children fold after five behind "显示全部 N 个 / Show all N" (N26).
- **N32** Search looks inside folded groups and folded rows. A match in
  a child shows its parent unfolded with the match visible; groups with
  no match are hidden, and the header count becomes "matches / total"
  ("3/9"). Filters work the same way. Clearing the search restores the
  fold state from before it.
- **N33** A folded group or parent shows the worst status among its
  rows, as the dot and one word with a count ("1 台不可达"), never a
  colour alone (H4, N14). A condition that changed without the user
  acting (a path that fell back, a link that switched over) is a pill on
  the affected row and one banner for the page (F2), not a pill on every
  row it touches.
- **N34** What a row is (its role or kind) is a neutral pill after the
  name, one per row; how it is reached and how it is doing stay in their
  own columns (N8). On touch the second line carries, in this order:
  the identifier, how it is reached, then the count of what it holds
  (N5).

## 5. Review checklist

1. Is the page's tier the one its type calls for, and only one? (N1, N3)
2. On touch, are rows still 44 or taller? (N5)
3. Do numbers line up, with units, in tabular digits? (N10)
4. Does anything jump sideways or reorder while data updates? (N9, N16)
5. Are truncated values recoverable by tooltip and copy? (N12)
6. Are absent, loading and failed values distinct? (N13, N14)
7. Are column choices and sort remembered? (N16, N17)
8. Does the settings first screen fit the budget, with advanced and
   diagnostic items on their detail pages? (N25)
9. Does every user-added list fold after five rows? (N26)
10. Does each master switch have its own section? (N27)
11. Is a long list grouped by one dimension, with counts and a folded
    summary on each header? (N28, N29)
12. Do rows unfold one level only, with the rest on a detail page? (N30)
13. Does search reach folded groups and children? (N32)
14. Does a folded group or parent show the worst status inside it, in
    words? (N33)

Products check N25–N27 in CI, not only in review: a static count of the
settings first screen's sections and rows, and a runtime measure of the
page height and of list lengths in the screenshot jobs (anixops-net
`docs/ui-ux.md`, "自动检查").
