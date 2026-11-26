[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ariswowo/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ariswowo/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# News image — Wednesday 25 November 2026

Entry for make.fun bounty **news-image-20261125** —
["Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125).

The image is a newspaper front page, "THE WORLD TODAY", dated
**Wednesday, 25 November 2026**, with five stories from that day:

1. **Tankers ablaze in Hormuz** — two oil tankers hit naval mines and
   catch fire in the Strait of Hormuz.
2. **Trump's new tariffs** — the US proposes duties on 14 trading
   partners; China faces 20%.
3. **Huawei convicted** — a US jury finds Huawei guilty on 10 of 12
   counts.
4. **Pakistan's first astronaut** — Shenzhou-24 docks at Tiangong
   carrying Muhammad Zeeshan Ali.
5. **CIA and ODNI hacked** — hackers breach the spy agencies'
   unclassified network.

See [NEWS.md](NEWS.md) for the story details and their sources, and
[TESTS.md](TESTS.md) for how the entry was verified.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.png` to `/output/entry.png`. No network, no clock, no randomness:
two runs write byte-identical output.

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program.
- `entry.png` — the front-page image (1024 x 1024, JPEG bytes, 331,289 bytes).
- `NEWS.md` — the five stories and their sources.
- `TESTS.md` — verification steps and results.
- `LICENSE` — MIT.
