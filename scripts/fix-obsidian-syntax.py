#!/usr/bin/env python3
"""Pre-process Hugo content to translate Obsidian-specific markdown syntax
into Hextra-compatible shortcodes.

Fixes:
  1. Obsidian callouts:  > [!type] body  -> Hextra callout shortcodes
     Supports nesting:   > > [!type] inside outer callouts
     Supports lists, inline formatting inside callouts
  2. Obsidian highlights: ==text==        -> <mark>text</mark>
  3. Obsidian comments:   %%text%%        -> <!-- text -->
  4. Obsidian tags:       #tag            -> <code>#tag</code>

Usage:
  python3 fix-obsidian-syntax.py content/ --output build-content/
  python3 fix-obsidian-syntax.py content/ --dry-run
"""

import re
import sys
from pathlib import Path


# --- Obsidian -> Hextra callout type mapping ---

CALLOTYPE_MAP = {
    "note": "default",
    "info": "info",
    "tip": "info",
    "hint": "info",
    "important": "important",
    "success": "default",
    "check": "default",
    "done": "default",
    "question": "info",
    "help": "info",
    "faq": "info",
    "warning": "warning",
    "caution": "warning",
    "attention": "warning",
    "failure": "error",
    "fail": "error",
    "missing": "error",
    "danger": "error",
    "error": "error",
    "bug": "error",
    "example": "info",
    "quote": "default",
    "cite": "default",
    "why": "info",
    "fun": "default",
    "audit": "warning",
}

KNOWN_TITLES = {
    "why we care": "info",
    "why we invented this": "info",
    "why this matters": "info",
    "why it works": "info",
    "fun fact": "default",
    "audit trigger": "warning",
    "audit flag": "warning",
}

CALLOUT_EMOJIS = {
    "default": "\U0001f4a1",
    "info": "\u2139\ufe0f",
    "warning": "\u26a0\ufe0f",
    "error": "\U0001f6ab",
    "important": "\u2757",
}


def detect_callout_type(raw_title):
    """Map Obsidian [!title] to (Hextra_type, display_label)."""
    raw = raw_title.strip("[]! ")
    lower = raw.lower()
    if lower in KNOWN_TITLES:
        return KNOWN_TITLES[lower], raw
    first = lower.split()[0] if lower.split() else ""
    if first in CALLOTYPE_MAP:
        return CALLOTYPE_MAP[first], raw
    return "default", raw


# --- Callout transform (stack-based, supports nesting) ---

CALLOUT_RE = re.compile(r"^(>*)>\s*(\[!.+?\])\s*$")
BLOCKQUOTE_RE = re.compile(r"^(>+)\s?(.*)")


def transform_callouts(text):
    """Transform Obsidian callouts to Hugo shortcodes, preserving nesting.

    Uses a stack to track open callouts by blockquote depth.
    This correctly handles:
      > [!outer]          -> opens callout at depth 0
      > > [!inner]        -> opens callout at depth 1 (nested)
      > > content         -> inner callout content
      > outer content     -> outer callout content
    """
    lines = text.split("\n")
    result = []
    stack = []  # [(depth, hextra_type, title), ...]

    i = 0
    while i < len(lines):
        line = lines[i]
        cm = CALLOUT_RE.match(line)

        if cm:
            depth = len(cm.group(1))
            htype, label = detect_callout_type(cm.group(2))

            # Close any open callouts at >= this depth
            while stack and stack[-1][0] >= depth:
                result.append("{{< /callout >}}")
                stack.pop()

            # Open new callout
            emoji = CALLOUT_EMOJIS.get(htype, CALLOUT_EMOJIS["default"])
            result.append(
                '{{{{< callout type="{}" emoji="{}" >}}}}'.format(htype, emoji)
            )
            result.append("**{}**".format(label))
            stack.append((depth, htype, label))
            i += 1
            continue

        # Not a callout line — check blockquote level
        bqm = BLOCKQUOTE_RE.match(line)
        if bqm:
            current_depth = len(bqm.group(1))
            content = bqm.group(2)

            # Close callouts that are at >= this blockquote depth
            while stack and stack[-1][0] >= current_depth:
                result.append("{{< /callout >}}")
                stack.pop()

            result.append(content)
        else:
            # Non-blockquote line — close ALL open callouts
            while stack:
                result.append("{{< /callout >}}")
                stack.pop()
            result.append(line)

        i += 1

    # Close any remaining open callouts
    while stack:
        result.append("{{< /callout >}}")
        stack.pop()

    return "\n".join(result)


# --- Other transforms ---


def transform_highlights(text):
    return re.sub(r"==(.+?)==", r"<mark>\1</mark>", text)


def transform_comments(text):
    text = re.sub(r"%%(.+?)%%", r"<!-- \1 -->", text)
    text = re.sub(
        r"^%%\s*$\n?(.*?)\n?^%%\s*$",
        r"<!-- \1 -->",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return text


def transform_tags(text):
    result = []
    in_code = False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            result.append(line)
            continue
        if in_code or s.startswith("#") or s.startswith("---") or s.startswith(">"):
            result.append(line)
            continue
        line = re.sub(r"(?<!\w)#([a-zA-Z][a-zA-Z0-9_/-]+)", r"<code>#\1</code>", line)
        result.append(line)
    return "\n".join(result)


# --- File processing ---


def process_file(filepath, source_root, output_dir=None, dry_run=False):
    if output_dir:
        rel = filepath.relative_to(source_root)
        dest = output_dir / rel
    else:
        dest = filepath

    original = filepath.read_text(encoding="utf-8")
    text = original
    text = transform_callouts(text)
    text = transform_highlights(text)
    text = transform_comments(text)
    text = transform_tags(text)

    if text == original and not output_dir:
        return False

    if dry_run:
        print("  Would process: {}".format(filepath))
        return True

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    if output_dir:
        print("  {}".format(rel))
    else:
        print("  {}".format(filepath))
    return True


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]

    if not args:
        print("Usage: fix-obsidian-syntax.py <source-dir> [--output <dir>]")
        sys.exit(1)

    source = Path(args[0]).resolve()
    output = None
    if "--output" in args:
        idx = args.index("--output")
        output = Path(args[idx + 1]).resolve()

    if not source.exists():
        print("ERROR: source not found: {}".format(source))
        sys.exit(1)

    files = sorted(source.rglob("*.md"))
    changed = 0
    for f in files:
        if process_file(f, source, output, dry_run):
            changed += 1

    label = "Would process" if dry_run else "Processed"
    print("\n{} {} of {} files.".format(label, changed, len(files)))


if __name__ == "__main__":
    main()
