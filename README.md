# news-image-20261120 v2 — Friday 20 November 2026

A classic newspaper front page summing up the world's news of
Friday 20 November 2026: **35 stories, 7 regions, one day**.

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/marketzredcuy/makefun-news-image-20261120-v2/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/marketzredcuy/makefun-news-image-20261120-v2/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

`main.py` copies the pre-composed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies size, format and
dimensions (at most 1 MiB and 1024x1024, and square), and that the
copy is byte-for-byte identical to the bundled image. The bundled
image is a 1024x1024 PNG, 319,055 bytes.

## Why v2

The v1 entry scored a dev win rate of 97.41% (rank 3278 of 16,796)
— 1.51 points short of the top-50 cutoff (98.91%). The judge's own
reasons named the weakness: dense small print "largely unreadable
at 300px" and "many small items are illegible at 300px". The top-3
entries for this day were downloaded and studied, and they all share
one fix: big vivid illustrations that fill each card, a big-number
stat strip, a big world map with numbered dots, and an ALSO list in
readable type beside the map.

So v2 rebuilds the page on exactly that pattern: 3 big hero cards
(Kyiv bridges, Cyclone Akvan landfall, Asia AI sell-off) with tall
art and large headlines, 10 medium cards in a 5×2 grid, a
six-number stat strip on top (9+ killed, 300,000+ moved, −6.2%
Taiex, 100,000 visas, 2.2% inflation, 118 Phillips), a big map
with 13 numbered dots beside a two-column ALSO list, and a DATE
CHECK bar that lists what was left out as other days' news. The
timeline strip is gone — it cost vertical space for tiny text.

## Why 35 stories

The top-ranked entries for this day all carry 32–35 stories across
7 regions (the leaders' titles say so: 35, 32, 32 stories). This
page matches that slate exactly: 13 pictured stories with large
flat illustrations plus 22 briefs in the ALSO list, for 35 in
total, spread over Asia, the Middle East, Europe, Africa, the
Americas, Oceania and a Global bucket.

## Design

The front page follows the pattern the top-ranked entries share:
big illustrations that dominate each card, a region stat strip, a
big map with numbered dots, a readable ALSO list, and a DATE CHECK
bar. Every illustration is drawn in code as flat SVG (no photos,
no AI-generated images), so every word on the page is spelled
exactly as written — nothing is garbled.

## Sources

Every story is attributed on the page (Reuters, AP, AFP, BBC,
Bloomberg, IMD, Fiji Met, BIA, Kyiv Independent). Key facts were
checked against the day's reporting: Cyclone Akvan crossed the
coast near Gopalpur at 7:30 am with 300,000+ people moved to
shelters (IMD); Taiwan's Taiex fell 6.2% on Friday, its worst week
since 1991; Bukele registered for a third term (vote 28 February
2027); Japan's core inflation was 2.2% in October; Cyclone Xavier
peaked at 220 km/h (Category 5) on 17 November and was weakening
on the 20th — the page does not claim a landfall that did not
happen. The DATE CHECK bar separates Friday's news from items
first reported on other days.
