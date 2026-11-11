import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class ArtifactTests(unittest.TestCase):
    def test_json_artifacts_parse(self):
        for path in (ROOT / "schemas").glob("*.json"):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))
        for path in (ROOT / "templates/messages").glob("*.json"):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))

    def test_skill_has_frontmatter_and_safety(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: whatsmyerror\n"))
        for phrase in ("read-only", "explicit approval", "Retry-After", "untrusted"):
            self.assertIn(phrase, text)

    def test_fixtures_exist(self):
        expected = ("js/unchecked_fetch.js", "python/swallowed.py", "php/raw_exception.php", "dart/dio_request.dart")
        for relative in expected:
            with self.subTest(fixture=relative):
                self.assertTrue((ROOT / "tests/fixtures" / relative).is_file())


if __name__ == "__main__":
    unittest.main()
