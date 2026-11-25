# Where each design choice comes from

For every choice in `DESIGN.md` this table names the course material behind it. Canvas material comes first (lecture slides, notebooks, the assignment text), then the reading list.

- "Page" is the page of the PDF file in `course/lectures/`. It is not always the number printed on the slide.
- "Checked" means: the file was opened and the point was found on that page or in that cell, on the date given. `research/tools/find_in_slides.py` finds the page of a phrase in a lecture PDF.
- Section 2 lists what still has to be opened again before it can be a reference in the notebook.

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
| 22 | The judge is another model than the agents (4, 8) | Evaluation lecture | pages 49, 51, 53 | LLM judges agree less with people on machine text and may prefer their own style. Other biases: position, length, style. Open models can be reproduced | 25 Nov |
| 23 | No chain-of-thought for the judge (8) | Evaluation lecture | page 52 | Chain-of-thought did not reliably improve agreement with people | 25 Nov, slide only |
| 24 | We rate each conversation on a 1 to 5 scale (9) | Evaluation lecture | pages 15 and 16 | Per-dialogue rating captures the overall quality. Likert ratings can score one model at a time | 25 Nov |
| 25 | Rating guide with clear questions and examples (9) | Evaluation lecture | page 21 | Be specific, give examples, use the same scales, test the questions first | 25 Nov |
| 26 | Cohen's kappa, maybe Fleiss' kappa (9) | Evaluation lecture | page 19 | Cohen's kappa for 2 raters, Fleiss' kappa for more | 25 Nov |
| 27 | Spearman correlation (9) | Notebook 3 | Q7 | Spearman between metric pairs | 25 Nov |
| 28 | The human sample follows from the judge's results (9) | Assignment text on Canvas | requirement on subjective metrics | The selection for manual evaluation has to be motivated by the automated findings | 24 Nov |
| 29 | It runs on Kaggle (10) | Course intro, 28 Oct | page 21 | The notebooks are designed for Kaggle, 30 GPU hours per week | 25 Nov |

"Slide only" means we read the lecture slide. The paper the slide cites was not opened.

## 2. Reading list

| # | Choice (section) | Source | What we take from it | Status |
| --- | --- | --- | --- | --- |
| 30 | Judge criteria and the hard part of the task (3, 8) | Zhao et al. 2023, "What do others think?", SIGDIAL, pp. 309-323 | Human evaluation with Appropriateness, Aspect Accuracy, Sentiment Accuracy on a 5-point scale. Models are weakest on Sentiment Accuracy | Checked 24 Nov in the ACL Anthology PDF |
| 31 | Turns as efficiency (7) | Jurafsky and Martin, appendix "Frame-Based Dialogue Systems", draft of 6 Jan 2026, section K.0.2 | Task success, slot error rate, and efficiency as dialogue length in seconds or turns | Checked 24 Nov |
| 32 | Adjacency pairs, grounding, sub-dialogues (1) | Jurafsky and Martin, chapter "Conversation and its Structure", draft of 6 Jan 2026 | The same ideas as Lecture 1 | Section list checked 24 Nov. The wording has to be opened again |
| 33 | Task success and dialogue efficiency (7) | Deriu et al. 2021, Artificial Intelligence Review 54 | Evaluation of task-oriented systems | To open again. Read only through a summary so far |
| 34 | Check the judge against people (8, 9) | Bavaresco et al. 2025, ACL short papers | LLM judges have to be validated against human judgments. Kappa for categories, Spearman for grades | To open again. Read only through a summary so far |
| 35 | Two LLMs agreeing is no proof (5) | Kambhampati et al. 2024, ICML | LLMs cannot verify their own output, outside checks are needed | To open again. Read only through a summary so far |
| 36 | Each criterion has a name, a definition and a scale (8) | Howcroft et al. 2020, INLG (named in Notebook 3) | What to report about a human evaluation | To open again. Read only through a summary so far |

A second try to open rows 32 to 36 on 25 Nov did not go through. Until they are opened again, the notebook cites them only where a Canvas file in section 1 says the same thing.

## 3. Our own findings

| # | Choice (section) | How we know |
| --- | --- | --- |
| 37 | Dialogues come from the test split (6) | Measured: train contains all 2,129 validation dialogues. `research/sources/split-overlap.txt` |
| 38 | All reviews of a place fit in the prompt (2) | Measured: 478 to 1,243 words per place, median 760 |
| 39 | 1,762 usable test dialogues, 74% hotel (6) | Measured. `research/sources/pool-count.txt` |
