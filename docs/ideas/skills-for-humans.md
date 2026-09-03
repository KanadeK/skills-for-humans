# Skills for Humans / 给人类的 Skill

## Problem Statement

如何把原本给 AI 安装的 Skill 格式反转成给人类直接阅读、仿佛安装在人类身上的生活技能包，让普通琐事、第一次尝试和失败补救既真正有用，又产生一本正经的戏剧感？

## Recommended Direction

把真正、可通过官方基础校验的 SKILL.md 当作产品媒介，而不是借来的装饰。每个文件直接对人说“你”，把人类写成 Runtime，把衣服、食材、时间、勇气和一通可能令人紧张的客服电话写成依赖与输入。步骤、安全边界和补救必须可信；喜剧只来自严肃机器语言与普通生活之间的比例失调。

中文是原创和首要语言，英文是首个完整本地化。一个读者不需要 AI、命令行、安装器或特殊应用，只要打开文件就能执行。AI 若读取文件，只能作为旁观的解释器或本地化助手，不能重新夺回执行者身份。

首版用四类 15 个 Skill 证明概念：九个家务能力、两个第一次尝试、两个尴尬社会任务、两个失败恢复。它们覆盖程序性任务、现场判断、情绪摩擦和补救，而不是把同一清单换标题凑数。

## Why this direction

限时同类复核没有发现同一产品边界：

- msimchowitz/writing-skills 把 Agent Skills 与人类指南严格分开，并明确人类项目没有 SKILL.md。本项目有意反转这条边界。
- x-cmd 的 life skills 仍是给 Agent 加载的知识图与执行规范。
- reysu/ai-life-skills 让 AI 管理 Obsidian 与生活信息，AI 仍是执行者。

可借鉴的是严格格式、flat 目录、清晰索引与本地验证；不借用 Agent 安装流程、知识库架构或原文表达。

## Key Assumptions to Validate

- [ ] 普通读者能在 README 首屏十秒内理解“这是给人类安装的 Skill”，而不会以为它是提示词库。
- [ ] 任一 SKILL.md 在没有 AI 的情况下仍能让人完成任务或作出安全停止决定。
- [ ] 七分实用、三分冷幽默能形成辨识度，又不拖慢动作、不羞辱读者、不遮蔽风险。
- [ ] 同一文件内的完整中英版本比首版 locale 目录更容易浏览和维护。
- [ ] 真实官方 frontmatter 与 Human Runtime 正文信息块可以同时通过官方 validator。

验证方式：自动格式/链接/目录测试，至少五个 fresh-context 读者审查，九个旧能力的 Agent 口吻扫描，食品/洗衣/刀火/过敏安全审查，以及 Release 下载后的离线浏览测试。

## MVP Scope

- 独立公开仓库 KanadeK/skills-for-humans。
- 15 个原创、中英完整、flat 目录的 Human Skills。
- 每个 Skill 使用真实 SKILL.md frontmatter，并在首屏显示 Human Runtime 信息。
- 中英双语 README、目录、格式规范、贡献模板。
- 标准库 validator、单元测试、确定性 ZIP 构建、Ubuntu/Windows CI。
- v0.1.0 GitHub Release，下载后不需安装即可浏览。

十五个是首版边界，不是长期上限。后续内容由真实使用、贡献质量和后台 Harvester 的证据发现推动。

## Not Doing

- 不做普通生活百科或教程站——媒介反转与可执行失败恢复才是产品。
- 不做 AI 聊天提示词集合——没有 AI 也必须完整可用。
- 不复制 codex-skill-harvester 的 SQLite、runs、campaign、候选队列、Plugin marketplace 或软件 Skills——Harvester 只做后台证据与维护。
- 不承诺首版收录世界上一切——十五个高质量 Skill 足以验证核心。
- 不做医疗、法律、财务、危机干预、燃气电气维修或凭据密集内容——冷幽默不进入高风险域。
- 不做网站、App、GitHub Pages、账号、搜索服务、生成式 UI 或预建 locale 框架——仓库与 Markdown 就是首版产品。
- 不使用受版权保护的角色、作品名、网络梗、嘲弄式笑话或大段来源表达。

## Open Questions after v0.1.0

- 哪些 Skill 真的被人按步骤走过，能诚实标记 Tested on human runtime？
- 下一种语言或地区差异是否已有足够贡献者，值得建立 locale 机制？
- “安装”是否需要一个只做离线复制/打开的辅助脚本，还是保持零工具更符合产品？
