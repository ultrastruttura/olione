from __future__ import annotations

import re
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path("assets/original-site")
OUT = Path("assets/photos/original")
OUT.mkdir(parents=True, exist_ok=True)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://www.olioevopredore.it/",
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
}

PAGES = {
    "home-page.html": "home",
    "luliveto.html": "uliveto",
    "la-raccolta.html": "raccolta",
    "al-frantoio.html": "frantoio",
    "i-nostri-prodotti.html": "prodotti",
    "contatti.html": "contatti",
}


def main() -> None:
    for html_name, slug in PAGES.items():
        raw = (ROOT / html_name).read_text(encoding="utf-8")
        # unescape js escaped urls
        text = raw.replace("\\/", "/").replace("\\x3d", "=").replace("\\u003d", "=")
        urls = set(
            re.findall(
                r"https://lh\d+-us\.googleusercontent\.com/sitesv-images-rt/[A-Za-z0-9_\-]+(?:=w\d+)?",
                text,
            )
        )
        print(slug, "found", len(urls))
        for i, url in enumerate(sorted(urls)):
            # Prefer a practical web size
            base = url.split("=")[0]
            candidates = [f"{base}=w2400", f"{base}=w1600", url, base]
            for cand in candidates:
                try:
                    req = Request(cand, headers=HEADERS)
                    data = urlopen(req, timeout=60).read()
                    if len(data) < 4000:
                        continue
                    ext = "jpg"
                    if data[:8] == b"\x89PNG\r\n\x1a\n":
                        ext = "png"
                    path = OUT / f"{slug}-{i}.{ext}"
                    path.write_bytes(data)
                    print("  OK", path.name, len(data), cand[-30:])
                    break
                except Exception as e:
                    print("  fail", cand[-40:], e)
            else:
                print("  NO", url[:100])


if __name__ == "__main__":
    main()
