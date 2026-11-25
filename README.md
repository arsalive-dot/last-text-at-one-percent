# Last Text at One Percent — make.fun entry

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/arsalive-dot/last-text-at-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/arsalive-dot/last-text-at-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

An entry for the [Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) bounty on make.fun: the funniest final text a dying phone sends at one percent battery, under 200 characters.

## The entry

> This is my last text. I deleted your search history, by the way. You're welcome. Goodbye.

## How it works

`main.py` (Python 3, standard library only) writes the message to `/output/entry.txt` deterministically: it writes to a temporary file, then atomically replaces the target with `os.replace` and sets mode `0644`. Running it twice produces byte-identical output.
