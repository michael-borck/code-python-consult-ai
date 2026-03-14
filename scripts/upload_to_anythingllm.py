#!/usr/bin/env python3
"""
Upload extracted RAG documents to AnythingLLM and embed them in a workspace.

Usage:
    python scripts/upload_to_anythingllm.py --create-workspace
    python scripts/upload_to_anythingllm.py --dry-run
    python scripts/upload_to_anythingllm.py --workspace my-slug

Set ANYTHINGLLM_API_KEY environment variable or use --api-key flag.
"""

import argparse
import os
import sys
import time
from pathlib import Path

try:
    import requests
    import yaml
except ImportError:
    sys.exit("Required: pip install requests pyyaml")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAG_DIR = PROJECT_ROOT / "rag-documents"


def parse_quarto_config():
    with open(PROJECT_ROOT / "_quarto.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_workspace_slug(config):
    """Derive a workspace slug from the book title."""
    title = config.get("book", {}).get("title", "untitled")
    slug = title.lower()
    slug = slug.replace(",", "").replace(":", "").replace("'", "")
    slug = "-".join(slug.split())
    return slug


def get_system_prompt(config):
    """Generate a system prompt scoping the bot to this book."""
    book = config.get("book", {})
    title = book.get("title", "this book")
    author = book.get("author", "the author")
    return (
        f"You are a helpful assistant for the book '{title}' by {author}. "
        f"Answer questions only based on the content provided from this book. "
        f"If a question is not covered by the book's content, politely say so "
        f"and suggest the user consult the book directly. "
        f"Be concise and cite specific chapters or sections when possible."
    )


def list_workspaces(base_url, headers):
    resp = requests.get(f"{base_url}/api/v1/workspaces", headers=headers)
    resp.raise_for_status()
    return resp.json().get("workspaces", [])


def create_workspace(base_url, headers, slug, config):
    system_prompt = get_system_prompt(config)
    book_title = config.get("book", {}).get("title", slug)
    payload = {
        "name": book_title,
        "slug": slug,
        "chatProvider": "anthropic",
        "chatModel": "claude-haiku-4-5-20251001",
        "openAiTemp": 0.5,
        "chatPrompt": system_prompt,
        "queryRefusalResponse": (
            "I can only answer questions about the book's content. "
            "This question doesn't appear to be covered in the material I have access to."
        ),
        "similarityThreshold": 0.25,
        "topN": 4,
    }
    resp = requests.post(f"{base_url}/api/v1/workspace/new", headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json().get("workspace", {})


def upload_file(base_url, headers, filepath):
    with open(filepath, "rb") as f:
        resp = requests.post(
            f"{base_url}/api/v1/document/upload",
            headers={"Authorization": headers["Authorization"]},
            files={"file": (filepath.name, f, "text/markdown")},
        )
    resp.raise_for_status()
    data = resp.json()
    if not data.get("success"):
        return None
    documents = data.get("documents", [])
    if documents:
        return documents[0].get("location")
    return None


def embed_documents(base_url, headers, slug, locations):
    payload = {"adds": locations, "deletes": []}
    resp = requests.post(
        f"{base_url}/api/v1/workspace/{slug}/update-embeddings",
        headers=headers,
        json=payload,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Upload RAG docs to AnythingLLM")
    parser.add_argument("--api-key", default=os.environ.get("ANYTHINGLLM_API_KEY"))
    parser.add_argument("--base-url", default="https://chat.eduserver.au")
    parser.add_argument("--workspace", help="Workspace slug (auto-derived if not set)")
    parser.add_argument("--create-workspace", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.api_key and not args.dry_run:
        sys.exit("Set ANYTHINGLLM_API_KEY or use --api-key flag")

    config = parse_quarto_config()
    slug = args.workspace or get_workspace_slug(config)
    book_title = config.get("book", {}).get("title", slug)

    print(f"Book:       {book_title}")
    print(f"Workspace:  {slug}")
    print(f"Server:     {args.base_url}")

    # Collect files to upload
    if not RAG_DIR.exists():
        sys.exit(f"No rag-documents/ found. Run extract_rag_documents.py first.")

    md_files = sorted(RAG_DIR.rglob("*.md"))
    print(f"Documents:  {len(md_files)}")

    if args.dry_run:
        print("\n[DRY RUN] Would upload:")
        for f in md_files:
            print(f"  {f.relative_to(PROJECT_ROOT)}")
        return

    headers = {
        "Authorization": f"Bearer {args.api_key}",
        "Content-Type": "application/json",
    }

    # Find or create workspace
    if args.create_workspace:
        print(f"\nCreating workspace '{slug}'...")
        try:
            ws = create_workspace(args.base_url, headers, slug, config)
            print(f"  Created: {ws.get('name', slug)}")
        except requests.HTTPError as e:
            print(f"  Error creating workspace: {e}")
            print("  Attempting to use existing workspace...")
    else:
        workspaces = list_workspaces(args.base_url, headers)
        found = [w for w in workspaces if w.get("slug") == slug]
        if not found:
            sys.exit(f"Workspace '{slug}' not found. Use --create-workspace to create it.")
        print(f"  Using existing workspace: {found[0].get('name')}")

    # Upload files
    print(f"\nUploading {len(md_files)} documents...")
    locations = []
    failures = []

    for filepath in md_files:
        rel = filepath.relative_to(PROJECT_ROOT)
        try:
            location = upload_file(args.base_url, headers, filepath)
            if location:
                locations.append(location)
                print(f"  OK: {rel}")
            else:
                failures.append(rel)
                print(f"  FAIL (no location): {rel}")
        except requests.HTTPError as e:
            failures.append(rel)
            print(f"  FAIL: {rel} — {e}")
        time.sleep(0.2)

    print(f"\nUploaded: {len(locations)} / {len(md_files)}")

    if failures:
        print(f"Failed:   {len(failures)}")
        for f in failures:
            print(f"  - {f}")

    # Embed documents
    if locations:
        print(f"\nEmbedding {len(locations)} documents into workspace '{slug}'...")
        try:
            result = embed_documents(args.base_url, headers, slug, locations)
            print(f"  Embedding complete: {result}")
        except requests.HTTPError as e:
            print(f"  Embedding failed: {e}")
            print("\n  Document locations for manual embedding:")
            for loc in locations:
                print(f"    {loc}")


if __name__ == "__main__":
    main()
