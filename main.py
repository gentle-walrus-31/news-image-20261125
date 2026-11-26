#!/usr/bin/env python3
"""Tariff Storm -- World News, 25 November 2026.

Entrypoint for the news-image-20261125 bounty. It takes the bundled
``front-page.png`` (the finished newspaper front page for 25 November
2026) and installs it as ``<output-dir>/entry.png``, after proving the
bundled file is exactly the image this entry was built from.

Facts of the bundled image, so a swapped or damaged file is caught:
  file:   front-page.png
  size:   144890 bytes
  sha256: cd633414c234ab6c6bdce297d2d11a9766ca4a30d9f9b2e536229ad65b76f1cb
  pixels: 1024 x 1024

Usage:
  python3 main.py [--check] [output-dir]

  --check     only validate the bundled image, write nothing.
  output-dir  directory receiving entry.png (default: /output).
"""

import hashlib
import os
import struct
import sys

EXPECTED_SHA256 = "cd633414c234ab6c6bdce297d2d11a9766ca4a30d9f9b2e536229ad65b76f1cb"
EXPECTED_BYTES = 144890
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
IMAGE_NAME = "front-page.png"


def fail(message):
    """Print an error and stop with a non-zero exit code."""
    print("main.py: error: %s" % message, file=sys.stderr)
    raise SystemExit(1)


def bundled_path():
    """Absolute path of the image shipped next to this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def read_bundled():
    """Read the bundled image, or stop if it is missing."""
    path = bundled_path()
    if not os.path.isfile(path):
        fail("bundled image not found: %s" % path)
    with open(path, "rb") as handle:
        return handle.read()


def check_png(data):
    """Validate the PNG bytes; stop with a clear reason on any mismatch."""
    if len(data) > MAX_BYTES:
        fail("image is %d bytes, over the 1 MiB limit" % len(data))
    if len(data) != EXPECTED_BYTES:
        fail("image is %d bytes, expected %d" % (len(data), EXPECTED_BYTES))
    if data[:8] != PNG_MAGIC:
        fail("bad PNG signature, not a PNG file")
    if len(data) < 33:
        fail("image too short to hold an IHDR chunk")
    if data[12:16] != b"IHDR":
        fail("first chunk is not IHDR")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail("image is %dx%d, expected %dx%d"
             % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        fail("sha256 mismatch: got %s" % digest)
    return width, height, digest


def write_entry(data, outdir, digest):
    """Write the image byte-for-byte and verify the written copy.

    ``digest`` is the sha256 check_png already computed for the source
    bytes, so the source is not hashed a second time here.
    """
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)
    with open(target, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != digest:
        fail("written file failed its sha256 round-trip check")
    return target


def usage_error():
    print(__doc__, file=sys.stderr)
    print("main.py: usage: python3 main.py [--check] [output-dir]",
          file=sys.stderr)
    raise SystemExit(2)


def main(argv):
    check_only = False
    outdir = "/output"
    rest = []
    for arg in argv[1:]:
        if arg == "--check":
            check_only = True
        elif arg.startswith("-"):
            usage_error()
        else:
            rest.append(arg)
    if len(rest) > 1:
        usage_error()
    if rest:
        outdir = rest[0]

    data = read_bundled()
    width, height, digest = check_png(data)
    if check_only:
        print("check ok: %s, %dx%d, %d bytes, sha256 %s"
              % (IMAGE_NAME, width, height, len(data), digest))
        return 0
    target = write_entry(data, outdir, digest)
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (target, width, height, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
