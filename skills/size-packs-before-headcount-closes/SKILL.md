---
name: size-packs-before-headcount-closes
description: "Human-readable instructions for choosing a fixed-pack quantity of ordinary event supplies when attendance is bounded but not final before purchase."
---
# 人数未定时决定买几包 / Size Packs Before Headcount Closes

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 一项物料 5–10 分钟 / 5–10 minutes for one supply |
| Requirements / 必要物品 | 已确认人数、尚可能参加的人数上限、每人用量、现存与每包件数、采购截止 / Confirmed count, bounded possible count, use per person, stock and pack count, purchase cutoff |
| Side effects / 现实副作用 | 你会知道多买一包覆盖了谁，而不是只知道“以防万一” / You will know whom one extra pack covers instead of saying “just in case” |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当一次已经确定的小型普通活动需要同一种**可逐件计数的日用品**，但付款截止早于最终回复人数时，加载这份 Skill。它只决定该物料今天买几包、能覆盖多少人、什么时候必须重算；不设计活动、不估算餐食营养或份量，也不负责大型公众活动的人流安全。没有真实采购截止，等人数确定后使用普通包装量判断即可。

### 准备与输入

先取得活动已确认人数、仍待回复但确实受邀的人数，以及已定方案中**每人会用几件**。把可能人数上限锁在真实邀请或座位范围内，不用“可能还有朋友来”无限加码。确认手上已可用的同款物料、现售每包实际件数、今天预算与空间，以及最后还能加买的真实时间和渠道。

例如一人需要一张普通姓名贴；已经 12 人确认，最多另有 10 位已受邀者可能答应，手头有 2 张可用，商店每包 10 张。这些数字只是算例。若物料涉及身份核验、出入安全、过敏或医疗用途，本 Skill 不替你决定数量或规则。

### 执行

1. **写两个有依据的人数。** 下界是已经确认的 12 人，上界是 12 加上仍可答应的 10 人，即 22 人。先核实“待回复”尚未过答复截止；取消者不再计入上界。每人用量若还没有确定，先向活动计划确认，不猜一个包装数。
2. **分别算最少包数。** 对下界与上界各用“人数 × 每人件数 − 已确认可用存量”，负数按 0 算，不足一包时向上取整。例子中 12 人缺 10 张，需 1 包；22 人缺 20 张，需 2 包。反查任一方案可覆盖的人数时，用“现存 + 拟买包数 × 每包件数”除以每人件数，只数完整人数。一包与两包的差异就是这次尚未确认的覆盖选择，不能用平均 17 人掩盖它。
3. **检查能否等、能否补。** 若最终回复会在付款截止前到，等回复再定包数。若先要付款，但截止后仍有可靠的补买渠道，就只为已确认人数买，并写下何时检查回复、最多还需加几包。若补买并不可靠，就在 1 包覆盖 12 人和 2 包覆盖 22 人之间作明确选择；同时写出少买时未覆盖的人数，或多买时最多剩多少张。
4. **给额外一包一个明确取舍。** 多买必须今天付得起、放得下、带得动；未用完的物料若可留给下一次用途，写明去向。若不能再用，也只有你明确接受这次可能的余量与花费，才选择覆盖上界。否则使用已确认的低包数，向活动负责人报告可能缺口，或选已经可用的替代办法；不能把“也许需要”伪装成必买事实。
5. **结账前再读一次状态。** 核对最新回复、实际每包件数和总价。任何人数、包装或截止变化都回到第 2 步；购买后才出现的新回复不让此前决定自动变成正确。

### 成功条件

付款前你能说出**买几包、至少覆盖多少已确认者、最多能覆盖到多少人、何时必须再查回复、若人数超出怎么办**。若关键人数或采购期限不明而无法给出可信覆盖，明确暂停购买决定也算完成。没有声明覆盖范围的“多买一包”不是计划。

### 常见报错、补救与停止

- **ERR_PENDING_AS_CONFIRMED：** 把所有待回复者写进已确认人数。拆成下界和上界，再比较包数；不替别人回复。
- **ERR_AVERAGE_HEADCOUNT：** 用一个平均人数买，结果可能既不能保证已确认者，也无意承担多买。回到两端与各自包数，明说接受哪种余量或缺口。
- **ERR_TOP_UP_FICTION：** 口头说“以后再买”，但店关门、配送不及或没有可付款渠道。把补买视为不可行，在今天的两种覆盖方案间重新决定或暂停。
- **ERR_PACK_COUNT_CHANGED：** 网上图片写 10 张，现售包装变成 8 张。按真实件数重算，不用旧记忆填今天的缺口。
- **ERR_HEADCOUNT_CHANGED：** 付款前来了新回复或有人取消。更新时间、人数和两端包数；已在付款后发生的变化交活动执行计划处理，不假装仍能改变本次订单。

### 假设、替代与现实副作用

这份 Skill 只处理小型、低风险活动中的普通可计数物料，例如已选定的姓名贴，不推断谁有权入场或活动应接纳多少人。实际报名方式、付款截止、售卖规格和行动能力会变；用真实通知、可访问的商品信息和你能承担的金额。看不清件数或无法去第二次商店时，可请店员展示标签、选择可行配送或事先准备可重复使用的物料；每种替代都要先确认真的可得。大型公众活动的安全容量不由购买包数决定。

现实副作用是你可能需要把“以防万一”翻译成一个具体的覆盖区间；数字会比焦虑诚实。

### 来源

- [美国 EPA：活动减废清单（存档）](https://archive.epa.gov/epawaste/wycd_archived/web/html/chklist.html) — 避免无差别分发一次性资料，并考虑可重复使用的姓名牌；不把其旧清单当作当前活动安全规则。
- [美国 FTC：The case of the shrinking packaging](https://consumer.ftc.gov/consumer-alerts/2024/10/case-shrinking-packaging) — 现售包装的实际件数应重新核对，不能只凭熟悉外观。
- Original synthesis — 已确认人数与可信上界、两端包数、覆盖范围和补买截止的决策流程；算例不是活动人数建议。

## English

Load this Skill when a confirmed small ordinary gathering needs one kind of **individually countable supply**, but you must pay before the final attendee replies arrive. You decide how many fixed packs to buy today, the number of people they cover, and when to recalculate. This does not design the event, plan meal portions or nutrition, or decide public crowd safety. If there is no real purchase cutoff, wait for the final count and use an ordinary package-size decision.

### Preparation and inputs

Get the number already confirmed, the number genuinely invited and still able to reply, and **units per attendee** from the existing event plan. Bound the possible headcount by actual invitations or seats, not an unlimited “someone may bring a friend.” Confirm usable stock, today's units per pack, budget and space, and the last time and real channel through which more can be bought.

Suppose one ordinary name badge is needed per person. Twelve people have confirmed, ten more invited people could still accept, you have two usable badges, and the store sells ten per pack. These are illustrative numbers. Supplies needed for identity control, access safety, allergy management, or medical use are outside this Skill's quantity decision.

### Execution

1. **Write two evidenced headcounts.** The lower count is the twelve confirmed people. The upper count is twelve plus ten invitees who may still accept: twenty-two. Check that pending replies are still possible; remove cancellations from the upper bound. If units per person are not settled, return to the event plan rather than guessing packs.
2. **Calculate both pack counts.** At each bound use “people × units per person − verified usable stock,” treating a negative gap as zero and rounding a partial pack up. In the example, twelve people leave a gap of ten badges, or one pack; twenty-two leave a gap of twenty, or two packs. To check how many people a chosen count covers, divide “stock + packs × units per pack” by units per person and count only whole people. The one-pack difference is the unresolved coverage choice. Averaging to seventeen people does not decide it.
3. **Check whether you can wait or top up.** If final replies arrive before payment must happen, wait. If payment comes first but a later purchase is genuinely possible, cover confirmed people now and record when to recheck replies and how many more packs could be needed. If top-up is not reliable, explicitly choose between one pack covering twelve people and two covering twenty-two; record either the people left uncovered or the maximum unused badges.
4. **Make the extra pack an explicit tradeoff.** You must be able to pay for, place, and carry it today. If unused units have a credible later use, record it. If they do not, choose upper-bound coverage only when you knowingly accept the possible remainder and cost. Otherwise use the lower count, tell the event organiser about the possible gap, or use an already available alternative. “Might need it” is not a purchase instruction.
5. **Reread the state before checkout.** Check the latest replies, actual pack count, and total price. A changed headcount, pack, or cutoff sends you back to step 2. Replies that arrive after payment do not retroactively make the earlier choice correct.

### Success

Before payment you can state **packs to buy, confirmed people covered, the highest attendance covered, when to recheck replies, and what happens if attendance exceeds coverage**. Pausing is a completed decision when a critical count or purchase deadline cannot be established. “One extra pack” without a coverage range is not a plan.

### Common errors, recovery, and stop points

- **ERR_PENDING_AS_CONFIRMED:** Every pending invitee is counted as confirmed. Separate the lower and upper counts, then compare pack counts; do not answer for other people.
- **ERR_AVERAGE_HEADCOUNT:** An average count masks both the guaranteed need and the possible surplus. Return to both ends and state which shortage or remainder you accept.
- **ERR_TOP_UP_FICTION:** Someone says “buy more later,” but the store will be closed, delivery is too late, or payment will not be possible. Treat top-up as unavailable; reconsider today's coverage choices or pause.
- **ERR_PACK_COUNT_CHANGED:** An online photo says ten badges, but today's pack has eight. Recalculate from actual contents, not the old image.
- **ERR_HEADCOUNT_CHANGED:** A reply or cancellation arrives before payment. Update the dated counts and both pack calculations. Changes after payment belong to event execution; they cannot change this purchase retroactively.

### Assumptions, alternatives, and side effects

This covers ordinary countable supplies for small low-risk gatherings, such as a chosen name badge. It does not decide admission rights or event capacity. Reply methods, purchase cutoffs, seller packs, and physical access differ. Use actual messages, accessible product details, and an amount you can afford. If print is hard to read or a second shop is inaccessible, ask staff to show the count, check workable delivery, or verify available reusable supplies before relying on them. Pack count is not a public-event safety limit.

You may need to translate “just in case” into a specific coverage interval. Numbers are more candid than nerves.

### Sources

- [US EPA: archived event-waste checklist](https://archive.epa.gov/epawaste/wycd_archived/web/html/chklist.html) — discourages indiscriminate one-time handouts and suggests reusable name badges; not used as current event-safety guidance.
- [US FTC: The case of the shrinking packaging](https://consumer.ftc.gov/consumer-alerts/2024/10/case-shrinking-packaging) — reread today's actual pack count rather than relying on familiar packaging.
- Original synthesis — confirmed and bounded possible counts, two pack calculations, coverage and top-up cutoff; example figures are not an event-attendance recommendation.
