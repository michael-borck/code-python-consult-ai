#!/usr/bin/env python3
"""
Extract book chapters into individual clean markdown files for RAG ingestion.

Reads _quarto.yml to discover chapters in reading order, strips Quarto markup,
and outputs clean markdown files into rag-documents/.

Usage:
    python scripts/extract_rag_documents.py
"""

import re
import shutil
from pathlib import Path

try:
    import yaml
except ImportError:
    import sys
    sys.exit("PyYAML is required: pip install pyyaml")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "rag-documents"


def parse_quarto_config():
    """Read _quarto.yml and return config dict."""
    with open(PROJECT_ROOT / "_quarto.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_chapter_files(config):
    """Extract ordered list of .qmd file paths from config."""
    book = config.get("book", {})
    files = []

    def collect(items):
        for item in items:
            if isinstance(item, str):
                files.append(item)
            elif isinstance(item, dict):
                if "chapters" in item:
                    collect(item["chapters"])

    collect(book.get("chapters", []))
    collect(book.get("appendices", []))
    return files


def strip_frontmatter(text):
    """Remove YAML frontmatter, extracting title if present."""
    match = re.match(r"\A---\n(.*?)\n---\n*", text, flags=re.DOTALL)
    title = None
    if match:
        try:
            fm = yaml.safe_load(match.group(1))
            if isinstance(fm, dict):
                title = fm.get("title")
        except yaml.YAMLError:
            pass
        text = text[match.end():]
    return text, title


def clean_content(text):
    """Strip Quarto/HTML markup, return clean markdown."""
    # Raw blocks
    text = re.sub(r"```\{=\w+\}.*?```", "", text, flags=re.DOTALL)
    # Mermaid blocks
    text = re.sub(r"```\{mermaid\}.*?```", "", text, flags=re.DOTALL)
    # Code blocks
    text = re.sub(r"```[^`]*?```", "", text, flags=re.DOTALL)
    # Images
    text = re.sub(r"!\[.*?\]\(.*?\)(\{.*?\})?", "", text)
    # HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Quarto section attributes {#sec-...}
    text = re.sub(r"\{#sec-[\w-]+(?:\s+[^}]*)?\}", "", text)
    # Quarto class attributes {.unnumbered .unlisted}
    text = re.sub(r"\{\.[\w-]+(?:\s+\.[\w-]+)*\}", "", text)
    # Figure/table attributes
    text = re.sub(r"\{[^}]*fig-alt[^}]*\}", "", text)
    # Callout blocks
    text = re.sub(r"^:::\s*\{.*?\}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^:::\s*$", "", text, flags=re.MULTILINE)
    # Cross-references
    text = re.sub(r"@(sec|fig|tbl)-[\w-]+", "", text)
    # Quarto shortcodes {{< ... >}}
    text = re.sub(r"\{\{<.*?>}\}", "", text)
    # Keep link text, drop URLs
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Collapse blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    config = parse_quarto_config()
    book = config.get("book", {})
    book_title = book.get("title", "Untitled")

    chapter_files = collect_chapter_files(config)

    # Clean output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    extracted = 0
    skipped = 0

    for chapter_path in chapter_files:
        full_path = PROJECT_ROOT / chapter_path
        if not full_path.exists():
            print(f"  Skipping (not found): {chapter_path}")
            skipped += 1
            continue

        raw = full_path.read_text(encoding="utf-8")
        body, fm_title = strip_frontmatter(raw)
        cleaned = clean_content(body)

        if not cleaned:
            skipped += 1
            continue

        # Determine output subdirectory
        parts = Path(chapter_path).parts
        if len(parts) > 1:
            subdir = parts[0]  # chapters/, appendices/, projects/, etc.
        else:
            subdir = "book-info"

        out_dir = OUTPUT_DIR / subdir
        out_dir.mkdir(parents=True, exist_ok=True)

        # Build output filename
        stem = Path(chapter_path).stem
        out_file = out_dir / f"{stem}.md"

        # Add source preamble and ensure H1 title
        lines = []
        lines.append(f"> This content is from *{chapter_path}*, part of *{book_title}*.\n")

        # Check if content already starts with an H1
        if not re.match(r"^#\s+", cleaned):
            title = fm_title or stem.replace("-", " ").replace("_", " ").title()
            lines.append(f"# {title}\n")

        lines.append(cleaned)

        out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        extracted += 1

    print(f"Book:       {book_title}")
    print(f"Output:     {OUTPUT_DIR}")
    print(f"Extracted:  {extracted} files")
    print(f"Skipped:    {skipped} files")


if __name__ == "__main__":
    main()
