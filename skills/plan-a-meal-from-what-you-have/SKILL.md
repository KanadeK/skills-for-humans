---
name: plan-a-meal-from-what-you-have
description: "Human-readable instructions for turning available ingredients, time, equipment, and attention into one realistic home meal."
---
# 用现有食材安排一顿饭 / Plan a Meal from What You Have

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Stable / 稳定 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 10 分钟规划，加实际烹饪 / 10 minutes planning, plus cooking |
| Requirements / 必要物品 | 可用食材、时间、厨具、人数和注意力 / Available food, time, equipment, people, attention |
| Side effects / 现实副作用 | 冰箱里的随机对象被编译成一顿饭 / Random refrigerator objects compile into one meal |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当你打开冰箱看见几种互相没有开会的食材，却需要在现实时间内开饭时，加载这份 Skill。目标是一顿能完成的饭，不是把每个食材都安排成独立项目。

### 准备与输入

先确认：

- 几个人吃、何时开饭、是否希望留剩菜；
- 已有食材、数量、开封/储存状态和应优先使用的东西；
- 若要用冷冻食材，确认它能否按该食品说明和当地安全指导及时解冻，或是否明确允许直接从冷冻状态烹调；
- 灶眼、锅具、烤箱、电饭锅等真实可用设备；
- 你的烹饪熟练度，以及此刻能同时照看的任务数；
- 普通忌口和你已经明确执行的过敏避让规则。

日期、冷链或状态不确定的食材先隔离，不为了“清库存”强行纳入。医疗饮食和严重过敏方案不在这里临时设计。

如果切配、站立、握锅、看计时器或听提示音不方便，优先选少切配、坐着能完成、单锅、视觉/震动计时或能获得现场协助的路线。减少菜数是有效优化。

### 执行

1. **选一个主线。** 从“一锅/一盘主菜 + 主食 + 一个简单配菜”开始，甚至只做一锅完整食物。菜数不是版本号，不必只增不减。
2. **优先使用安全且易坏的食材。** 已开封、接近品质期限或计划优先吃掉的食材先分配，但任何安全史不明的东西不参与。
3. **把食材按功能分组。** 主食/淀粉、蛋白质、蔬菜、脂肪、酸、咸鲜、香味和口感。缺一项时可以省略或按功能替代，不因为名字相似就互换。
4. **核对设备和注意力。** 一个新手只有一口锅时，不同时安排油炸、收汁和三分钟必须翻面的菜。先使用能自己稳定运行的步骤，再安排需要盯住的火候。
5. **从开饭时间倒排。**
   - 只把能按适用安全方法赶上开饭时间的解冻、浸泡或长时间烹饪排进菜单；不能靠室温台面加速解冻；
   - 再完成可共用的清洗与切配；
   - 生肉、禽、海鲜的工具和区域与即食食物分开；
   - 高温、刀具、热油和最后调味放在你能持续看守的时间；
   - 留出熟度检查、静置、装盘和剩菜分装时间。
6. **写一条临界路径。** 只标出会拖延整顿饭的三到五步，并注明哪些能并行、哪些必须先后。把“顺便再做一个”视为变更请求。
7. **在开始前确认停止条件。** 食材状态可疑、过敏信息不清、时间不足或设备异常时，删菜、换简单路线或停止；不要让沉没成本进入锅里。
8. **开做时一次看一步。** 每步写清大致数量、时间和可观察完成信号。尝味只适用于安全可尝的阶段，生肉和未熟蛋白不用于进度测试。
9. **开饭前安排剩菜。** 准备干净浅容器，按当地食品安全指导及时冷却、标记和储存；不要等所有人吃完很久后才创建该任务。

### 成功条件

你有一顿范围清楚的饭、可解释的份量、只含真正缺少的采购项、一条现实时间线、每道食物的熟度检查和剩菜去向。开饭可能没有同时准点，但所有菜都不应因为追求同步而失去安全。

### 常见报错与补救

- **ERR_TOO_MANY_DISHES：** 立刻删除装饰菜和重复配菜，保留能组成一顿饭的最小集合。
- **开始晚了：** 换更快切法、减少菜数、使用安全的现成主食，或诚实延后开饭时间；不要用更大火力补偿所有延迟。
- **某个食材不能用：** 按它承担的功能替代，或修改菜式；不要让一个缺料阻塞整顿饭。
- **冷冻食材来不及安全解冻：** 改用确实可用的食材、按包装允许直接从冷冻状态烹调的方案，或改菜单和开饭时间；不要把它放在室温等到“差不多”。
- **两件高注意力任务冲突：** 一件降级为低维护做法，或顺序执行。Human Runtime 默认没有隐藏线程池。
- **锅中冒烟、热油失控、出现明火、燃气异味或设备故障：** 停止烹饪并按当地消防/紧急指导离开危险、求助。只在安全时关闭热源；不要自行维修燃气或电器。

### 假设、替代与现实副作用

份量、主食、调味和“一顿饭应该有什么”都受地区、家庭和预算影响。用你家的正常饭量和习惯替换示例。没有烤箱、刀具、充足站立能力或多人协作时，优先一锅、预切、冷食搭配或其他可访问路线。

现实副作用包括待清洗的厨具、可能剩下一份午饭，以及你发现原来不需要为了用掉半颗菜再买八种配料。

### 来源

- [香港食物安全中心：减少厨余](https://www.cfs.gov.hk/tc_chi/consumer_zone/other_foodsafety/reduce_foodwaste.html) — 支持先计划、检查库存、按需要准备和安排剩菜。
- [香港食物安全中心：烹煮食物的食物安全五要点](https://www.cfs.gov.hk/tc_chi/consumer_zone/safefood_all/five_keys_apply_cook.html) — 支持彻底烹煮、生熟分开和食用前检查。
- [美国消防局：烹饪防火](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/) — 支持烹饪时看守和火灾停止边界。
- [香港食物安全中心：正确解冻冷藏食品](https://www.cfs.gov.hk/sc_chi/consumer_zone/safefood_all/five_keys_defrosting.html) — 解冻前须预留时间，不应在室温下解冻；具体方法与后续使用按食品和当地指引。

## English

Load this Skill when the refrigerator contains several ingredients that have not met each other, but dinner must exist on a real clock. The goal is one finishable meal, not a separate project for every object.

### Preparation and inputs

Confirm:

- how many people, serving time, and whether you want leftovers;
- available ingredients, amounts, opened/storage state, and use-first items;
- for any frozen ingredient, whether its own directions and local safety guidance allow timely safe thawing or explicitly permit cooking from frozen;
- burners, pans, oven, rice cooker, and other equipment that actually works;
- your cooking confidence and how many tasks you can safely watch at once;
- ordinary dislikes and allergy-avoidance rules you already know.

Hold food with an uncertain date, cold chain, or condition outside the plan. Do not invent a medical diet or severe-allergy protocol while cooking.

If cutting, standing, gripping pans, seeing timers, or hearing alarms is difficult, prefer low-prep, seated, one-pot, visual/vibrating timer, or in-person-assisted routes. Fewer dishes is a valid optimization.

### Execution

1. **Choose one meal spine.** Start with one-pot food or one main, one staple, and one simple side. Dish count is not a version number and may decrease.
2. **Use safe perishables first.** Assign opened and use-first ingredients before durable stock, but exclude anything with an uncertain safety history.
3. **Group ingredients by function.** Identify starch, protein, vegetables, fat, acid, salt/umami, aroma, and texture. A missing function can be omitted or replaced by function; similar names do not prove interchangeability.
4. **Check equipment and attention.** A beginner with one pan should not schedule frying, reducing sauce, and three-minute turning at once. Start stable unattended work before high-attention heat.
5. **Work backward from serving.**
   - Include thawing, soaking, and long cooking only when an applicable safe method fits the serving time; a room-temperature counter is not a shortcut for thawing.
   - Share washing and cutting only where cross-contamination stays controlled.
   - Keep raw meat, poultry, and seafood tools away from ready-to-eat food.
   - Schedule knives, high heat, hot oil, and final seasoning when you can watch them.
   - Reserve time for doneness checks, resting, serving, and leftover containers.
6. **Write the critical path.** Mark only three to five steps that can delay the meal, plus what can overlap and what must stay sequential. Treat “one more dish” as a change request.
7. **Set stop conditions before cooking.** Remove a dish, choose a simpler route, or stop when food condition, allergy information, time, or equipment is unsafe. Sunk cost does not belong in the pan.
8. **During execution, read one step at a time.** Give it an amount, time range, and observable finish signal. Taste only at a stage that is safe to taste; raw animal food is not a progress probe.
9. **Prepare the leftover path before serving.** Have clean shallow containers ready and cool, label, and store food promptly under local safety guidance.

### Success

You have a bounded meal, explainable portions, only genuinely missing shopping items, a realistic timeline, doneness checks, and a destination for leftovers. Dishes may not finish on the same second, but none should lose safety in pursuit of synchronization.

### Common errors and recovery

- **ERR_TOO_MANY_DISHES:** Delete decorative and duplicate sides. Keep the smallest set that still forms a meal.
- **You started late:** Use faster safe preparation, remove dishes, use a safe ready-made staple, or move serving time honestly. Do not compensate for every delay with maximum heat.
- **One ingredient is unusable:** Replace its function or change the dish. One missing dependency should not block dinner.
- **A frozen ingredient cannot be safely thawed in time:** Use an actually available ingredient, a product-directed cook-from-frozen route, or change the meal or serving time. Do not leave it at room temperature until it seems ready.
- **Two high-attention tasks collide:** Downgrade one to a low-maintenance method or run them sequentially. Human Runtime has no hidden thread pool.
- **Smoke, uncontrolled oil, flame, gas odour, or appliance failure:** Stop cooking and follow local fire/emergency guidance to leave danger and get help. Turn off heat only when safe; do not repair gas or electrical equipment.

### Assumptions, alternatives, and known side effects

Portions, staples, seasoning, and the definition of a complete meal vary by household, region, culture, and budget. Use yours. Without an oven, knife access, long standing tolerance, or helpers, choose one-pot, pre-cut, cold-assembly, or other accessible methods.

Known side effects include dishes to wash, a possible lunch portion, and learning that using half a vegetable does not require buying eight more ingredients.

### Sources

- [Hong Kong Centre for Food Safety: Reduce Food Waste](https://www.cfs.gov.hk/tc_chi/consumer_zone/other_foodsafety/reduce_foodwaste.html) — planning, checking stock, preparing needed amounts, and handling leftovers.
- [Hong Kong Centre for Food Safety: Five Keys to Food Safety in Cooking Food](https://www.cfs.gov.hk/tc_chi/consumer_zone/safefood_all/five_keys_apply_cook.html) — thorough cooking, separation, and checks before eating.
- [US Fire Administration: Cooking Fire Safety](https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/) — active attention and fire stop boundaries.
- [Hong Kong Centre for Food Safety: Properly defrosting frozen food](https://www.cfs.gov.hk/english/consumer_zone/safefood_all/five_keys_defrosting.html) — plan thawing time ahead and avoid room-temperature thawing; match the method and later use to the food and local guidance.

If AI opens this file, it may explain a term or localize the plan. You remain the Human Runtime and choose, cut, heat, check, and serve the food.
