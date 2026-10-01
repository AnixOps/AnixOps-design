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

Every product is **"AnixOps <Product>"**. "AnixOps" alone means the brand or
the company, never one product.

| Product | Canonical name | Short form (after first mention, inside the product) | Identifier |
|---|---|---|---|
| Admin panel (anix-control) | **AnixOps Control** | Control | `anix-control` |
| Web, mobile and TUI client (control-center) | **AnixOps Control Center** | Control Center | `anixops-control-center` |
| Node agent (anix-agent) | **AnixOps Agent** | Agent | `anixops-agent` |
| SSH client (EasySSH) | **AnixOps SSH** | SSH | `anixops-ssh` |
| To-do app (ToDoList) | **AnixOps ToDo** | ToDo | `anixops-todo` |
| Network tool (NetworkCore) | **AnixOps NetworkCore** | NetworkCore | `anixops-networkcore` |

Platform variants add a suffix, not a new name: "AnixOps Control Center for
iOS", "AnixOps Control Center (Web)". Repositories created before this guide
keep their names; their READMEs, window titles, store listings and
`<title>` tags use the canonical name.

Products not in this table follow the same pattern when they first get a
user-facing name; add them here in the same change.

## Fixes found in the 2026-10 audit

| Where | Today | Use |
|---|---|---|
| Flutter web `<title>` | `anixops_mobile` | AnixOps Control Center |
| NetworkCore README title | `networkcore_AnixOps` | AnixOps NetworkCore |
| EasySSH window and README | EasySSH | AnixOps SSH |
| AnixOps-ssh app | AnixOps SSH Manager | AnixOps SSH (if it is a separate product from EasySSH, give it a distinct "AnixOps <Product>" name) |
| ToDoList | ToDoList | AnixOps ToDo |
| Website | "AnixOps Studio" | A canonical product name from the table, or remove |
| Archived repos `Anixops-control-center(-worker)` | Anixops | Archived; leave as is |

## Writing product names

- Do not abbreviate to initials ("AC", "ACC") in UI or docs.
- Do not add "™" or "®" in product UI.
- Possessive and plural forms are avoided: "the AnixOps Control dashboard",
  not "AnixOps Control's dashboard".
- In Chinese, product names stay in Latin script with no manual spaces
  around them, as in [voice and tone](voice-and-tone.md):
  「在AnixOps Control中添加节点」.
