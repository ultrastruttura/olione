"""Scrape olioevopredore.it pages for text, links, and images."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; OlioneRebuild/1.0)"}
BASE = "https://www.olioevopredore.it"
OUT = Path("assets/original-site")
OUT.mkdir(parents=True, exist_ok=True)


def fetch(url: str) -> str:
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


def extract_links(html: str) -> list[str]:
    found = set()
    for m in re.findall(r'https://www\.olioevopredore\.it(/[a-zA-Z0-9\-_/]*)', html):
        found.add(m.rstrip("/") or "/")
    for m in re.findall(r'href=["\'](/[a-zA-Z0-9\-_/]*)["\']', html):
        found.add(m.rstrip("/") or "/")
    return sorted(found)


def extract_images(html: str) -> list[str]:
    imgs = set()
    for m in re.findall(r'https://static\.wixstatic\.com/media/[^"\'\\\s\)]+', html):
        imgs.add(m.split("/v1/")[0] if "/v1/" in m else m)
    # also encoded urls
    for m in re.findall(r"static\.wixstatic\.com%2Fmedia%2F[^\"'\\s]+", html):
        from urllib.parse import unquote

        u = "https://" + unquote(m)
        imgs.add(u.split("/v1/")[0] if "/v1/" in u else u)
    return sorted(imgs)


def extract_text_blobs(html: str) -> list[str]:
    # Prefer JSON data blobs used by Wix
    texts: list[str] = []
    # visible text between tags, rough
    cleaned = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    cleaned = re.sub(r"<style[\s\S]*?</style>", " ", cleaned, flags=re.I)
    cleaned = re.sub(r"<[^>]+>", "\n", cleaned)
    for line in cleaned.splitlines():
        t = " ".join(line.split())
        if len(t) < 2:
            continue
        if t.startswith("{") or "window." in t:
            continue
        texts.append(t)

    # Also pull quoted Italian sentences from raw html
    for m in re.findall(r'"(?:text|title|label|content)"\s*:\s*"([^"]{8,})"', html):
        t = " ".join(m.replace("\\n", " ").split())
        if t and t not in texts:
            texts.append(t)
    return texts


def main() -> None:
    seed_paths = [
        "/",
        "/home-page",
        "/i-nostri-prodotti",
        "/contatti",
        "/chi-siamo",
        "/il-territorio",
        "/territorio",
        "/azienda",
        "/l-azienda",
        "/la-nostra-storia",
        "/gallery",
        "/galleria",
        "/dove-siamo",
        "/oliveto",
        "/produzione",
    ]

    discovered: set[str] = set(seed_paths)
    pages: dict[str, dict] = {}

    # expand from home
    try:
        home_html = fetch(BASE + "/")
        (OUT / "home-raw.html").write_text(home_html, encoding="utf-8")
        for p in extract_links(home_html):
            discovered.add(p)
    except Exception as e:
        print("home fail", e)

    for path in sorted(discovered):
        url = BASE + ("" if path == "/" else path)
        try:
            html = fetch(url)
        except Exception as e:
            print("SKIP", path, e)
            continue
        imgs = extract_images(html)
        texts = extract_text_blobs(html)
        pages[path] = {
            "url": url,
            "len": len(html),
            "images": imgs,
            "texts": texts,
            "links": extract_links(html),
        }
        safe = path.strip("/").replace("/", "_") or "root"
        (OUT / f"{safe}.html").write_text(html, encoding="utf-8")
        print(f"OK {path} imgs={len(imgs)} texts={len(texts)}")
        for p in pages[path]["links"]:
            discovered.add(p)

    # second pass for newly discovered
    for path in sorted(discovered - set(pages)):
        url = BASE + ("" if path == "/" else path)
        try:
            html = fetch(url)
        except Exception as e:
            print("SKIP2", path, e)
            continue
        pages[path] = {
            "url": url,
            "len": len(html),
            "images": extract_images(html),
            "texts": extract_text_blobs(html),
            "links": extract_links(html),
        }
        safe = path.strip("/").replace("/", "_") or "root"
        (OUT / f"{safe}.html").write_text(html, encoding="utf-8")
        print(f"OK2 {path} imgs={len(pages[path]['images'])} texts={len(pages[path]['texts'])}")

    summary = {
        "pages": {
            k: {
                "url": v["url"],
                "images": v["images"],
                "texts": v["texts"][:200],
                "text_count": len(v["texts"]),
            }
            for k, v in pages.items()
        }
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print("DONE pages", len(pages))


if __name__ == "__main__":
    main()
