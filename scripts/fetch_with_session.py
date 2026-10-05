from __future__ import annotations

import http.cookiejar
import re
import urllib.request
from pathlib import Path

OUT = Path("assets/photos/original")
OUT.mkdir(parents=True, exist_ok=True)

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [
    (
        "User-Agent",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    ),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
]


def get(url: str) -> bytes:
    req = urllib.request.Request(url)
    with opener.open(req, timeout=60) as r:
        return r.read()


PAGES = {
    "raccolta": "https://www.olioevopredore.it/la-raccolta",
    "frantoio": "https://www.olioevopredore.it/al-frantoio",
    "contatti": "https://www.olioevopredore.it/contatti",
}


def main() -> None:
    for slug, page_url in PAGES.items():
        print("visit", page_url)
        html = get(page_url).decode("utf-8", "replace")
        text = html.replace("\\/", "/").replace("\\x3d", "=").replace("\\u003d", "=")
        # Capture longest possible token
        urls = re.findall(
            r"https://lh\d+-us\.googleusercontent\.com/sitesv-images-rt/[A-Za-z0-9_\-]+(?:[=]w\d+)?",
            text,
        )
        # Also from const imageUrl
        urls += re.findall(r"imageUrl\s*=\s*'([^']+)'", text)
        urls += re.findall(r'imageUrl\s*=\s*"([^"]+)"', text)
        urls = [u.replace("\\/", "/") for u in urls]
        urls = sorted(set(urls), key=len, reverse=True)
        print(" urls", len(urls))
        for u in urls[:3]:
            print(" ", u)
            base = u.split("=")[0]
            for cand in [base, u, base + "=w1600"]:
                try:
                    data = get(cand)
                    print("  got", len(data), cand[-50:])
                    if len(data) > 4000:
                        path = OUT / f"{slug}-0.jpg"
                        path.write_bytes(data)
                        print("  SAVED", path)
                        break
                except Exception as e:
                    print("  err", e)


if __name__ == "__main__":
    main()
