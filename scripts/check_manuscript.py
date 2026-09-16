#!/usr/bin/env python3
"""Regression checks for the revised manuscript (stdlib only).

Focuses on the defects found in the 2026-09-16 developmental audit:
the three listings that contradicted their own claims, dead links,
the chatbot version ladder, and build-configuration honesty.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RENDERED_CHAPTERS = {
    "chapters/after_vibe_coding.qmd": 1,
    "chapters/getting_started.qmd": 2,
    "chapters/values.qmd": 3,
    "chapters/variables.qmd": 4,
    "chapters/output.qmd": 5,
    "chapters/input.qmd": 6,
    "chapters/operators.qmd": 7,
    "chapters/using_functions.qmd": 8,
    "chapters/creating_functions.qmd": 9,
    "chapters/making_decisions.qmd": 10,
    "chapters/lists.qmd": 11,
    "chapters/going_loopy.qmd": 12,
    "chapters/strings.qmd": 13,
    "chapters/dictionaries.qmd": 14,
    "chapters/files.qmd": 15,
    "chapters/errors_and_exceptions.qmd": 16,
    "chapters/debugging.qmd": 17,
    "chapters/testing.qmd": 18,
    "chapters/modules_and_packages.qmd": 19,
    "chapters/orientating_your_objects.qmd": 20,
}

EXPECTED_VERSIONS = [f"v0.{n}" for n in range(2, 10)] + \
                    [f"v1.{n}" for n in range(0, 10)] + ["v2.0"]

STALE_LINKS = (
    "michaelborck.dev",
    "michaelborck.education",
)


def manuscript_files():
    files = ["index.qmd", "copyright.qmd"]
    files += sorted(RENDERED_CHAPTERS)
    files += ["acknowledgments.qmd", "about-author.qmd",
              "appendices/setting_up_python.qmd"]
    return files


def skip_appledouble(paths):
    return [p for p in paths if not p.name.startswith("._")]


def chapter_text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class ManuscriptChecks(unittest.TestCase):
    def test_no_stale_links(self):
        for name in manuscript_files():
            text = chapter_text(name)
            for target in STALE_LINKS:
                with self.subTest(file=name, target=target):
                    self.assertNotIn(target, text)

    def test_about_page_uses_verified_destinations(self):
        text = chapter_text("about-author.qmd")
        self.assertIn("https://github.com/michael-borck", text)
        self.assertIn("https://books.borck.education", text)

    def test_no_mermaid_diagrams(self):
        for name in manuscript_files():
            with self.subTest(file=name):
                self.assertNotIn("{mermaid}", chapter_text(name))

    def test_no_dangling_chapter_references(self):
        pattern = re.compile(r"[Cc]hapter (\d+)")
        for name in manuscript_files():
            text = chapter_text(name)
            for match in pattern.finditer(text):
                number = int(match.group(1))
                with self.subTest(file=name, ref=match.group(0)):
                    self.assertTrue(
                        1 <= number <= 20,
                        f"{match.group(0)} outside rendered numbering",
                    )

    def test_recent_words_uses_ordered_list(self):
        text = chapter_text("chapters/using_functions.qmd")
        self.assertNotIn("sorted(unique_words)", text)
        self.assertNotIn("unique_words = set()", text)
        self.assertIn("unique_words = []", text)
        self.assertIn("unique_words[-5:]", text)
        self.assertIn("not in unique_words", text)

    def test_debug_toggle_declares_global(self):
        text = chapter_text("chapters/debugging.qmd")
        self.assertIn("global debug_mode", text)

    def test_files_reference_card_reads_once(self):
        text = chapter_text("chapters/files.qmd")
        self.assertIn("pick ONE way", text)
        self.assertIn("f.readlines() returns []", text)

    def test_chatbot_version_ladder_is_complete(self):
        combined = "\n".join(chapter_text(name) for name in RENDERED_CHAPTERS)
        found = set(re.findall(r"\bv(\d\.\d)\b", combined))
        for version in EXPECTED_VERSIONS:
            with self.subTest(version=version):
                self.assertIn(version[1:], found)

    def test_download_links_are_site_absolute(self):
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        for target in ("code-python-consult-ai.pdf",
                       "code-python-consult-ai.epub"):
            with self.subTest(target=target):
                self.assertIn(f"href: /{target}", config)
                self.assertNotIn(f"href: {target}", config)

    def test_source_encoding_is_utf8(self):
        paths = skip_appledouble(sorted(ROOT.glob("**/*.qmd")))
        for path in paths:
            if "_book" in path.parts or "_print_source" in path.parts:
                continue
            with self.subTest(file=str(path)):
                path.read_text(encoding="utf-8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
