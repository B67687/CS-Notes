# Nacai's CS Notes

Computer science notes — math, hardware, networking, and systems engineering — built as a static site with [Hugo](https://gohugo.io/) + [Hextra](https://imfing.github.io/hextra/).

**Site:** https://b67687.github.io/CS-Notes/

## Quick start

```sh
hugo server -D
```

## Structure

| Path                       | What                                        |
| -------------------------- | ------------------------------------------- |
| `content/`                 | Markdown source (198 notes)                 |
| `scripts/convert-vault.py` | Converts Obsidian vault → Hugo content      |
| `layouts/`                 | Custom render hooks (KaTeX, callouts)       |
| `assets/katex/`            | KaTeX client-side renderer                  |
| `hugo-content/`            | Raw Obsidian vaults (source for conversion) |

## Build

```sh
pip install pyyaml   # if missing
python3 scripts/convert-vault.py
hugo
```

Output goes to `public/` — auto-deployed via GitHub Actions on push to `main`.

## License

The notes and site content are provided for reference.
