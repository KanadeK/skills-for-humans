# 贡献 Human Skill / Contributing a Human Skill

[中文](#中文) · [English](#english)

## 中文

感谢你给人类增加一个可安装的技能。这里的“安装”指读懂并执行，不是把文件复制进模型目录。

### 先判断它是不是一个 Skill

合适的贡献：

- 有一个清楚、可重复的人类任务；
- 至少有一个不那么显然的判断；
- 输入、成功、失败和恢复能说清；
- 与已有 15 个 Skill 的用户目标或行为边界不同；
- 普通人无需 AI 也能照着做；
- 风险属于 Everyday / 日常。

不合适的贡献：

- 一篇普通生活百科或无限延伸的知识文章；
- 一组给 AI 的聊天提示词；
- 只换标题、工具或地区名称的近重复；
- 医疗、法律、财务、危机干预、燃气/电气维修、凭据密集或现实控制；
- 需要执行不受信任脚本、复制版权内容或暴露个人信息。

### 创建

1. 复制 templates/SKILL.md 到 skills/<kebab-case-name>/SKILL.md。
2. 先写原创中文，再写完整、自然的 English 本地化。
3. frontmatter 只保留 name 和 description。
4. Human Runtime 表中填写现实时间、依赖、副作用和 Everyday 安全范围。
5. 在正文直接称“你”，写清执行、成功、常见报错、补救和停止条件。
6. 客观事实用短来源链接说明用途；不需要外部事实时写 Original synthesis。
7. 更新 SKILLS.md，保持 flat 路径不随分类移动。

### 质量门槛

- 一名真实人类必须能读懂；最好实际按步骤走一遍。
- 只有确实走过并记录范围、结果和限制时，才能写 Tested on human runtime。
- 没有证据时保留 Not yet / 尚未。不得伪造实测，也不能把 AI 审查、validator 或 CI 当成人类实测。
- AI 可以协助起草、检查遗漏或本地化，但不得批量倾倒相似 Skill。
- 说明该 Skill 为什么不与现有能力重复。
- 明确地域、文化、费用、设备、行动、视觉、听觉、感官或沟通假设，并提供实际替代路径。
- 笑点拿掉后流程仍成立；任何安全数字、边界、付款、同意和截止时间都不用玩笑表达。
- 翻译是本地化：两种语言事实、成功和恢复一致，但句子不必逐字镜像。

### 验证

在仓库根目录运行：

    python scripts/validate_skills.py
    python -m unittest discover -s tests -v
    python scripts/build_release.py --output dist

还要用 OpenAI 随附的 quick_validate.py 检查新增 Skill 文件夹。

提交 PR 时写明：

- 用户任务与非重复性；
- 来源或 Original synthesis；
- 风险和停止边界；
- 中英本地化检查；
- Tested on human runtime 的真实状态；
- 你运行过的命令和结果。

## English

Thank you for adding something installable to a human. Here, installation means understanding and doing—not copying a file into a model directory.

### Decide whether it is a Skill

A suitable contribution:

- has one clear, repeatable human task;
- contains at least one non-obvious decision;
- defines inputs, success, failure, and recovery;
- differs from the user goal or behaviour boundary of existing Skills;
- works for a person without AI;
- stays inside Everyday safety scope.

Not suitable:

- a general life encyclopedia or unbounded article;
- a collection of chat prompts for AI;
- a near-duplicate with only title, tool, or region changed;
- medical, legal, financial, crisis, gas/electrical repair, credential-heavy, or real-world-control work;
- anything that runs untrusted scripts, copies protected prose, or exposes personal data.

### Create

1. Copy templates/SKILL.md to skills/<kebab-case-name>/SKILL.md.
2. Write original Chinese first, then a complete natural English localization.
3. Keep only name and description in frontmatter.
4. Fill the Human Runtime table with real time, dependencies, side effects, and Everyday safety scope.
5. Address “you” directly and cover execution, success, common errors, recovery, and stop conditions.
6. Link short sources for objective facts; write Original synthesis when no external authority is needed.
7. Update SKILLS.md while keeping the flat path stable across category changes.

### Quality gate

- A real person must understand it; preferably, someone follows the steps.
- Write Tested on human runtime only when a person actually completed a recorded scope and the result/limitations are available.
- Otherwise keep Not yet / 尚未. Do not fabricate human testing or relabel AI review, validation, or CI as human testing.
- AI may help draft, find omissions, or localize; it may not bulk-dump similar Skills.
- Explain why the capability is not a duplicate.
- State regional, cultural, cost, equipment, mobility, visual, hearing, sensory, and communication assumptions with practical alternatives.
- Remove every joke and the workflow must still work. Never hide safety numbers, payment, consent, boundaries, or deadlines inside humour.
- Translation is localization: facts, success, and recovery stay aligned, while sentences need not mirror word for word.

### Verify

Run from the repository root:

    python scripts/validate_skills.py
    python -m unittest discover -s tests -v
    python scripts/build_release.py --output dist

Also run OpenAI's bundled quick_validate.py against every added Skill directory.

In the PR, record:

- human task and non-duplication;
- sources or Original synthesis;
- risk and stop boundary;
- bilingual localization review;
- real Tested on human runtime status;
- commands and results.
