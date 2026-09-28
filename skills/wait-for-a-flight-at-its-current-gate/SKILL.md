---
name: wait-for-a-flight-at-its-current-gate
description: "Human steps to use current airport and airline flight information to wait in a permitted area, identify the correct assigned gate and boarding status, and avoid treating a printed gate as final."
---
# 用实时信息在正确登机口候机 / Wait for a Flight at Its Current Gate

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 随航班候机时间；临近登机持续复核 / During the flight's wait, with checks near boarding |
| Requirements / 必要物品 | 已办理本次航班所需手续、航班号/日期/目的地、机场或运营航司的当前航班信息及可达候机区 / Required pre-boarding steps completed, flight number/date/destination, current airport or operating-airline flight information and a reachable waiting area |
| Side effects / 现实副作用 | 需要留意状态和时间，登机口未公布时暂不去猜测 / Attention is spent on status and time; an unannounced gate is not guessed |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你已进入普通航班的允许候机区，要知道**本次航班的登机口何时公布、现在是否登机**时，用这份 Skill把票面/手机信息与机场出发屏、航司实时状态对上，再在正确开放区域等待。目标是到可核验的登机口并看懂当前状态；口号尚未公布时保留可复查路径。值机、安检和实际登机是其他动作；登机牌上印的口号可能变化，不是永久指令。

### 准备与输入

记下实际运营航司、航班号、日期、出发机场/航站楼、显示目的地与登机牌/订单状态。找机场当日出发屏、航司官方 App/网站、可访问的广播或服务台。代码共享航班可能显示多个号码，用运营航司及时间/目的地交叉辨认。确认自己位于可合法等候的区域、能按需要看或听到更新；没有手机可用现场屏和工作人员，不把短信推送设成唯一信息来源。

### 执行

1. **在出发屏找到这班，而非只找目的地。** 对照航班号或实际运营方、日期/时间、目的地和状态。附近可能有同目的地的另一班，不能只跟着穿同航空公司衣服的人走。
2. **区分“未分配口”与“已分配口”。** 口号未公布就留在允许候机区，按机场/航司提示定期看屏、广播或官方状态。看到口号后查看它所在的航站楼/区域及当前状态；登机牌上的旧口号需以实时信息核对，不能独立证明还在原处。
3. **按可及的开放路线过去。** 在确保能留出到登机口的时间后，依机场当前导向/官方地图到对应区域。需要长距离、电梯或协助时及早问机场/航司，不为不确定时间冲进关闭通道或绕过控制区域。到口后再次对照口边显示的航班号、目的地和状态。
4. **在候机中持续读回。** 看口边屏、机场主屏、航司实时通知与工作人员广播；显示“延误”“登机中”“口号调整”“取消”是不同状态。变口时重新核对同一航班并改走开放路线；取消或登机疑问找航司正式人员，不以周围乘客开始排队作为唯一依据。
5. **在正确状态交给登机流程。** 当前口号与航班身份一致、工作人员已按本航班宣布办理时，准备按该航司指示进入登机流程。本文不教分组顺序、查票或机舱安全动作，也不保证仅因你站在口边就赶上了航班。

### 成功条件

你从当期机场/航司信息确认这班的登机口和状态，位于正确开放候机区域并能继续收到变化；或口号未公布时安全等待且知道从哪查。只看见同一目的地或登机牌上的旧口号不算确认。

### 常见报错与补救

- **登机牌印了口号，主屏却显示另一个：** 用航班号、日期与运营方核最新信息，必要时问工作人员，别坚持旧票面。
- **屏幕还没公布口号：** 继续在允许区候机并看官方状态，不闯到“通常使用”的区域。
- **同目的地多班：** 再核航班号、时间与承运方，不随另一班排队。
- **手机没网或通知不来：** 用机场屏、广播/文字显示和工作人员核对，别把推送缺席当航班未变化。
- **口边屏显示取消或不属于此班：** 停止排队，找航司正式服务渠道确认最新安排，不靠旧截图猜换乘资格。

### 假设、替代与现实副作用

本 Skill 只处理普通候机状态核对，不保证登机时间、票务、安检后转航站楼权限或延误赔偿。伦敦希思罗、盖特威克与 Delta 的官方页面说明实际信息会更新，具体机场/航司/日期必须查本班。听觉、视觉、移动不便时可使用文字屏、可及地图、广播或机场协助；不要求同时会用所有方式。等口号公布可能耗时，但跟错口会浪费更多。

### 来源

- [Heathrow：Departure lounge and boarding](https://www.heathrow.com/departures/departure-lounge-and-boarding)（英文，英国机场）— 登机口可在临近起飞才显示，应定期看当日出发屏并留到口时间；其具体分钟数不外推。
- [Gatwick：My Flight FAQs](https://www.gatwickairport.com/My_Flight)（英文，英国机场）— 登机口可能变化，候机厅航班信息屏显示本班口号和登机状态。
- [Delta：Fly Delta App](https://www.delta.com/us/en/delta-digital/mobile)（英文，美国航司）— 官方应用提供航班状态与登机口变化通知；没有 App 仍可用机场正式信息。
- Original synthesis — 以航班身份、口号公布状态、到口读回和持续复核组成一次候机任务，不把旧登机牌当实时来源。

## English

Use this Skill once you are in a permitted departure area for an ordinary flight and need to know **when its gate is announced and whether boarding has begun**. Match your ticket or phone details to live airport departures and operating-airline status, then wait in the correct open area. Finish at a verified gate with a current status, or retain a recheck route while no gate is assigned. Check-in, security, and boarding are separate actions. A printed boarding-pass gate can change.

### Preparation and inputs

Note operating airline, flight number, date, departure airport/terminal, displayed destination, and boarding-pass or booking state. Find today's airport departure displays, official airline app/site, accessible announcements, or a service desk. Codeshares can have multiple flight numbers, so cross-check operating carrier, time, and destination. Wait in an area open to you where updates can be seen or heard. Without a phone, use screens and staff; push notifications need not be your only source.

### Execution

1. **Find this flight, not just its destination.** Compare flight ID or operating carrier, date/time, destination, and status on current departures. Another flight may head to the same city; following someone in the same airline colours is not verification.
2. **Separate unassigned from assigned gate.** If no gate appears, stay in a permitted lounge and revisit screens, announcements, or official status at an interval the airport advises. When assigned, note terminal/zone and status. Compare any old gate printed on your pass against live information; it is not independent proof.
3. **Use an open accessible path to the gate.** Allow time for the actual distance and follow current airport signs or official maps. Ask airport/airline staff early about long routes, lifts, or help. Do not enter a closed or controlled area to save an estimated minute. At the gate, compare its display with your flight ID, destination, and status again.
4. **Keep reading during the wait.** Use gate and main displays, airline updates, and staff announcements. Delayed, boarding, gate changed, and cancelled are different states. For a new gate, verify the same flight and use an open route. For cancellation or unclear boarding, use airline staff; a crowd queue is not the only evidence.
5. **Hand over to boarding only at the right status.** When the current gate and flight match and staff announce this flight's procedure, prepare to follow the operating airline's boarding instructions. This file does not set group order, check documents, or teach cabin safety, and merely standing nearby cannot guarantee boarding.

### Success

Current airport/airline information identifies this flight's gate and status, and you are in the correct open waiting area with a way to notice change. A not-yet-announced gate with safe waiting and a known official recheck source is also valid. A matching destination or old printed gate alone is insufficient.

### Common errors and recovery

- **Pass says one gate, current display another:** Match flight/date/operator in live information and ask staff if needed; do not insist on the printed number.
- **No gate announced yet:** Stay in a permitted area and watch official status rather than entering a “usual” gate area.
- **Several flights share a destination:** Recheck flight number, time, and operator before joining a queue.
- **Phone has no connection or alert:** Use airport displays, visible/audible announcements, and staff rather than assuming silence means no change.
- **Gate display shows cancelled or another flight:** Stop queueing and seek current airline arrangements, not a guess from an old screenshot.

### Assumptions, alternatives, and side effects

This is ordinary gate/status monitoring, not a guaranteed boarding time, fare ruling, controlled-terminal access, or delay compensation guide. Heathrow, Gatwick, and Delta pages illustrate changing information; your own flight/date/operator controls. Use text displays, accessible maps, announcements, or staff for hearing, sight, or mobility needs. Waiting for a gate may take time, but waiting at the wrong one costs more.

### Sources

- [Heathrow: Departure lounge and boarding](https://www.heathrow.com/departures/departure-lounge-and-boarding) — gates may appear near departure, so check current screens and allow travel time; its exact minutes do not transfer.
- [Gatwick: My Flight FAQs](https://www.gatwickairport.com/My_Flight) — gates may change; departure displays show gate and boarding state.
- [Delta: Fly Delta App](https://www.delta.com/us/en/delta-digital/mobile) — official app status and gate-change notices are available, while on-site official information remains useful without an app.
- Original synthesis — flight identity, gate-announcement state, gate-side readback, and continued monitoring form one waiting task.

If AI opens this file, it may read a flight display. You verify, wait, move, or ask staff.
