# Skills for Humans / 给人类的 Skill v0.1.0

[中文](#中文) · [English](#english)

## 中文

AI 有 Skill，人类也该有。

v0.1.0 提供 15 份真正的 SKILL.md，但 Runtime: Human。文件直接给人阅读和执行，不要求聊天框、安装器、数据库或网站。

### 首版内容

- 9 个 Chores：买菜规划、挑易腐食材、买后收纳、衣物分桶、洗衣机设置、羊毛洗护、现有食材备餐、按功能替代、熟度与剩菜。
- 2 个 First Attempts：第一次独自去陌生餐馆；先试新爱好再买装备。
- 2 个 Awkward Social Tasks：给客服打电话；退回买错或不合适的商品。
- 2 个 Recovery：救一锅过咸的菜；发现要迟到时做现实降级。

每份 Skill 都有完整中文原创、自然英文本地化、Human Runtime 信息、现实依赖、执行步骤、成功条件、常见报错、补救、假设、替代路径和短来源。

### 格式与质量

- frontmatter 只使用官方基础 name 与 description。
- 15/15 文件通过 OpenAI 随附 quick_validate.py。
- 标准库 validator 检查 Human Runtime、中英完整性、直接人称、Agent 口吻、placeholder、链接、目录和风险边界。
- fresh-context Codex 作为人类读者随机审查 6 个 Skill；7 个 Required 问题全部修复并复审通过。
- 12 项单元/集成测试、确定性双构建和解压后重验通过。
- 所有 Human test 仍诚实标为 Not yet / 尚未；AI 审查和 CI 不冒充人类实测。

### 安全

食品、洗衣机、化学品、刀火、过敏和冷链边界保留严肃表达。医疗、法律、财务、危机干预、燃气/电气维修、凭据密集和现实控制型 Skill 不在首版。

### 资产

- skills-for-humans-v0.1.0.zip
- SHA256SUMS.txt
- GitHub 自动生成的 source archives

ZIP 解压后即可浏览，也可以在解压目录运行 python scripts/validate_skills.py。

## English

AI has Skills. Humans should too.

v0.1.0 contains 15 real SKILL.md files, but Runtime: Human. People read and execute them directly; no chat box, installer, database, or website is required.

### First-release contents

- 9 Chores: market planning, choosing perishables, grocery storage, laundry sorting, washer settings, wool care, meal planning from available food, functional substitution, and doneness/leftovers.
- 2 First Attempts: eating alone at an unfamiliar restaurant; trying a hobby before buying the gear.
- 2 Awkward Social Tasks: calling customer service; returning an unsuitable purchase.
- 2 Recovery Skills: rescuing salty food; making a realistic downgrade when late.

Every Skill contains original Chinese, natural complete English localization, Human Runtime information, real dependencies, execution, success, common errors, recovery, assumptions, accessible alternatives, and short sources.

### Format and quality

- Frontmatter uses only the official base name and description fields.
- All 15 pass OpenAI's bundled quick_validate.py.
- The standard-library validator checks Human Runtime, bilingual completeness, direct address, Agent voice, placeholders, links, catalog consistency, and risk boundaries.
- Fresh-context Codex readers reviewed 6 randomly selected Skills as human readers; all 7 Required findings were fixed and passed targeted re-review.
- 12 unit/integration tests, deterministic double-build, and extracted-tree revalidation pass.
- Every Human test remains honestly marked Not yet / 尚未. AI review and CI do not impersonate human testing.

### Safety

Food, washer, chemical, knife/heat, allergy, and cold-chain boundaries stay serious. Medical, legal, financial, crisis-intervention, gas/electrical repair, credential-heavy, and real-world-control Skills are excluded.

### Assets

- skills-for-humans-v0.1.0.zip
- SHA256SUMS.txt
- GitHub-generated source archives

Unzip and browse directly, or run python scripts/validate_skills.py in the extracted repository.
