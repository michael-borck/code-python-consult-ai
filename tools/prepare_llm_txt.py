#!/usr/bin/env python3
"""
Generate a clean text file from a Quarto book for LLM ingestion.

Reads _quarto.yml to discover all chapters and appendices in reading order,
strips frontmatter, HTML tags, images, Quarto directives, and other markup,
then writes a single llm.txt file in the project root.

Usage:
    python tools/prepare_llm_txt.py              # writes llm.txt
    python tools/prepare_llm_txt.py output.txt   # writes to output.txt
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")


def parse_quarto_chapters(quarto_path):
    """Extract ordered list of .qmd file paths from _quarto.yml."""
    with open(quarto_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    book = config.get("book", {})
    files = []

    def collect(items):
        for item in items:
            if isinstance(item, str):
                files.append(item)
            elif isinstance(item, dict):
                # A part with nested chapters
                if "chapters" in item:
                    collect(item["chapters"])

    chapters = book.get("chapters", [])
    collect(chapters)

    appendices = book.get("appendices", [])
    collect(appendices)

    return files


def strip_frontmatter(text):
    """Remove YAML frontmatter between --- markers."""
    return re.sub(r"\A---\n.*?\n---\n*", "", text, count=1, flags=re.DOTALL)


def strip_images(text):
    """Remove image references (![...](...){...})."""
    return re.sub(r"!\[.*?\]\(.*?\)(\{.*?\})?", "", text)


def strip_html_tags(text):
    """Remove HTML tags and comments."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    return text


def strip_mermaid(text):
    """Remove mermaid code blocks."""
    return re.sub(r"```\{mermaid\}.*?```", "", text, flags=re.DOTALL)


def strip_quarto_directives(text):
    """Remove Quarto-specific directives and attributes."""
    # Section cross-reference attributes {#sec-...}
    text = re.sub(r"\{#sec-[\w-]+(?:\s+[^}]*)?\}", "", text)
    # Figure/table attributes {fig-alt="..." ...}
    text = re.sub(r"\{[^}]*fig-alt[^}]*\}", "", text)
    # Generic Quarto attributes on headings {.unnumbered .unlisted}
    text = re.sub(r"\{\.[\w-]+(?:\s+\.[\w-]+)*\}", "", text)
    # Callout blocks ::: {.callout-...}
    text = re.sub(r"^:::\s*\{.*?\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^:::\s*$", "", text, flags=re.MULTILINE)
    # Cross-references like @sec-something or @fig-something
    text = re.sub(r"@(sec|fig|tbl)-[\w-]+", "", text)
    return text


def strip_code_blocks(text):
    """Remove fenced code blocks (```...```)."""
    return re.sub(r"```[^`]*?```", "", text, flags=re.DOTALL)


def strip_raw_blocks(text):
    """Remove raw content blocks like ```{=html}...```."""
    return re.sub(r"```\{=\w+\}.*?```", "", text, flags=re.DOTALL)


def clean(text):
    """Apply all cleaning steps."""
    text = strip_frontmatter(text)
    text = strip_raw_blocks(text)
    text = strip_mermaid(text)
    text = strip_code_blocks(text)
    text = strip_images(text)
    text = strip_html_tags(text)
    text = strip_quarto_directives(text)
    # Remove leftover markdown link syntax but keep link text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Remove bold/italic markers
    text = re.sub(r"\*{1,3}(.*?)\*{1,3}", r"\1", text)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    project_root = Path(__file__).resolve().parent.parent
    quarto_path = project_root / "_quarto.yml"

    if not quarto_path.exists():
        sys.exit(f"Not found: {quarto_path}")

    # Read book metadata
    with open(quarto_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    book = config.get("book", {})
    title = book.get("title", "Untitled")
    subtitle = book.get("subtitle", "")
    author = book.get("author", "Unknown")

    # Get chapter list
    chapter_files = parse_quarto_chapters(quarto_path)

    # Build output
    output_file = sys.argv[1] if len(sys.argv) > 1 else "llm.txt"
    output_path = project_root / output_file

    sections = []
    sections.append(title.upper())
    if subtitle:
        sections.append(subtitle)
    sections.append(f"By {author}")
    sections.append("=" * 60)

    found = 0
    skipped = 0
    for chapter_path in chapter_files:
        full_path = project_root / chapter_path
        if not full_path.exists():
            print(f"  Skipping (not found): {chapter_path}")
            skipped += 1
            continue
        text = full_path.read_text(encoding="utf-8")
        cleaned = clean(text)
        if cleaned:
            sections.append(f"\n{'=' * 60}")
            sections.append(f"SOURCE: {chapter_path}")
            sections.append(f"{'=' * 60}\n")
            sections.append(cleaned)
            found += 1

    output_path.write_text("\n".join(sections) + "\n", encoding="utf-8")

    word_count = sum(len(s.split()) for s in sections)
    print(f"Written to:  {output_path}")
    print(f"Word count:  ~{word_count:,}")
    print(f"Chapters:    {found} included, {skipped} skipped")


if __name__ == "__main__":
    main()
