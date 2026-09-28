---
name: verify-a-recipient-address-before-shipping
description: "Human-readable steps for checking an ordinary parcel's recipient and return-address entries with the real person and selected carrier before submission."
---
# 寄出前把收件地址与真人对一遍 / Verify a Recipient Address Before Shipping

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 每票 5–10 分钟 / 5–10 minutes per shipment |
| Requirements / 必要物品 | 收件人本人确认的当前资料、拟用承运方式、待提交地址字段 / Recipient-confirmed current details, chosen service, pending address fields |
| Side effects / 现实副作用 | 旧聊天里的地址不能自动续任 / An old chat address cannot renew itself |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当普通包裹已选定承运方式、你正准备提交面单或寄送资料时加载。你要让**收件人、当前地址、单元/邮编等实际适用字段与系统待提交内容一致**，并保留尚不能确认的部分。这里不判定货物可寄性、包装是否合格、法律地址效力或跨境报关；H131 负责普通包装。

### 准备与输入

从收件人本人或经授权的机构获得其愿意用于这一次配送的现行地址，不从旧聊天、订单模板或地图上自动继承。准备实际承运商与服务类型的当期地址字段要求；不同服务对邮政信箱、代收点、单位号和联系电话规则不同。地址信息只在你、收件人和真正承运所需的渠道使用，不在公开群里贴完整标签。

### 执行

1. **先确定谁实际收。** 写收件人愿意使用的姓名或机构称谓、收件位置和能接受这次寄送的联系办法；给亲友/前台/公司时先确认他们有权限接收，别把“住在那附近”当同意。
2. **逐字段对照地址。** 比较收件人提供的信息与面单草稿中的街道/门牌、楼栋、单元、楼层、城市/地区、邮编及方向词（只取当地/承运商适用项）。原资料缺一项就问本人；不要凭街景、相似楼号或自动补全结果猜。
3. **核对服务能否到这个地址类型。** 对邮政信箱、代收点、园区或特殊入口，查你已选承运商/服务的现行规则；例如 USPS 与 UPS 在美国的地址类型安排并不相同。不可用就换经收件人同意的合适服务/地点，不在系统里塞一个看似可通过的假街址。
4. **检查寄件/退回资料。** 按实际承运要求核对寄件人、退回地址和必要联络字段。非必需私人细节不写外露标签；门禁码、密码或私人备注不得为了省事贴在包裹外面，确需配送说明时走承运方支持且收件人同意的正式渠道。
5. **提交前做一次读回。** 让收件人或有权代表复述关键地址，逐字对照你将提交的草稿和正式标签预览，尤其是数字、单元和邮编。系统建议“标准化”地址却改了实际单元时先问，未确认就暂停提交。

### 完成与停止

本次收件人与实际服务的地址类型、关键字段、退回资料已从本人/正式规则对上待提交内容，或有清楚待确认项而尚未提交。这只证明资料核对，不保证承运商已经收件或最终送达。收件人没确认、地址冲突、服务不支持或需公开敏感门禁资料时停在草稿。

### 常见报错与补救

- **复制了去年的地址：** 联系收件人核对这一次，不把联系人列表当现址证据。
- **楼号和单元号被自动补全改掉：** 与收件人逐字回读，未确认就不要提交面单。
- **承运服务不收该信箱/代收类型：** 询问实际承运方可用选择，再获收件人同意，不伪造地址。
- **标签暴露私人门禁码：** 停止打印/提交，改走正式受控配送说明渠道，必要时请收件人自行授权。
- **只有机构总址没有具体部门：** 问收件人/机构该服务所需称谓与内部路由，别擅填一个想象的办公室。

### 假设、替代与副作用

这是普通国内寄送前的资料核对，地区格式和承运规则差异大，USPS/UPS 的美国示例不构成全球模板。视力、阅读或语言不便时用收件人认可的读回方式或可信协助者，不把完整地址公开展示。副作用是旧聊天里的地址不再自动获得连任资格。

### 来源

- [美国 USPS：Addressing Your Mail](https://pe.usps.com/text/dmm100/addressing-mail.htm) — 在其美国邮政格式中，收件人、街道、单元、城市/州和邮编各有用途；不移植为全球固定行数。
- [美国 UPS：How to Write a Shipping Address](https://www.ups.com/us/en/support/shipping-support/print-shipping-labels/how-to-write-address) — 其美国包裹地址提示保留单元和方向信息；具体服务限制以实际承运商为准。
- 本次本人读回、系统自动改址停点与非必需私人信息最小化为 Original synthesis。

## English

Load this Skill when an ordinary parcel has a chosen carrier service and you are about to submit its label or shipment fields. Make **the recipient, current address and applicable unit or postal details match what will actually be submitted**, keeping unknowns visible. This does not judge item eligibility, packaging, legal address status or customs. H131 owns ordinary parcel preparation.

### Preparation and inputs

Get the address this recipient or authorised organisation agrees to use for this shipment, not one automatically carried over from an old chat, order template or map. Read the selected carrier and service's current address-field rules; mailbox, access point, unit and phone rules differ. Share complete address only with you, the recipient and channels genuinely needed for carriage, not a public group.

### Execution

1. **Name who actually receives it.** Use the recipient's agreed name or organisation, delivery point and suitable contact route for this parcel. Confirm a friend, reception or workplace has authority to accept it; being nearby is not consent.
2. **Compare each address element.** Match recipient-provided information to pending label fields for street and number, building, unit, floor, city or area, postal code and directionals where the market and service use them. Ask the person about a missing field; do not infer it from street view, similar building numbers or autocomplete.
3. **Check that this service can use the address type.** For a PO box, access point, campus or special entry, read the chosen carrier and service's live rule. USPS and UPS in the US do not treat every address type alike. If unsupported, choose a feasible service or place with the recipient's agreement rather than inventing a street address that passes a form.
4. **Check sender and return details.** Verify sender, return location and any necessary contact field under the actual carrier's rules. Keep unnecessary private detail off an exposed label. Do not print access codes, passwords or private notes outside; use an official controlled instruction channel with the recipient's consent if access information is genuinely needed.
5. **Read back before submission.** Have the recipient or authorised representative restate key details and compare character by character with the draft and final label preview, especially numbers, unit and postal code. If an address-standardisation suggestion changes a real unit, ask first. Do not submit while it remains uncertain.

### Success and stop

The recipient, selected service's address type, key fields and return details match the recipient or real provider and the pending label, or unresolved lines are held before submission. This is data checking, not proof of carrier acceptance or delivery. Stop at the draft for unconfirmed recipient, conflicting address, unsupported service or pressure to expose sensitive access details.

### Common errors and recovery

- **Last year's address was copied:** Confirm this shipment with the recipient; an old contact is not current-location proof.
- **Autocomplete changed building or unit numbers:** Read them back exactly with the recipient before submitting.
- **This service rejects the mailbox or pickup type:** Check actual carrier choices and obtain recipient agreement; do not fabricate a location.
- **An access code appears on the outside label:** Stop printing or submitting and use an authorised controlled delivery-instruction route if appropriate.
- **Only an organisation headquarters address is known:** Ask for the department or internal routing this service needs; do not invent an office.

### Assumptions, alternatives, and side effects

This checks data before an ordinary domestic shipment. Formats and provider rules differ by region; USPS and UPS US examples are not a global template. Use the recipient's accessible readback or trusted help when sight, reading or language differs, without displaying the complete address publicly. Last year's chat address no longer renews itself automatically.

### Sources

- [US USPS: Addressing Your Mail](https://pe.usps.com/text/dmm100/addressing-mail.htm) — in its US postal format, recipient, street, unit, city or state and ZIP serve separate purposes; not a universal line count.
- [US UPS: How to Write a Shipping Address](https://www.ups.com/us/en/support/shipping-support/print-shipping-labels/how-to-write-address) — its US guidance retains apartment and directional details; the actual carrier's service rule governs.
- Recipient readback for this shipment, autocomplete stop and minimising unnecessary private information are Original synthesis.
