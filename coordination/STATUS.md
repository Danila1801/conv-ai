# Status

Last updated: Wed 25 Nov 2026 (session 3 of the day), by Goktug's Claude session.

## Where we are

The assignment and all course material have been read. The data has been measured.
Draft 2 of the design is in `DESIGN.md` and waits for the group. `docs/evidence.md` says which course file and page each choice rests on. The pilot notebook is written and waits to be run on Kaggle.

## Board

States: not started, in progress, in review, done, blocked.

| # | Work package | Owner | State | Branch | Note |
| --- | --- | --- | --- | --- | --- |
| A | Design decisions | Goktug | in review | `wp-a-design` | Draft 2 is in `DESIGN.md`, with Antonia's notes worked in. Everyone: read it and comment in the pull request. Two choices wait for the TAs, one waits for the pilot |
| B | Questions to the TAs | Antonia | not started | | Questions are in `docs/ta-questions.md`. Office hour Fri 27 Nov 13:00, NU-2B17 |
| C | Data and choice of dialogues | Dan | not started | | Can start now. `DESIGN.md` section 6 says which dialogues, section 10 has the JSON format. `pick_dialogues` in `pilot/pilot.py` is a starting point |
| D | Beginner and two Experts | Goktug | in progress | `wp-a-design` | Prompts are in `pilot/pilot.py`. Not run on a GPU yet |
| E | Conversation loop and stopping | Goktug | in progress | `wp-a-design` | Loop and stopping are in `pilot/pilot.py`, for both ways of writing the final reply. Tested with canned replies (`pilot/test_loop.py`), not with the model |
| F | Counted metrics and plots | Dan | not started | | Waits for E (needs the JSON format) |
| G | LLM judge | Dan | not started | | Waits for A (criteria) |
| H | Full run | Goktug | not started | | Waits for D, E |
| I | Rating guide and sheet | Antonia | not started | | Can start once the criteria are fixed in A |
| J | Human ratings | all | not started | | Thu 3 and Fri 4 Dec |
| K | Agreement | Antonia | not started | | |
| L to O | Notebook text | see `WORKSPLIT.md` | not started | | |
| P | Reference check | Antonia | not started | | The list of traps is in `docs/reading-list-notes.md`, section 1. `docs/evidence.md`, section 2, lists the papers that still have to be opened again |
| Q | Final run on Kaggle | Goktug | not started | | |
| R, S, T | Division of labour, hand-in, defence practice | all | not started | | |

## In progress right now

The pilot (`pilot/pilot.ipynb`) waits to be run on Kaggle. Nobody is editing it.

## Waiting on a person

- Goktug or Dan: look at the branch `final-project-setup` and merge it into `main`. It removes the old `project/` placeholder and moves `notebooks/` to `course/notebooks/`. `presentation/` stays as it was.
- Dan: check that Antonia has access to this repo.
- Dan or Antonia: run `pilot/pilot.ipynb` on Kaggle and put `pilot_conversations.jsonl` in `results/pilot/`. The Kaggle account has to be phone verified, otherwise the GPU and the internet switch are locked (that stopped Goktug). Then: Settings -> Accelerator -> GPU T4 x2, internet on, Run All. It is 24 short conversations.
- All: read `DESIGN.md` and say what you would change.
- Antonia or whoever is on campus: the TA questions on Friday.
- All: read `WORKSPLIT.md` and say if the split is fine.

## Requests between work packages

Format: date, from, to, what is needed, what breaks without it.

- 25 Nov, from Goktug's session, to a person: `CLAUDE.md` says "Antonia works without Claude". She now uses the free plan for questions. The line can be updated by a person. Nothing breaks if it stays.

## Decisions taken

| Date | Who | Decision | Why |
| --- | --- | --- | --- |
| 25 Nov | Goktug | The goal is to meet every requirement of the assignment fully. No extras for their own sake | It is a course assignment, not a competition |
| 25 Nov | Goktug | We use this repo (it was the presentation repo) for the project. A clean copy is made for the hand-in | One place for all three, and the hand-in has no working notes |
| 25 Nov | Goktug | Dialogues come from the test split | Train contains val in the data repo (measured) |
| 25 Nov | Goktug | The models run on Kaggle, not on a local PC | It is where the course notebooks run, and where the graders can run ours |
| 25 Nov | Goktug | `presentation/` stays in the repo | We may still want the deck and the Q&A |
| 25 Nov | Goktug | Who writes the final reply (Beginner or Expert) is decided after the pilot | Antonia's notes and draft 1 differ, and the pilot can show which works better |
| 25 Nov | Goktug | Canvas files and the reading list are the first source for every method we use | It is what the assignment asks for, and it keeps the references safe |
