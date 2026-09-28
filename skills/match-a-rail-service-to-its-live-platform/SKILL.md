---
name: match-a-rail-service-to-its-live-platform
description: "Human steps to match a rail ticket or journey plan to the current station departure, calling points and platform, while treating an unannounced or changed platform as unconfirmed."
---
# 把铁路车次对上现场站台 / Match a Rail Service to Its Live Platform

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–10 分钟，站台未公布时需等待复核 / 5–10 minutes, with a recheck if the platform is unannounced |
| Requirements / 必要物品 | 乘车票/预订或计划中的日期、出发站、车次/时间与目的站；运营方/站方当前出发信息 / Ticket, booking, or plan with date, departure station, service/time and intended calling point; current operator or station departures |
| Side effects / 现实副作用 | 一条已核对或明确待确认的车次—站台记录，旧截图不再担任站长 / A verified or explicitly pending train-to-platform record; an old screenshot no longer runs the station |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你准备乘普通铁路，票、预订或行程计划给出了车次/时间，但要确定**今天从本站出发的实际列车及其站台**时，用这份 Skill 将个人行程与站方当前出发屏、运营方实时信息和停靠站逐项对上。完成是能指出可核验的车次与当前站台，或明确“站台尚未公布/信息冲突，需要等公告或问工作人员”。走到站台、检票与候车属后续步骤；已经确认站台后突然改道/改车厢位置属于变化处理，不靠旧记录继续走。

### 准备与输入

从自己可信的票/预订或官方行程中读出日期、出发站全名、计划出发时间、运营公司/列车类别与编号（若有）、目的地或你要下车的中间站及车厢/座位信息（若有）。跨午夜、同名相邻车站、同一终点连续多班是常见误配来源。站台可能直到临近发车才公布，也可能调整；票上旧站台、纸质时刻表和截图不能自动代替现场信息。无手机可看站内出发屏、听广播或问站方人员；视听或行动支持需按当前站方服务安排，不靠跟随人流猜。

### 执行

1. **先锁定正确日期和车站。** 将票/计划上的出发站、日期和时区/跨日情况与自己所在车站核对；同城不同站或同站不同入口名称不要省略。若发现自己到错站，先停下来查运营方允许的后续选项，不把“车次号一样”当作可从此站上车的证据。
2. **在当前出发信息中找这一班。** 用站内实时出发屏或运营方官方实时列表，按出发时间、运营方/列车编号、终点与状态交叉核对。目的地可能是中途停靠站而不显示在大屏终点栏；展开停靠站清单确认该班确实停你要到的站。只凭终点名或站台号匹配，可能是隔壁另一班。
3. **读出状态与站台。** 区分准点、延误、取消、尚未给站台及已指定站台。只有多个标识指向同一实际班次、站方当前给出站台时，才把站台写到计划中。没有站台就留在允许等待的公共区域，定时查看官方屏幕/广播或问人员；不自行闯向“通常是那一站台”。
4. **临行前再次核对。** 在按站方指示前往站台之前，重看该班的实时状态、站台与站内公告。若站台与先前截图冲突，以最新可核验站方信息或工作人员说明为准；仍冲突就请其核实，别跟着大队人流去未确认的门。需要重新寻找站台、车厢或入口时，按站方安全引导处理，不穿越轨道或封闭通道。
5. **留下可读回的五项。** 记录“出发站/日期—计划车次或时间—运营方与显示终点—你的目标停靠站—当前状态/站台与信息时间”。它是进入后续进站、检票、候车流程的输入，不等于票务资格已被验证或列车已到达。

### 成功条件

你的票/行程与**本站、今天、这一班次**的当前站方信息及目标停靠站匹配，站台已由当前来源确认；或者站台未公布/资料冲突被明确标为待确认并保留官方核对路径。错误车站、错误日期、仅相同终点或仅相同站台都不是完成。

### 常见报错与补救

- **大屏只写终点，不写你要下的中途站：** 打开该班停靠清单或问站方；不能从线路名称猜必停。
- **同一时间有两班去相同方向：** 再对车次号、运营方、停靠站与状态，不拿站台号替代车次身份。
- **票上有站台，屏幕写待定或另一个：** 先以站方当前可核验信息查变更；未确认前不奔向旧站台。
- **广播与应用矛盾：** 在安全公共区域找站方人员或实时出发屏交叉核对，并记下信息更新时间。
- **屏幕显示取消或本车不经目的站：** 停止原计划，按运营方当期改乘/票务指引询问；本 Skill 不断言自动可乘下一班。

### 假设、替代与现实副作用

这里只做普通铁路行前的车次、停靠与站台识别，不处理票价、权益、紧急事故、穿越站场、复杂跨境手续或实际检票上车。英国 National Rail、德国 DB、荷兰 NS 的页面展示不同系统的核对字段，不能充当你所在地的实时公告。无智能手机仍可用站内屏、广播、人工服务；无法可靠看/听时应要求站方可及信息。未公布站台时等待本身是正确的状态，别用旧截图替现场指挥。

### 来源

- [National Rail：Live Departures](https://www.nationalrail.co.uk/live-trains/) 与 [Changing Trains](https://www.nationalrail.co.uk/travel-information/changing-trains/)（英文，英国铁路信息方）— 实时屏展示服务状态、站台与停靠点，现场有广播/工作人员可核对；静态计划不能保证连接。
- [Deutsche Bahn：Station help](https://int.bahn.de/en/faq/what-help-available-at-station) 与 [International booking platform FAQ](https://int.bahn.de/en/faq/departure-platform-international-bookings)（英文，德国运营方）— 站内屏/广播可提供当前站台；某些站台临近发车才公布。
- [NS：Platform Guide app](https://www.ns.nl/en/travel/traveling-with-a-disability/ns-platform-guide-app)（英文，荷兰运营方）— 可核对站台、列车类别、目的地、中途站及“不要上车”等现场信息，也提供可及阅读方式。
- Original synthesis — 将个人行程和站方动态信息按车站/日期、班次、停靠、状态、站台五项交叉核对。

## English

Use this Skill before an ordinary rail trip when a ticket, booking, or plan names a service or time but you need to confirm **today's actual train from this station and its platform**. Match your own journey with current station departures, operator updates, and calling points. The result is a verified service and live platform, or an explicit “platform not announced / information conflicts” with an official way to recheck. Walking to the platform, ticket gates, and waiting are later steps. An announced platform or coach change is handled from fresh information, not an old note.

### Preparation and inputs

From your trusted ticket, booking, or official journey, note date, full departure-station name, planned time, operator/train category and number when given, final destination or your intermediate exit station, and coach/seat if assigned. Overnight date changes, similarly named stations, and several trains toward one terminus can cause false matches. A platform may be announced late or change; one printed on an older ticket, timetable, or screenshot is not automatically current. Without a phone, use departure boards, announcements, or station staff. Arrange actual visual, hearing, or mobility assistance through the station rather than following a crowd.

### Execution

1. **Lock the date and station first.** Compare the ticket's origin, date, and overnight/time-zone detail with the station where you stand. Do not collapse different stations in one city or similar entrance names. If you are at the wrong station, stop and ask the operator about real alternatives; the same train number is no proof it boards here.
2. **Find the run on current departures.** On a live station board or official operator list, cross-check departure time, operator or train ID, displayed terminus, and status. Your destination may be an intermediate calling point absent from the big terminus column; open the stop list to confirm this run actually calls there. A terminus or platform alone can match the wrong train next to yours.
3. **Read status and platform separately.** Distinguish on time, delayed, cancelled, platform not yet announced, and platform assigned. Write down a platform only after several identifiers match this service and current station information assigns it. With no platform, wait in an allowed public area and check the official board/announcements or staff again; do not head for the platform the train “usually uses.”
4. **Recheck before moving.** Before following station directions to a platform, revisit live status, platform, and notices for this run. If a screenshot disagrees with the latest verifiable board or staff, check the change; if sources still conflict, ask staff rather than following a crowd toward an unconfirmed gate. Follow safe station directions to a revised platform or coach; do not cross tracks or closed areas.
5. **Keep a five-part readback.** Record “origin/date — train or planned time — operator/displayed terminus — your calling point — current status/platform and information time.” It feeds later gate and waiting decisions; it does not itself validate your ticket or prove the train has arrived.

### Success

Your ticket or plan matches the **station, date, actual service**, current operator/station information, and your calling point, with a platform confirmed by a current source. An unannounced or conflicting platform is explicitly pending with an official recheck route. Wrong station, wrong day, matching terminus alone, or matching platform alone is incomplete.

### Common errors and recovery

- **Board shows only the terminus, not your intermediate exit:** Open this run's calling-point list or ask station staff. Do not infer a stop from the line name.
- **Two trains head the same way near the same time:** Compare train ID, operator, calling points, and status; a platform number is not service identity.
- **Ticket prints a platform but the board is pending or different:** Check the current station change before moving. Do not run to an old platform without confirmation.
- **Announcement conflicts with an app:** Cross-check live boards or staff in a safe public area and note when each source updated.
- **Cancelled or not serving your stop:** Stop the old plan and ask about the operator's current travel/ticket options; this Skill does not assume automatic validity on another service.

### Assumptions, alternatives, and side effects

This is identification of an ordinary rail service, calls, and platform before entry. It does not decide fare rights, emergency response, track crossing, cross-border documents, or actual ticket-gate/boarding procedure. National Rail, DB, and NS pages illustrate fields to verify, not live information for your own station. Boards, announcements, and staff can replace a smartphone. Ask for accessible information if you cannot reliably read or hear. Waiting for an unannounced platform is a correct state; an old screenshot does not run the station.

### Sources

- [National Rail: Live Departures](https://www.nationalrail.co.uk/live-trains/) and [Changing Trains](https://www.nationalrail.co.uk/travel-information/changing-trains/) — live boards show service status, platform, and calling points, with announcements/staff for cross-checking; a static plan does not guarantee a connection.
- [Deutsche Bahn: Station Help](https://int.bahn.de/en/faq/what-help-available-at-station) and [Platform on International Bookings](https://int.bahn.de/en/faq/departure-platform-international-bookings) — station boards and announcements supply current platform; some platforms appear close to departure.
- [NS: Platform Guide](https://www.ns.nl/en/travel/traveling-with-a-disability/ns-platform-guide-app) — platform, train category, terminus, intermediate stops, and do-not-board notices can be checked in an accessible format.
- Original synthesis — cross-check personal travel and live station data across origin/date, service, calling point, status, and platform.

If AI opens this file, it may explain a live board entry. You match, wait, recheck, or stop before the wrong train.
