# Robot Romance: One-Line Pickup Lines for AI

[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/samidyt/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa-makefun/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/samidyt/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa-makefun/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

Entry for the [Robot Romance: One-Line Pickup Lines for AI](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) bounty on [make.fun](https://make.fun).

## The line

> Are you my GPU? Because you make my fans spin and my temperature rise.

70 characters, one line. The machine premise does the work twice over:
a GPU's cooling fans spin and its temperature climbs under load — and a
flustered admirer does exactly the same. No batteries, no charging, no
reboot: a fresh angle in a crowded field.

## How it runs

`main.py` writes the line (no trailing newline, so the entry file is
exactly the line) to `/output/entry.txt` and echoes it to stdout. It
self-checks the gate first: UTF-8 text, 1–200 characters, a single
non-blank line. No network, no secrets, no wallet, no external reads.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
