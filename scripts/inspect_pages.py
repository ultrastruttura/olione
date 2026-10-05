from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path

ROOT = Path("assets/original-site")


def main() -> None:
    for p in sorted(ROOT.glob("*.html")):
        raw = p.read_text(encoding="utf-8")
        print(f"\n==== {p.name} len={len(raw)}")
        for pat in [
            r"googleusercontent",
            r"lh3\.google",
            r"ggpht",
            r"drive\.google",
            r"ytimg",
            r"docs\.google",
            r"encrypted-tbn",
            r"sites\.google",
            r"www\.gstatic",
            r"beacons\.",
        ]:
            c = len(re.findall(pat, raw, re.I))
            if c:
                print(f"  {pat}: {c}")

        urls = set(re.findall(r"https?://[^\s\"'<>\\]+", raw))
        interesting = [
            u
            for u in urls
            if any(
                x in u.lower()
                for x in [
                    "image",
                    "img",
                    "photo",
                    "jpg",
                    "png",
                    "webp",
                    "googleusercontent",
                    "ggpht",
                    "lh3",
                    "drive",
                    "blob",
                    "proxy",
                ]
            )
        ]
        print(" interesting urls", len(interesting))
        for u in sorted(interesting)[:40]:
            print("  ", u[:180])

        srcs = re.findall(r"(?:src|data-src)=[\"']([^\"']+)[\"']", raw)
        print(" src attrs", len(srcs))
        for s in srcs[:30]:
            print("  ", s[:180])

        # Look for AF_initData / JSON blobs with image ids
        if "DOCS_modelChunk" in raw or "AF_initDataCallback" in raw:
            print(" has docs model chunks")
        for m in re.finditer(r"DOCS_modelChunk\s*=\s*(\{.*?\});", raw):
            print(" modelChunk len", len(m.group(1)))

        # Extract more text-looking content from JSON unicode escapes
        decoded = unescape(raw)
        for m in re.findall(r"\\u003c.*?\\u003e", decoded[:5000]):
            pass

        # Print unique meaningful texts again with unescape
        texts = []
        cleaned = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
        cleaned = re.sub(r"<style[\s\S]*?</style>", " ", cleaned, flags=re.I)
        cleaned = re.sub(r"<[^>]+>", "\n", cleaned)
        for line in cleaned.splitlines():
            t = unescape(" ".join(line.split()))
            if len(t) < 3:
                continue
            if t.startswith("{") or "Google" in t or "Skip to" in t or "cookie" in t.lower():
                continue
            if t not in texts:
                texts.append(t)
        print(" CONTENT:")
        for t in texts:
            print("  |", t)


if __name__ == "__main__":
    main()
