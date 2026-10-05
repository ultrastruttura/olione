"""Headless mobile layout audit with Playwright if available, else basic checks."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "http://127.0.0.1:5173/"
OUT = ROOT / "assets" / "mobile-audit"
OUT.mkdir(parents=True, exist_ok=True)


def audit_with_playwright() -> dict:
    from playwright.sync_api import sync_playwright

    results = {"ok": True, "viewports": []}
    viewports = [
        {"name": "iphone-se", "width": 375, "height": 667},
        {"name": "iphone-14", "width": 390, "height": 844},
        {"name": "pixel-7", "width": 412, "height": 915},
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for vp in viewports:
            page = browser.new_page(viewport={"width": vp["width"], "height": vp["height"]})
            page.goto(URL, wait_until="networkidle", timeout=30000)
            # measure overflow
            metrics = page.evaluate(
                """() => {
                  const doc = document.documentElement;
                  const body = document.body;
                  const issues = [];
                  if (doc.scrollWidth > doc.clientWidth + 1) {
                    issues.push({type:'horizontal-overflow', scrollWidth: doc.scrollWidth, clientWidth: doc.clientWidth});
                  }
                  // find overflowing elements
                  const bad = [];
                  for (const el of document.querySelectorAll('body *')) {
                    const r = el.getBoundingClientRect();
                    if (r.width > 0 && (r.right > window.innerWidth + 2 || r.left < -2)) {
                      const cs = getComputedStyle(el);
                      if (cs.position === 'fixed' || cs.overflow === 'hidden') continue;
                      bad.push({
                        tag: el.tagName.toLowerCase(),
                        cls: (el.className || '').toString().slice(0,80),
                        left: Math.round(r.left),
                        right: Math.round(r.right),
                        w: Math.round(r.width)
                      });
                      if (bad.length >= 12) break;
                    }
                  }
                  if (bad.length) issues.push({type:'elements-out', items: bad});
                  // hero brand size
                  const brand = document.querySelector('.hero-brand');
                  const place = document.querySelector('.hero-place');
                  const header = document.querySelector('.site-header');
                  return {
                    issues,
                    brandH: brand ? Math.round(brand.getBoundingClientRect().height) : null,
                    placeW: place ? Math.round(place.getBoundingClientRect().width) : null,
                    placeScroll: place ? place.scrollWidth : null,
                    headerH: header ? Math.round(header.getBoundingClientRect().height) : null,
                    scrollWidth: doc.scrollWidth,
                    clientWidth: doc.clientWidth
                  };
                }"""
            )
            shot = OUT / f"{vp['name']}.png"
            page.screenshot(path=str(shot), full_page=False)
            entry = {"viewport": vp, "metrics": metrics, "shot": str(shot)}
            if metrics.get("issues"):
                results["ok"] = False
            results["viewports"].append(entry)
            page.close()
        browser.close()
    return results


def main() -> int:
    try:
        results = audit_with_playwright()
    except Exception as e:
        print("PLAYWRIGHT_UNAVAILABLE", e)
        return 2
    (OUT / "report.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    return 0 if results.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
