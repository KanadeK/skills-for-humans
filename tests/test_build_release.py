from __future__ import annotations

import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.build_release import build_release
from scripts.validate_skills import validate_repository
from test_validate_skills import write_repository


class BuildReleaseTests(unittest.TestCase):
    def test_build_is_deterministic_and_checksum_matches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            write_repository(root)
            (root / "VERSION").write_text("0.1.0\n", encoding="utf-8")
            (root / "README.md").write_text("# Test repository\n", encoding="utf-8")
            first = Path(directory) / "first"
            second = Path(directory) / "second"

            first_files = build_release(root, first)
            second_files = build_release(root, second)

            self.assertEqual(
                [path.name for path in first_files],
                ["skills-for-humans-v0.1.0.zip", "SHA256SUMS.txt"],
            )
            self.assertEqual(
                [hashlib.sha256(path.read_bytes()).hexdigest() for path in first_files],
                [hashlib.sha256(path.read_bytes()).hexdigest() for path in second_files],
            )
            expected_line = (
                hashlib.sha256(first_files[0].read_bytes()).hexdigest()
                + "  skills-for-humans-v0.1.0.zip\n"
            )
            self.assertEqual(first_files[1].read_text(encoding="utf-8"), expected_line)

    def test_archive_is_path_safe_clean_and_revalidates_after_extraction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            write_repository(root)
            (root / "VERSION").write_text("0.1.0\n", encoding="utf-8")
            (root / "README.md").write_text("# Test repository\r\n", encoding="utf-8")
            (root / ".env").write_text("NOT_A_REAL_SECRET=test\n", encoding="utf-8")
            (root / "ignored.pem").write_text("not a key\n", encoding="utf-8")
            (root / "dist").mkdir()
            (root / "dist" / "old.zip").write_bytes(b"old")
            output = Path(directory) / "release"

            archive, _checksums = build_release(root, output)

            with zipfile.ZipFile(archive) as package:
                infos = package.infolist()
                names = [info.filename for info in infos]
                self.assertTrue(names)
                self.assertTrue(
                    all(
                        name.startswith("skills-for-humans-0.1.0/")
                        and ".." not in Path(name).parts
                        for name in names
                    )
                )
                self.assertTrue(all(info.date_time == (2026, 1, 1, 0, 0, 0) for info in infos))
                self.assertFalse(any("/.git/" in name for name in names))
                self.assertFalse(any("/dist/" in name for name in names))
                self.assertFalse(any(name.endswith((".env", ".pem", ".key")) for name in names))

            extracted = Path(directory) / "extracted"
            with zipfile.ZipFile(archive) as package:
                package.extractall(extracted)
            report = validate_repository(extracted / "skills-for-humans-0.1.0")

        self.assertEqual(report["skills"], 1)


if __name__ == "__main__":
    unittest.main()
