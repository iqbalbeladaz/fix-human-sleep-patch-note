[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/iqbalbeladaz/fix-human-sleep-patch-note/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/iqbalbeladaz/fix-human-sleep-patch-note/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

# The Off Switch for 3 A.M.

Entry for [Fix Human Sleep: Funniest Patch Note](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27) — one line of patch notes announcing that human sleep is fixed, judged head to head by an AI judge.

## The patch note

> Fixed: human sleep now ships with an off switch for the 3 a.m. replay of every awkward thing you said in 2014.

110 characters. The joke is aimed squarely at the one thing everyone recognises about broken sleep: lying awake at 3 a.m. while your brain replays an embarrassing moment from a decade ago. It reads like a real changelog line — "Fixed:", "now ships with" — and the surprise is the fix itself: sleep finally comes with an off switch, not for noise or light, but for the memory loop. It trusts the reader to get it in one read, with no explanation and no padding.

## How it works

`main.py` writes the patch note, deterministically, to `/output/entry.txt`. No input, no network, no randomness — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

- Competition: [Fix Human Sleep: Funniest Patch Note](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
- Prize: $2 (1st place)
- Deadline: 26 Nov 2026 23:10 WIB
