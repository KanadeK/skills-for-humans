# Spec: Skills for Humans / 给人类的 Skill v0.1.0

## Objective

创建一个独立、公开、以中文原创为主的 Human Skill 仓库。文件继续使用官方兼容的 SKILL.md 形状，但内容由人类直接阅读和执行。

目标读者：

- 会逛 GitHub、喜欢 AI 或技术文化的人；
- 第一次做某件普通小事，希望获得清楚步骤的人；
- 碰到轻微尴尬或小型失败，需要现实补救而不是励志口号的人；
- 需要完整英文版本的读者，而不是被迫阅读中文原稿的附属摘要。

核心体验：

1. README 首屏十秒内说明“AI 有 Skill，人类也该有”。
2. 读者打开一个 SKILL.md，先看到 Runtime: Human 和现实依赖。
3. 读者无需 AI，能照着中文或英文部分执行。
4. 成功、失败、停止和补救条件都明确。
5. 少量冷幽默提供反差，但不会抢走任务或安全信息。

## Product identity

- 正式名称：Skills for Humans / 给人类的 Skill。
- GitHub slug：KanadeK/skills-for-humans。
- 主要语言：简体中文原创。
- 首个本地化：完整英文。
- 内容比例：约七分实用、三分一本正经的冷幽默。
- Runtime：Human。肉身负责观察、沟通和物理执行。
- AI compatibility：仅来自合法 SKILL.md 结构；AI 可解释、朗读或本地化，不能成为产品的默认执行者。

## Commands

开发分支完成后，仓库根目录支持：

    python scripts/validate_skills.py
    python -m unittest discover -s tests -v
    python scripts/build_release.py --output dist
    python scripts/validate_skills.py --root <解压后的目录>

发布前还要从本机 OpenAI 随附的 skill-creator 目录逐个执行：

    python quick_validate.py <skill-directory>

Python 要求 3.12+，项目本身只使用标准库。官方 validator 所需依赖只能安装在隔离的 validator 环境，不成为项目运行依赖。

## Project structure

    README.md                 简体中文首页
    README.en.md              完整英文首页
    SKILLS.md                 中英目录与稳定链接
    AGENTS.md                 仓库长期规则
    CONTRIBUTING.md           Human Skill 贡献门槛
    LICENSE                   MIT
    CHANGELOG.md              人类可读版本变化
    docs/ideas/               产品一页定义
    docs/spec.md              权威规格
    docs/human-skill-format.md Human Skill 语义格式
    skills/<slug>/SKILL.md    flat、稳定的正式内容
    templates/SKILL.md        唯一贡献模板
    scripts/validate_skills.py 标准库 validator
    scripts/build_release.py   确定性 ZIP 与校验和
    tests/                    行为与发布测试
    .github/workflows/ci.yml  Ubuntu/Windows 门槛
    tasks/                    可恢复执行计划

禁止创建空目录、Plugin marketplace、SQLite、数据库、后台 campaign 文件、网站、App、locale 框架或没有当前使用者的抽象。

## Official Skill compatibility

格式权威仅使用 OpenAI 官方 Build skills 文档与本机随附 quick_validate.py。

每个 skills/<slug>/SKILL.md：

- 文件夹名和 frontmatter name 相同，均为 1–64 字符 kebab-case；
- frontmatter 必须且只需 name、description；不为 Human Runtime 发明未经确认的 YAML 键；
- description 清楚说明人类任务和边界，即使被 Agent 索引也不会误认为它应代替人完成现实动作；
- 正文是有效 Markdown，不依赖私有路径、外部脚本或在线运行时。

官方文档仍把正文描述为 Agent 指令。本项目只复用文件协议：正文的产品读者是人。这个张力是明确设计，不是遗漏。

## Human Skill information model

首屏使用统一、可见的 Human Runtime 信息表：

- Runtime / 运行时：Human / 人类
- Status / 状态
- Difficulty / 难度
- Time / 预计时间
- Requirements / 必要物品
- Side effects / 现实副作用
- Safety scope / 安全范围：Everyday / 日常

同一文件必须有可链接的中文和 English 区段。两种语言都完整表达以下语义，但正文标题和叙事顺序可按任务调整：

- 何时加载；
- 安装前准备或依赖；
- 输入与需要确认的未知；
- 实际执行；
- 成功条件；
- 常见报错；
- 回滚或补救；
- 已知副作用；
- 地域、设备、文化、身体或能力假设；
- Sources / 来源，或明确 Original synthesis。

正文直接称你 / you。严禁 ask the user、the user operates、do not claim the user、tell the user、have the user 等 Agent 口吻。AI 兼容说明最多一个短段，只能说明 AI 可帮助解释或本地化，而物理执行属于你。

## Language strategy

- 中文先写，决定结构、细节和笑点；英文根据任务语境重新表达，不逐句僵硬映射。
- 中文和英文都必须能单独完成任务，不能互相要求“参见另一语言”才能获得关键步骤。
- 来源事实保持一致；文化习惯若只适用一地，明确标注而不是强行统一。
- v0.1.0 不建立 locale 文件夹、翻译键或生成管线。
- 未来只有在真实第三语言贡献出现时，才决定同文件扩展、独立本地化文件或地区变体；稳定 slug 不随分类移动。

## Humor and dignity

- 正确动作、安全、时效和不知道的地方一律认真。
- 冷幽默集中在标题、依赖、报错、副作用与 patch-note 式措辞。
- 每个 Skill 只保留少量真正贴合场景的笑点；笑点拿掉后，工作流仍然成立。
- 不使用网络梗、动漫/影视名称、夸张营销语或受保护角色。
- 不羞辱不会做家务、社恐、失败、贫穷、残障、语言水平或文化差异。
- 不用幽默掩盖地区差异、设备差异、危险或证据不足。

## v0.1.0 content

Chores：

1. plan-a-market-trip
2. choose-fresh-perishables
3. put-away-groceries
4. sort-a-laundry-load
5. choose-washer-settings
6. wash-wool-knitwear
7. plan-a-meal-from-what-you-have
8. substitute-an-ingredient-by-function
9. check-doneness-and-store-leftovers

First Attempts：

10. eat-alone-at-an-unfamiliar-restaurant
11. try-a-hobby-before-buying-the-gear

Awkward Social Tasks：

12. call-customer-service
13. return-the-wrong-item

Recovery：

14. rescue-salty-food
15. recover-when-you-are-running-late

这里共有 15 个独立 Skill。咸味补救从原“食材替代”中分离，因为它处理已发生失败、输入和成功边界不同；熟度与剩菜仍是一个连续的食品安全任务。

## Sources and safety

- 九个 Harvester 生活能力只提供官方来源链接和必要事实种子，不复制 Agent 口吻、Plugin 文件或大段表达。
- 食品事实优先 FDA、香港食物安全中心等政府来源；洗护符号与羊毛护理使用政府/权威行业来源；具体洗衣机按钮必须服从读者手中准确型号说明书。
- 社会情景、第一次尝试与轻度补救可以标为 Original synthesis，并明确文化、商家政策、费用、无障碍与沟通方式差异。
- 食品外观和气味不能单独证明安全。过敏、婴幼儿食品、罐藏、发酵、严重污染等不在轻松 Skill 范围。
- 刀、热锅、明火和湿电器只写常规停止条件；燃气、电气或机械维修不进入 Skill。
- 不执行第三方脚本，不提交网页原文缓存，不复制许可证不明材料。

## Testing strategy

自动测试只守稳定边界：

- frontmatter、name、description 与官方 quick_validate 兼容；
- Human Runtime 信息块字段完整；
- 中文和英文区段均达到可执行内容下限；
- 直接称你 / you，且没有 Agent 口吻残留；
- 无 placeholder、绝对私有路径、断开的本地链接或重复 name；
- skills 目录与 SKILLS.md 完全一致；
- Safety scope 为 Everyday，不发布禁区能力；
- 构建 ZIP 路径安全、时间戳固定、内容确定，SHA256SUMS.txt 可复算；
- 解压后的仓库 validator 仍通过。

测试不锁死标题、具体笑话、行数或全文快照。内容质量由 fresh-context 读者审查负责：

- 随机至少五个 Skill；
- 人不借助 AI 是否理解并能执行；
- 幽默是否存在但不抢任务；
- 是否有 Agent 口吻；
- 是否暗藏文化、设备、身体或经济假设；
- 失败后是否能恢复或安全停止。

九个从 Harvester 事实种子重写的 Skill 另做全文 Agent 口吻扫描。食品、过敏、刀火、化学品和洗衣机相关内容做单独安全审查。本轮不为人的生活动作制造虚假自动化 E2E。

## Code style

Python 保持直接、标准库、类型标注和快速失败。公开函数接受 Path，不读取隐式工作目录；命令失败返回非零。

    def validate_repository(root: Path) -> dict[str, int]:
        skill_paths = sorted((root / "skills").glob("*/SKILL.md"))
        if not skill_paths:
            raise ValidationError("no Human Skills found")
        return {"skills": len(skill_paths)}

测试以输入/输出和文件状态为准，不断言内部调用顺序。

## Boundaries

Always：

- 先更新 spec/plan，再改变身份或格式；
- 用 TDD 实现 validator 与构建；
- 每个 Skill 完成中英内容、安全和来源检查；
- 精确暂存、分片提交、合并前五轴审查；
- Release 后从远端重新下载验证。

Ask first：

- 改项目名、slug、许可证或 Human Runtime 核心；
- 增加依赖、脚本执行型 Skill、第三语言架构或新高风险域；
- 删除或重写已发布 tag/Release。

Never：

- 把 AI 重新写成默认执行者；
- 伪造 Tested on human runtime；
- 添加 Harvester 数据库或后台实现；
- 自动发布高风险内容；
- 运行外部脚本、提交密钥或版权不明大段材料。

## Success criteria

- README 首屏十秒内说明这是“给人类安装的 Skill”。
- 任一 SKILL.md 无需 AI 即可实际照做。
- 15 个 Skill 具有独立目标、完整中英内容、Human Runtime 信息和恢复路径。
- 所有 Skill 通过仓库 validator 与官方 quick_validate。
- 幽默不妨碍正确动作、安全边界和尊严。
- 仓库没有 Harvester 数据库、运行报告、候选队列或后台实现噪声。
- Ubuntu/Windows CI、测试、链接、目录一致性与确定性构建通过。
- v0.1.0 可从 GitHub Release 下载，校验、解压、浏览并在隔离目录重新验证。
- 仓库公开信息、tag、Release target、main CI、贡献者与许可证被实际回读。
- Harvester README 通过另一个独立 PR 恢复为后台引擎，并链接本项目；旧 v0.2.0 历史保持不变。

## Open questions

v0.1.0 没有阻塞性开放问题。真实 human-runtime 走读、第三语言与辅助安装器都留到发布后的证据阶段。
