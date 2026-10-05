from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path("assets/original-site")
OUT = Path("assets/photos/original")
OUT.mkdir(parents=True, exist_ok=True)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://www.olioevopredore.it/",
    "Accept": "*/*",
}


def fetch(url: str) -> bytes:
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=45) as r:
        return r.read()


def main() -> None:
    for p in sorted(ROOT.glob("*.html")):
        raw = p.read_text(encoding="utf-8")
        print("\n==", p.name)
        # Google Sites often nests image ids as long base64-ish tokens after sitesv-images
        tokens = set(re.findall(r"sitesv-images(?:-rt)?/([A-Za-z0-9_\-]{30,})", raw))
        # Also look for ["image", "..."] patterns
        tokens |= set(re.findall(r'"(AMxu72[A-Za-z0-9_\-]{20,})"', raw))
        tokens |= set(re.findall(r"(AMxu72[A-Za-z0-9_\-]{20,})", raw))
        print("tokens", len(tokens))
        for t in sorted(tokens):
            print(" ", t[:80])

        # Try page-published.json style endpoints used by some sites
        # Extract site id / page id if present
        for m in re.findall(r"/_/view/_/js[^\"']+", raw)[:1]:
            print(" js", m[:100])

        # Search for raw image urls with =w###
        for m in re.findall(r"https://[^\"'\\s]*sitesv-images[^\"'\\s]*", raw):
            print(" rawurl", m[:140])


if __name__ == "__main__":
    main()
