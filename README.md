[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/EthanWw-code/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/EthanWw-code/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# news-image-20261124 — The World in One Image

Entry for the make.fun bounty "Sum up 24 November's world news in one image".

## What it is

A program (`main.ts`, Node 22, standard library only, no network) that writes one
image to `/output/entry.png`: a newspaper front page summing up the world news of
Tuesday 24 November 2026. The image is bundled in this repository as `entry.png`
and the program copies it deterministically — running it twice writes identical bytes.

## The image

A front page ("THE WORLD", 24 November 2026) covering:

- Lead: Iran vows to use "all its tools" against the U.S. naval blockade; Vance and
  Rubio meet Qatar's PM at the White House.
- Gaza: Israeli strikes kill Hamas security chief Naeem Abu Nahel and six others.
- Ukraine: Russian strike on Zaporizhzhia flats kills 2, wounds 40, including 4 children.
- Tech: Jensen Huang reinstated as Nvidia CEO; Senate Democrats vow an inquiry.
- Courts: Oregon and Virginia sue SpaceX over Grok images.
- Also: UK to host the 2035 Women's World Cup; Germany first to access Ukraine's
  Delta system; NATO vows to defend against space threats.

The image was drawn with Python/Pillow from verified 24 November 2026 reporting
(1024×1024 PNG, under 1 MiB).

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Writes `out/entry.png`. Run it twice and the bytes are identical.

## License

MIT — see LICENSE.
