#!/usr/bin/env python3
"""news-image-20261120 v2 entrypoint: copy the pre-composed front page
to the harness output directory.

The entry is a program that writes one image to /output/entry.png:
this module copies the bundled entry.png (a 1024x1024 newspaper
front page summing up Friday 20 November 2026 in 35 stories) to
$MAKEFUN_OUTPUT_DIR/entry.png and verifies the copy is byte-for-byte
identical, within the size limit, square and 1024x1024.

Only the Python standard library is used. No network access.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1 * 1024 * 1024
MAX_SIDE = 1024


def read_png_size(path):
    """Return the (width, height) of a PNG from its IHDR chunk.

    The PNG signature is 8 bytes; the IHDR chunk follows (4-byte
    length, 4-byte type "IHDR"), then width and height as big-endian
    uint32. Only the standard library is used.
    """
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The copy must be byte-for-byte: a truncated or altered copy
    # would still pass the size checks, so compare digests.
    if sha256_file(src) != sha256_file(dst):
        raise SystemExit("copy mismatch: entry.png did not copy cleanly")
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes (limit 1 MiB)")
    width, height = read_png_size(dst)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(
            f"entry.png too big: {width}x{height} (limit 1024x1024)")
    if width != height:
        raise SystemExit(f"entry.png is not square: {width}x{height}")
    # The bundled image is the whole entry: a zero-byte or truncated
    # copy would pass the size checks, so refuse anything implausibly
    # small as well as anything over the limit.
    if size < 100_000:
        raise SystemExit(f"entry.png implausibly small: {size} bytes")
    print(f"wrote {dst} ({size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
