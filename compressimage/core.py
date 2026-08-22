from PIL import Image

def compress(in_path, out_path, quality=70):
    im = Image.open(in_path)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im.save(out_path, "JPEG", quality=quality, optimize=True)
    return out_path
