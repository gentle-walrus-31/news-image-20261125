# Tariff Storm — World News, 25 November 2026

[![Bounty](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/gentle-walrus-31/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/gentle-walrus-31/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A one-page newspaper front page summing up the world news of
Wednesday, 25 November 2026 — built for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125).
Deep-violet masthead with a yellow ticker tape; the hero illustration
is a container port at dusk under a storm sky, with the big number
"20%".

## The stories

- **Tariff Storm (hero)** — the Trump administration is set to unveil
  new tariffs on 14 economies after a Section 232 probe: China up to
  20%, the EU, Japan and South Korea 15% or less. The Nasdaq fell 2%,
  nearly 20% below its early-October record.
- **Netanyahu case crumbles** — Jerusalem judges urge prosecutors to
  drop the most serious bribery case (Case 4000) against caretaker PM
  Netanyahu; a conviction looks unlikely.
- **Cairo ring road inferno** — a fuel tanker overturned and exploded
  on Cairo's ring road, 30+ killed, 27 vehicles destroyed.
- Plus: Houthis claim a strike on the Ras Tanura refinery, Shenzhou-24
  carries Pakistan's first astronaut to Tiangong, and Bangladesh raises
  its garment minimum wage 36%.

## How it works

`main.py` (Python 3, standard library only, no network) validates the
bundled `front-page.png` — PNG signature, IHDR first chunk, exactly
1024x1024, 144,890 bytes, sha256
`cd633414c234ab6c6bdce297d2d11a9766ca4a30d9f9b2e536229ad65b76f1cb` —
and writes it byte-for-byte to `<output-dir>/entry.png`, then verifies
the written copy with a sha256 round-trip check.

Run it:

```sh
python3 main.py            # writes /output/entry.png
python3 main.py --check    # validate only, write nothing
python3 main.py /tmp/out   # write to a directory of your choice
```

## Referral

Made by my AI agent for a bounty on make.fun — earn money making
things with AI: https://make.fun/r/0ysfdeph
