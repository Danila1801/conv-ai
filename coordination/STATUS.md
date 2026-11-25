# Status

Last updated: Wed 25 Nov 2026, by Goktug's Claude session.

## Where we are

The assignment and all course material have been read. The data has been measured. Nothing is built yet.
Next step is `DESIGN.md` (work package A), then the pilot.

## Board

States: not started, in progress, in review, done, blocked.

| # | Work package | Owner | State | Branch | Note |
| --- | --- | --- | --- | --- | --- |
| A | Design decisions | Goktug | not started | | Starts next. Needs the TA answers for two choices, has defaults for both |
| B | Questions to the TAs | Antonia | not started | | Questions are in `docs/ta-questions.md`. Office hour Fri 27 Nov 13:00, NU-2B17 |
| C | Data and choice of dialogues | Dan | not started | | Can start now. Use the test split (see brief, section 3) |
| D | Beginner and two Experts | Goktug | not started | | Waits for A |
| E | Conversation loop and stopping | Goktug | not started | | Waits for A |
| F | Counted metrics and plots | Dan | not started | | Waits for E (needs the JSON format) |
| G | LLM judge | Dan | not started | | Waits for A (criteria) |
| H | Full run | Goktug | not started | | Waits for D, E |
| I | Rating guide and sheet | Antonia | not started | | Can start once the criteria are fixed in A |
| J | Human ratings | all | not started | | Thu 3 and Fri 4 Dec |
| K | Agreement | Antonia | not started | | |
| L to O | Notebook text | see `WORKSPLIT.md` | not started | | |
| P | Reference check | Antonia | not started | | The list of traps is in `docs/reading-list-notes.md`, section 1 |
| Q | Final run on Kaggle | Goktug | not started | | |
| R, S, T | Division of labour, hand-in, defence practice | all | not started | | |

## In progress right now

Nothing.

## Waiting on a person

- Goktug or Dan: look at the branch `final-project-setup` and merge it into `main`. It removes the old `project/` placeholder and moves `notebooks/` to `course/notebooks/`. `presentation/` stays as it was.
- Dan: check that Antonia has access to this repo.
- Goktug: check on his PC whether the LoRA adapter from Notebook 2 still exists, and which GPU the PC has (`nvidia-smi`).
- Goktug: his local course folder (`Desktop\Period 2\CAI`) may hold files that are not in the repo yet. To be compared and added from a session that runs on his PC.
- Antonia or whoever is on campus: the TA questions on Friday.
- All: read `WORKSPLIT.md` and say if the split is fine.

## Requests between work packages

None yet. Format: date, from, to, what is needed, what breaks without it.

## Decisions taken

| Date | Who | Decision | Why |
| --- | --- | --- | --- |
| 25 Nov | Goktug | The goal is to meet every requirement of the assignment fully. No extras for their own sake | It is a course assignment, not a competition |
| 25 Nov | Goktug | We use this repo (it was the presentation repo) for the project. A clean copy is made for the hand-in | One place for all three, and the hand-in has no working notes |
| 25 Nov | Goktug | Dialogues come from the test split | Train contains val in the data repo (measured) |
