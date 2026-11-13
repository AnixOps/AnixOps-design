# Legal: terms of use, acceptable use and disclaimer

[`terms.zh-CN.md`](terms.zh-CN.md) is the baseline user agreement shared by
every AnixOps product: scope and definitions, how it relates to the software
licences, the acceptable use policy (prohibited uses), MITM / certificate /
script rules, third-party content, operator duties, the "as is" disclaimer,
limitation of liability, abuse reporting, changes and governing law.

It is written in Simplified Chinese because the products' users are; the
Chinese text is authoritative. **It is a draft and not legal advice. Have a
lawyer review it before a store listing or commercial launch.**

## How a product adopts it

Each product repository has a `TERMS.md` made of three parts, in this order:

1. A header that names the product, the baseline version it follows
   (`基准版本 2.0.0`) and links back here.
2. **产品补充条款** (product supplement): who the product is for and the extra
   rules that follow from what it does. A supplement may only add or tighten;
   where it conflicts with the common terms, the stricter rule applies.
3. The common terms: everything between `BEGIN COMMON TERMS` and
   `END COMMON TERMS` in `terms.zh-CN.md`, copied verbatim.

The README of the product links `TERMS.md` next to `LICENSE`.

| Repository | Audience | Supplement focus |
|---|---|---|
| `networkcore_anixops` | Developers who embed the kernel | Integrators publish their own terms; MITM/scripts off by default; no remote certificate install API |
| `anixops-net` | End users of the client apps | Own device only; user-imported subscriptions, plugins and scripts; certificate trust is a manual user step; app stores |
| `mitm_anixops` | Developers of MITM adapters and recipe authors | Own traffic only; declared host scope; no recipes that defeat third-party security; adapters must not auto-trust roots |
| `anx` | Operators that run anx-node / anx-server (closed source) | Proprietary licence first; operator duties; no use to attack or impersonate third-party services |
| `anix-control` | Operators of the panel | Operator is the service provider to its users; own terms, KYC and log retention as required by law; abuse handling |
| `anixops-ansible` | Operators deploying hosts | Only on hosts you own or administer; secrets handling; operator duties |

## Changing it

- Change the common terms here first, bump the version at the top of
  `terms.zh-CN.md` (patch: wording; minor: a new clause; major: a clause whose
  meaning changes), add a `CHANGELOG.md` entry, then open one PR per product
  repository that copies the new common terms and updates the header version.
- Product-only changes go in that product's supplement and do not change the
  baseline version.

## Open items

- A public abuse-report e-mail address (section 11 says it is to be announced).
- Governing law and court (section 13): England and Wales (decided by the
  owner on 2026-11-13, terms 2.0.0); local mandatory consumer protection is
  kept. Confirm with a lawyer.
- A privacy policy is a separate document and is not part of this baseline.
