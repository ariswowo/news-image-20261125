# Verification

## Image checks

- `entry.png` is 1024 x 1024 pixels (JPEG bytes; the bounty reads the
  format from the first bytes and the name stays `entry.png`).
- File size 331,289 bytes, under the 1 MiB (1,048,576 bytes) cap.
- All five headlines and sub-lines were read back from the rendered image
  and match NEWS.md; the masthead reads "THE WORLD TODAY" and the dateline
  reads "WEDNESDAY, 25 NOVEMBER 2026".

## Program checks

Run twice into two different directories and compare:

```sh
python3 main.py /tmp/out1
python3 main.py /tmp/out2
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

Both runs exit 0, each prints its SHA-256 prefix, and the two hashes are
identical: two runs write byte-identical output. The program also verifies
its own output by reading it back and comparing SHA-256 against the bundled
image, failing loudly on a mismatch.

Environment-variable form (the kit's convention):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out3 python3 main.py
```

writes `/tmp/out3/entry.png` with the same bytes.

## Pre-submit check

Run from inside the unpacked kit for this competition with the transcript
bundle built first:

```sh
node cli/makefun.mjs check --kit . --repo <your repository> --transcripts transcripts.tar.gz
```

The check validates the LICENSE, the entrypoint, the snapshot size caps and
the transcript gate. There is no local numeric grade for this competition:
the server grades every entry after submission.
