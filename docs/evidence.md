# Where each design choice comes from

For every choice in `DESIGN.md` this table names the course material behind it. Canvas material comes first (lecture slides, notebooks, the assignment text), then the reading list.

- "Page" is the page of the PDF file in `course/lectures/`. It is not always the number printed on the slide.
- "Checked" means: the file was opened and the point was found on that page or in that cell, on the date given. `research/tools/find_in_slides.py` finds the page of a phrase in a lecture PDF.
- Section 2 is the reading list. All of it was opened by 25 Nov. What is left to confirm is listed under its table.

## 1. Canvas material (checked)

| # | Choice (section in DESIGN.md) | Source | Where | What it says, in our words | Checked |
| --- | --- | --- | --- | --- | --- |
| 1 | Two LLM agents talk to each other (1) | Lecture 1, Conversation and its Structure, 28 Oct | page 23 | Synthetic conversations made with two prompts, one per role, are shown as a way to get dialogue data | 25 Nov |
| 2 | Beginner asks, Expert answers (1) | Lecture 1 | page 6 | Adjacency pairs: a question is followed by an answer | 25 Nov |
| 3 | A follow-up question is allowed (1) | Lecture 1 | page 6 | Side sequences: detours for clarifications and corrections | 25 Nov |
| 4 | The Beginner shows it understood before the end (1) | Lecture 1 | page 16 | Grounding: a contribution has a presentation phase by the speaker and an acceptance phase by the hearer | 25 Nov |
| 5 | Replies are short and only from the reviews (1, 3) | Lecture 1 | page 13 | Grice's maxims: quality (truthful, with evidence) and quantity (as informative as needed) | 25 Nov |
| 6 | The whole dialogue is in message 1, and the Beginner says what the user wants (1) | Lecture Transformers, Post-training and Alignment, 20 Nov | page 36 | Over 15 LLMs and 6 tasks, performance fell from 90% to 65% when the instructions came over several turns. Full information in one message restored it | 25 Nov, slide only |
| 7 | Risk that the Beginner just agrees (1) | same lecture | pages 30 and 31 | Sycophancy: assistants tend to agree with the user's view. The slides are about a model and a human user. That it also happens between our two agents is our own guess, and the pilot has to show it | 25 Nov, slide only |
| 8 | The Expert gets reviews in its prompt (2) | Notebook 1, Notebook 4 | N1: Q3, `get_reviews`. N4: `knowledge2sources` | The course gives the model the review sentences from `knowledge.json` | 25 Nov |
| 9 | Expert A zero-shot, Expert B chain-of-thought (3) | Prompting lecture, 18 Nov. Notebook 4 | pages 19 and 27. N4: Q1 to Q4 | Zero-shot and few-shot prompts. Chain-of-thought splits a task into simpler steps. N4 asks for the answer inside `<output>` tags | 25 Nov |
| 10 | Prompting, not fine-tuning, for both Experts (3) | Prompting lecture | page 53, pages 9 to 11 | "Use fine tuning when appropriate, try well engineered prompts first". Pros and cons of fine-tuning | 25 Nov |
| 11 | The Notebook 2 adapter does not fit an Expert that reads reviews (3) | Notebook 2 | text above `reformat_dataset` | The training examples hold only the dialogue and the response, no reviews | 25 Nov |
| 12 | Tree of Thoughts is too slow here (3) | Notebook 4 | Tree-of-Thoughts section, intro text | About 30 model calls per dialogue with the default settings | 25 Nov |
| 13 | Role and task are stated in the system prompt (3) | Prompting lecture | page 47 | Supplying mission and vision in the prompt reduces hallucinations | 25 Nov |
| 14 | Steps are a numbered list (3) | Prompting lecture | page 50 | Structured text works better than a wall of text | 25 Nov |
| 15 | Replies have a length limit (3, 4) | Prompting lecture | page 53 | Limit the output length | 25 Nov |
| 16 | Sampling values come from the model card (4) | Prompting lecture. Qwen3-1.7B model card | page 48. Card: non-thinking mode | Lower temperature for deterministic tasks, and check the model card. Card: temperature 0.7, top-p 0.8, top-k 20, context 32,768 | 25 Nov |
| 17 | Thinking mode off (4) | Notebook 4 | text above `query_qwen` | It is switched off because it makes the model much slower | 25 Nov |
| 18 | Seed 3407 (4, 6) | Notebook 2, Notebook 4 | N2: imports cell. N4: `run_pipeline_tot` | The course uses this seed | 25 Nov |
| 19 | The reply is inside a tag that code cuts out (5) | Notebook 4 | Q4 (`<output>`), Tree-of-Thoughts step 3 (`<answer>`) | The course does it the same way | 25 Nov |
| 20 | Turns as a metric, and task success (7) | Evaluation lecture, 13 Nov. Lecture 2, 30 Oct | pages 5 and 6. Pages 8 and 20 | Task-oriented dialogue is measured by task success rate and dialogue efficiency. The example counts 3 turns. Success means task completion | 25 Nov |
| 21 | Judge returns JSON inside tags (8) | Notebook 3 | `query_qwen_as_a_judge` | Coherence judge with `<JSON>` tags and a parser | 25 Nov |
| 22 | The judge is another model than the agents (4, 8) | Evaluation lecture | pages 49, 51, 53 | LLM judges agree less with people on machine text and may prefer their own style. Other biases: position, length, style. Open models can be reproduced | 25 Nov, slide. The paper behind page 49: row 34 |
| 23 | No chain-of-thought for the judge (8) | Evaluation lecture | page 52 | Chain-of-thought did not reliably improve agreement with people | 25 Nov, slide. The paper behind it: row 34 |
| 24 | We rate each conversation on a 1 to 5 scale (9) | Evaluation lecture | pages 15 and 16 | Per-dialogue rating captures the overall quality. Likert ratings can score one model at a time | 25 Nov |
| 25 | Rating guide with clear questions and examples (9) | Evaluation lecture | page 21 | Be specific, give examples, use the same scales, test the questions first | 25 Nov |
| 26 | Cohen's kappa, maybe Fleiss' kappa (9) | Evaluation lecture | page 19 | Cohen's kappa for 2 raters, Fleiss' kappa for more | 25 Nov |
| 27 | Spearman correlation (9) | Notebook 3 | Q7 | Spearman between metric pairs | 25 Nov |
| 28 | The human sample follows from the judge's results (9) | Assignment text on Canvas | requirement on subjective metrics | The selection for manual evaluation has to be motivated by the automated findings | 24 Nov |
| 29 | It runs on Kaggle (10) | Course intro, 28 Oct | page 21 | The notebooks are designed for Kaggle, 30 GPU hours per week | 25 Nov |

"Slide only" means we read the lecture slide. The paper the slide cites was not opened.

## 2. Reading list

All seven were opened. "Where" is the section in the copy we read.

| # | Choice (section) | Source | Where | What we take from it | Checked |
| --- | --- | --- | --- | --- | --- |
| 30 | Judge criteria and the hard part of the task (3, 8) | Zhao et al. 2023, "What do others think?", SIGDIAL, pp. 309-323 | Human evaluation table | Human evaluation with Appropriateness, Aspect Accuracy, Sentiment Accuracy on a 5-point scale. Models are weakest on Sentiment Accuracy | 24 Nov, ACL Anthology PDF |
| 31 | Turns as efficiency (7) | Jurafsky and Martin, appendix K "Frame-Based Dialogue Systems", release of 19 Aug 2026 | Section K.0.2, Evaluating Task-Based Dialogue | Task success rate, slot error rate, and efficiency as the length of the dialogue in seconds or in turns | 25 Nov, live file. 24 Nov, January 2026 file, same section |
| 32 | Adjacency pairs, grounding, sub-dialogues (1) | Jurafsky and Martin, chapter "Conversation and its Structure", release of 19 Aug 2026 (chapter 26 there, chapter 25 in the January 2026 files) | Sections 26.1.3 Grounding and 26.1.4 Subdialogues and Dialogue Structure | The hearer signals that they understood. A question expects an answer (adjacency pair). A clarification or a correction can sit between the two parts | 25 Nov, live file. The chapter calls itself a first stub. "Presentation and acceptance phase" is the wording of Lecture 1, we did not look for it in the book |
| 33 | Task success and dialogue efficiency (7) | Deriu et al. 2021, "Survey on evaluation methods for dialogue systems", Artificial Intelligence Review | Section 3.4 Evaluation. 3.4.1 for PARADISE. 2.2 for what a good evaluation method needs | Task-success rate: did the system meet the user's goal. Dialogue efficiency: number of turns or elapsed time | 25 Nov, arXiv:1905.04071 version 2 (26 Jun 2020). Volume 54(1) and pages 755-810 are only from a search result |
| 34 | Check the judge against people (8, 9). No chain-of-thought for the judge (8). The judge is not the agents' model (4) | Bavaresco et al. 2025, "LLMs instead of Human Judges?", ACL 2025 short papers, pp. 238-255 | Section 3 for the statistics. Sections 1 and 5 for the conclusion. Appendix H for chain-of-thought. Section 4 for human against machine text | Cohen's kappa for categories and Spearman for grades. An LLM judge has to be validated against human ratings for the task first. Chain-of-thought gave no reliable gain. The models agree more with people on human-written text than on machine text | 25 Nov, arXiv:2406.18403 version 3 (2 Jun 2025). Volume and pages from the ACL Anthology page. The Anthology PDF itself was not opened |
| 35 | No third LLM as referee for stopping (5) | Kambhampati et al. 2024, "Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks", ICML, PMLR 235, pp. 22895-22907 | Section 2.2. Section 3.1 for outside critics | LLMs are not reliable at verifying plans, so self-critique does not reliably help. Correctness has to come from outside verifiers | 25 Nov, arXiv:2402.01817 version 3 and the PMLR page. The paper is about planning. It says nothing about two LLMs checking each other. Using it for our case is our own step, and the notebook has to say so |
| 36 | Each criterion has a name, a definition and a scale (8, 9) | Howcroft et al. 2020, "Twenty Years of Confusion in Human Evaluation", INLG, pp. 169-182 (named in Notebook 3) | Section 5 and Table 7 | A human evaluation should report at least the criterion's name and definition, the scale, and the exact question and instructions the raters got. Based on 165 INLG and ENLG papers from 2000 to 2019 | 25 Nov, ACL Anthology PDF. It gives no standard definitions to adopt. Ours come from Zhao et al. |

Left to do before these become references in the notebook:

- Deriu et al.: confirm volume, issue and pages on the publisher's page, https://doi.org/10.1007/s10462-020-09866-x. That page did not open in the assistant's session.
- Trap in the book: on the book's site the file `25.pdf` is now "Discourse Coherence". "Conversation and its Structure" is `26.pdf` in the release of 19 Aug 2026. Lectures 1 and 2 cite that release, so we cite it too. The January 2026 files are under `old_jan26/`.

## 3. Our own findings

| # | Choice (section) | How we know |
| --- | --- | --- |
| 37 | Dialogues come from the test split (6) | Measured: train contains all 2,129 validation dialogues. `research/sources/split-overlap.txt` |
| 38 | All reviews of a place fit in the prompt (2) | Measured: 478 to 1,243 words per place, median 760 |
| 39 | 1,762 usable test dialogues, 74% hotel (6) | Measured. `research/sources/pool-count.txt` |
