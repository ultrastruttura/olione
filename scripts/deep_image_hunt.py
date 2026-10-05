from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen

ROOT = Path("assets/original-site")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; OlioneRebuild/1.0)"}


def main() -> None:
    for p in sorted(ROOT.glob("*.html")):
        raw = p.read_text(encoding="utf-8")
        print("\n==", p.name)
        # unescape common encodings
        variants = [raw, unquote(raw), raw.replace("\\u003d", "=").replace("\\u0026", "&").replace("\\/", "/")]
        found = set()
        for text in variants:
            for m in re.findall(r"https://[^\"'\\s<>]+", text):
                if any(k in m for k in ["sitesv-images", "googleusercontent.com/a/", "ggpht", "lh3", "lh7", "ci3", "ci4", "ci5", "ci6"]):
                    found.add(m.split("\\")[0])
            for m in re.findall(r"/sitesv-images-rt/[A-Za-z0-9_\-]+", text):
                found.add("https://lh7-us.googleusercontent.com" + m)
        print("found", len(found))
        for u in sorted(found):
            print(" ", u[:160])

        # Try fetching atari embed iframe if present - sometimes lists images
        embeds = re.findall(r"https://[0-9]+-atari-embeds\.googleusercontent\.com/[^\"'\\s]+", raw)
        print("embeds", embeds[:2])


if __name__ == "__main__":
    main()
