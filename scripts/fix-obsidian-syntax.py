#!/usr/bin/env python3
"""Pre-process Hugo content to translate Obsidian-specific markdown syntax
into Hextra-compatible HTML.

Fixes:
  1. Obsidian callouts:  > [!type] body  -> Hextra callout div
  2. Obsidian highlights: ==text==        -> <mark>text</mark>
  3. Obsidian comments:   %%text%%        -> <!-- text -->
  4. Obsidian tags:       #tag            -> <code>#tag</code>

Usage:
  # In-place (modifies source files)
  python3 fix-obsidian-syntax.py content/

  # To output dir (leaves source intact - recommended for CI)
  python3 fix-obsidian-syntax.py content/ --output build-content/

  # Dry run
  python3 fix-obsidian-syntax.py content/ --dry-run
"""

import re
import sys
from pathlib import Path


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

CALLOUT_STYLES = {
    "default": "hx:border-green-200 hx:bg-green-100 hx:text-green-900 "
    "hx:dark:border-green-200/30 hx:dark:bg-green-900/30 hx:dark:text-green-200",
    "info": "hx:border-blue-200 hx:bg-blue-100 hx:text-blue-900 "
    "hx:dark:border-blue-200/30 hx:dark:bg-blue-900/30 hx:dark:text-blue-200",
    "warning": "hx:border-amber-200 hx:bg-amber-100 hx:text-amber-900 "
    "hx:dark:border-amber-200/30 hx:dark:bg-amber-900/30 hx:dark:text-amber-200",
    "error": "hx:border-red-200 hx:bg-red-100 hx:text-red-900 "
    "hx:dark:border-red-200/30 hx:dark:bg-red-900/30 hx:dark:text-red-200",
    "important": "hx:border-purple-200 hx:bg-purple-100 hx:text-purple-900 "
    "hx:dark:border-purple-200/30 hx:dark:bg-purple-900/30 hx:dark:text-purple-200",
}

CALLOUT_EMOJIS = {
    "default": "\U0001f4a1",
    "info": "\u2139\ufe0f",
    "warning": "\u26a0\ufe0f",
    "error": "\U0001f6ab",
    "important": "\u2757",
}

CALLOUT_TPL = (
    '<div class="hx:overflow-x-auto hx:mt-6 hx:flex hx:rounded-lg '
    "hx:border hx:py-2 hx:ltr:pr-4 hx:rtl:pl-4 "
    "hx:contrast-more:border-current hx:contrast-more:dark:border-current "
    '{style}">\n'
    '  <div class="hx:ltr:pl-3 hx:ltr:pr-2 hx:rtl:pr-3 hx:rtl:pl-2">\n'
    '    <div class="hx:select-none hx:text-xl" '
    "style=\"font-family: 'Apple Color Emoji', 'Segoe UI Emoji', "
    "'Segoe UI Symbol';\">{emoji}</div>\n"
    "  </div>\n"
    '  <div class="hx:w-full hx:min-w-0 hx:leading-7">\n'
    '    <div class="hx:mt-6 hx:leading-7 hx:first:mt-0">\n'
    "{body}\n"
    "    </div>\n"
    "  </div>\n"
    "</div>"
)


def detect_callout_type(title):
    raw = title.strip("[]! ")
    lower = raw.lower()
    if lower in KNOWN_TITLES:
        return KNOWN_TITLES[lower], raw
    first = lower.split()[0] if lower.split() else ""
    if first in CALLOTYPE_MAP:
        return CALLOTYPE_MAP[first], raw
    return "default", raw


def transform_callouts(text):
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r"^>\s*(\[!.+?\])\s*$", lines[i])
        if m:
            htype, label = detect_callout_type(m.group(1))
            body = ["        <p><strong>{}</strong></p>".format(label)]
            j = i + 1
            while j < len(lines):
                bqm = re.match(r"^>\s?(.*)", lines[j])
                if not bqm:
                    break
                c = bqm.group(1).strip()
                if c:
                    c = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", c)
                    c = re.sub(r"\*(.+?)\*", r"<em>\1</em>", c)
                    c = re.sub(r"`(.+?)`", r"<code>\1</code>", c)
                    body.append("        <p>{}</p>".format(c))
                j += 1
            out.append(
                CALLOUT_TPL.format(
                    style=CALLOUT_STYLES.get(htype, CALLOUT_STYLES["default"]),
                    emoji=CALLOUT_EMOJIS.get(htype, CALLOUT_EMOJIS["default"]),
                    body="\n".join(body),
                )
            )
            i = j
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


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
