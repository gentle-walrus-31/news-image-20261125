#!/usr/bin/env python3
"""Entry program for the make.fun bounty ``news-image-20261125``.

"Sum up 25 November's world news in one image."

The entry is a single newspaper-style front page, ``front-page.png``
(1024x1024), summing up the world news of Wednesday 25 November
2026. This program copies that bundled image, byte for byte, to
``/output/entry.png`` — the one file the bounty judges.

It runs with no network, no randomness and no clock: the same input
always produces the same output, so the two grading runs write
identical bytes.

Before copying, the program checks the bundled image so a corrupt
or wrong-sized file can never be submitted silently:

* it must be a real PNG (8-byte signature, IHDR first);
* it must be exactly 1024x1024 pixels;
* it must be at most 1 MiB (the bounty limit);
* after writing, the output is read back and its SHA-256 is
  compared with the source; any mismatch aborts and removes the
  partial output.

The front page (``front-page.png``, SHA-256
``cd633414c234ab6c6bdce297d2d11a9766ca4a30d9f9b2e536229ad65b76f1cb``,
144,890 bytes) covers stories all first reported on
25 November 2026: the Trump administration's new tariffs on 14
economies, China up to 20% (hero); Jerusalem judges urging
prosecutors to drop the most serious bribery case against Benjamin
Netanyahu; a fuel tanker explosion on Cairo's ring road killing at
least 30 people; the Houthis claiming a strike on Saudi Arabia's
Ras Tanura refinery; China launching Shenzhou-24 with Pakistan's
Muhammad Zeeshan Ali, the first foreigner aboard Tiangong;
Bangladesh raising the garment minimum wage 36%; plus an ALSO
TODAY strip (Poland's planned no-fly zone, RSF drones killing 19
in Sudan, the US Army detonating 4,400 kg of explosives in Iowa,
AI stocks tumbling, China probing its Shanghai party chief,
miners trapped in a flooded Indonesian gold mine).

Usage
-----
    python3 main.py                # writes /output/entry.png
    python3 main.py /tmp/out       # writes /tmp/out/entry.png (testing)
    python3 main.py --check        # validate only, write nothing

Exit code 0 means the image was written and verified (or, with
--check, that it passed validation). Anything else means validation
failed.

Only the Python standard library is used.
"""

from __future__ import annotations

import hashlib
import struct
import sys
from pathlib import Path

SOURCE = "front-page.png"
OUT_NAME = "entry.png"
DEFAULT_OUT = Path("/output")

WANT_W, WANT_H = 1024, 1024
MAX_SIZE = 1024 * 1024  # 1 MiB

SIGNATURE = b"\x89PNG\r\n\x1a\n"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dimensions(data: bytes) -> tuple[int, int]:
    """Read (width, height) from a PNG byte string's IHDR chunk."""
    if len(data) < 33 or data[:8] != SIGNATURE:
        raise ValueError("not a PNG file: bad signature or too short")
    size, kind = struct.unpack(">I4s", data[8:16])
    if kind != b"IHDR" or size != 13:
        raise ValueError("not a PNG file: first chunk is not IHDR")
    return struct.unpack(">II", data[16:24])


def load(repo: Path) -> bytes:
    path = repo / SOURCE
    if not path.is_file():
        raise FileNotFoundError(f"bundled image {SOURCE!r} missing")
    data = path.read_bytes()
    if len(data) > MAX_SIZE:
        raise ValueError(f"image is {len(data)} bytes, over the 1 MiB limit")
    w, h = dimensions(data)
    if (w, h) != (WANT_W, WANT_H):
        raise ValueError(f"image is {w}x{h}, expected {WANT_W}x{WANT_H}")
    return data


def emit(data: bytes, dest: Path) -> None:
    """Write *data* to *dest* and verify the round trip byte for byte."""
    want = digest(data)
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        back = dest.read_bytes()
    except OSError as exc:
        print(f"error: cannot write {dest}: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if back != data or digest(back) != want:
        try:
            dest.unlink()
        except OSError:
            pass
        print("error: output differs from source after write",
              file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote:  {dest} ({len(back)} bytes, verified)")


def run(argv: list[str]) -> int:
    check_only = bool(argv) and argv[0] == "--check"
    args = argv[1:] if check_only else argv
    if len(args) > 1:
        print("usage: python3 main.py [--check] [output-dir]",
              file=sys.stderr)
        return 2
    out_dir = Path(args[0]) if args else DEFAULT_OUT
    repo = Path(__file__).resolve().parent
    try:
        data = load(repo)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    w, h = dimensions(data)
    print(f"validated: {SOURCE} is {w}x{h} PNG, {len(data)} bytes "
          f"(<= 1 MiB)")
    print(f"sha256: {digest(data)}")
    if check_only:
        print("check only: nothing written")
        return 0
    emit(data, out_dir / OUT_NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
