# Conversational AI (VU, XB_0119), Group 7

Group: Antonia Bulai, Danila Popusoi, Goktug Yildirim.

This repo started as the place for our paper presentation (13 Nov 2026). The presentation is done, so the repo is now for the **final project**. The old presentation files are still in the git history (last commit that has them: `e1c909a`).

## The final project

We build a tutorial-style notebook with two LLM agents that talk to each other.

A user asks something about a hotel or a restaurant. The dialogues come from the DSTC11 Track 5 data, the same data as in the course notebooks.
The Beginner agent passes the request on and asks questions. The Expert agent has the customer reviews and answers from them.
At the end they produce one reply that could be sent back to the user.

We run at least 50 of these conversations with two different versions of the Expert and compare them:

- with things we can count (number of turns, number of tokens),
- with an LLM that judges the final reply,
- with our own ratings on a small set, to see if the LLM judge agrees with us.

## What's coming up

| When | What | Where |
|---|---|---|
| Fri 27 Nov 2026, 13:00 | TA office hour (our questions are in `docs/ta-questions.md`) | NU-2B17 |
| Wed 2 Dec 2026 | Quiz 5 | in class |
| Fri 4 Dec 2026, 13:00 | TA office hour | NU-2B17 |
| **Wed 9 Dec 2026, 23:59** | **Final project notebook** (one .ipynb) | Canvas |
| 10-11 Dec 2026 | Oral defence of the project | |
| Mon 14 Dec 2026, 15:30 | Exam | |

## Where things are

| Path | What is in it |
|---|---|
| `WORKSPLIT.md` | Who does what, and by when |
| `coordination/STATUS.md` | Where we are right now. Read this first |
| `docs/project-brief.md` | The assignment in our own words, what we measured in the data, open points |
| `docs/reading-list-notes.md` | Notes on the course readings and what we can cite them for |
| `docs/ta-questions.md` | Questions for the TA office hour |
| `research/tools/` | Small scripts we used to look at the data |
| `research/sources/` | The output of those scripts |
| `notebook/` | The final notebook (not started yet) |
| `course/` | Lectures, papers, Canvas notes and the weekly notebooks (`course/notebooks/`, a1 has a filled version) |
| `tools/keyboard_check.py` | Checks a text file for characters that are not on a normal keyboard |

## How to run

There is no project notebook yet. The data scripts work like this:

    git clone https://github.com/lkra/dstc11-track5.git data/dstc11-track5
    python research/tools/inspect_data.py data/dstc11-track5/data
    python research/tools/split_overlap.py data/dstc11-track5/data

The `data/` folder is in `.gitignore`, so the dataset is never committed.

## Working together

- Pull before you start: `git pull`
- One branch per work package (see `WORKSPLIT.md`), then a pull request into `main`. One other person looks at it before it is merged.
- Commit small, and say what you changed in the message.
- When you stop, write where you are in `coordination/STATUS.md`.
- Never commit API keys or `.env` files.
- Big binary files (videos, model weights, the dataset) do not go in here.
