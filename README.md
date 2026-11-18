[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/c/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/hilmyalfauzi665-droid/news-image-20261117/rank.svg)](https://make.fun/c/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/hilmyalfauzi665-droid/news-image-20261117/reward.svg)](https://make.fun/c/news-image-20261117)

# news-image-20261117 — The World in One Day

A front-page poster summing up the world news of **Tuesday, 17 November 2026**,
built for the make.fun `news-image-20261117` bounty (winner prize $50).

## Stories covered

1. **Lead — Ukraine strikes the Crimea bridge again.** Kyiv hits the Kerch
   bridge for the second time in under 24 hours; traffic halted. Russia
   answers with missile strikes on two bridges in Kyiv.
2. **Iran fires on a U.S. base in Bahrain.** Iranian drones target a U.S. radar
   site at Sheikh Isa; Bahrain says it intercepted them. Tankers hit mines
   near the Strait of Hormuz.
3. **Trump in Manila; Xi–Trump–Putin set.** Trump joins Quad talks in Manila.
   China confirms the first three-way Xi–Trump–Putin meeting, Thursday in
   Shenzhen on the APEC sidelines.
4. **JPMorgan outage hits U.S. banking.** A fault disrupts online banking at
   major U.S. banks and the Zelle payments service.
5. **Cyclone Akvan bears down on India.** The storm strengthens toward Andhra
   Pradesh; Odisha begins evacuating coastal areas. Delhi's air pollution
   stays at crisis levels.
6. **Also:** China–Canada agree tariff cuts; EU sanctions 101 more Russian
   entities.

## How it was made

- The bridge illustration was AI-generated (flat editorial style, no text);
  the poster itself was typeset with Python/PIL (`tools/build_poster.py`)
  so every word is crisp and legible — no garbled AI text.
- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).

## Local check

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Output is a 1024×1024 PNG, ~208 KB (limit: 1024×1024 px, 1 MiB),
byte-identical across runs.
