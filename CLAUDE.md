# Rules for AI assistants in this repo

- Never add AI attribution: no "Co-Authored-By: Claude", no "Generated with Claude Code", no commits authored as an AI. Humans commit.
- Slides and docs follow the deck standard: a claim as the title, real numbers with a source line, a visual on every slide, a cool green palette (#F2F5F3 / #17231F / #2C6E5F), never orange.
- Keyboard-only characters everywhere: write -> for arrows and - for dashes, no middle dots, curly quotes or ellipsis characters. Run presentation/tools/keyboard_check.py before sharing.
- Never commit API keys.

# Working on the final project

More than one Claude session works here (Goktug's and Dan's). They do not share a chat. This file and the `coordination/` folder are how they stay in step. Antonia works without Claude, so anything she needs must be readable by a person.

## Read first, in this order

1. `coordination/STATUS.md` - where things stand, what is in progress, what is next.
2. `WORKSPLIT.md` - who owns which work package.
3. `docs/project-brief.md` - the assignment, the data facts, the open points.
4. `DESIGN.md` - the decisions (once it exists). It wins over the brief when they differ. The assignment text and answers from the teachers win over both.
5. The newest three entries of `coordination/LOG.md`.

## The goal

Full marks on the assignment's requirements. Not being original for its own sake. Follow the course notebooks (same data, same Qwen models, same libraries) unless a requirement needs something else. When you add something beyond the notebooks, say which requirement it serves.

## Project rules, with the reason for each

1. **Stay inside your person's work packages.** Ask whose session you are if it is not clear. If you need a change in someone else's part, write it under "Requests" in `coordination/STATUS.md`. Reason: two sessions editing the same file overwrite each other.
2. **Never add a reference you have not opened in this session.** The assignment says a fabricated reference fails the whole project, and a misplaced one costs points. `docs/reading-list-notes.md` lists what was read. Lines marked "agent" there are not confirmed yet. Cite Jurafsky and Martin by chapter title and draft date, and lectures by title and date, because the numbers differ between sources.
3. **Dialogues for the experiments come from the test split only.** In the data repo the train split contains the validation split (measured, see `research/sources/split-overlap.txt`).
4. **Only free, open models that run on Kaggle.** No paid API calls. Reason: the graders must be able to run the notebook, and nobody has a budget.
5. **Keep the code simple and comment the why.** All three students defend this in an oral exam. Code they cannot explain costs them points.
6. **Text for the notebook and the docs is plain student English.** Short sentences, no filler. Say what was done, why, and which course material it connects to.
7. **Say what you checked and what you did not.** "Tests pass" comes with what was run. A number comes with how it was measured.
8. **Do not change the rules in this file yourself.** If a rule is in the way, write the problem under "Requests" and let a person decide.

## Only a person does these

- Merging into `main`. Work goes on a branch and into a pull request.
- Inviting people to the repo, or changing its visibility.
- Anything that goes to the teachers or TAs (Canvas, email, the hand-in).
- Deciding between options in `DESIGN.md`.

## Hand-over rule

Before a session stops, in the same commit or pull request as the work:

1. Update your rows in `coordination/STATUS.md` (state, branch, one-line note).
2. Add one entry at the top of `coordination/LOG.md`: date, whose session, what was done, what was checked, what was not, what comes next.
3. Add one line to `coordination/AI-USAGE.md`: date, whose session, what the assistant did. The group states its AI use in the notebook and writes that statement from this file, so keep it accurate.

Commit subject: work package letter, then the result as a plain sentence. Example: `G: Judge returns one score per criterion and parses in 50 of 50 test cases`.

## Not part of the hand-in

At the end the group makes a clean copy of the repo for the hand-in. These paths stay behind: `CLAUDE.md`, `coordination/`, `research/raw/`, `course/`, `presentation/`, `.claude/`. Do not put anything the notebook needs in them.
