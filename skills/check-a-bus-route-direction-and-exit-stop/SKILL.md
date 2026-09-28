---
name: check-a-bus-route-direction-and-exit-stop
description: "Human steps to compare an operator's current bus stop sequence and direction, choose the correct boarding-side stop and exit stop, and recheck route variants before riding."
---
# 核对公交线路方向和下车站 / Check a Bus Route, Direction, and Exit Stop

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 5–10 分钟 + 临行复核 / 5–10 minutes plus a departure check |
| Requirements / 必要物品 | 起点、目的地与出行时间，当前公交运营方的线路/站序/服务公告，能识别的上车站及下车站 / Origin, destination and travel time, current operator route/stop sequence and alerts, identifiable boarding and exit stops |
| Side effects / 现实副作用 | 一条含方向、上车站和下车站的可核对计划；路线变化时需要重选 / A checkable plan with direction, boarding stop, and exit stop; changes may require replanning |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你知道要去哪里，但同一公交线在道路两侧、环线或不同支线上的方向不易判断时，用这份 Skill 查**运营方当前的站序和行驶方向**，留下上车站、方向标识及下车站的三项确认。目标是知道“从哪个站上、坐哪个方向、在哪站下”，而不是凭车号猜；真正排队、支付与上车归 H142，下车换乘归 H143，步行找路归 D17。

### 准备与输入

确定出发地、目的地、出行日期和大致时间，最好知道目的地附近希望到达的街口或官方站名。使用当地运营方官网、官方行程规划器、当前站牌/线路图或可信客服，查这段时间的线路、两个方向的站序与服务公告。只看“路线号相同”不够；一些线路有支线、短程终点、环线和临时改道。没有手机时用站牌、纸质时刻表或运营方电话；视觉或阅读不便可用可及版本/客服或可信协助，不凭颜色猜方向。

### 执行

1. **从目的地倒推一个下车站。** 在运营方当前线路图/行程规划器上找到目的地对应的实际站名或站点编号；若有多个相近站，选能够确认后续路程的一站，不把地图上的街道位置当成车辆必停站。记下下车站的前一站，作为途中提醒。
2. **把上车站放进同一站序。** 查运营方建议的上车站、站点编号或站牌方向；确认那一站在计划车辆的行进站序中位于下车站之前。街对面的同号线路可能往相反方向。只知道“这条线经过两站”，还没证明从这个站能按顺序到达目的地。
3. **核对方向和变体。** 记下线路号、运营方给出的方向/终点显示、支线或短程标记，并确认这班次确实经过下车站。环线或两边终点名称相似时，以实际站序而非“看起来朝东/朝市中心”判断；若信息冲突，先用运营方的实时状态、站牌或客服澄清，不靠同号车碰碰运气。
4. **临行前查一次变化。** 官方实时信息与服务公告可能显示停靠站关闭、绕行、班次终点变化或时刻表不含的临时变更。按出发时的信息更新上车站和下车站；旧截图只记录旧计划。线路或时刻不确定到无法确认站序时，暂停这条计划，改查另一条可核验路线。
5. **留下三行可用记录。** 写/存“上车站（编号/方向）—线路与显示方向/变体—下车站（及前一站）”，必要时附运营方状态入口。到站后再由 H142 按现场车辆标识执行上车核对；本文不替你支付或保证车辆一定按预报时间到。

### 成功条件

你能从当前运营方资料指出具体上车侧的站、对应线路及方向/变体、它在站序中先于下车站，以及临行需要复核的变化；或者发现无法确认并停下重选。单有线路号或一张没有日期的地图不足以确认方向。

### 常见报错与补救

- **车号对了但站牌在路对面：** 比较两个站点编号或站序，选择会先经过上车站再到下车站的一侧；过街路线安全本身另按当地规则处理。
- **看到同一个终点名却有支线/短程车：** 逐班核对实际经过站与显示终点，不能只看线路颜色或号数。
- **目的地在环线中：** 用站序计算从这个上车站到目标站的实际方向，不假设环线有普通往返的两个终点。
- **地图与现场公告冲突：** 先看运营方最新状态并询问官方人员/客服；不凭旧截图强行上车。
- **下车站名相似：** 记下站点编号、前一站或相邻路口作交叉核对，避免在同名附近站提前或过晚下车。

### 假设、替代与现实副作用

这是普通城市公交的行前线路判断，不提供实时路线推荐、票价/支付、无障碍设备保证、穿越道路或紧急交通指导。线路与站序由当地运营方当期资料决定；伦敦与新南威尔士的官方工具只是如何核对的实例。无智能手机可用站牌、纸图或客服；行动、视听限制需要的实际车辆与站点可及性由 H150 专门确认。计划可能因绕行失效，临行复核是任务一部分。

### 来源

- [Transport for NSW：Help using routes, stops and timetables](https://transportnsw.info/plan/instructions-planning-guides/help-using-routes-timetables)（英文，澳大利亚运营方）— 线路图含方向与变体，时刻表可能不含短期变化；行程规划器可查站序、实时信息与公告。
- [Transport for NSW：How to use the Trip Planner](https://transportnsw.info/plan/instructions-planning-guides/how-to-use-trip-planner)（英文，运营方）— 起终点、站点出发信息和实时服务是不同核对输入。
- [Transport for London：Using buses in London](https://tfl.gov.uk/modes/buses/using-buses-in-london?intcmp=53125) 与 [TfL Buses](https://tfl.gov.uk/modes/buses/)（英文，英国运营方）— 当地站牌显示站名、服务线路和驶往方向；运营方提供计划、实时到站及变化入口。
- Original synthesis — 将下车站、上车侧站序、线路方向/变体和临行复核写成三行可验证计划，不把某城市的线路号外推。

## English

Use this Skill when you know your destination but the direction of a bus route is unclear across opposite-side stops, loops, or branches. Check the **current operator stop sequence and direction** and leave with three confirmed pieces: boarding stop, route/direction, and exit stop. A route number alone is a guess. Queueing, fare, and boarding belong to H142; alighting and transfer belong to H143; street navigation belongs to D17.

### Preparation and inputs

Identify origin, destination, travel date, and approximate time, preferably with a desired nearby street corner or official stop name. Use the local operator's site, trip planner, current stop sign/map, or trusted support to inspect the routes, both direction sequences, and alerts for that time. Same route number may include branches, short workings, loops, or diversions. Without a phone, use stop signs, printed timetables, or the operator's call channel. Use accessible formats, support, or trusted help for reading or vision needs; colour alone does not identify direction.

### Execution

1. **Work backward from an exit stop.** Find the actual stop name or ID serving the destination on the current operator route map or planner. If several stops are nearby, choose one whose onward route you can confirm. A street point on a map is not proof a bus stops there. Note the preceding stop as an on-board reminder.
2. **Put boarding and exit in one sequence.** Find the suggested boarding stop, stop ID, or signed direction. Confirm that it appears **before** the exit stop in the intended service's stop order. The same route across the street may run the other way. Knowing a route serves both stops does not prove it connects them in that order from your side.
3. **Check direction and variant.** Record route number, displayed direction or terminus, branch or short-working marker, and whether that actual service serves the exit stop. On loops or where terminal names look similar, use stop order instead of “towards downtown” or compass guesswork. If sources conflict, ask the operator's live status, sign, or support before riding.
4. **Recheck near departure.** Live status and alerts may report a closed stop, diversion, changed terminus, or short-term change omitted from a static timetable. Update boarding and exit under the departure-time information; an old screenshot preserves only an old plan. If you cannot verify the sequence, pause this route and choose one you can confirm.
5. **Keep a three-line card.** Write or save “boarding stop (ID/direction) — route and displayed direction/variant — exit stop (and preceding stop),” plus the operator status route when useful. H142 handles the actual vehicle-side boarding check. This file neither pays a fare nor guarantees a predicted arrival.

### Success

Using current operator information, you can name the specific boarding-side stop, route and direction/variant, show that boarding precedes exit in its stop sequence, and know what to recheck before departure. Discovering uncertainty and replanning is also valid. A route number or undated map alone is insufficient.

### Common errors and recovery

- **Right route number, stop across the road:** Compare stop IDs or sequences; choose the side that precedes the exit stop. Safe street crossing follows local guidance separately.
- **Same terminus label but branch or short route:** Check this run's served stops and displayed destination; do not rely on route colour or number alone.
- **Destination on a loop:** Use actual sequence from your boarding stop, not an assumed pair of opposite termini.
- **Map conflicts with a site notice:** Check the operator's latest status or ask official staff/support instead of following a stale screenshot.
- **Similar exit stop names:** Keep the ID, preceding stop, or nearby intersection as a cross-check.

### Assumptions, alternatives, and side effects

This is pre-trip route-direction checking for ordinary city buses. It gives no live route recommendation, fare/payment rule, accessibility guarantee, road-crossing instruction, or emergency traffic advice. Current local operator information controls the route. London and NSW tools illustrate verification, not a route for your city. Stop signs, printed maps, or support can replace a smartphone. H150 addresses actual accessibility of vehicles and stops. A diversion can invalidate the card, so rechecking is part of completion.

### Sources

- [Transport for NSW: Routes, Stops and Timetables](https://transportnsw.info/plan/instructions-planning-guides/help-using-routes-timetables) — maps include directions and variants, while static timetables can miss short-term changes; the planner can show sequence, live information, and alerts.
- [Transport for NSW: Trip Planner Guide](https://transportnsw.info/plan/instructions-planning-guides/how-to-use-trip-planner) — origins/destinations, stop departures, and live service are separate planning inputs.
- [Transport for London: Using Buses](https://tfl.gov.uk/modes/buses/using-buses-in-london?intcmp=53125) and [TfL Buses](https://tfl.gov.uk/modes/buses/) — local signs display stop, routes, and destination direction, with operator planning and live updates.
- Original synthesis — combine exit, boarding-side sequence, route variant, and departure recheck into a three-part plan without exporting one city's route numbers.

If AI opens this file, it may explain an operator's stop list. You verify, record, recheck, or change the bus plan.
