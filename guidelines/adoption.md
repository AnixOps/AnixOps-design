# Adopting 1.0.0

Where each AnixOps product diverges from this system today (from the
read-only org audit of 2026-10-01) and what it changes to adopt 1.0.0. Owner
decisions behind this list: one accent for every product (no sub-brand
accents), anix-control's `#0064FA` migrates to the indigo accent, EasySSH and
ToDoList carry the AnixOps brand, and the product names in
[naming](naming.md).

## Every product

1. Replace literal colours with tokens: copy the file for your stack from
   [platforms](platforms.md); primaries such as `#0064FA`, `#3B82F6`,
   `#0A6DE6`, `#0071E3`, `#007AFF`, `#007BFF` and `#5665E6` become
   `--accent` / `--accent-fill`. The semantic `#22C55E` / `#F59E0B` / `#EF4444`
   become `--success` / `--warning` / `--danger`, whose light values are
   darker so they pass WCAG AA as text.
2. Replace framework default icons (Flutter, Tauri, Vite) and missing
   `/favicon.svg` files with the set in `brand/assets/`.
3. Ship Inter from `fonts/inter/`; drop references to fonts that are not
   shipped (SF Pro web fonts, placeholder Inter TTFs, Segoe UI art).
4. Use the canonical name in titles, window captions, store listings and
   README headings, and add the README banner.
5. Neutral slate (`#0F172A`, `#1E293B`, `#334155`, `#94A3B8`) is replaced by
   the system neutrals (`--bg`, `--label-*`, `--separator`). Slate survives
   only as the backdrop of the brand tile in marketing art
   (`--brand-slate-900/800`).

## Per product

| Product (repo) | Stack | Diverges today | Adopt 1.0.0 |
|---|---|---|---|
| **AnixOps Control** (anix-control) | Vue 3, hand-written CSS | Primary `#0064FA`, dark `#17171A` | `tokens.css`; accent `#4F5BE8`/`#818CF8`, dark bg `#000`; UI redesign plan U1 consumes the tokens |
| **AnixOps Control Center** web (control-center/web) | Vue 3 + Tailwind | Tailwind sky on slate; `/favicon.svg` missing | Tailwind preset, favicon set, banner |
| **AnixOps Control Center** mobile (control-center/mobile) | Flutter M3 | Primary `#3B82F6`; placeholder `app_icon.png`, `logo.png` and Inter TTFs; web title `anixops_mobile` | `anixops_tokens.dart`, `app-icon/` via flutter_launcher_icons, Inter TTFs, web title |
| **AnixOps Control Center** TUI (control-center) | bubbletea + lipgloss | 256-colour 62/57/86/241 | Go module `TermAccent`/`TermSuccess`/`TermMuted`, `ColorEnabled`, `Banner` |
| **AnixOps Agent** (anix-agent) | cobra CLI | No colour policy or banner | Go module; `--color`, `NO_COLOR`, `--version` banner ([terminal](terminal.md)) |
| **AnixOps SSH** (EasySSH) | egui | Name "EasySSH"; `#5665E6`/`#7E89FF` | `anixops_tokens.rs`; rename; icon set |
| AnixOps-ssh | Tauri + React | Name "AnixOps SSH Manager"; Tauri default icon | `tokens.css` (+ shadcn mapping if used), `tauri/` icons; name per [naming](naming.md) |
| **AnixOps NetworkCore** (NetworkCore) | Tauri + React | Green accent `#A8E8C4` and grid icon; README `networkcore_AnixOps` | Indigo accent, AnixOps mark and `tauri/` icons; green may stay only as a chart colour |
| **AnixOps ToDo** (ToDoList) | Vue 3 + Element Plus | Unbranded | `element-plus.css`, mark, rename |
| Website (AnixOps-website) | Vue 3 + Element Plus | Gradient `#00D4FF→#6366F1`; "AnixOps Studio"; `/favicon.svg` missing | Gradient `#38BDF8→#6366F1`, `element-plus.css`, favicon set, OG image |
| node-platform | Next 15 + Tailwind + shadcn | "A" monogram favicon; primary `#0A6DE6` | Hexagon mark favicons, Tailwind v4 theme + shadcn mapping |
| Blog | Hono SSR | Primary `#3B82F6` | `tokens.css`, favicon set, OG image |
| Prompt-To-Website | Vue 3, hand-written CSS | Primary `#0071E3` | `tokens.css` |
| CodeDrivenMedia | — | Primary `#007AFF` | `tokens.css` or the platform file for its stack |
| AnixOps-network | Flask + Bootstrap | Primary `#007BFF` | `tokens.css`; map Bootstrap's `--bs-primary` and friends to the tokens |
| Anixops-control-center, -worker | — | Archived | No change |

## Order

1. AnixOps Control (flagship, redesign in progress) and Control Center web,
   mobile and TUI, so the main product line is consistent first.
2. AnixOps Agent and the other CLIs: colour policy and banner.
3. Website, Blog and node-platform: public faces (favicon, OG image).
4. AnixOps SSH, NetworkCore, ToDo and the rest.

Track adoption per repository with an issue that links this page and the
version adopted.
