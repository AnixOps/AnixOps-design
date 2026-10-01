# Naming

## The name

- **AnixOps**: capital A, capital O, one word. In prose, titles, UI, store
  listings, README headings and commit messages.
- **anixops**: lowercase only where the medium forces it: package and module
  names, binaries, domains, Docker images, bundle IDs
  (`com.anixops.controlcenter`), environment variables (`ANIXOPS_*`).
- Never "Anixops", "ANIXOPS", "Anix Ops", "Anix-Ops" or "AnixOPS". Never
  translate or transliterate it: Chinese copy also writes "AnixOps".

## Products

Every product is **"AnixOps <Product>"**. "AnixOps" alone means the brand,
never one product.

| Product | Canonical name | Short form (after first mention, inside the product) | Identifier |
|---|---|---|---|
| Admin panel (anix-control) | **AnixOps Control** | Control | `anix-control` |
| Web, mobile and TUI client (control-center) | **AnixOps Control Center** | Control Center | `anixops-control-center` |
| Node agent (anix-agent) | **AnixOps Agent** | Agent | `anixops-agent` |
| SSH client (EasySSH and AnixOps-ssh, merging) | **AnixOps SSH** | SSH | `anixops-ssh` |
| To-do app (ToDoList) | **AnixOps ToDo** | ToDo | `anixops-todo` |
| Network tool (NetworkCore) | **AnixOps NetworkCore** | NetworkCore | `anixops-networkcore` |

Platform variants add a suffix, not a new name: "AnixOps Control Center for
iOS", "AnixOps Control Center (Web)". Repositories created before this guide
keep their names; their READMEs, window titles, store listings and
`<title>` tags use the canonical name.

Products not in this table follow the same pattern when they first get a
user-facing name; add them here in the same change.

## The studio: AnixOps Studio

**AnixOps Studio** is the one-person studio that makes AnixOps products. It is
the maker, not a product: never put it in the product table or name an app
"AnixOps Studio".

- Use it where the maker is named: store publisher and developer name, About
  dialogs (「AnixOps Studio 出品」 / "Made by AnixOps Studio"), website footer,
  press and contact pages.
- **It is not a legal entity yet.** Until one is registered, legal text
  (copyright lines, licenses, privacy policies, store legal fields) names the
  owner as a person; "AnixOps Studio" may follow as a trading name, never as
  the rights holder on its own.
- If a business is registered later (for example a Chinese 个体工商户), its
  registered name goes in legal text only, exactly as on the licence. Chinese
  registered names are written in Chinese characters, so the registered name
  and the brand can differ; the brand stays "AnixOps" and the studio "AnixOps
  Studio" in all product and marketing copy.

## Fixes found in the 2026-10 audit

| Where | Today | Use |
|---|---|---|
| Flutter web `<title>` | `anixops_mobile` | AnixOps Control Center |
| NetworkCore README title | `networkcore_AnixOps` | AnixOps NetworkCore |
| EasySSH window and README | EasySSH | AnixOps SSH |
| AnixOps-ssh app | AnixOps SSH Manager | AnixOps SSH (the two merge into one product) |
| ToDoList | ToDoList | AnixOps ToDo |
| Website | "AnixOps Studio" used like a product | The studio name, used as maker only (see above) |
| Archived repos `Anixops-control-center(-worker)` | Anixops | Archived; leave as is |

## Writing product names

- Do not abbreviate to initials ("AC", "ACC") in UI or docs.
- Do not add "™" or "®" in product UI.
- Possessive and plural forms are avoided: "the AnixOps Control dashboard",
  not "AnixOps Control's dashboard".
- In Chinese, product names stay in Latin script with no manual spaces
  around them, as in [voice and tone](voice-and-tone.md):
  「在AnixOps Control中添加节点」.
