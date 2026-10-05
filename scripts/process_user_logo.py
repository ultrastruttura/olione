from pathlib import Path

import numpy as np
from PIL import Image

BRAND = Path("assets/brand")
BRAND.mkdir(parents=True, exist_ok=True)

src = Image.open("logo.png").convert("RGBA")
arr = np.array(src)
rgb = arr[:, :, :3].astype(np.float32)
lum = rgb.mean(axis=2)

# Transparent background: keep dark letter ink, drop near-white
# Soft alpha from darkness so serifs/antialias survive
alpha = np.clip((235 - lum) * (255 / 235), 0, 255).astype(np.uint8)
alpha[lum > 240] = 0

black = np.zeros_like(arr)
black[:, :, 0:3] = 0
black[:, :, 3] = alpha
Image.fromarray(black).save(BRAND / "logo.png")

white = np.zeros_like(arr)
white[:, :, 0:3] = 255
white[:, :, 3] = alpha
Image.fromarray(white).save(BRAND / "logo-white.png")
print("logo transparent", black.shape, "ink px", int((alpha > 20).sum()))

oliva = Image.open("oliva.png").convert("RGBA")
oa = np.array(oliva)
owhite = (oa[:, :, 0] > 245) & (oa[:, :, 1] > 245) & (oa[:, :, 2] > 245)
ores = oa.copy()
ores[owhite, 3] = 0
Image.fromarray(ores).save(BRAND / "oliva.png")
print("oliva", oliva.size)

for src_name, out_name, tw in [
    ("logo.png", "logo-sm.png", 240),
    ("logo-white.png", "logo-white-sm.png", 240),
]:
    im = Image.open(BRAND / src_name)
    # Add a little transparent padding so serifs never clip when scaled
    pad = 8
    canvas = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    canvas.paste(im, (pad, pad), im)
    canvas.thumbnail((tw, 120), Image.Resampling.LANCZOS)
    canvas.save(BRAND / out_name)
    print(out_name, canvas.size)
