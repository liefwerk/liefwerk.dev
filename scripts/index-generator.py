#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"

pages = []
for path in sorted(PAGES_DIR.glob("*.html")):
    if path.name == "index.html":
        continue
    html = path.read_text()
    title = re.search(r"<title>(.*?)</title>", html)
    pages.append({
        "href": f"/pages/{path.name}",
        "title": title.group(1) if title else path.stem,
    })

links = "\n".join(
    f'        <p><a class="link" href="{p["href"]}">{p["title"]}</a></p>'
    for p in pages
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../-.css">
    <link rel="icon" type="image/x-icon" href="../-.ico">
    <title>pages</title>
</head>

<body>
    <section>
{links}
    </section>
    <section class="or">
        <p>or <a class="link" href="/">go back home</a></p>
    </section>
<footer>
    &ndash; 2026
</footer>
</body>
</html>
"""

(PAGES_DIR / "index.html").write_text(html)
print(f"Wrote {PAGES_DIR / 'index.html'} ({len(pages)} pages)")