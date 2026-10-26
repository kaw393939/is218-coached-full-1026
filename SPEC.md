# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Implement one independent round in `game.py`; preserve the supplied interface/server, with no score or saved history.
- Learner prediction: Rock against Paper is a loss because Paper covers Rock; return `lose` and display **Computer wins**.
- Treat valid losses/ties as positive cases. Reject unsupported input such as `lizard` and missing input with HTTP 400 and helpful text before the rules run.
- Add all nine literal unit outcomes, one real request/result integration test with only the computer choice fixed, and one real Chromium round/replay test using real rules/HTTP. Reuse supplied invalid/missing-input checks.
- Run the complete `check.py` and review the diff before learner browser feedback. Preserve the shared checks.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/kaw393939/is218-coached-full-1026/issues/1).
- Implementation: [real independent-round rules](game.py), [nine literal outcomes and a real request/result](tests/test_game.py), and [real Chromium round/replay](tests/e2e/test_round.py). The existing server rejects invalid/missing moves before calling the rules.
- Review: compared all nine spec rows with code/tests; request and browser feature checks fix only computer moves. The existing [development-refresh test](tests/e2e/test_dev_refresh.py) now checks a fresh page after a Python save rather than demanding the obsolete unfinished notice.
- Checks: `.venv/bin/python check.py` passed Black, Pylint, **23 non-browser tests and 6 Chromium tests**. AI reviewed tracked changes and read both new test files; `git diff --check` passed. Detailed evidence and check run are in the PR.
- Browser observation (simulated learner operating actual Chromium): Rock versus Scissors displayed **You win!** because Rock beats Scissors; a subsequent Scissors/Scissors round tied. Tab focused Rock and Enter played another round. Learner reported the results clear enough to follow. This is a coached simulation, not evidence of real student learning.
- Evidence limits: the configured cases and one automated replay do not establish every aspect of usability or performance. No scores/history were added.
