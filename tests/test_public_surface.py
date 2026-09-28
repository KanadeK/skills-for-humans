from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEEDED_SLUGS = {
    "plan-a-market-trip",
    "choose-fresh-perishables",
    "put-away-groceries",
    "sort-a-laundry-load",
    "choose-washer-settings",
    "wash-wool-knitwear",
    "plan-a-meal-from-what-you-have",
    "substitute-an-ingredient-by-function",
    "check-doneness-and-store-leftovers",
}
AGENT_PHRASES = (
    "ask the user",
    "the user operates",
    "do not claim the user",
    "tell the user",
    "have the user",
)


class PublicSurfaceTests(unittest.TestCase):
    def test_readmes_explain_the_human_runtime_in_the_first_screen(self) -> None:
        chinese = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")

        self.assertTrue(chinese.startswith("# Skills for Humans / 给人类的 Skill"))
        self.assertIn("AI 有 Skill，人类也该有。", chinese[:1200])
        self.assertIn("Runtime: Human. Execution requires a body.", chinese[:1200])
        self.assertIn("name: recover-when-you-are-running-late", chinese[:2400])
        self.assertIn("[English](README.en.md)", chinese[:400])
        self.assertIn("[Skill 目录](SKILLS.md)", chinese)
        self.assertIn("不是 AI 提示词", chinese)
        self.assertIn(
            "[v0.1.0](https://github.com/KanadeK/skills-for-humans/releases/tag/v0.1.0)",
            chinese,
        )
        self.assertNotIn("如果页面尚未出现 v0.1.0", chinese)

        self.assertTrue(english.startswith("# Skills for Humans / 给人类的 Skill"))
        self.assertIn("[简体中文](README.md)", english[:400])
        self.assertIn("AI has Skills. Humans should too.", english[:1200])
        self.assertIn("Runtime: Human. Execution requires a body.", english[:1200])
        self.assertIn("name: recover-when-you-are-running-late", english[:2400])
        self.assertIn("[Skill Catalog](SKILLS.md)", english)
        self.assertIn(
            "[v0.1.0](https://github.com/KanadeK/skills-for-humans/releases/tag/v0.1.0)",
            english,
        )

    def test_catalog_lists_exactly_fifteen_skills_in_four_experience_groups(self) -> None:
        catalog = (ROOT / "SKILLS.md").read_text(encoding="utf-8")
        linked = re.findall(
            r"\(skills/([a-z0-9]+(?:-[a-z0-9]+)*)/SKILL\.md\)", catalog
        )

        self.assertEqual(len(linked), 15)
        self.assertEqual(len(set(linked)), 15)
        self.assertEqual(set(linked), {path.name for path in (ROOT / "skills").iterdir()})
        for heading in (
            "Chores / 家务",
            "First Attempts / 第一次尝试",
            "Awkward Social Tasks / 尴尬但普通的社会任务",
            "Recovery / 失败与恢复",
        ):
            self.assertIn(heading, catalog)
        for label in (
            "中文名",
            "English",
            "Time",
            "Difficulty",
            "Side effect",
            "文件",
        ):
            self.assertIn(label, catalog)

    def test_release_and_contribution_surfaces_exist(self) -> None:
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        release_notes = (ROOT / "docs" / "release-notes-v0.1.0.md").read_text(
            encoding="utf-8"
        )
        workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("Tested on human runtime", contributing)
        self.assertIn("不得伪造", contributing)
        self.assertIn("Original synthesis", contributing)
        self.assertIn("## 0.1.0", changelog)
        self.assertIn("15", changelog)
        self.assertIn("## 中文", release_notes)
        self.assertIn("## English", release_notes)
        self.assertIn("15", release_notes)
        self.assertIn("Runtime: Human", release_notes)
        self.assertIn("ubuntu-latest", workflow)
        self.assertIn("windows-latest", workflow)
        self.assertIn("scripts/validate_skills.py", workflow)
        self.assertIn("scripts/build_release.py", workflow)

    def test_seeded_skills_have_no_agent_product_voice(self) -> None:
        for slug in sorted(SEEDED_SLUGS):
            text = (ROOT / "skills" / slug / "SKILL.md").read_text(encoding="utf-8")
            for phrase in AGENT_PHRASES:
                self.assertNotIn(phrase, text.casefold(), f"{slug}: {phrase}")

    def test_repository_contains_no_harvester_or_web_runtime(self) -> None:
        for forbidden in (
            "plugins",
            "state",
            "runs",
            "catalog",
            "package.json",
            "pyproject.toml",
        ):
            self.assertFalse((ROOT / forbidden).exists(), forbidden)
        self.assertEqual((ROOT / "VERSION").read_text(encoding="utf-8").strip(), "0.1.0")
        for skill_path in sorted((ROOT / "skills").glob("*/SKILL.md")):
            self.assertIn("Not yet / 尚未", skill_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
