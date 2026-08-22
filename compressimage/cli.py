import argparse, os
from compressimage import core

def main(argv=None):
    p = argparse.ArgumentParser(prog="compressimage", description="Comprime imagens (Pillow).")
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--quality", type=int, default=70)
    args = p.parse_args(argv)
    core.compress(args.input, args.output, args.quality)
    before = os.path.getsize(args.input); after = os.path.getsize(args.output)
    print("antes=%d bytes depois=%d bytes" % (before, after))
    return 0
