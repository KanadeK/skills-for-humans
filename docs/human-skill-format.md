# Human Skill format

Skills for Humans uses a real SKILL.md envelope and a human-first body.

## Compatibility envelope

The YAML frontmatter contains exactly:

    ---
    name: one-kebab-case-job
    description: "A concise description of the human task and its boundary."
    ---

This is the same minimum shape documented by OpenAI. Human Runtime fields do not belong in invented frontmatter keys; they remain visible to a person at the top of the Markdown body.

## First-screen contract

Every Skill begins with:

1. A bilingual title.
2. Links to 中文 and English anchors.
3. A visible two-column Human Runtime table containing:
   - Runtime / 运行时
   - Status / 状态
   - Difficulty / 难度
   - Time / 预计时间
   - Requirements / 必要物品
   - Side effects / 现实副作用
   - Safety scope / 安全范围

Runtime is Human / 人类. The v0.1.0 safety scope is Everyday / 日常. A contributor cannot relabel medical, legal, financial, crisis, credential, gas, or electrical work as “everyday” to bypass review.

## Complete language sections

The 中文 section is the original. English is a full localization, not a summary.

Both sections must let a reader answer:

- Is this the moment to load the Skill?
- What do you need, and what must you confirm first?
- What do you actually do?
- What does success look like?
- What common failure looks like?
- Can you recover, downgrade, or stop safely?
- What side effects remain afterward?
- Which regional, cultural, financial, equipment, mobility, or sensory assumptions apply?
- Which short sources support objective facts, or is this Original synthesis?

Headings can follow the task rather than a universal template. The validator checks that these meanings are present without locking exact prose or jokes.

## Voice

The file speaks directly to 你 / you.

Good:

    先把订单号、你能接受的结果和一句开场白写在纸上。

Wrong product:

    Ask the user for the order number and tell them what to say.

AI may explain, read aloud, or localize a Human Skill. It may not claim the phone call, cooking, washing, purchase, return, or other physical act happened. Keep this compatibility note short; the body belongs to the human reader.

## Humor

The useful procedure must survive if every joke is removed.

- Good places: dependency names, harmless error labels, known side effects, patch-note phrasing.
- Bad places: temperatures, deadlines, allergies, chemical warnings, consent, costs, return policies, accessibility, or any uncertainty.
- Maximum ambition: a small smile while the reader still knows exactly what to do next.

## Sources

Use short links and a one-line statement of what fact they support. Do not paste upstream instructions. When no external authority is needed, say Original synthesis and state the cultural or access assumptions.

## Human testing

Do not write Tested on human runtime unless someone actually followed the steps. Record what was attempted, what changed, and any limitation in the contribution or PR. Structural validation and AI review are not human testing.
