import os

ROOT = r"C:\Users\Namikaz\Sync-Namikaz\Hugo\Computing-Notes\content"


def has_yaml_front_matter(lines):
    return lines[0].strip() == "---"


def inject_front_matter(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not has_yaml_front_matter(lines):
        title = os.path.splitext(os.path.basename(path))[0]
        front_matter = [
            "---\n",
            f'title: "{title}"\n',
            "date: 2025-11-08\n",
            "draft: false\n",
            "---\n\n",
        ]
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(front_matter + lines)
        print(f"✅ Injected front matter into: {path}")
    else:
        print(f"🟢 Already valid: {path}")


for root, _, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".md"):
            inject_front_matter(os.path.join(root, file))
