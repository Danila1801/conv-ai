# Hand-over log

Newest entry on top. One entry per working session. Keep entries short.

## Wed 25 Nov 2026 (session 4), Goktug's Claude session (claude.ai, cloud)

**Done**
- Opened the five sources that were marked "to re-check": Jurafsky and Martin (chapter "Conversation and its Structure" and appendix K), Deriu et al. 2021, Bavaresco et al. 2025, Kambhampati et al. 2024, Howcroft et al. 2020. `docs/evidence.md` section 2 now says where each point sits. `DESIGN.md` and `docs/reading-list-notes.md` are updated to match.
- `CLAUDE.md`: the line about Antonia now says she has the free Claude plan. Goktug said so in the chat.

**Found**
- On the book's site, `25.pdf` is now "Discourse Coherence". "Conversation and its Structure" is `26.pdf` in the release of 19 Aug 2026. We cite that release, as Lectures 1 and 2 do.
- Kambhampati et al. 2024 is about planning. It shows that LLMs do not verify plans reliably. It says nothing about two LLMs checking each other. `DESIGN.md` section 5 now says that this step is ours.

**Checked**
- Each row 31 to 36 of `docs/evidence.md` was read in the copy named in its last column (arXiv copies for three papers).

**Not checked**
- Volume 54(1) and pages 755-810 of Deriu et al. on the publisher's page. The page did not open from this session.
- The ACL Anthology PDF of Bavaresco et al. (the arXiv copy of 2 Jun 2025 was read).
- The pilot has still not run with the real model.

**Next**
- Same as session 3: Dan or Antonia run the pilot, then decide who writes the final reply and build D and E.

## Wed 25 Nov 2026 (session 3), Goktug's Claude session (claude.ai, cloud)

**Done**
- `DESIGN.md` is now draft 2. Antonia's design notes were compared with draft 1. Taken over: one `Agent` class and one conversation function with the Expert versions as a config table, the Beginner says what the user wants in its first message, every saved conversation carries its settings, and the option that the Expert writes the final reply after the Beginner agrees. Not taken over: a fine-tuned Expert from Notebook 2, and a plain text marker in place of tags. The list is at the top of `DESIGN.md`.
- The pilot now runs both ways of writing the final reply: 6 dialogues x 2 Experts x 2 ways = 24 conversations.
- `docs/evidence.md`: one row per design choice with the Canvas file, the PDF page or notebook cell, and the date it was checked.
- `research/tools/find_in_slides.py`: finds the page of a phrase in a lecture PDF.

**Checked**
- `python pilot/test_loop.py <data dir>` passes: 24 conversations with canned replies, every stopping case for both ways of writing the reply.
- `pilot/pilot.ipynb` was rebuilt, passes the nbformat check, and its code cells compile.
- Every page number in section 1 of `docs/evidence.md` was looked up in the PDF files in `course/lectures/`. The notebook facts were looked up in `course/notebooks/`.

**Not checked**
- The pilot has still not run with the real model. Goktug's Kaggle account is not phone verified, so the GPU was locked.
- Rows 32 to 36 of `docs/evidence.md` (four reading-list papers and the wording of one book chapter) could not be opened again in this session.

**Next**
- Dan or Antonia run the pilot on Kaggle (see `STATUS.md`).
- With the result: decide who writes the final reply, fix prompts and settings, then build D and E in `notebook/sections/`.
- Open rows 32 to 36 again.

## Wed 25 Nov 2026 (session 2), Goktug's Claude session (claude.ai, cloud)

**Done**
- `DESIGN.md`, draft 1: twelve sections, each with what we chose, why, the other options and the course link. Branch `wp-a-design`.
- `pilot/pilot.py` and `pilot/pilot.ipynb`: 6 test dialogues, Expert A (direct) and Expert B (step by step), conversation loop, stopping by `<answer>` tag with a cap of 7 messages, saves `pilot_conversations.jsonl`.
- `notebook/build_notebook.py`: builds a .ipynb from a .py file with `# %%` cell marks.
- Added the files from Goktug's local course folder that the repo did not have (three lectures, two teasers, Notebooks 3 and 4, the reading list). `presentation/` was put back.

**Checked**
- `python pilot/test_loop.py <data dir>` passes: 12 conversations with canned replies, every stopping case (quick, follow-up, never answers, answer too early) ends as section 5 of the design says.
- The code cells of `pilot/pilot.ipynb` compile, and the notebook file passes the nbformat check.
- Qwen3 model card opened for the sampling values and the context length used in the design.
- Size of the Expert's first prompt in the six pilot dialogues: about 1,020 words on average for Expert A and 1,070 for Expert B. This is a word count from the canned run, not a real token count.

**Not checked**
- The pilot has never run with the real model. Nothing is known yet about role keeping, the step format of Expert B, or speed.
- The design has not been reviewed by anyone. Sources marked "to re-check" in it have not been opened again.

**Next**
- Goktug runs the pilot on Kaggle. With the result: fix prompts and settings, then build work packages D and E properly in `notebook/sections/`.
- After the TA answers on Friday: settle sections 2 and 10 of the design.
- Dan can start C, and G once the criteria in section 8 are agreed.

## Wed 25 Nov 2026, Goktug's Claude session (claude.ai, cloud)

**Done**
- Turned this repo from the presentation repo into the project repo, on the branch `final-project-setup` (not merged, a person does that).
  - Removed the old `project/README.md` placeholder (still in the history, commit `e1c909a`). `presentation/` stays as it was.
  - Moved `notebooks/` to `course/notebooks/`.
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
