# Voice and tone

Short, active, and about the result. Chinese and English are written
separately; never machine-translate one from the other.

## Rules (both languages)

- Buttons are verbs that say what happens: 「添加节点」/ "Add node", not
  「确定」/ "OK".
- Errors say what happened and what to do: 「无法连接节点 hk-01：连接超时。检查防火墙是否放行 443 端口。」
- Confirmations name the object: 「删除节点 hk-01？此操作无法撤销。」
- Empty states name what is missing and offer the first action:
  「暂无节点」+ 「添加节点」 / "No nodes" + "Add node".
- No exclamation marks in system copy; no blame (「你输入错了」).

- Describe what the software does in neutral technical terms; the word list
  and replacements are in [terminology.md](terminology.md).
- Interface copy is written in a formal, concise register (W1–W7 below).

## Formal register (W1–W7)

Interface copy is written language, not speech: short, impersonal and
factual. These rules apply to every string a product shows (labels, buttons,
titles, hints, footnotes, empty states, toasts, errors, dialogs, consent and
permission text) in every language. The words W1–W3 and W5 forbid are listed
in [`formal-copy.json`](formal-copy.json); product repositories copy it and
check their string tables in CI (the AnixOps Net client: `ui_lint.py` U7, U8).

- **W1 No second person.** No 「你」「您」 in Chinese, no "you / your" in
  English. Name the object or the action instead:
  「只打开可信来源的插件」 / "Turn on only plugins from trusted sources",
  not 「只打开你信任的插件」 / "Turn on only plugins you trust".
- **W2 No colloquial words.** No sentence-final particles (吧、呢、啊、哦、啦、呀、嘛、了),
  no 「一下」「咱」「啥」「搞」「弄」「就行」「再说」「记得」「放心」, no 「别」 (a command is 「勿」 or 「不」;
  「别人」「别的」 are 「他人」「其他」), no 「还没有」 (write 「暂无」 or 「尚未」).
  English has no contractions ("can't", "isn't", "it's"), no interjections
  ("Oops", "Hmm") and no fillers ("just", "simply", "easily", "basically").
- **W3 No exclamation marks**, in either language.
- **W4 What, not why or how.** A hint says what the control does and what it
  changes, in one sentence. It does not explain the reason, the mechanism or
  the steps; that belongs in the documentation. Keep only what the user needs
  to decide: data that leaves the device, a change to the system, an action
  that cannot be undone.
- **W5 No explanatory connectives.** No 「因为」「所以」「因此」「由于」「这样」
  「以便」「从而」「为了」「也就是说」「换句话说」; no "because", "so that",
  "in order to", "that way", "which means", "in other words". If a sentence
  needs one, it is an explanation (W4): cut it.
- **W6 At most two sentences per string**, one where possible. Labels,
  buttons, titles and column headers are a word or a short phrase without a
  full stop.
- **W7 Fixed patterns.** Empty state 「暂无节点」 / "No nodes". Status
  「已连接」「正在连接」「未连接」 / "Connected", "Connecting", "Not connected".
  Failure 「导入失败：证书已过期」 / "Import failed: the certificate has
  expired", not "Couldn't import". Confirmation 「删除节点 hk-01？」 /
  "Delete node hk-01?". Deferral 「稍后」 / "Later", not 「稍后再说」 /
  "Maybe later".

Errors, legal text, consent and privacy disclosures follow the same rules.
Rewording them keeps every fact, obligation and listed data item; only the
phrasing changes.

Examples:

| Avoid | Write |
|---|---|
| 还没有插件。粘贴一个插件网址导入试试吧。 | 暂无插件。 |
| 开启后，我们会在本机生成一张根证书，这样才能解密 HTTPS 流量。 | 开启时生成并信任本机根证书。 |
| 别担心，你的密码不会被上传。 | 密码不会上传。 |
| Couldn't reach the node. You may want to check your network! | Connection to the node failed. Check the network. |
| Just paste your link here and we'll take care of the rest. | Paste a subscription link. |

## Chinese

- Full-width punctuation（，。：；？！「」）.
- A space between a number and its unit: `128.4 GB`, `500 Mbps`, `30 天`.
- No manual space between Chinese and Latin words; the font handles it.
- Dates: `2026-11-30`; relative times 「3 分钟前」 with the absolute time on hover.

## English

- Sentence case for titles and buttons: "Copy subscription link".
- No contractions (W2).

## Glossary (seed)

| 中文 | English | Note |
|---|---|---|
| 节点 | Node | Proxy service node (`Node`) |
| 转发节点 | Forward node | Forward execution node (`ForwardNode`); never call it 节点 alone |
| 转发规则 | Forward rule | |
| 隧道 | Tunnel | |
| 限速 | Speed limit | |
| 订阅 | Subscription | |
| 订阅链接 | Subscription link | |
| 订阅模板 | Subscription template | |
| 流量 | Traffic | GB, TB |
| 速率 | Rate | Mbps |
| 到期 | Expires | |
| 工单 | Ticket | |
| 帮助中心 | Help Center | |
| 封禁 / 解封 | Ban / Unban | |
| 凭据 | Credentials | |
| 部署 | Deployment | |
| 审计日志 | Audit log | |
| 插件中心 | Plugin Center | |
| 组网 | Mesh | The private-network feature and its page; never a third-party product name |
| 网络 | Network | One mesh network the device joins: 「加入」/ "Join", 「已加入」/ "Joined" |
| 成员 | Member | A device in a network; 「本机」/ "This device" for the local one |
| 地区 | Region | A group of members joined to the others by border members |
| 边界 | Border | Role: links a region to other regions |
| 网关 | Gateway | Role: advertises the local network it sits in |
| 宿主 | Host | Role: joins on behalf of the virtual machines it runs |
| 接入端 | Client | Role: joins only; does not relay or advertise (phones) |
| 通告子网 | Advertised subnet | 「通告」/ "Advertise" is the verb |
| 直连 | Peer-to-peer | Between members. The routing policy 「直连」 stays "Direct" |
| 中转 | Relayed | With the hop count: 「中转 2 跳」/ "Relayed · 2 hops" |
| 跨区 | Cross-region | 「跨区 3 跳」/ "Cross-region · 3 hops" |
| 途经点 | Waypoint | A member a custom path must pass through |
| 已回落 | Fell back | A custom path that is using the default path; the message names the unreachable member |
| 已自动切换 | Switched automatically | A cross-region link that is taking a detour |
| 未启用前向保密 | No forward secrecy | Label on a network using the standard mode |
