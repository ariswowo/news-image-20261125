#!/usr/bin/env python3
"""make.fun bounty news-image-20261125: "Sum up 25 November's world news in one image".

The entry image is a newspaper front page for Wednesday 25 November 2026,
bundled in this repository as entry.png (1024 x 1024, JPEG bytes, under
1 MiB). NEWS.md lists the five stories on the page and where each was
reported.

This program uses only the Python standard library. It needs no network,
reads no clock and uses no randomness: it copies the bundled bytes to
/output/entry.png, so two runs always write byte-identical output. That is
the approach the bounty itself names: "the simplest program copies an
image the repository holds".

Run it:
    python3 main.py
    python3 main.py /tmp/out/entry.png
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py

An optional first argument names the output file outright; without one
the MAKEFUN_OUTPUT_DIR/OUTPUT_DIR environment variable (a directory) is
honoured, falling back to /output/entry.png. After writing, the program
reads the output back and checks its SHA-256 against the bundled bytes,
failing loudly instead of silently shipping a corrupt copy. It also
refuses a bundled image over the bounty's 1 MiB limit instead of
shipping it.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png"
MAX_IMAGE_BYTES = 1_048_576  # the bounty's image size limit


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def output_path(argv) -> Path:
    """Where the image goes.

    Precedence: an explicit argv path (a file, or a directory to put
    entry.png in), then the kit's MAKEFUN_OUTPUT_DIR / OUTPUT_DIR
    environment variable (a directory), then /output/entry.png.
    """
    if len(argv) > 1:
        given = Path(argv[1])
        # An existing directory, or a suffix-less path, names the
        # directory to put entry.png in; anything else is the file.
        if given.is_dir() or not given.suffix:
            return given / "entry.png"
        return given
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value) / "entry.png"
    return Path("/output/entry.png")


def main(argv) -> int:
    if len(argv) > 2:
        print("usage: python3 main.py [output-path]", file=sys.stderr)
        return 2
    if not BUNDLED.is_file():
        print(f"error: bundled image {BUNDLED} is missing", file=sys.stderr)
        return 1
    bundled_size = BUNDLED.stat().st_size
    if bundled_size > MAX_IMAGE_BYTES:
        print(f"error: bundled image {BUNDLED} is {bundled_size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    out = output_path(argv)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED, out)
    expected = sha256_of(BUNDLED)
    if sha256_of(out) != expected:
        print(f"error: {out} does not match the bundled image", file=sys.stderr)
        return 1
    print(f"wrote {out} ({out.stat().st_size} bytes, sha256 {expected[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
