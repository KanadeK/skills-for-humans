from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import ValidationError, validate_repository


VALID_SKILL = """---
name: make-tea
description: "Human-readable instructions for making one cup of tea without turning the kettle into a personality test."
---
# 泡一杯茶 / Make One Cup of Tea

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Stable / 稳定 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 minutes / 5–10 分钟 |
| Requirements / 必要物品 | Tea, water, cup / 茶、水、杯子 |
| Side effects / 现实副作用 | One warm drink and one wet tea bag / 一杯热饮和一个湿茶包 |
| Safety scope / 安全范围 | Everyday / 日常 |

## 中文

你在想喝一杯热茶、又不想把厨房升级成饮品实验室时加载这份 Skill。

### 准备与输入

先确认茶叶类型、杯子大小、可安全使用的热水设备，以及你是否需要无咖啡因选项。看不清设备说明时，先停下来找说明书。

### 执行

1. 用干净杯子装好茶。
2. 按设备说明烧水，手和电线远离水汽与积水。
3. 倒水后按茶叶包装建议计时；不知道时从较短时间开始。
4. 取出茶包或过滤茶叶，先小口确认温度。

### 成功条件

茶汤达到你愿意继续喝的浓度和安全入口温度，退出码可以记作 0。

### 常见报错与补救

太浓时加少量热水；太淡时延长浸泡或下次增加茶叶。烫到无法入口不是“性能富余”，请等待降温。

### 假设、替代与现实副作用

这里假设你能安全取得热水。若握持或搬运热水不方便，请使用带稳固把手的容器、较小水量或请现场可信的人协助。现实副作用是一只待清洗的杯子。

### 来源

- Original synthesis；具体水温与时间以茶叶和设备说明为准。

## English

Load this Skill when you want one warm cup of tea without promoting the kitchen into a beverage laboratory.

### Preparation and inputs

Confirm the tea type, cup size, a hot-water device you can use safely, and whether you need a caffeine-free option. If the controls are unclear, stop and find the manual.

### Execution

1. Put the tea in a clean cup.
2. Heat water according to the appliance instructions, keeping hands and cables away from steam and pooled water.
3. Pour and time the steep using the package guidance; if it is unknown, start shorter.
4. Remove or strain the tea, then test the temperature with a small sip.

### Success

The drink is at a strength and temperature you are willing to keep drinking. Exit code 0 is available if you enjoy paperwork.

### Common errors and recovery

Dilute tea that is too strong with a little hot water. Steep longer or use more tea next time if it is weak. Too hot to drink is not excess performance; wait.

### Assumptions, alternatives, and side effects

This assumes you can obtain and handle hot water safely. If lifting or gripping is difficult, use less water, a stable handled vessel, or ask a trusted person who is physically present to assist. The known side effect is one cup that needs washing.

### Sources

- Original synthesis; follow the tea packaging and appliance manual for exact temperature and timing.
"""


def write_repository(root: Path, *, slug: str = "make-tea", text: str = VALID_SKILL) -> None:
    skill_root = root / "skills" / slug
    skill_root.mkdir(parents=True)
    (skill_root / "SKILL.md").write_text(text, encoding="utf-8")
    (root / "SKILLS.md").write_text(
        f"- [Make Tea](skills/{slug}/SKILL.md)\n", encoding="utf-8"
    )


class ValidateSkillsTests(unittest.TestCase):
    def test_valid_human_skill_repository_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_repository(root)

            report = validate_repository(root)

        self.assertEqual(report, {"skills": 1, "catalog_entries": 1})

    def test_frontmatter_is_official_and_directory_matches(self) -> None:
        invalid_cases = {
            "extra-frontmatter": VALID_SKILL.replace(
                "description:", "runtime: human\ndescription:", 1
            ),
            "wrong-name": VALID_SKILL.replace("name: make-tea", "name: boil-water", 1),
            "missing-description": VALID_SKILL.replace(
                'description: "Human-readable instructions for making one cup of tea without turning the kettle into a personality test."\n',
                "",
                1,
            ),
        }
        for label, text in invalid_cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_repository(root, text=text)

                with self.assertRaises(ValidationError):
                    validate_repository(root)

    def test_human_runtime_bilingual_semantics_and_agent_voice_are_enforced(self) -> None:
        invalid_cases = {
            "missing-runtime-field": VALID_SKILL.replace(
                "| Time / 预计时间 | 5–10 minutes / 5–10 分钟 |\n", "", 1
            ),
            "missing-english-recovery": VALID_SKILL.replace(
                "### Common errors and recovery", "### When the cup disappoints", 1
            ).replace("Dilute tea", "Adjust tea", 1),
            "agent-facing-language": VALID_SKILL.replace(
                "Confirm the tea type", "Ask the user to confirm the tea type", 1
            ),
            "placeholder": VALID_SKILL.replace(
                "one warm cup of tea", "one TODO cup of tea", 1
            ),
        }
        for label, text in invalid_cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                write_repository(root, text=text)

                with self.assertRaises(ValidationError):
                    validate_repository(root)

    def test_catalog_and_local_links_are_exact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_repository(root)
            (root / "SKILLS.md").write_text("- Nothing here yet\n", encoding="utf-8")

            with self.assertRaisesRegex(ValidationError, "catalog"):
                validate_repository(root)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_repository(
                root,
                text=VALID_SKILL.replace(
                    "### 来源", "[missing local note](missing.md)\n\n### 来源", 1
                ),
            )

            with self.assertRaisesRegex(ValidationError, "broken local link"):
                validate_repository(root)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_repository(root)
            (root / "SKILLS.md").write_text(
                "- [One](skills/make-tea/SKILL.md)\n"
                "- [Again](skills/make-tea/SKILL.md)\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValidationError, "catalog"):
                validate_repository(root)

    def test_high_risk_names_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_repository(
                root,
                slug="medical-diagnosis",
                text=VALID_SKILL.replace(
                    "name: make-tea", "name: medical-diagnosis", 1
                ),
            )

            with self.assertRaisesRegex(ValidationError, "high-risk"):
                validate_repository(root)


if __name__ == "__main__":
    unittest.main()
