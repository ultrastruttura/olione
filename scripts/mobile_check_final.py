from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path("assets/mobile-audit")
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto("http://127.0.0.1:5173/", wait_until="networkidle")

        page.click("[data-nav-toggle]")
        page.wait_for_timeout(200)
        page.click('[data-mobile-nav] a[href="#contatti"]')
        page.wait_for_timeout(700)
        page.screenshot(path=str(OUT / "iphone-contatti-anchor.png"))
        info = page.evaluate(
            """() => {
              const label = [...document.querySelectorAll('label span')]
                .find((s) => s.textContent.trim() === 'Nome');
              const header = document.querySelector('[data-header]');
              const section = document.querySelector('#contatti');
              const lr = label.getBoundingClientRect();
              const hr = header.getBoundingClientRect();
              const sr = section.getBoundingClientRect();
              return {
                labelTop: Math.round(lr.top),
                headerBottom: Math.round(hr.bottom),
                sectionTop: Math.round(sr.top),
                covered: lr.top < hr.bottom - 1,
              };
            }"""
        )
        print("anchor", info)

        page.goto("http://127.0.0.1:5173/", wait_until="networkidle")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / "iphone-footer.png"))

        page.goto("http://127.0.0.1:5173/", wait_until="networkidle")
        page.screenshot(path=str(OUT / "iphone-hero-final2.png"))
        brand = page.evaluate(
            """() => {
              const b = document.querySelector('.hero-brand').getBoundingClientRect();
              return {
                left: Math.round(b.left),
                right: Math.round(b.right),
                vw: window.innerWidth,
              };
            }"""
        )
        print("brand", brand)
        browser.close()


if __name__ == "__main__":
    main()
