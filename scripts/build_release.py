from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.validate_skills import ValidationError, validate_repository


ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
EXCLUDED_PARTS = {".git", ".tmp", ".venv", "__pycache__", "dist"}
EXCLUDED_SUFFIXES = {".key", ".pem", ".pyc", ".pyo"}
VERSION_RE = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)")


def _version(root: Path) -> str:
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if VERSION_RE.fullmatch(version) is None:
        raise ValidationError("VERSION must contain one semantic version")
    return version


def _release_files(root: Path, output: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.resolve().is_relative_to(output):
            continue
        if path.is_symlink():
            raise ValidationError(f"release input contains a symlink: {relative.as_posix()}")
        if not path.is_file():
            continue
        if path.name.startswith(".env") or path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        files.append(path)
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def _portable_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if b"\0" in data:
        return data
    text = data.decode("utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def build_release(root: Path, output: Path) -> list[Path]:
    root = root.resolve()
    output = output.resolve()
    validate_repository(root)
    version = _version(root)
    output.mkdir(parents=True, exist_ok=True)

    archive_path = output / f"skills-for-humans-v{version}.zip"
    prefix = f"skills-for-humans-{version}"
    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for source in _release_files(root, output):
            relative = source.relative_to(root).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}", ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, _portable_bytes(source))

    checksum_path = output / "SHA256SUMS.txt"
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    checksum_path.write_text(
        f"{digest}  {archive_path.name}\n",
        encoding="utf-8",
        newline="\n",
    )
    return [archive_path, checksum_path]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the deterministic Skills for Humans release archive."
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args(argv)
    for artifact in build_release(args.root, args.output):
        print(artifact)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
