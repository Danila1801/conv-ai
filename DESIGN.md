# Design decisions

Draft 2, 25 Nov 2026. Work package A. Not agreed by the group yet: read it, and write what you would change in the pull request.

Two choices wait for the TAs (marked "waits for TA"). Six things can only be settled by running the pilot (section 11).

**Changed in draft 2**, after Antonia's design notes:
- Who writes the final reply is open again. Antonia's notes have the Expert write it after the Beginner agrees. The pilot now runs both ways (sections 1 and 5).
- The Beginner's first message says in one sentence what the user wants (section 1).
- Both agents are one small class and one function runs the conversation. The Expert versions are a config table, and every saved conversation carries its settings (section 10).
- Each choice now names the Canvas file and page behind it. The full table is `docs/evidence.md`.
- Not taken over: a fine-tuned Expert from Notebook 2 (reasons in section 3), and a text marker like "FINAL ANSWER:" (we use tags, as Notebook 4 does).

Later on 25 Nov the five sources that were marked "to re-check" were opened. Two sentences changed because of it: what Kambhampati et al. can be cited for (section 5), and which release of Jurafsky and Martin we cite (section 1).

Each decision is written the same way: what we chose, why, what else we could have done, which course material it connects to, and what would make us change it. Numbers that we picked ourselves are marked "our setting". They sit at the top of the notebook as variables.

Sources are marked: (checked) = opened and confirmed, (measured) = we ran it, (to re-check) = taken from our reading notes, has to be opened again before it becomes a reference in the notebook.

## 1. Roles: who sees what, and who writes the final reply

**Chosen.**
- The Beginner sees the dialogue with the user. It does not see any review. Its prompt is the same in every experiment, so only the Expert changes.
- Message 1 is the Beginner's. Code puts the dialogue with the user in it, word for word. The Beginner model adds one sentence on what the user wants, and its question to the Expert.
- The Expert sees what the Beginner writes, plus the reviews of the place. It answers the Beginner.
- After an Expert answer the Beginner either asks one follow-up question or moves to the end.

**Open: who writes the final reply.** The pilot runs both, and we decide by reading the conversations.

| | Option 1: the Beginner writes it | Option 2: the Expert writes it, after the Beginner says the answer covers the request |
| --- | --- | --- |
| Shortest conversation | 3 messages | 4 messages |
| For | The Beginner has a real job. The information has to travel through the conversation | The reply comes from the agent that has the reviews, so less gets lost. What we change (the Expert) directly produces what we measure (the reply) |
| Against | A small model may change facts when it rewrites the Expert's answer | The Beginner may just agree every time. The Post-training lecture shows that assistants tend to agree with their user (sycophancy, 20 Nov, PDF pages 30 and 31). That it also happens between two agents is our guess |

**Why.**
1. It is what the assignment describes: the Beginner starts and may quote the history, the Expert knows the reviews, the Beginner does not.
2. In both options the Beginner has no reviews, so what it needs has to come through the conversation. That is why the conversation is needed and why the number of turns means something.
3. It follows how conversation is described in Lecture 1 (Conversation and its Structure, 28 Oct, PDF pages 6 and 16): the Beginner's question and the Expert's answer are an adjacency pair, a follow-up is a clarification sub-dialogue, and the final reply shows that the Beginner understood the Expert (grounding). Same ideas in Jurafsky and Martin, chapter "Conversation and its Structure", release of 19 Aug 2026, sections on grounding and on subdialogues (checked).
4. The quote is added by code so it is exact. A small model that copies a 100-word dialogue can change it.
5. The whole dialogue is in message 1, and the Beginner sums up what the user wants. The Post-training lecture (20 Nov, PDF page 36) showed that models do worse when a task is spread over several turns, and recover when everything is in one message. It also fits the assignment, which speaks of a booking based on preferences and constraints: the Beginner's sentence is where those get named.
6. Two LLMs with one prompt each, talking to each other, is how the synthetic dialogues in Lecture 1 were made (PDF page 23).

**Other options.**
- The Expert answers the user directly and the Beginner checks nothing. Then the Beginner adds nothing and every conversation is two messages long.
- A free discussion without fixed jobs. Hard to stop, and a small model drifts.

**Decided by:** the pilot. We take the option whose final replies stay closer to the reviews. If both are equally good, the one with fewer format problems.

## 2. How the Expert gets the reviews (waits for TA, question 1)

**Chosen as default.** The Expert's prompt holds all reviews of the place the dialogue is about: 10 reviews, between 478 and 1,243 words, median 760 (measured). Which place it is comes from the dataset label (`entity_id`). The review sentences that the dataset marks as relevant for the dialogue are **not** given to the Expert. We keep them for the evaluation.

**Why.**
1. "The Expert should be aware of the knowledge base" is true under both readings of the assignment.
2. It fits in the prompt. The model's context is 32,768 tokens (model card, checked).
3. It needs no retrieval code.
4. The Expert has real work: find the sentences that matter among about 55. That is what makes it the expert.
5. The marked sentences stay independent, so the judge and we can check the final reply against them.

**Other options.**
- Give the Expert only the marked sentences, as Notebooks 1 and 4 do (`get_reviews`, `knowledge2sources`). Simplest, and the course does it. But the Expert then has almost nothing to do, and the TAs may read it as a shortcut.
- Retrieval over the whole knowledge base (Lecture 9, 25 Nov). One more part that can fail on its own and would need its own evaluation.

**Would change it:** if the TAs say the marked sentences are expected, we switch to `knowledge2sources`. It is a one-line change. If the pilot shows the 1.7B model cannot handle all reviews, same switch.

We only use dialogues about one place whose knowledge is reviews (no FAQs). There are 1,762 of those in the test split (measured).

## 3. The two Expert versions

**Chosen.**
- **Expert A, direct.** A plain instruction (zero-shot): answer the Beginner's question from the reviews in two or three sentences.
- **Expert B, step by step.** Same model, same reviews. The prompt makes it work in steps first (chain-of-thought): name what the user asks about, copy the review sentences about it and mark each as positive or negative, count them, then write the answer inside `<output>` tags. Only the `<output>` part goes to the Beginner. The steps are counted in the tokens.

**Why.**
1. Both are prompting methods from Notebook 4 (zero-shot, and chain-of-thought with tags) and from the Prompting lecture (18 Nov, PDF pages 19 and 27). They need no training. The same lecture advises to try well-engineered prompts before fine-tuning (page 53).
2. Only one thing differs between A and B, so a difference in the results can be explained.
3. It aims at the known hard part of this task. In the dataset paper's human evaluation, models come close to the human reference on fluency and relevance but not on "sentiment accuracy", which is whether the reply's mix of positive and negative matches the reviews (Zhao et al. 2023, human evaluation table, checked).

**What we expect** (written down now, because the assignment asks us to reflect if the results differ): B gets better sentiment accuracy than A, most of all when reviews disagree, and B costs more tokens. Turns should be about the same.

**Other options.**
- A few-shot Expert (Notebook 4). A good second choice. It needs hand-picked examples, which is one more choice to defend.
- A LoRA Expert (Notebook 2). The Notebook 2 adapter was trained on dialogues without reviews in the input, so it does not fit an Expert that reads reviews. A new adapter costs hours of GPU, and train contains val (measured).
- Tree of Thoughts (Notebook 4). About 30 model calls per dialogue there. Too slow for 120 conversations.

**Would change it:** if the pilot shows the model does not keep to the step format. Then fewer steps, or the 3B model for the agents.

## 4. Model and settings

**Chosen.**
- Both agents: Qwen3-1.7B, thinking mode off (`enable_thinking=False`), temperature 0.7, top-p 0.8, top-k 20.
- Token limit per message: 300 for the Beginner and Expert A, 600 for Expert B (our setting).
- Seed 3407, as in the notebooks.
- Judge: Qwen2.5-3B-Instruct with greedy decoding.

**Why.**
1. Qwen3-1.7B is the model of all four notebooks. Thinking is off there too, because it is slow.
2. Both agents use the same model, so they differ only in prompt and knowledge.
3. The sampling values are the ones the Qwen3 model card gives for non-thinking mode (checked). The Prompting lecture says to check the model card for this (PDF page 48).
4. The judge is a different model from the agents. The Evaluation lecture (13 Nov, PDF page 49) warns that LLM judges lean towards their own kind of text. In the paper behind it, the judges agree less with people on machine text than on human text (Bavaresco et al. 2025, section 4, checked). Qwen2.5-3B is also a notebook model, so we need no permission for it (TA question 2 asks anyway).
5. The judge decodes greedily so its scores are the same on every run, like the evaluators in Notebook 4.

**Other options.** Qwen2.5-3B for the agents: the pilot can show if it is needed. Greedy decoding for the agents: the model card gives sampling values for this mode and warns against greedy decoding in thinking mode, so we follow the card. With sampling we fix the seed and save every conversation, so the numbers in the notebook are the ones we analysed.

## 5. How a conversation stops

**Chosen.**
- The writer (Beginner or Expert, see section 1) ends the conversation by writing the reply for the user inside `<answer>` and `</answer>`.
- After every message of the writer, code looks for a complete tag. If it is there, the conversation stops and the text inside is the final reply.
- Cap (our setting): 7 messages if the Beginner writes, 8 if the Expert writes, so the last message is always the writer's. The last message gets an extra line: "This is your last message, write the reply now." A conversation that needed this is marked "stopped by cap".
- An `<answer>` that comes too early, or from the other agent, is cut out and counted as a format problem. Too early means before message 3 if the Beginner writes, and before message 4 if the Expert writes.

**Why.**
1. The assignment asks for a stopping mechanism and for a turn that can be sent to the user. The tag gives both.
2. Notebook 4 does the same with `<answer>` and `<output>` tags.
3. Code decides whether the conversation is over, not a model. So it always ends, and we can count how it ended.
4. The shortest conversation is 3 or 4 messages and the longest 7 or 8, so "turns until completion" can differ between conversations.

**Other options.** A fixed number of turns: then the turn count is the same everywhere and measures nothing. A plain text marker like "FINAL ANSWER:": it works too, but Notebook 4 already uses tags and they are easier to cut out. A third model as referee: more calls, and LLMs are not reliable at checking output. Kambhampati et al. 2024 (section 2.2, checked) show this for plans. That it also holds for a referee in our conversations is our own step.

## 6. Which dialogues, and how many

**Chosen.** 60 dialogues from the test split (our setting): 30 hotel, 30 restaurant, drawn at random with seed 3407 from the 1,762 usable ones. Each is run with Expert A and with Expert B. That gives 120 conversations.

**Why.** It is at least 50 under both readings of the assignment (TA question 3). Test split, because train contains val (measured). Half hotel and half restaurant, because the pool is 74% hotel (1,307 of 1,762, measured). 60 and not 50, so a few failures do not push us under 50.

**Other option.** The first 50 of train, as the notebooks do. Not random, and it is the split a fine-tuned model would have seen.

## 7. Counted metrics

Per conversation:
- number of messages until it stopped,
- tokens the models wrote, in total and per agent (counted with the model's tokenizer; for Expert B the hidden steps are counted separately),
- how it stopped (answer tag or cap),
- seconds (only as information, it depends on the hardware).

Reported per Expert version as mean and median, in one table and one figure. A and B run on the same dialogues, so we also report the difference per dialogue.

Only if there is time: ROUGE-L and BERTScore of the final reply against the dataset's reference answer, with the functions from Notebook 3.

**Course link.** The Evaluation lecture (13 Nov, PDF pages 5 and 6) names task success rate and dialogue efficiency as the metrics for task-oriented dialogue, and counts turns in its example. Efficiency measured as length in turns is also in Jurafsky and Martin, appendix "Frame-Based Dialogue Systems", section on evaluating task-based dialogue (checked), and in Deriu et al. 2021, section 3.4 (checked in the arXiv copy). Counting tokens is our own extension of "length".

## 8. The LLM judge

**Chosen.** Four questions about the final reply. The first three are the criteria of the dataset paper's human evaluation, in our words:

| Criterion | Scale | Meaning |
| --- | --- | --- |
| Appropriateness | 1 to 5 | The reply is fluent and fits naturally after the user's last message |
| Aspect accuracy | 1 to 5 | The reply gives relevant and useful information about the thing the user asked about |
| Sentiment accuracy | 1 to 5 | The share of positive and negative opinion in the reply matches the reviews |
| Request fulfilled | yes or no | The reply answers what the user asked, and what it says agrees with the reviews |

The judge sees the dialogue with the user, the review sentences the dataset marks as relevant, and the final reply. One criterion per call. The answer comes as JSON inside `<JSON>` tags, as in Notebook 3. If it cannot be parsed we ask once more, then count it as missing.

**Why.**
1. Notebook 3's judge gives one "coherence" score from the user input and the reply. The assignment also wants "how often the request was fulfilled", and that cannot be judged without the reviews.
2. These criteria were made for exactly this task and come with definitions (Zhao et al. 2023, checked).
3. A 1 to 5 scale, because we rate the same conversations by hand and nobody can rate "0.73".
4. One criterion per call keeps each prompt short for a small model.
5. The judge does not reason step by step first. The Evaluation lecture reports that chain-of-thought did not reliably improve agreement with people (PDF page 52). The paper behind that slide says the same (Bavaresco et al. 2025, appendix H, checked).

**Other options.** Notebook 3's coherence judge unchanged: it does not answer the fulfilment question. All criteria in one call: fewer calls, but small models mix the scores up.

## 9. Human rating and agreement

**Chosen.**
- All three of us rate the same 30 conversations: 15 dialogues, each with Expert A and Expert B (our setting).
- We pick them after the judge has scored everything: the 10 dialogues where the judge's scores for A and B differ most, and 5 at random from the rest.
- The order is shuffled and the sheet does not say which Expert it was.
- Same four criteria and scales as the judge.
- Agreement on yes/no: Cohen's kappa for each pair of raters, and for our majority vote against the judge. Agreement on 1 to 5: Spearman correlation for each pair of raters, and for our mean score against the judge.

**Why.**
1. The assignment wants the choice of the manual set to follow from the judge's findings, for example to check that an improvement "stems from the right reasons". The dialogues where the judge sees the biggest difference are where its verdict matters most. The random ones show whether it also holds elsewhere.
2. Cohen's kappa is in the Evaluation lecture (13 Nov, PDF page 19). Spearman is what Notebook 3 uses to compare metrics (Q7).
3. One rating per conversation on a 1 to 5 scale is the per-dialogue Likert option from the same lecture (pages 15 and 16). The rating guide follows its advice: clear questions, examples, the same scales, and a test round first (page 21).

**Other options.** Fleiss' kappa for three raters at once (also in the Evaluation lecture): can be added. Pairwise "which reply is better" ratings: more work for us.

## 10. How the notebook is put together

- Both agents are one small `Agent` class, and one `run_conversation` function runs them. What differs between Expert A and Expert B sits in one config table. A new variant is a new row in that table, not new code.
- While we work, each notebook section is its own file in `notebook/sections/`: text as `.md`, code as `.py` with `# %%` between cells. `notebook/build_notebook.py` joins them into the one `.ipynb` we hand in. So two people never edit the same file.
- Results are saved in `results/`: `conversations.jsonl`, `judge_scores.csv`, `human_ratings.csv`.
- A switch at the top of the notebook, `USE_SAVED_RESULTS`. On: load the saved files, the notebook runs in minutes. Off: generate everything again (waits for TA, question 4).
- It runs on Kaggle with a T4 GPU, like the course notebooks.

One line of `conversations.jsonl` (work packages F and G build on this):

    {"dialogue_id": 123, "domain": "hotel", "entity_id": "7", "entity_name": "...",
     "expert_version": "A", "final_writer": "beginner",
     "config": {"model": "Qwen/Qwen3-1.7B", "seed": 3407, "temperature": 0.7, "max_messages": 7},
     "history": [{"speaker": "U", "text": "..."}],
     "gold_reviews": ["..."], "reference_response": "...",
     "messages": [{"n": 1, "agent": "beginner", "text": "...", "hidden": "",
                   "new_tokens": 41, "seconds": 2.3, "format_ok": true}],
     "final_reply": "...", "stop_reason": "answer_tag", "n_messages": 3, "n_new_tokens": 180}

## 11. What the pilot has to tell us

The pilot (`pilot/pilot.ipynb`) runs 6 dialogues, 3 hotel and 3 restaurant, with both Experts and both ways of writing the final reply. That is 24 conversations.

1. Does the model keep its role? The Beginner must not invent review facts. The Expert must not write the reply for the user when that is not its job, or before the Beginner agreed.
2. Does Expert B keep to the steps and the `<output>` tag?
3. How often does the conversation end with the `<answer>` tag, and after how many messages?
4. How many seconds does a conversation take? From that: the time for 120 conversations and 480 judge calls.
5. How many tokens is the Expert's prompt with all reviews of a place?
6. Which way of writing the final reply gives replies that stay closer to the reviews (section 1)?

## 12. What we are not doing

- No fine-tuned Expert and no retrieval. Reasons in sections 2 and 3. Both go under future work.
- No dialogues about two places at once, and no FAQ knowledge. It keeps the Expert's prompt simple.
- No results split by "reviews agree" against "reviews disagree" in the main plan. Only if there is time.

## 13. Where the choices come from

`docs/evidence.md` has one row per choice: the source, the page or cell, what it says, and when we checked it. Canvas files (lectures, notebooks, the assignment) come first, then the reading list. All sources in it were opened by 25 Nov. Left to confirm: the volume and pages of Deriu et al. on the publisher's page.
