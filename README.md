# Skills for Humans / 给人类的 Skill

[English](README.en.md)

[![CI](https://github.com/KanadeK/skills-for-humans/actions/workflows/ci.yml/badge.svg)](https://github.com/KanadeK/skills-for-humans/actions/workflows/ci.yml)

> **AI 有 Skill，人类也该有。**
>
> **Runtime: Human. Execution requires a body.**

这是 15 份写给人类直接阅读和执行的真正 SKILL.md。它们处理买菜、洗衣、做饭、第一次独自进餐、给客服打电话、退货，以及事情已经搞砸一点以后怎么补救。

没有聊天框是必需依赖。打开文件，读完输入和停止条件，然后由 Human Runtime，也就是你，执行。

一份真实文件长这样：

    ---
    name: recover-when-you-are-running-late
    description: "Human-readable instructions for calculating an honest ETA..."
    ---
    # 出门前发现又要迟到了 / Recover When You Are Running Late

    | Runtime / 运行时 | Human / 人类 |
    | Time / 预计时间 | 5–15 分钟决定并出发 |
    | Side effects / 现实副作用 | 少做几项，但不要求物理定律加班 |

    ERR_找不到关键物品：
    给搜索设一个短而明确、符合你行动/视觉/注意力需求的上限。
    仍找不到且活动离不开它时，通知改期。

机器格式是认真的，生活也是真的。反差负责让人想打开，步骤负责让人能做完。

## 如何“安装”

1. 打开 [Skill 目录](SKILLS.md)。
2. 选择当前真的遇到的任务。
3. 打开对应 skills/<slug>/SKILL.md。
4. 阅读 Human Runtime 信息、准备项和安全边界。
5. 让你的肉身执行；成功、降级、停止和补救都是合法输出。

你也可以从 [GitHub Releases](https://github.com/KanadeK/skills-for-humans/releases) 下载已发布 ZIP，解压后离线浏览。如果页面尚未出现 v0.1.0，main 上的内容仍只是候选，不能把本地构建当作发布。

## v0.1.0 有什么

### Chores / 家务

- 去菜市场前做计划
- 挑选易腐食材
- 买菜回家后收纳
- 给衣服分桶
- 选择洗衣机设置
- 洗羊毛针织物
- 用现有食材安排一顿饭
- 按功能替代缺少的食材
- 判断熟度和处理剩菜

### First Attempts / 第一次尝试

- 第一次独自去陌生餐馆
- 不先买齐装备地尝试新爱好

### Awkward Social Tasks / 尴尬但普通的社会任务

- 给客服打电话
- 把买错或不合适的东西退回去

### Recovery / 失败与恢复

- 菜做咸了以后尽量救回来
- 出门前发现要迟到了

十五个是首版范围，不是长期上限。不会为了声称“覆盖世界”把一件事换十五个标题。

## 它为什么不是 AI 提示词库

- 正文直接称你，由你完成观察、沟通和物理动作。
- 没有 AI 时，每份 Skill 仍然完整。
- AI 可以朗读、解释或本地化，但只是可选旁观者。
- 文件保留官方兼容的 name、description 和 SKILL.md 结构；Human Runtime 信息放在正文，不发明第二套 metadata。
- 每个 Skill 都写成功条件、常见报错、恢复路径、现实副作用和假设。

格式依据 OpenAI 官方 [Build skills](https://developers.openai.com/codex/skills) 文档，并使用随附 quick_validate.py 逐份校验。项目自己的 validator 还检查中英完整性、目录、链接、Human Runtime 和 Agent 口吻残留。

## 七分有用，三分一本正经

笑点应该出现在依赖、报错和副作用里，不应出现在温度、过敏、化学品、付款、同意或截止时间里。

我们不嘲笑不会做家务、第一次尝试、社交紧张、贫穷、残障或文化差异。一个 Skill 拿掉笑话后仍必须能工作；如果拿掉步骤只剩笑话，它没有通过构建。

## 安全边界

- 食品外观和气味不能单独证明安全；过敏、婴幼儿食品、罐藏、发酵和疾病处理不做轻松补丁。
- 洗衣服从标签与准确机型说明书；不混用危险清洁剂，不维修电气、燃气或机械设备。
- 做饭遇到失控热油、明火、燃气异味或设备故障时停止并按当地紧急指导处理。
- 本项目不收录医疗、法律、财务、危机干预、凭据密集或现实控制型 Skill。
- 地域、文化、价格、设备、行动、视觉、听觉和沟通假设必须明说并提供替代路径。

## 贡献

从 [模板](templates/SKILL.md) 开始，并阅读 [Human Skill 格式](docs/human-skill-format.md) 与 [CONTRIBUTING.md](CONTRIBUTING.md)。

AI 可以协助起草，但不能批量倾倒。最好让至少一名人类按步骤走过；没有真实走读证据时必须诚实写 Not yet / 尚未，而不是把 validator 通过当作 Tested on human runtime。

## 项目边界

[codex-skill-harvester](https://github.com/KanadeK/codex-skill-harvester) 是后台发现、证据、去重与维护引擎。本仓库只有给人看的最终 Skill，不包含它的 SQLite、campaign、候选队列、运行报告或软件工程 Plugin。

## License

[MIT](LICENSE)
