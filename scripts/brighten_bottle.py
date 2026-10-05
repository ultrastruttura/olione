"""Slightly brighten only the bottle region; keep background as-is."""
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from rembg import remove

SRC = Path("assets/photos/original/prodotti-0.jpg")
OUT = Path("assets/photos/prodotti.jpg")


def main() -> None:
    # Start from current polished full-frame image if present, else original
    base_path = OUT if OUT.exists() else SRC
    base = Image.open(base_path).convert("RGB")
    # Prefer re-deriving from original so we don't stack brighten forever
    orig = Image.open(SRC).convert("RGB")
    w, h = orig.size
    cropped = orig.crop((int(w * 0.04), int(h * 0.02), int(w * 0.98), int(h * 0.99)))

    # Same light global polish as before (mild)
    from PIL import ImageOps

    polished = ImageOps.autocontrast(cropped, cutoff=0.6)
    polished = ImageEnhance.Brightness(polished).enhance(1.04)
    polished = ImageEnhance.Contrast(polished).enhance(1.08)
    polished = ImageEnhance.Color(polished).enhance(1.04)
    polished = ImageEnhance.Sharpness(polished).enhance(1.08)

    # Soft vignette (same as light polish)
    arr = np.array(polished).astype(np.float32)
    hh, ww = arr.shape[:2]
    yy, xx = np.ogrid[:hh, :ww]
    cy, cx = hh * 0.48, ww * 0.58
    ry, rx = hh * 0.75, ww * 0.7
    dist = ((yy - cy) / ry) ** 2 + ((xx - cx) / rx) ** 2
    vig = np.clip(1.0 - 0.12 * np.clip(dist - 0.35, 0, None), 0.88, 1.0)
    arr *= vig[..., None]
    polished = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    polished = polished.filter(ImageFilter.UnsharpMask(radius=1.2, percent=40, threshold=3))

    # Mask bottle only
    rgba = polished.convert("RGBA")
    cut = remove(rgba)
    alpha = np.array(cut)[:, :, 3].astype(np.float32) / 255.0
    # Soften mask edges
    mask_img = Image.fromarray((alpha * 255).astype(np.uint8), "L").filter(
        ImageFilter.GaussianBlur(1.2)
    )
    alpha = np.array(mask_img).astype(np.float32) / 255.0

    # Brighten bottle layer slightly
    bright = ImageEnhance.Brightness(polished).enhance(1.18)
    bright = ImageEnhance.Contrast(bright).enhance(1.05)

    base_arr = np.array(polished).astype(np.float32)
    bright_arr = np.array(bright).astype(np.float32)
    a = alpha[..., None]
    out = base_arr * (1 - a) + bright_arr * a
    final = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

    final.thumbnail((1400, 1860), Image.Resampling.LANCZOS)
    final.save(OUT, quality=92, optimize=True)
    print("saved", OUT, final.size)


if __name__ == "__main__":
    main()
