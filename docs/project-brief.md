# Project brief

Last changed 25 Nov 2026. This is the assignment in our own words, what we know about the data, and what is still open.

If this file and the assignment text on Canvas disagree, Canvas wins. Answers from the teachers or TAs win over everything.

Our goal is simple: meet every requirement of the assignment fully. We follow the course notebooks where we can and only add something when a requirement needs it.

## 1. What we hand in

One tutorial-style Jupyter notebook. In it, two LLM agents talk to each other to answer a user's request about a hotel or a restaurant.

- The **Beginner** starts every conversation. It knows the dialogue with the user. It does not know the reviews.
- The **Expert** knows the customer reviews (the DSTC11 Track 5 knowledge base).
- They talk until they have a reply for the user. The conversation has to stop by itself.
- We do this with **two versions of the Expert** and compare them.

| | |
| --- | --- |
| Deadline | Wed 9 Dec 2026, 23:59. One .ipynb on Canvas |
| Weight | 30% of the course. Half for the notebook, half for the oral defence |
| Oral defence | Thu 10 or Fri 11 Dec, with the teachers |
| Late | minus 10% per day |
| Group | Group 7: Antonia Bulai, Danila Popusoi, Goktug Yildirim |
| Gen AI | Allowed "in a limited way, with disclosure" (course intro slides). We state our use in the notebook |
| TA office hours | Fri 27 Nov and Fri 4 Dec, 13:00 to 14:00, NU-2B17 |

## 2. The requirements, and how we plan to meet each one

The plan column is a draft. The final choices go into `DESIGN.md`.

| # | The assignment asks for | Our plan (draft) |
| --- | --- | --- |
| R1 | At least 50 conversations, always started by the Beginner. The Beginner may quote the conversation history. Histories may come from DSTC | At least 50 dialogues from the DSTC11 test split, hotels and restaurants. Each one is run with both Expert versions. The Beginner opens by quoting the dialogue with the user |
| R2 | A way to stop the conversation. The output is a turn the system could send to the user | The Beginner ends the conversation by writing the reply for the user inside a tag, like the `<answer>` tags in Notebook 4. Code cuts the reply out. A cap on the number of turns catches conversations that do not end, and we count how often that happens |
| R3 | Agents designed for their role. The Expert knows the reviews, the Beginner does not | The Beginner's prompt holds only the dialogue with the user. The Expert's prompt holds the reviews of the hotel or restaurant. How the Expert gets them is open point A3 |
| R4 | Two versions of the Expert, with different prompting or fine-tuning | Two candidates. (a) Two prompting styles from Notebook 4: a plain instruction against a step-by-step one that first lists what the reviews say for and against. (b) A prompted model against one with a LoRA adapter, as in Notebook 2. We lean to (a) because it needs no training time |
| R5a | Objective metrics: turns before completion, length in tokens, and so on | Turns until the conversation stops, tokens per conversation (counted with the model's tokenizer), and how it ended (tag or cap) |
| R5b | Subjective metrics like in Notebook 3, with an LLM judge and with people. How often the request was fulfilled. Agreement between people and judge on a small set. The choice of that set is motivated by the judge's findings | An LLM judge as in Notebook 3, with criteria that fit this task: the three the dataset paper used for people (Appropriateness, Aspect Accuracy, Sentiment Accuracy) and a yes or no on "did the reply answer the request". The three of us rate about 15 to 20 conversations with the same criteria. We pick them after we see the judge's scores. Then we compute agreement between us, and between us and the judge |
| R6 | Every choice motivated, explained and tied to course material. If the results differ from what we expected, we reflect on why. Not too many references, and all of them correct | Each choice gets one or two sentences of why, with a pointer to a lecture or a reading. Every reference is opened and checked before hand-in (work package P) |
| R7 | The fixed structure: title with group ID and names, introduction, setup, methodology, experimental setup, results with figures or tables, conclusions (findings, lessons, future work), division of labour | The notebook sections follow this list in this order |

Not required, only if there is time: show the results separately for dialogues where the reviews agree and where they disagree. Notebooks 1 and 2 ask about this by hand, and the dataset paper says it is the hard part of the task.

We did not find a rubric with points per part in the course files. It is one of the TA questions.

## 3. What we measured in the data

The notebooks clone `github.com/lkra/dstc11-track5`. We ran the scripts in `research/tools/` on it on 24 Nov. The raw output is in `research/sources/`.

| | |
| --- | --- |
| Knowledge base | 33 hotels and 110 restaurants. 10 reviews each. 1,430 reviews, 8,013 review sentences |
| Review sentences per hotel or restaurant | about 52 (hotels) and 57 (restaurants), median |
| Dialogues that end in a question about reviews | train 16,897, val 2,129, test 2,798 |
| Dialogue history | always ends with the user. About 7 turns and 105 words, median |
| Relevant review sentences per dialogue | 3, median |
| Reference answer | 23 words, median |
| Test dialogues about one place, with reviews only | 1,762 (1,307 hotel, 455 restaurant) |

**The train split contains the validation split.** All 2,129 validation dialogues are also in train (16,897 = 14,768 + 2,129). A script in the data repo joins them (`CLTeamL/data_augmentation/combine_test_val.py`). No test dialogue is in train or val. So we take our dialogues from the **test** split. This matters most if one Expert is fine-tuned on train.

## 4. Open points, and what we do if nobody tells us otherwise

| # | Open point | Our default |
| --- | --- | --- |
| A1 | 50 conversations in total, or per Expert version? | At least 50 dialogues, each run with both versions |
| A2 | The assignment speaks of "booking based on preferences and constraints". In the data, the last user turn is a question like "Is the wifi reliable?" | The user request is the last user turn of a DSTC11 dialogue, read together with its history |
| A3 | May the Expert get the review sentences the dataset marks as relevant, or must it find them? | The Expert gets all reviews of the place and finds the relevant ones itself. Fine under both readings |
| A4 | Which models? | The two from the notebooks, Qwen3-1.7B and Qwen2.5-3B |
| A5 | Who are the people in the human evaluation? | The three of us. We rate without seeing which Expert it was |
| A6 | Do the graders run the notebook? | We build it so it runs top to bottom on Kaggle, and hand it in with the outputs saved |

A1, A3, A4 and A6 are in `docs/ta-questions.md`.

## 5. What `DESIGN.md` has to settle

1. What each agent sees, and who writes the final reply.
2. How the Expert gets the reviews.
3. The two Expert versions.
4. Which model, and the settings (temperature, token limit, thinking mode off).
5. The stopping rule and the cap on turns.
6. Which dialogues, and how many.
7. The counted metrics.
8. The judge: criteria, scale, prompt, which model.
9. The human rating: which conversations, the sheet, the agreement statistics.
10. How the notebook is put together: one file per section, saved results, running on Kaggle.

Each choice is written as: what we chose, why, what else we could have done, and which course material it connects to.

## 6. Not checked yet

- No model has been run. We do not know yet how well a small Qwen model keeps to its role, or how long a conversation takes.
- The reading notes in `docs/reading-list-notes.md` mark what was confirmed at the source and what was not.
- The papers of the student presentations were not read, except MultiWOZ and Mem0.
