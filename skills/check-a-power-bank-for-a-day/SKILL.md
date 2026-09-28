---
name: check-a-power-bank-for-a-day
description: "Human-readable instructions for checking a power bank's stored energy, usable output, and port capability against ordinary devices for a day away from an outlet."
---
# 买前核对移动电源够不够用 / Check a Power Bank for a Day Away

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 计划充电的普通设备与次数、设备输入要求、候选移动电源 Wh/输出口规格 / Ordinary devices and desired top-ups, device input requirements, candidate Wh/output-port details |
| Side effects / 现实副作用 | mAh 与 W 被迫承认不是同一种量 / mAh and W must admit they measure different things |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你要买一台普通 USB 移动电源，支持一天内手机、平板等设备离开插座时使用，加载这份 Skill。结果是“输出接口有依据、储能有现实余量的候选”或“资料不足/不适合”。它不保证精确充满次数，不供医疗设备、应急生命支持或改装电源使用，也不判断航空携带规则。

### 准备与输入

写下要充的准确设备和大概需要几次补电，而不是只说“越大越好”。找设备说明书中的充电输入接口和必要供电协议/功率；找候选移动电源标出的 Wh（瓦时），若只有 mAh 还需电芯标称电压才能换算为 Wh。另找它的**实际输出口**规格、一次使用多个口时的限制，以及制造商是否提供额定可输出容量。预计使用的线缆能力需另行核对。

### 执行

1. **把任务写成补电需求。** 例如“一部手机在外一整天需一次完整补电，另给耳机补一次”。尽可能从准确设备资料取得电池 Wh；拿不到时只记录具体使用次数，不发明通用手机容量。
2. **分开能量与功率。** Wh 表示储存能量，W 表示某个输出口在规定条件下能供给的功率。印在盒上的 mAh 若未注明电压，不能直接与另一台设备的 mAh 比；制造商有 Wh 或额定输出容量时优先使用。
3. **先核能否充，再核够不够。** 对照移动电源某一输出口、设备输入要求和线缆，确认接口、协议与所需功率有明确资料。一个很大的电池若没有设备需要的输出条件，仍不是合格候选。
4. **估计可用补电次数。** 若能取得设备 Wh 与移动电源 Wh，可把期望补电的总能量与候选比较；输出转换和设备充电都有损失，标称储能不能一比一交给设备。没有制造商可用输出或可靠试验资料时，只给“纸面下限不够/可能有余量但次数未确认”，不报整数承诺。
5. **检查实际携带与同时使用。** 是否可接受重量和体积、各输出口是否会共享总功率，都按候选说明核对。携带方式的详细安排归另一个采购任务；航空规则不在本 Skill 内。

### 成功与停止

完成时，你能指出准确设备、一个有资料支持的输出路径、储能单位与补电目标，以及估算仍不确定的损失。若标称 Wh 已低于你需要交给设备的能量，可直接排除；若只有 mAh、输出规则或设备要求不明，就暂停肯定结论。电池鼓胀、破损、发热异常或非标准供电设备应停止普通选购，寻求制造商支持。

### 常见报错与补救

- **20,000 mAh 直接除以手机 5,000 mAh 得“四次”：** 两者的电压与输出损失可能不同，先看 Wh 和额定输出；不要把商当验收结果。
- **只看最大 W，不看是哪一个口：** 查计划插的准确输出口和多口同时使用限制。
- **储能足够但电脑不充：** 回到电脑准确输入协议/功率与电源输出的相容性；不要靠更大 mAh 猜解决。
- **小字或技术表难读：** 放大制造商规格、请可信的人读回单位与端口；缺 Wh 或电压时向厂商问清，而不是随手假设电芯电压。

### 假设、替代与现实副作用

本流程只处理普通消费设备的一天补电，不把特定品牌的转换效率当通用百分比。温度、负载、线缆和电池老化都可能改变实际输出，因此购前只能形成有限估计。你不需把设备使用记录上传到陌生计算器；纸笔足够。如果旅行涉及航空或其他场所限制，另查当地现行规定。

### 来源

- [Anker 支持：移动电源标称与额定容量](https://service.anker.com/uk/article-description/Why-is-the-Rated-Capacity-of-Power-Banks-Lower-Than-Expected) — mAh 需连同电压看，Wh 表示储能，输出转换和设备充电存在损失；页面百分比只是品牌示例，不用于保证次数。
- [Dell：USB-C 能力说明](https://www.dell.com/support/kbdoc/en-us/000141238/guide-to-usb-type-c) — 准确设备的充电输入、协议与端口能力须按其说明书核对，外形相同不保证供电功能。

## English

Load this Skill before buying an ordinary USB power bank for a day when a phone, tablet, or similar device will be away from an outlet. The result is a candidate with a documented output path and plausible energy margin, or a clear unknown or mismatch. It does not promise an exact number of full charges, power a medical or life-support device, modify a battery, or decide airline rules.

### Preparation and inputs

List the exact devices and approximate top-ups needed rather than saying “as big as possible.” Find each device's charging port and required protocol/power in its manual. Find the candidate bank's Wh (watt-hours); mAh alone needs the cell's nominal voltage to convert to Wh. Also find the **particular output port's** capabilities, shared-output limits when several ports run, and any maker-rated usable output capacity. Check the planned cable separately.

### Execution

1. **Name the top-up job.** For example, one full phone recharge during a day out plus one earbud top-up. Use the exact device's battery Wh when available. If it is not available, record the task without inventing a universal phone size.
2. **Separate energy from power.** Wh describes stored energy; W describes power available at a stated output port. A box's mAh without voltage cannot be directly divided by another device's mAh. Prefer the maker's Wh or rated usable output where provided.
3. **Confirm it can charge before asking how often.** Match one bank output, the device's input requirement, and the cable for connector, protocol, and necessary power. A large battery lacking the required output is still an unsuitable candidate.
4. **Estimate usable top-ups cautiously.** Where both devices and bank have Wh values, compare desired total device energy with the bank. Output conversion and device charging lose energy, so nominal stored Wh cannot all reach the device. Without a maker-rated usable output or reliable test, report only “below the paper minimum” or “possible margin; number of charges unconfirmed,” not an integer promise.
5. **Check practical carrying and simultaneous use.** Confirm whether weight and bulk suit you and whether multiple ports share a total power limit. Detailed carrying plans belong to a separate shopping task; airline rules are outside this Skill.

### Success and stop conditions

You finish with exact devices, one documented output route, energy units, the top-up goal, and the uncertainty from losses. If rated Wh is already below the energy you need delivered to devices, reject it. If Wh, output rules, or device requirements are missing, pause a positive conclusion. Stop ordinary shopping for a swollen, damaged, or abnormally hot battery or non-standard power device and use maker support.

### Common errors and recovery

- **20,000 mAh was divided by a 5,000 mAh phone and called “four charges”:** Voltage and conversion loss can differ. Check Wh and rated output before estimating; the quotient is not acceptance.
- **Only the largest W number was read:** Find the exact output port and simultaneous-use limit you intend to use.
- **Stored energy looks enough but a laptop cannot charge:** Check that laptop's exact input protocol/power against the bank output instead of adding more mAh by guesswork.
- **Small technical print is inaccessible:** Enlarge the maker's specifications or ask a trusted person to read back units and ports. Ask the maker for missing Wh or voltage rather than assuming a cell value.

### Assumptions, alternatives, and side effects

This covers ordinary consumer devices for a day away, not a universal conversion-efficiency percentage from one brand. Temperature, load, cable, and battery age can alter delivered energy; a purchase check is a limited estimate. You need not upload a usage history to an unfamiliar calculator; paper notes are enough. For air travel or other venue limits, check current local rules separately.

### Sources

- [Anker Support: Nominal and rated power-bank capacity](https://service.anker.com/uk/article-description/Why-is-the-Rated-Capacity-of-Power-Banks-Lower-Than-Expected) — mAh needs voltage, Wh expresses stored energy, and conversion/charging losses occur; its percentages are brand examples, not guaranteed charge counts.
- [Dell: USB-C capability guide](https://www.dell.com/support/kbdoc/en-us/000141238/guide-to-usb-type-c) — read the exact device's charging input, protocol, and port capabilities; matching connector shape does not prove power support.
