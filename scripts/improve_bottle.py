"""Cut out Olione bottle and composite on a clean product background."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from rembg import remove

SRC = Path("assets/photos/original/prodotti-0.jpg")
OUT = Path("assets/photos/prodotti.jpg")
OUT_PNG = Path("assets/photos/prodotti-cutout.png")


def main() -> None:
    src = Image.open(SRC).convert("RGBA")
    # Focus crop: bottle is center-right; keep wood bottom, reduce vase dominance
    w, h = src.size
    crop = src.crop((int(w * 0.18), int(h * 0.05), int(w * 0.92), int(h * 0.98)))

    cut = remove(crop)
    cut.save(OUT_PNG)

    arr = np.array(cut)
    alpha = arr[:, :, 3]
    ys, xs = np.where(alpha > 12)
    x1, x2 = int(xs.min()), int(xs.max())
    y1, y2 = int(ys.min()), int(ys.max())
    pad = 24
    bottle = cut.crop(
        (
            max(0, x1 - pad),
            max(0, y1 - pad),
            min(cut.width, x2 + pad),
            min(cut.height, y2 + pad),
        )
    )

    # Gentle product polish
    bottle = ImageEnhance.Contrast(bottle).enhance(1.08)
    bottle = ImageEnhance.Color(bottle).enhance(1.05)
    bottle = ImageEnhance.Sharpness(bottle).enhance(1.12)

    # Canvas — soft warm paper matching site, not peach wall
    cw, ch = 1200, 1600
    canvas = Image.new("RGB", (cw, ch), (245, 243, 238))
    # subtle vertical gradient
    grad = np.linspace(242, 252, ch, dtype=np.uint8)
    gimg = np.tile(grad[:, None], (1, cw))
    canvas = Image.fromarray(
        np.stack([gimg, gimg - 1, gimg - 4], axis=2).clip(0, 255).astype(np.uint8),
        "RGB",
    )

    # Scale bottle to sit elegantly
    max_h = int(ch * 0.78)
    bw, bh = bottle.size
    scale = max_h / bh
    nw, nh = int(bw * scale), int(bh * scale)
    bottle_r = bottle.resize((nw, nh), Image.Resampling.LANCZOS)

    # Soft contact shadow
    shadow = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    sx = (cw - nw) // 2 + 18
    sy = ch - int(ch * 0.11) - 40
    # elliptical shadow under bottle
    sh = Image.new("L", (int(nw * 0.72), 70), 0)
    from PIL import ImageDraw

    d = ImageDraw.Draw(sh)
    d.ellipse((0, 0, sh.width - 1, sh.height - 1), fill=110)
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    shadow.paste(
        Image.merge("RGBA", [Image.new("L", sh.size, 0)] * 3 + [sh]),
        (sx + int(nw * 0.14), sy + nh - 36),
        sh,
    )

    base = canvas.convert("RGBA")
    composed = Image.alpha_composite(base, shadow)
    px = (cw - nw) // 2
    py = ch - nh - int(ch * 0.10)
    composed.paste(bottle_r, (px, py), bottle_r)

    final = composed.convert("RGB")
    final = ImageEnhance.Contrast(final).enhance(1.03)
    final.save(OUT, quality=92, optimize=True)
    print("saved", OUT, final.size)


if __name__ == "__main__":
    main()
