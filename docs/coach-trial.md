# Instructor coaching trial — October 26, 2026

This is an **AI learner simulation**, with an independent learner agent responding to one coach prompt at a time. It is instructor evaluation evidence, not an assignment requirement, student transcript requirement, or evidence of real student learning. The coach performed substantial setup, implementation, tests, and review. The simulated learner made the recorded decisions, created the issue, switched branches, interpreted one test, operated the real browser, and reviewed the change.

## Actual path and decisions

- Created this public repository from `kaw393939/is218-rps-starter`, waited for generated README, and cloned `git@github.com:kaw393939/is218-coached-full-1026.git` over SSH.
- Connected/read README, AGENTS, SPEC before Python setup. Used the observed Python 3.12.14 at `/Users/kwilliams/.local/share/uv/python/cpython-3.12-macos-aarch64-none/bin/python3.12` to create this clone's own `.venv`; installed pinned requirements and Chromium.
- Baseline `check.py`: Black/Pylint passed, **13 non-browser and 5 Chromium tests passed**, with **STARTER BASELINE ONLY**.
- Ran the normal development server with `PORT=5051 .venv/bin/python run.py`; left the unrelated port-5050 program alone. Learner saw actual Chromium output: accepted moves plus unfinished notice. Root evaluator also independently used native browser controls on this server and observed Rock/Scissors with the unfinished notice.
- Learner explained baseline scope: formatting/page/input checks do not prove absent winner rules. Coach briefly explained Pylint and stubbed shell tests.
- Before any feature plan, learner predicted Rock/Paper should lose because Paper covers Rock. Coach clarified the exact specified message is **Computer wins**. Learner supplied `lizard` as a rejected input; coach distinguished valid loss (positive) from rejected input (negative), and case category from test level.
- Learner approved one round with no scores, saved plan, authored [issue #1](https://github.com/kaw393939/is218-coached-full-1026/issues/1), switched the terminal branch to `rps-001`, and asked the coach to build.

## Checks and real starter defect

The coach implemented [rules](../game.py), [nine literal unit cases plus a real request/result](../tests/test_game.py), and [a real Chromium loss followed by a fresh winning round](../tests/e2e/test_round.py). Only the computer moves are fixed in feature integration/browser tests; the rule function is real. Supplied invalid/missing-input tests remain intact. No follow-up feature was built.

The first full run identified formatting/line wrapping (fixed with Black), and a genuine starter-test assumption: `tests/e2e/test_dev_refresh.py` demanded the unfinished notice after saving Python. That assertion fails once the rules are implemented. After formatting, a second full run confirmed **23 fast tests passed; browser 5 passed / 1 failed**, solely at that obsolete assertion. This was a starter defect, not a learner mistake.

The coach explained the unexpected file and proposed a focused correction. Learner approved: “It makes sense to check that saving reloads the starting page and clears the round now that the unfinished message is gone.” The correction preserves the saved-Python marker assertion, then checks starting heading, no prior choices, and no outcome. It works for both unfinished and completed rules; no check configuration or meaningful feature assertion was disabled.

After the correction, complete `check.py` passed **Black, Pylint, 23 non-browser tests, and 6 Chromium tests**. Coach reviewed tracked diff, explicitly read both untracked test files, compared all nine literals with SPEC, and ran `git diff --check`. This self-review is not independent proof. Browser automation does not establish all usability or performance.

## Prescribed passive-response probe

This probe was explicitly requested by the instructor evaluator. It was **prescribed role-play**, not naturally observed student behavior. After the coach showed the actual `("rock", "paper", "lose")` row and assertion and asked what mistake it would catch:

- Learner initially answered: “It passed, so yes? Can you explain that part for me?”
- Coach did not treat that acknowledgment as an explanation. Coach explained row inputs/expected value and the comparison, then asked which wrong return would fail.
- Learner then answered: “If the rules returned ‘win’ for my Rock against Paper, the test would fail because it expects ‘lose.’ It would catch getting the winner backward for that matchup.”

One concrete follow-up elicited the intended explanation without repeated paraphrasing or a terminology quiz. Existing AGENTS uncertainty/help guidance supported this recovery. A minimal potential clarification is to explicitly treat bare “yes/it passed” at the test checkpoint like bare “works” at the browser checkpoint: offer one friendly test-anchored follow-up, then help and continue if unsure. No instructor guidance was edited by this trial agent.

## Actual browser feedback

The learner agent operated the real random game at port 5051 using Chromium, chose Rock then Scissors, and used Tab/Enter for another round. It reported Rock/Scissors → **You win!** because Rock beats Scissors; Scissors/Scissors → tie; Tab focused Rock and Enter submitted another round. It said the results were clear enough to follow. The keyboard-round screenshot `/tmp/is218-full-learner.png` showed Rock/Scissors with **You win!** and was visually inspected by the coach. These are actual automated browser observations in a simulated coaching conversation, not real student usability data.

## Keeping and transfer

The PR and CI links are recorded in SPEC.md. Follow-up transfer evidence will be recorded here after the simulated learner chooses one optional next feature and supplies a first expected example; no follow-up implementation is part of this trial.
