# Hand-over log

Newest entry on top. One entry per working session. Keep entries short.

## Wed 25 Nov 2026, Goktug's Claude session (claude.ai, cloud)

**Done**
- Turned this repo from the presentation repo into the project repo, on the branch `final-project-setup` (not merged, a person does that).
  - Removed `presentation/` and the old `project/README.md` placeholder. They are still in the history, last commit with them is `e1c909a`.
  - Moved `notebooks/` to `course/notebooks/` and the character checker to `tools/keyboard_check.py`.
  - New: `README.md`, `WORKSPLIT.md`, `coordination/`, `docs/`, `research/`, `notebook/`. `CLAUDE.md` keeps the four old rules and adds the project rules.
- Brief rewritten around the assignment's requirements (`docs/project-brief.md`). The earlier "how to stand out" part was dropped on Goktug's instruction.

**Checked**
- The data numbers in the brief, by running the three scripts in `research/tools/` on a fresh clone of `lkra/dstc11-track5`.
- In `docs/reading-list-notes.md`, the lines marked "checked".

**Not checked**
- Lines marked "agent" in the reading notes.
- No model has been run. Nothing is known yet about speed, or about how well a small Qwen model keeps to a role.
- The 17 student-presentation papers (only MultiWOZ and Mem0 were read, because they are also on the reading list).

**Next**
- Work package A: write `DESIGN.md` with the decisions listed in the brief, section 5.
- A pilot notebook: 5 conversations, to see whether the model follows the roles and how long a conversation takes.
- Dan can start work package C now. It does not depend on the design.

## Tue 24 Nov 2026, Goktug's Claude session (claude.ai, cloud)

**Done**
- Read the Canvas page, Notebooks 1 to 4 and all lecture slides in the Claude project.
- Ten sub-agents opened every link of the course reading list. Their raw notes are in `research/raw/`. The checked summary is `docs/reading-list-notes.md`.
- Measured the dataset (`research/sources/`). Found that train contains val.

**Not checked**
- Most reading notes came through a summarising tool. See the "How far to trust this" note at the top of the reading notes.
