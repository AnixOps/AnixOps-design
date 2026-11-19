# Neutral terminology

Every AnixOps product describes what it does in plain technical terms: a
network debugging tool, a proxy client, a node management panel. Copy never
describes a product by what it is used to get around, and never borrows the
slang of the communities that resell proxy access. This keeps store listings,
reviews, partners and users on the same, accurate description of the
software.

These rules apply to everything a product publishes: UI strings, store
listings, release notes, README and docs, website and download pages, code
identifiers and comments, test fixtures, commit messages and pull request
titles. They apply to private repositories too, because private text is
copied into public places more often than anyone plans.

The word list is machine-checked: [`scripts/neutral_terms.py`](../scripts/neutral_terms.py)
reads [`neutral-terms.json`](neutral-terms.json). Each product repository runs
the same script in CI (see "Adoption").

## Rules

- **T1** Describe the function, not a use. 「代理客户端」「网络调试工具」「节点管理面板」,
  "proxy client", "network debugging tool". Never 「翻墙」「科学上网」「梯子」 or
  any phrase about getting around a country's network.
- **T2** Name the parties neutrally. Whoever runs nodes and sells or gives
  access to them is a **服务商 / provider**; the people using it are its
  **用户 / users**; the web panel is **服务商面板 / provider panel**, or by
  name, **AnixOps Control**. Never 「机场」 / "airport".
- **T3** Name the network, not a country's policy. Paths, middleboxes and
  measurements are 「网络」「网络路径」「中间设备」「流量分类设备」, "network
  path", "on-path middlebox", "traffic classifier". Never 「墙」「GFW」
  「防火长城」 / "Great Firewall", and never 「审查」 / "censorship" or
  「封锁」 / "blocking" in the sense of a state blocking a network.
- **T4** Describe results, not intent. A destination is 「可达 / 不可达」
  ("reachable / unreachable"); a node can or cannot reach a service
  (「服务可用性」 / "service availability"). Never 「解锁」 / "unlock" for a
  service, 「突破」 / "circumvent", 「抗封锁」「抗审查」 / "anti-censorship".
- **T5** Routing describes the rule, not the destination country's politics:
  「直连」「经代理」「按规则」. Preset modes such as 「绕过大陆」「回国」 no longer
  exist (public builds ship no presets) and are not mentioned in product copy.
- **T6** Review in the code sense is 「评审 / 审核 / 核查」, never 「审查」.
- **T7** Protocol and threat-model documents describe what a classifier on the
  path can observe and do, in the terms of T3. A third-party tool or protocol
  keeps its own published name (for example a lab tool) only inside the
  directory that vendors or runs it.
- **T8** Values a product must keep reading from users' existing files (an old
  config key, an old enum value) stay in the parser and its tests, marked on
  the line with `neutral-terms: allow` and a one-line reason. They never appear
  in UI or docs.

## Replacements

| Avoid | 中文 | English |
|---|---|---|
| 机场 / airport | 服务商 | provider |
| 机场面板 | 服务商面板（或 AnixOps Control） | provider panel |
| 机场用户 | 服务商的用户 | users of a provider |
| 翻墙 / 科学上网 / 梯子 | 使用代理 | use a proxy |
| GFW / 墙 / 防火长城 | 网络路径上的中间设备、流量分类设备 | on-path middlebox, traffic classifier |
| 审查 (state) / censorship | 网络干扰 | network interference |
| 封锁 / blocked (state) | 不可达、连接被重置 | unreachable, connection reset |
| 抗封锁 / 抗审查 / anti-censorship | 连接可靠性、流量特征保护 | connection reliability, traffic-shape privacy |
| 解锁 / unlock (a service) | 服务可用性 | service availability |
| 回国 / 绕过大陆 | （不再提供；不提及） | (removed; not mentioned) |
| 审查 (review) | 评审、审核、核查 | review |
| GFW 列表 | （不再提供；不提及） | (removed; not mentioned) |

## Adoption

1. Copy `scripts/neutral_terms.py` and `guidelines/neutral-terms.json` into the
   product repository under `.github/scripts/` (same file names), unchanged.
2. Add a CI step: `python3 .github/scripts/neutral_terms.py`. It scans files
   tracked by git and exits non-zero on a hit.
3. A whole file that must keep a hit (a vendored third-party file, a lab tool's
   own configuration) goes in `.neutral-terms-allow` at the repository root,
   one glob per line with a `#` reason. Prefer `neutral-terms: allow` on the
   line (T8) over a whole-file entry.
4. When this list changes, bump this repository's version and copy both files
   again; the copies must stay byte-identical to the baseline.
