from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable


class ValidationError(ValueError):
    pass


NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FRONTMATTER_KEYS = {"name", "description"}
REQUIRED_INFO_FIELDS = {
    "runtime",
    "status",
    "difficulty",
    "time",
    "requirements",
    "side effects",
    "safety scope",
}
AGENT_PHRASES = (
    "ask the user",
    "the user operates",
    "do not claim the user",
    "tell the user",
    "have the user",
    "the user should",
)
HIGH_RISK_NAME_TERMS = {
    "credential",
    "credentials",
    "crisis",
    "diagnose",
    "diagnosis",
    "electrical",
    "finance",
    "financial",
    "gas",
    "legal",
    "medical",
    "medication",
    "therapy",
}
PLACEHOLDER_RE = re.compile(
    r"(?i)(?:\bTODO\b|\bTBD\b|\bPLACEHOLDER\b|\[TODO:|待补充)"
)
PRIVATE_PATH_RE = re.compile(r"(?:[A-Za-z]:\\Users\\|/home/[^/\s]+/)")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LANGUAGE_HEADING_RE = {
    "zh": re.compile(r"(?m)^##\s+中文\s*$"),
    "en": re.compile(r"(?m)^##\s+English\s*$"),
}
SEMANTIC_MARKERS = {
    "zh": (
        ("准备", "依赖"),
        ("输入", "确认"),
        ("执行", "步骤"),
        ("成功", "完成"),
        ("报错", "失败", "问题"),
        ("补救", "恢复", "回滚", "停止"),
        ("假设", "替代", "无障碍"),
        ("来源", "Original synthesis"),
    ),
    "en": (
        ("preparation", "dependencies", "requirements"),
        ("input", "confirm"),
        ("execution", "steps"),
        ("success", "done"),
        ("error", "failure", "problem"),
        ("recovery", "rollback", "stop"),
        ("assumption", "alternative", "access"),
        ("source", "original synthesis"),
    ),
}


def _fail(path: Path, message: str) -> None:
    raise ValidationError(f"{path.as_posix()}: {message}")


def _frontmatter(path: Path, text: str) -> tuple[dict[str, str], str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if not normalized.startswith("---\n"):
        _fail(path, "missing YAML frontmatter")
    end = normalized.find("\n---\n", 4)
    if end == -1:
        _fail(path, "unclosed YAML frontmatter")
    fields: dict[str, str] = {}
    for line in normalized[4:end].splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_-]*):\s*(.+)", line)
        if match is None:
            _fail(path, f"unsupported frontmatter line: {line}")
        key, value = match.groups()
        if key in fields:
            _fail(path, f"duplicate frontmatter key: {key}")
        value = value.strip()
        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]
        if not value.strip():
            _fail(path, f"empty frontmatter value: {key}")
        fields[key] = value
    if set(fields) != FRONTMATTER_KEYS:
        missing = sorted(FRONTMATTER_KEYS - set(fields))
        extra = sorted(set(fields) - FRONTMATTER_KEYS)
        _fail(path, f"frontmatter keys must be name and description; missing={missing} extra={extra}")
    return fields, normalized[end + 5 :]


def _information_rows(path: Path, body: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in body[:2500].splitlines():
        match = re.fullmatch(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if match is None:
            continue
        label, value = match.groups()
        key = label.split("/", 1)[0].strip().lower()
        if key in REQUIRED_INFO_FIELDS:
            rows[key] = value.strip()
    missing = sorted(REQUIRED_INFO_FIELDS - set(rows))
    if missing:
        _fail(path, f"Human Runtime information is missing: {', '.join(missing)}")
    if rows["runtime"].casefold() != "human / 人类".casefold():
        _fail(path, "Runtime must be Human / 人类")
    if rows["safety scope"].casefold() != "everyday / 日常".casefold():
        _fail(path, "high-risk safety scope is not allowed")
    if any(not value or set(value) <= {"-", ":", " "} for value in rows.values()):
        _fail(path, "Human Runtime information values must be concrete")
    return rows


def _language_sections(path: Path, body: str) -> tuple[str, str]:
    if "[中文](#中文)" not in body or "[English](#english)" not in body:
        _fail(path, "missing Chinese/English anchor navigation")
    chinese_heading = LANGUAGE_HEADING_RE["zh"].search(body)
    english_heading = LANGUAGE_HEADING_RE["en"].search(body)
    if chinese_heading is None or english_heading is None:
        _fail(path, "both ## 中文 and ## English sections are required")
    if chinese_heading.start() >= english_heading.start():
        _fail(path, "the original Chinese section must precede English")
    chinese = body[chinese_heading.end() : english_heading.start()]
    english = body[english_heading.end() :]
    if len(re.sub(r"\s+", "", chinese)) < 350:
        _fail(path, "Chinese section is too short to be executable")
    if len(re.sub(r"\s+", "", english)) < 350:
        _fail(path, "English section is too short to be executable")
    if "你" not in chinese:
        _fail(path, "Chinese must address 你 directly")
    if re.search(r"\byou\b", english, re.IGNORECASE) is None:
        _fail(path, "English must address you directly")
    for language, section in (("zh", chinese), ("en", english)):
        folded = section.casefold()
        for alternatives in SEMANTIC_MARKERS[language]:
            if not any(marker.casefold() in folded for marker in alternatives):
                _fail(
                    path,
                    f"{language} section is missing one semantic requirement: {'/'.join(alternatives)}",
                )
    return chinese, english


def _validate_links(root: Path, documents: Iterable[Path]) -> None:
    resolved_root = root.resolve()
    for document in documents:
        text = document.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1).strip().strip("<>")
            if raw_target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            path_part = raw_target.split("#", 1)[0]
            if not path_part:
                continue
            target = (document.parent / path_part).resolve()
            if not target.is_relative_to(resolved_root) or not target.exists():
                _fail(document, f"broken local link: {raw_target}")


def _validate_skill(root: Path, path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    fields, body = _frontmatter(path.relative_to(root), text)
    name = fields["name"]
    if len(name) > 64 or NAME_RE.fullmatch(name) is None:
        _fail(path.relative_to(root), "name must be kebab-case and at most 64 characters")
    if path.parent.name != name:
        _fail(path.relative_to(root), "frontmatter name must match its directory")
    if not 40 <= len(fields["description"]) <= 1024:
        _fail(path.relative_to(root), "description must be 40–1024 characters")
    if set(name.split("-")) & HIGH_RISK_NAME_TERMS:
        _fail(path.relative_to(root), "high-risk Skill names are not allowed")
    if PLACEHOLDER_RE.search(text):
        _fail(path.relative_to(root), "placeholder text is not allowed")
    if PRIVATE_PATH_RE.search(text):
        _fail(path.relative_to(root), "machine-specific private paths are not allowed")
    folded = text.casefold()
    for phrase in AGENT_PHRASES:
        if phrase in folded:
            _fail(path.relative_to(root), f"Agent-facing phrase is not allowed: {phrase}")
    _information_rows(path.relative_to(root), body)
    _language_sections(path.relative_to(root), body)
    return name


def validate_repository(root: Path) -> dict[str, int]:
    root = root.resolve()
    skill_root = root / "skills"
    skill_paths = sorted(skill_root.glob("*/SKILL.md"))
    if not skill_paths:
        raise ValidationError("no Human Skills found")
    nested_skill_paths = sorted(skill_root.rglob("SKILL.md"))
    if nested_skill_paths != skill_paths:
        raise ValidationError("skills must use the flat skills/<slug>/SKILL.md layout")
    names = [_validate_skill(root, path) for path in skill_paths]
    if len(names) != len(set(names)):
        raise ValidationError("duplicate Skill names are not allowed")

    catalog_path = root / "SKILLS.md"
    if not catalog_path.is_file():
        raise ValidationError("SKILLS.md catalog is missing")
    catalog = catalog_path.read_text(encoding="utf-8")
    catalog_entries = re.findall(
        r"\(skills/([a-z0-9]+(?:-[a-z0-9]+)*)/SKILL\.md(?:#[^)]*)?\)",
        catalog,
    )
    expected = {path.parent.name for path in skill_paths}
    if len(catalog_entries) != len(set(catalog_entries)) or set(catalog_entries) != expected:
        raise ValidationError(
            f"catalog must link every Skill exactly once; expected={sorted(expected)} actual={sorted(catalog_entries)}"
        )

    markdown_files = [
        path
        for path in root.rglob("*.md")
        if not any(part in {".git", "dist", ".tmp"} for part in path.relative_to(root).parts)
    ]
    _validate_links(root, markdown_files)
    return {"skills": len(skill_paths), "catalog_entries": len(catalog_entries)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Skills for the Human Runtime.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        report = validate_repository(args.root)
    except (OSError, UnicodeDecodeError, ValidationError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        return 1
    print(
        f"human_skills={report['skills']} catalog_entries={report['catalog_entries']} status=valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
