# Reading list: what each source is, and what the final project may cite it for

Made 24 Nov 2026. Ten agents opened every link in `CAI_Reading_List_Links.html` (36 book PDFs, 11 reading-list items, 4 extra syllabus papers, plus Howcroft et al., which Notebook 3 points to).

**How far to trust this.** The agents read through a tool that returns a small model's summary of each page, not the raw text. So:
- **checked** = the main session opened the source again and confirmed the point.
- **agent** = reported by one agent, not yet confirmed. Open the PDF before you cite a number, a section or a page from these lines.
- **search** = seen only in a search result or a library record.

Before anything from here goes into the notebook as a reference, it is opened once more. That is planned for 7 Dec.

## 1. Citation traps

| # | Trap | What is right | How known |
| --- | --- | --- | --- |
| 1 | Jurafsky and Martin chapter numbers. Three numberings are in use | The chapter files of the January 2026 draft print: 5 Embeddings, 7 Large Language Models, 8 Transformers, 9 Post-training: Instruction Tuning, Alignment, and Test-Time Compute, 10 Masked Language Models, 11 Information Retrieval and Retrieval-Augmented Generation, 25 Conversation and its Structure, K Frame-Based Dialogue Systems. The full-book PDF of the same date lists 9 Masked Language Models, 10 Post-training, 11 "Retrieval-based Models". The lecture slides cite a later draft (19 Aug 2026) where it is "Chapter 26: Conversation and its Structure", "Chapter 7: Transformers and Pretraining" and "Chapter 8: Post-training". **Cite by chapter title, draft date and file URL, never by number alone** | contents page and ch. 25, K: checked. Others: agent |
| 2 | Brown et al. (2020). The Canvas page lists "Mann, B." first | First author is Tom B. Brown. Published in Advances in NeurIPS 33, pp. 1877-1901. The Prompting slides have it right | agent |
| 3 | MultiWOZ. The Canvas page says 2020 | EMNLP 2018, pp. 5016-5026 | agent |
| 4 | Tree of Thoughts. The Canvas page says 2024 | NeurIPS 2023 (Advances in NeurIPS 36) | search |
| 5 | Kambhampati, Stechly and Valmeekam (2025). The Wiley page does not open from here | The free copy is arXiv:2504.09762 **version 1**. Later versions under the same arXiv number are a different paper ("Stop Anthropomorphizing Intermediate Tokens..."). Journal details: Annals of the NYAS 1547(1), pp. 33-40 | v1: checked. Pages: search |
| 6 | Mem0. The Canvas page says ECAI | arXiv:2504.19413 names no venue. A Crossref record lists ECAI 2025 (IOS Press) | search |
| 7 | Baez Santamaria et al. (2023). Two author orders in the slides | Printed order: Baez Santamaria, Krause, Donatelli, Vossen. The agent did not find the subtitle "Towards Enhanced Data Modelling and Long-term Memory" in the PDF | agent |
| 8 | Where things sit in the January 2026 chapter files | Temperature: ch. 7, section 7.4.3. Top-k and top-p: ch. 8, section 8.6. LoRA: ch. 8, section 8.8.3 (not in Post-training). In-context learning: 7.3 and 8.9.1. Chain-of-thought: ch. 9, section 9.4.1 | agent |
| 9 | Zhao et al. (2023) page numbers | Proceedings of the 24th SIGDIAL meeting, pp. 309-323 | checked |
| 10 | Deriu et al. year | Artificial Intelligence Review 54(1), pp. 755-810. Online 25 June 2020, issue dated 2021. Open access | search |
| 11 | Lecture numbers. The Canvas schedule and the slide titles count differently | The Evaluation lecture is "L6" on Canvas and "Lecture 3" on its slides. The slides titled "Lecture 6" are Transformers, Post-training and Alignment. **Cite a lecture by its title and date** | checked |

## 2. High relevance

| Source | What it is | What we may cite it for | What it does not support |
| --- | --- | --- | --- |
| **Zhao et al. (2023)**, "What do others think?", SIGDIAL | The paper behind our data. Crowd-written reviews (10 each for 33 hotels and 110 restaurants) added to MultiWOZ dialogues. Three subtasks: turn detection, knowledge selection, response generation | The task and data (19,696 instances; 1,430 reviews; 8,013 sentences). The human-evaluation criteria: Appropriateness, Aspect Accuracy, Sentiment Accuracy, 5-point scale, 240 instances, 3 raters, Gwet's gamma 0.73 / 0.75 / 0.62. The generative models come close to the reference on the first two (4.40 to 4.58 against 4.70, and 4.54 to 4.68 against 4.77) and lag on Sentiment Accuracy (3.20 to 3.98 against 4.50). The stated hard part: combining reviews that disagree. All checked | It gives no share of agreeing against disagreeing reviews. "Unseen" test items are unseen aspects, not unseen entities |
| **J&M appendix K**, Frame-Based Dialogue Systems | Frames, slots, state tracking, policy, generation | Section K.0.2: task success, slot error rate, and efficiency measured as dialogue length in seconds or turns. Checked. This is the textbook citation for "number of turns" | No user satisfaction, no PARADISE, nothing on LLMs. Checked |
| **Deriu et al. (2021)**, survey | Sorts dialogue systems into task-oriented, conversational, question answering, and gives evaluation methods for each | Section 3.4: task success and dialogue efficiency (turns, time, repair turns), PARADISE. Section 2.2: lab, in-field and crowd evaluation; what a good evaluation method should be. Agent | Tokens are not mentioned. Counting tokens is our own extension of "dialogue length" |
| **Bavaresco et al. (2025)**, ACL short | JUDGE-BENCH: 20 datasets, 11 LLMs, over 70,000 instances. Agreement measured with Cohen's kappa (categories) and Spearman (grades) | LLM judges vary a lot by task and property, so validate against humans first. Chain-of-thought does not reliably help the judge. Judges agree better with humans on human text than on machine text. Agent | The models are 7B and larger. The dialogue sets are chit-chat. No result for our kind of task |
| **Smith et al. (2022)**, NLP4ConvAI | Compares per-turn and per-dialogue, pairwise and single-model human ratings | No method wins everywhere. Pairwise is more sensitive when replies differ in length; per-turn when replies are nonsense; whole-dialogue for subtle differences. Agent | Crowd workers chatting live in chit-chat. No advice on sample size for 10 to 20 conversations |
| **Howcroft et al. (2020)**, INLG (from Notebook 3) | 165 NLG papers: criterion names and definitions are a mess | The duty to report, for each criterion, its name, definition, scale and the exact instructions. Agent | It gives no standard definitions to adopt. We take ours from Zhao et al. |
| **J&M ch. 25**, Conversation and its Structure | Turns, speech acts, grounding, subdialogues, initiative, implicature, dialogue acts | Adjacency pairs (question, answer), clarification subdialogues, grounding (presentation and acceptance), closing acts. Sections 25.1.1 to 25.2 checked | No stopping rule and no evaluation. The four Gricean maxims are listed in Lecture 1, not here (agent) |
| **J&M ch. 7**, Large Language Models | Prompting, sampling, training, evaluation, harms | System prompts, zero-shot, few-shot, in-context learning (7.3). Temperature (7.4.3). Hallucination and sycophancy (7.7). Agent | No recommended temperature. No LLM-as-a-judge |
| **J&M ch. 8 and ch. 9** | Transformers; post-training | LoRA: frozen W, trained A and B (8.8.3). Top-k, top-p (8.6). Supervised fine-tuning (9.1). DPO (9.3.2). Chain-of-thought as test-time compute (9.4.1). Agent | No comparison of LoRA with prompting. Parts of ch. 9 are unfinished stubs |
| **J&M ch. 11**, IR and RAG | tf-idf, BM25, dense retrieval, RAG | RAG as "retrieve, then generate from the passages", used to reduce hallucination by grounding (11.4). BM25 (11.1). Agent | Single questions only, not conversations |
| **Kambhampati et al. (2024)**, ICML position paper | LLMs cannot plan or verify their own output; pair them with outside critics (LLM-Modulo) | A warning: two LLM agents agreeing is not proof the answer is right, so add a check that does not depend on them. Title, authors, venue checked; content agent | It does not study one LLM checking another in a dialogue. Do not say it shows that fails |
| **Brown et al. (2020)** and **Yao et al. (2023)** | Few-shot learning; Tree of Thoughts | Definitions of zero-, one- and few-shot. Search over "thoughts" and its token cost (about 5 to 100 times chain-of-thought). Agent | Results are on other tasks (Game of 24 and similar) |

## 3. Medium and low relevance

| Source | One line | Use for us |
| --- | --- | --- |
| Budzianowski et al. (2018), MultiWOZ | 10,438 Wizard-of-Oz dialogues, 7 domains (agent) | One sentence on where the dialogue histories come from |
| J&M ch. 12, Machine Translation, section 12.6 | Human rating, BLEU, chrF, BERTScore, bootstrap test (agent) | Textbook source for BLEU and BERTScore if we report them. ROUGE is not in these chapters |
| J&M ch. 4, section 4.11.1, and appendix B, section B.9.1 | Paired bootstrap test (agent) | Comparing two Expert versions on the same dialogues |
| J&M ch. 5 and ch. 10 | Cosine similarity; contextual embeddings (agent) | Background only. Neither covers sentence embeddings for retrieval |
| J&M ch. 22 and ch. 24 | Sentiment lexicons; discourse coherence (agent) | Only if we label review sentiment with a lexicon, or define coherence |
| Edge et al. (2024), GraphRAG | Graph index and community summaries for corpus-wide questions (agent) | An example of a pairwise LLM judge with named criteria. One entity's 10 reviews fit in a prompt, so the method itself does not fit us |
| Chhikara et al. (2025), Mem0 | Memory layer for long conversations; fewer tokens, lower accuracy than full context (agent) | The accuracy against token cost trade-off, at most |
| Pan et al. (2024), LLMs and knowledge graphs | Survey with three ways to combine them (read as arXiv:2306.08302; agent) | General claim that outside knowledge at answer time grounds an LLM |
| Pan et al. (2023), Logic-LM | LLM writes logic, a solver reasons, errors drive a repair loop (agent) | Another "outside checker" pattern. Not dialogue |
| Kambhampati, Stechly, Valmeekam (2025) | Reasoning models combine test-time inference and post-training on traces; the visible "thinking" is not shown to be reasoning; using LLMs as verifiers "is known to be problematic" (preprint v1, checked) | Why we keep Qwen3's thinking mode off or do not treat it as evidence. Low |
| Baez Santamaria et al. (2023) | Compares 5 dialogue datasets and proposes an annotation scheme (agent) | None for the build |

## 4. Opened, nothing for the project

J&M chapters 2, 3, 6, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23 and appendices A, C, D, E, F, G, H, J (all agent). Chapter 2 has BPE tokenisation, a possible footnote for "length in tokens". Chapter 17 mentions a paired test for comparing two scores.

## 5. Could not be opened

| Link | What happened | Does it matter? |
| --- | --- | --- |
| All "VU Library" links | Need a VU login | No. Every item was read from a free copy |
| Talk videos (.mp4) for MultiWOZ and Smith et al. | Video cannot be watched | No |
| Springer page for Deriu et al. | Fetch failed. Read from the arXiv and university repository copies | Only for exact section numbers in the journal layout |
| Wiley page for Kambhampati et al. (2025) | Fetch failed. Read as arXiv v1 | Only if you quote the journal version |
| IEEE page for Pan et al. (2024) | Empty page. Read as arXiv | Pages 3580-3599 not confirmed |
| J&M appendix I | The file is empty (0 bytes) on the site | No |

## 6. What the reading list does not give us

- Nothing on two LLM agents talking to each other. Closest course material: the synthetic agent-and-patient dialogues in Lecture 1, and three papers on the presentation list (Harbar and Chudziak 2025; Liu et al. 2025; Chawla et al. 2021), not read yet.
- No stopping rule. Ours will be our own design, motivated by closing acts and grounding.
- No ready definitions of quality criteria except in Zhao et al. (2023).
- Agreement statistics: named in the Evaluation lecture of 13 Nov (Cohen, Fleiss, Scott, Krippendorff), used in Bavaresco et al. (kappa, Spearman) and Zhao et al. (Gwet). None of the readings teaches how to compute them.
