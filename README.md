# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/gentle-walrus-31/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/gentle-walrus-31/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image summary of the world news of Wednesday 25 November 2026, built for the [make.fun bounty](https://make.fun/bounty/news-image-20261125) "Sum up 25 November's world news in one image" ($100, top 50 paid).

![World News front page, 25 November 2026](front-page.png)

## The front page

"Tariff Storm" — a deep-violet and yellow broadsheet on pale lilac
paper (1024×1024 PNG), a different look from the navy 19 Nov, crimson
20 Nov, teal 21 Nov, charcoal-and-gold 22 Nov, emerald 23 Nov and
burnt-orange 24 Nov editions — with a tariff ticker tape under the
masthead and a clear visual hierarchy, so the news explains itself
with no feed attached:

- **Hero — TARIFF STORM.** The Trump administration is poised to
  unveil new tariffs on 14 economies after a Section 232 probe into
  excess factory capacity: China up to 20%, the EU, Japan and South
  Korea 15% or less. Markets rattled: the Nasdaq fell 2% on
  Wednesday, nearly 20% below its early-October record.
  Illustrated with a container port at dusk under a storm sky.
- **Netanyahu case crumbles.** Jerusalem judges urge prosecutors to
  drop the most serious bribery case (Case 4000) against caretaker
  PM Benjamin Netanyahu, saying a conviction is unlikely. "Today,
  the trial fell apart," he said.
- **Cairo ring road inferno.** A fuel tanker overturns and explodes
  on Cairo's ring road, killing at least 30 people and destroying
  27 vehicles; 39 ambulances rush to the scene.
- **Houthis hit refinery.** Houthis claim a strike on Ras Tanura,
  Saudi Arabia's biggest refinery; satellite images show black
  smoke.
- **First foreign astronaut.** China launches Shenzhou-24 with
  Pakistan's Muhammad Zeeshan Ali — the first foreigner aboard the
  Tiangong station.
- **Bangladesh pay rise.** Garment minimum wage up 36% to 17,000
  taka (~$139) after weeks of protests; garments are 80% of exports.
- **Also today:** Poland plans a no-fly zone on its Ukraine border;
  RSF drones kill 19 in Sudan; the US Army detonates 4,400 kg of
  explosives in Iowa; AI stocks tumble (Nasdaq –2.8%, Nvidia –5%);
  China probes its Shanghai party chief; miners trapped in a flooded
  Indonesian gold mine.

Sources: Reuters, Wall Street Journal, AP, BBC, Daily Summary of
World. Every story was date-checked as first reported on
25 November 2026.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=0ysfdeph&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>

## How it works

`main.py` (Python 3.13, standard library only, no network) validates
the bundled `front-page.png` — PNG signature, exactly 1024×1024, at
most 1 MiB — and writes it byte-for-byte to `/output/entry.png`,
then reads the output back and verifies its SHA-256 matches the
source. Running it twice produces identical bytes.

```bash
python3 main.py           # writes /output/entry.png
python3 main.py --check   # validate only, write nothing
```

The image itself was drawn with Pillow (build-time only); the entry
program needs no third-party packages.

## License

MIT — see [LICENSE](LICENSE).
