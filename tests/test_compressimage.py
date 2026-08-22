import os, tempfile
from PIL import Image
from compressimage import core

def test_compress():
    d = tempfile.mkdtemp(); inp = os.path.join(d, "in.png"); out = os.path.join(d, "out.jpg")
    Image.new("RGB", (64, 64), (255, 0, 0)).save(inp)
    core.compress(inp, out, 50)
    assert os.path.exists(out) and os.path.getsize(out) > 0

def test_quality_smaller():
    d = tempfile.mkdtemp(); inp = os.path.join(d, "in.png"); o1 = os.path.join(d, "a.jpg"); o2 = os.path.join(d, "b.jpg")
    Image.new("RGB", (128, 128), (0, 255, 0)).save(inp)
    core.compress(inp, o1, 90); core.compress(inp, o2, 20)
    assert os.path.getsize(o2) <= os.path.getsize(o1)
