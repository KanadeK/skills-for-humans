---
name: prevent-overlapping-household-orders
description: "Human-readable coordination for one shared household item when two people may buy it at the same time, before either pays twice."
---
# 别让两个人同时补同一件 / Prevent Overlapping Household Orders

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 分钟，加上对方回复时间 / 5–10 minutes plus response time |
| Requirements / 必要物品 | 同一件共享物品、可联系的购买人、简短状态记录 / One shared item, reachable buyers, a short status note |
| Side effects / 现实副作用 | 家庭群里会多一条明确的“谁来买” / One explicit “who is buying” message |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当两个人可能在同一段时间为同一家庭购买同一种普通物品，而你们还没确认**谁负责付款**时，加载这份 Skill。这里解决的是同时行动造成的重复取得；个人在付款前判断“家里已有的还够不够”，请先单独核对。已发生的双重付款、取消、配送和退货属于别的任务。

### 准备与输入

只选一件这次确实需要的共享物品，确认要在哪次活动前用到、家中有没有可用的、是否已有未到货订单，以及哪些人可能正在购买。用双方都能收到的方式联系：短信、电话、纸条、当面说或双方已在用的清单。无须安装新应用，也无须互发付款凭据、账户或完整订单截图。

### 执行

1. **先发一条可回答的信息。** 写清物品、用途和截止时间，例如“周五打扫要一包普通垃圾袋；我还没付款。你已经买了，或正准备买吗？”不要只发一张没有文字的商品图，让对方猜版本和意图。
2. **把状态分开。** 对方回复“家里有”“我已下单”“我正在看”“我没买”分别是不同状态。“正在看”不等于已买；“已下单”也不要再算作零库存。双方都核对自己能查到的实物或订单信息，不把未回复当成“没有”。
3. **指定这次唯一购买人。** 确实还需要购买时，明确一人负责，并请另一人确认停止购买同一需求。记录“物品—购买人—待买/已付款—回报时间”即可。没有收到确认且并不急用，就暂缓付款，约一个再核对的时间。
4. **付款结果立刻回报。** 成功后只报“已买、预计何时可用”；付款失败或放弃时改回“未买”，让另一人再决定。具体金额、收货地址或订单号只有在确实需要且双方愿意时才单独分享。
5. **处理时间紧张的例外。** 如果普通用途不能等回复，先查你有权查看的订单和库存；仍不确定时，说明“我现在为这一次用途买，暂勿重复购买”，并在购买后更新结果。明确标注这是带不确定性的例外，不把它当成双方已经同步。

### 完成条件

付款前，双方能看到同一件物品的“已有 / 已下单 / 一人待买 / 暂缓核对”状态，且只有一个被确认的购买人。若对方无法回复，结论是“未同步”，并有等待或一次紧急用途的明确处理；沉默不是批准。

### 常见报错与补救

- **两人同时说“我来买”：** 谁都先别付款；约定一人撤回，另一人明确回复收到后再继续。
- **信息交叉，回复过期：** 把状态和更新时间放在一条新消息里；旧的“没买”不能覆盖后来“已付款”。
- **指定的人到时没有回报：** 先问是否已付款，不把超时当作自动交接；确认未买后才改派购买人。确实等不了时，使用上面的带不确定性例外。
- **有人说“我放购物车了”：** 继续问是否已付款。购物车不能证明取得，支付状态才会改变是否再买。
- **不方便打字或看屏幕：** 用简短电话、语音或纸条确认，并重复一遍最终购买人和状态。
- **发现双方都已付款：** 停止第三次购买，保存各自订单状态；需要取消或退货时转入对应售后流程，不在这里猜商家政策。

### 假设、替代与现实副作用

这份 Skill 假设相关的人愿意为共同采购交换必要的状态，不要求他们共享账号、实时定位或全部购物记录。不同住、轮班、网络不稳定或语言不同，可以约定一个固定的文字、电话或纸面交接点。若对方不愿协作，你只能标记自己的决定和不确定性，不能替对方承诺不买。

多出一条消息和几分钟等待是现实副作用；得到的是一次可追溯的购买责任，而不是一套家庭监督系统。

### 来源

- Original synthesis。此处是普通家庭购买协调流程；具体商品状态、费用、配送和商家规则以实际记录为准。

## English

Load this Skill when two people might buy the same ordinary item for one household during the same shopping window and have not agreed **who will pay**. It handles a duplicate caused by simultaneous action. Check whether usable stock already covers the need as a separate personal purchase decision. If two payments have already happened, cancellation, delivery, and returns belong to their own tasks.

### Preparation and inputs

Choose one shared item that is actually needed this time. Confirm when it will be used, whether usable stock exists, whether an order is already pending, and who else might buy it. Use a channel both people can access: a text, call, note, face-to-face conversation, or a list you already share. No new app, payment credentials, account access, or full order screenshots are required.

### Execution

1. **Send a question that can be answered.** State the item, use, and deadline: “We need one pack of ordinary bin liners for Friday's cleaning. I haven't paid. Have you bought them or are you about to?” A product image without context makes the other person guess the version and purpose.
2. **Keep the states distinct.** “We have some,” “I ordered it,” “I'm looking,” and “I haven't bought it” mean different things. Looking is not buying; a pending order is not zero stock. Each person checks stock or order information they can legitimately access. No reply means unknown, not no purchase.
3. **Name one buyer for this need.** If a purchase remains necessary, one person takes responsibility and the other confirms they will stop buying for the same need. A note saying “item — buyer — to buy/paid — report by [time]” is enough. Without confirmation and without urgency, defer payment and set a time to check again.
4. **Report the payment outcome promptly.** After success, send “bought; expected to be available by [time].” If payment fails or you abandon the purchase, return the state to “not bought” so the other person can decide. Share amounts, addresses, or order numbers separately only if needed and agreed.
5. **Handle a time-sensitive exception.** If an ordinary immediate use cannot wait for a reply, first check orders and stock you are entitled to see. If still uncertain, say “I am buying for this one use now; please pause your purchase,” then report the outcome. Mark this as an uncertain exception, not as confirmed synchronization.

### Success

Before payment, both people can see one item's state as “already have / ordered / one assigned buyer / waiting to check,” and only one buyer has been confirmed. If someone cannot reply, the state is “not synchronized,” with a clear wait or immediate-use action. Silence is not approval.

### Common errors and recovery

- **Both say “I'll buy it”:** Both pause payment. One withdraws; the other continues only after that is acknowledged.
- **Messages cross or a reply becomes stale:** Put the state and update time in one new message. An old “not bought” cannot override a later “paid.”
- **The assigned buyer misses the report time:** Ask whether they paid; a missed update does not automatically hand the purchase over. Reassign only after confirming no purchase, or use the uncertain immediate-use exception above if it cannot wait.
- **Someone says “It's in my cart”:** Ask whether they have paid. A cart is an intention; payment changes the acquisition state.
- **Typing or reading a screen is difficult:** Use a brief call, voice message, or written note, and repeat the final buyer and state.
- **Both have already paid:** Stop a third purchase and keep each order's status. Use a separate cancellation or returns process; do not guess a seller's policy here.

### Assumptions, alternatives, and known side effects

This Skill assumes the people involved are willing to exchange the minimum information needed for a shared purchase. It does not require shared accounts, live location, or access to every shopping record. Different homes, shifts, unreliable networks, or different languages may call for a fixed text, call, or paper handoff. If the other person will not coordinate, you can record your own decision and uncertainty but cannot promise what they will do.

The side effect is one extra message and possibly a few minutes of waiting. The result is responsibility for one purchase, not a household surveillance system.

### Sources

- Original synthesis. This is an everyday coordination procedure; verify the particular product state, cost, delivery, and seller terms from actual records.
