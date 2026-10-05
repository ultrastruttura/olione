"""Light polish on original bottle photo — keep background, no cutout."""
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

SRC = Path("assets/photos/original/prodotti-0.jpg")
OUT = Path("assets/photos/prodotti.jpg")


def main() -> None:
    im = Image.open(SRC).convert("RGB")

    # Mild crop: less empty top, keep vase + bottle composition
    w, h = im.size
    im = im.crop((int(w * 0.04), int(h * 0.02), int(w * 0.98), int(h * 0.99)))

    # Gentle auto-contrast (very mild)
    im = ImageOps.autocontrast(im, cutoff=0.6)

    # Lighten a touch + slight contrast/color
    im = ImageEnhance.Brightness(im).enhance(1.04)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageEnhance.Color(im).enhance(1.04)
    im = ImageEnhance.Sharpness(im).enhance(1.08)

    # Soft vignette to calm peach wall without looking fake
    arr = np.array(im).astype(np.float32)
    hh, ww = arr.shape[:2]
    yy, xx = np.ogrid[:hh, :ww]
    cy, cx = hh * 0.48, ww * 0.58  # bias toward bottle
    ry, rx = hh * 0.75, ww * 0.7
    dist = ((yy - cy) / ry) ** 2 + ((xx - cx) / rx) ** 2
    vig = np.clip(1.0 - 0.12 * np.clip(dist - 0.35, 0, None), 0.88, 1.0)
    arr *= vig[..., None]
    im = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

    # Very light unsharp (subtle)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=40, threshold=3))

    im.thumbnail((1400, 1860), Image.Resampling.LANCZOS)
    im.save(OUT, quality=92, optimize=True)
    print("saved", OUT, im.size)


if __name__ == "__main__":
    main()
