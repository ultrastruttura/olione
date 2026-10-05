from __future__ import annotations

import re
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path("assets/original-site")
OUT = Path("assets/photos/original")
OUT.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; OlioneRebuild/1.0)"}


def main() -> None:
    mapping = {
        "home-page.html": "home",
        "luliveto.html": "uliveto",
        "la-raccolta.html": "raccolta",
        "al-frantoio.html": "frantoio",
        "i-nostri-prodotti.html": "prodotti",
        "contatti.html": "contatti",
    }
    for html_name, slug in mapping.items():
        raw = (ROOT / html_name).read_text(encoding="utf-8")
        urls = re.findall(r"https://lh\d+-us\.googleusercontent\.com/sitesv-images-rt/[A-Za-z0-9_\-]+", raw)
        urls = sorted(set(urls))
        print(slug, "urls", len(urls))
        for i, url in enumerate(urls):
            # try common size suffixes used by google sites
            candidates = [
                url,
                url + "=s2048",
                url + "=w2400",
                url + "=s0",
            ]
            saved = False
            for cand in candidates:
                try:
                    req = Request(cand, headers=HEADERS)
                    data = urlopen(req, timeout=45).read()
                    if len(data) < 2000:
                        continue
                    # detect ext
                    ext = "jpg"
                    if data[:8] == b"\x89PNG\r\n\x1a\n":
                        ext = "png"
                    elif data[:4] == b"RIFF":
                        ext = "webp"
                    path = OUT / f"{slug}-{i}.{ext}"
                    path.write_bytes(data)
                    print("  saved", path.name, len(data), "via", cand[-20:])
                    saved = True
                    break
                except Exception as e:
                    print("  fail", cand[-30:], e)
            if not saved:
                print("  NO SAVE", url[:80])

        # Also search for more image hashes in page JSON
        hashes = re.findall(r"sitesv-images-rt/([A-Za-z0-9_\-]{20,})", raw)
        print("  hashes", len(set(hashes)))


if __name__ == "__main__":
    main()
