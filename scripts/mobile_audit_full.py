"""Full-page mobile screenshots + menu open check."""
from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "mobile-audit"
URL = "http://127.0.0.1:5173/"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(URL, wait_until="networkidle")
        page.screenshot(path=str(OUT / "iphone-14-full.png"), full_page=True)

        page.click("[data-nav-toggle]")
        page.wait_for_timeout(300)
        page.screenshot(path=str(OUT / "iphone-14-menu.png"), full_page=False)

        metrics = page.evaluate(
            """() => ({
              scrollWidth: document.documentElement.scrollWidth,
              clientWidth: document.documentElement.clientWidth,
              menuHidden: document.querySelector('[data-mobile-nav]').hidden,
              bodyNavOpen: document.body.classList.contains('nav-open'),
              headerOpen: document.querySelector('[data-header]').classList.contains('is-open'),
              menuHeight: Math.round(document.querySelector('[data-mobile-nav]').getBoundingClientRect().height),
            })"""
        )
        print(metrics)
        browser.close()


if __name__ == "__main__":
    main()
