#!/usr/bin/env python3
"""
Wraps the Claude-Artifact-style fragment index.html (no doctype/html/head/body —
the Artifact tool injects that at publish time) into a standalone, valid HTML
document for GitHub Pages, which serves the file as-is with no such wrapping.

Run this after editing index.html and before pushing to the hestrafiske repo.
"""
import sys

SRC = "src.fragment.html"
OUT = "index.html"

def main():
    with open(SRC, encoding="utf-8") as f:
        fragment = f.read()

    style_open = fragment.index("<style>")
    style_close = fragment.index("</style>") + len("</style>")

    head_meta = fragment[:style_open]
    style_block = fragment[style_open:style_close]
    body_content = fragment[style_close:]

    doc = (
        "<!doctype html>\n"
        '<html lang="sv">\n'
        "<head>\n"
        + head_meta +
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + style_block + "\n"
        "</head>\n"
        "<body>\n"
        + body_content +
        "\n</body>\n</html>\n"
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", OUT, len(doc), "bytes")

if __name__ == "__main__":
    main()
