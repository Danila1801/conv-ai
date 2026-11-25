# Raw agent notes on the CAI reading list (24 Nov 2026)

These are the unedited notes of ten reading agents. They read each source through a summarising tool, so numbers, sections and page ranges here are NOT verified. Check the PDF before citing anything. The checked digest is reading-list-notes.md.


---

<!-- file: A-slp3-dialogue-rag.md -->

# Batch A: SLP3 (Jan 2026 draft) chapters on dialogue and RAG

General note on method: WebFetch returns a small model's summary, not raw text. Every READ tag below means "stated in the summary returned for the PDF". Each PDF was returned as a complete document (the tool said no offset was needed). I used 3 to 4 fetches per document. Page numbers were not returned, so none are given. Equation and figure numbers are as reported by the tool.

## 1. Chapter 25: Conversation and its Structure

**Verified citation**: Jurafsky, D. and Martin, J. H., Speech and Language Processing, 3rd ed. draft, Chapter 25 "Conversation and its Structure", draft dated January 6, 2026. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/25.pdf. Draft, not a published edition. The author names were not in the returned text; I take them from the book title the course lists (OURS).
**Access**: opened fully (whole document, tool said it was complete). The chapter describes itself as an "initial stub" and is short (a few paragraphs per section) followed by the reference list.

**Sections** (READ):
25.1 Properties of Human Conversation: 25.1.1 Turns; 25.1.2 Speech Acts; 25.1.3 Grounding; 25.1.4 Subdialogues and Dialogue Structure; 25.1.5 Initiative; 25.1.6 Inference and Implicature. 25.2 Dialog Acts and Corpora (no subsections).

**What it is**: A short conceptual chapter on what makes human conversation work, using one running example, a 20-turn travel agent/client dialogue (Fig. 25.1). It then introduces dialogue-act tagsets (Verbmobil-1, HIS restaurant system, DAMSL). It is descriptive background, not an evaluation or system-building chapter.

**Key points**
- Turns (25.1.1): a turn is one speaker's contribution, from one word to several sentences. Fig. 25.1 shows both (C13 is "OK.", A10 is several sentences). Speakers start almost immediately after the other finishes because they predict turn ends. Endpointing (detecting that the user finished) is hard because of noise and pauses. The chapter says LLMs also face the problem of when to start talking. It also covers interruption/overlap (A16/C17). READ.
- Speech acts (25.1.2): utterances are actions (Wittgenstein 1953, Austin 1962). Bach and Harnish's four classes: constatives, directives, commissives, acknowledgments. A question counts as a directive; stating a constraint is a constative. READ.
- Grounding (25.1.3): conversation builds common ground (Stalnaker; Clark 1996). Clark and Schaefer (1989) give presentation and acceptance phases and five methods from weakest to strongest: continued attention, next contribution, acknowledgment, demonstration, display. Example: repeating "in May" is a demonstration. Continuers like "uh huh" are backchannels. READ.
- Adjacency pairs and subdialogues (25.1.4): first pair part (question, proposal) sets up an expected second part (answer, accept/reject). Side sequences, correction and clarification subdialogues interrupt the main pair; presequences ("Can you make train reservations?") precede a request. READ.
- Initiative (25.1.5): system initiative, user initiative, mixed initiative. Mixed is normal for humans and hard for systems. Chapter says LLM-based systems often lack natural initiative switching. READ.
- Inference and implicature (25.1.6): listeners infer beyond the literal words (client mentions a meeting, agent infers the travel reason). Attributed to Grice (1975, 1978). Only the maxim of RELEVANCE is named. The other maxims (quantity, quality, manner) are NOT listed. READ (summary of the tool; worth a 10-second check in the PDF).
- Dialogue acts (25.2): a dialogue act merges speech-act and grounding functions in one tag. Fig. 25.2 Verbmobil-1 scheduling tags (18); Fig. 25.3 HIS restaurant tags (11: HELLO, INFORM, REQUEST, REQALTS, CONFIRM, CONFREQ, SELECT, AFFIRM, NEGATE, DENY, BYE), marked as valid for system and/or user; Fig. 25.4 sample HIS restaurant dialogue; DAMSL forward and backward functions incl. OPENING, CLOSING, THANKING (Fig. 25.5). Says dialog acts can be used to analyze "human-LLM conversation". READ.
- Ending a conversation: the chapter has no stopping criterion for a conversation. The nearest content is BYE (HIS) and CLOSING (DAMSL) acts, and knowing when to stop talking when interrupted (25.1.1). READ.
- Evaluation: none in this chapter. READ (tool said no evaluation discussion).
- Multi-agent conversation, "chatbot": not discussed. READ.

**Relevance to our project**: medium-high for conversation design motivation (not for metrics).
- Turns (25.1.1): a conversation is a sequence of turns; we can define a turn budget and count turns (objective metric) in these terms.
- Adjacency pairs (25.1.4): Beginner question -> Expert answer is a first pair part / second pair part; clarification subdialogues justify the Expert asking a clarifying question or the Beginner querying again.
- Grounding (25.1.3): justifies Beginner acknowledging/repeating the Expert's answer before moving on, and a closing check that both sides agree (common ground) before the final system turn.
- Initiative (25.1.5): Beginner starts every conversation (user-like initiative), Expert responds; allowing the Expert to ask back is mixed initiative.
- Dialogue acts (25.2): HIS restaurant tags (INFORM, REQUEST, CONFIRM, SELECT, BYE) are a ready vocabulary for labeling agent turns or for prompting acts; CLOSING/BYE motivate a stop rule that fires on a closing act plus agreement.
- Implicature/relevance (25.1.6): Expert answers should be relevant to the Beginner's question; the chapter supports the relevance maxim only.
- Stopping rule: the chapter does not give one. We could cite it only for "dialogues have explicit closing acts (BYE, CLOSING)", not for a numeric limit or an agreement test (OURS).

**Caveats**: Human conversation framing; no LLM-agent guidance. Only one Gricean maxim named. Short stub; a draft. The summarizer noted a small inconsistency between the prose and Fig. 25.1 (the prose cites A8 and A10 as "OK" examples while the figure shows "OK" at A12, A16, A20); do not cite specific turn labels without opening the PDF. Searle is not cited.

---

## 2. Chapter K: Frame-Based Dialogue Systems

**Verified citation**: Jurafsky, D. and Martin, J. H., Speech and Language Processing, 3rd ed. draft, Appendix K "Frame-Based Dialogue Systems", draft dated January 6, 2026. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/K.pdf. Draft. Authors from the book title the course lists (OURS).
**Access**: opened fully (tool said whole chapter, ending at page 11 of the PDF, with Historical Notes containing a "[TBD: Modern history of neural dialogue systems]" placeholder).

**Sections** (READ): K.0.1 Frames and Slot Filling (reported as "Frames and Slots" in the body); K.0.2 Evaluating Task-Based Dialogue; K.1 Dialogue Acts and Dialogue State: K.1.1 Dialogue Acts; K.1.2 Dialogue State Tracking; K.1.3 Dialogue Policy: Which act to generate; K.1.4 Natural language generation: Sentence Realization. Then unnumbered Historical Notes and references.

**What it is**: A short appendix on classic frame-based (slot-filling) task-oriented dialogue: a frame with typed slots, a state tracker, a policy that picks the next act, and a generator that turns the act into text. Running example is air travel; restaurant (HIS) dialogue acts appear in K.1.1.

**Key points**
- Frames and slots (K.0.1): a frame is a knowledge structure whose slots are filled with user values; the example is air travel (origin, destination, dates, times), with typed slots and a sample question per slot. Alarm and calendar domains are mentioned. Domain classification, intent detection and slot filling extract the information; slot filling is usually BIO tagging with a pretrained encoder; values are normalized to an ontology (e.g., "SF" to an airport code). READ.
- EVALUATION (K.0.2), exactly as returned: (a) task success rate, how often the right action is taken (e.g., booking the right flight); (b) slot error rate = (inserted + deleted + substituted slots) / total reference slots (Eq. K.1), worked example: "Make an appointment with Chris at 10:30 in Gates 104" with one wrong slot (TIME) of three gives 1/3; (c) precision, recall, F-score; (d) efficiency measures such as dialogue length in seconds or number of turns. User satisfaction and PARADISE are NOT discussed in K.0.2. READ. This section is the only evaluation text in K; Ch 25 has none (see Ch 25 above).
- Dialogue acts (K.1.1): generalize speech acts and represent grounding; Fig. K.4 lists HIS restaurant acts (HELLO, INFORM, REQUEST, CONFIRM, AFFIRM, NEGATE, BYE ...) with who may use them; Fig. K.5 sample dialogue labeled with acts. READ.
- Dialogue state tracking (K.1.2): the tracker keeps the whole frame state summarizing all user constraints so far (Fig. K.6), not just the current utterance; act detection is like intent classification and is often joint with slot filling; also detecting user corrections (hard, e.g., hyperarticulation; features like similarity to prior utterance, prosody, ASR confidence). READ.
- Dialogue policy (K.1.3): early systems ask until all slots are filled, then query and report; better policies choose the next act (content planning); explicit vs implicit confirmation and rejection; ASR confidence thresholds decide between reject, explicit confirm, implicit confirm, no confirm. READ.
- NLG (K.1.4): sentence realization maps act plus slot-values to text (Fig. K.7); delexicalization (placeholders for values), encoder-decoder from frames to delexicalized sentences, then relexicalization (Fig. K.9). MultiWOZ is named here as a hand-labeled corpus used to train such a realizer. READ.
- MultiWOZ appears in K.1.4 and the references. The string "DSTC" does not appear, but the Historical Notes describe the annual state-tracking evaluation and cite Williams et al. (2016) "The dialog state tracking challenge series". LLMs are not mentioned (pretrained encoders and neural models only). READ.

**Relevance to our project**: high for conceptual grounding of the booking task; medium for evaluation.
- Frames/slots: a hotel or restaurant request (area, price range, name, parking, etc.) is a frame; the "request fulfilled" metric can be defined as task success over the requested slots (OURS, plausible but the chapter does not discuss reviews).
- Evaluation (K.0.2): can be cited for "task success rate", "slot error rate" (Eq. K.1) and "number of turns" as efficiency, which supports our objective metrics (turns) and the "how often the request was fulfilled" requirement. It does NOT support user-satisfaction scales or LLM-judge evaluation.
- State tracking and policy (K.1.2, K.1.3): the Beginner/Expert can be described as maintaining a dialogue state; explicit/implicit confirmation (K.1.3) motivates a confirmation turn before finalizing.
- NLG (K.1.4): the final turn "the system could send to the user" is the NLG step.
- MultiWOZ named as a corpus (K.1.4): can be cited only for "MultiWOZ is a hand-labeled dialogue corpus"; nothing on DSTC11 Track 5 or reviews.

**Caveats**: Classic pipeline design, speech-recognition-centered in places (ASR thresholds). No LLM-based systems, no knowledge-grounded dialogue, no multi-agent setups. Unfinished draft.

---

## 3. Chapter 11: Information Retrieval and Retrieval-Augmented Generation

**Verified citation**: Jurafsky, D. and Martin, J. H., Speech and Language Processing, 3rd ed. draft, Chapter 11 "Information Retrieval and Retrieval-Augmented Generation" (running head "Retrieval-Based Models"), draft dated January 6, 2026. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/11.pdf. Draft. Authors from the course's book title (OURS).
**Access**: opened fully (whole chapter through the reference list ending with Zhou et al., 2024). The Exercises heading appears without problems.

**Sections** (READ): 11.1 Information Retrieval (11.1.1 Representing documents as vectors; 11.1.2 Term weighting: tf-idf and BM25; 11.1.3 Document Scoring; 11.1.4 Efficiently finding documents: the Inverted Index); 11.2 Evaluation of Information-Retrieval Systems; 11.3 Information Retrieval with Dense Vectors; 11.4 Retrieval-Augmented Generation (RAG); 11.5 Datasets; 11.6 Evaluating Question Answering; 11.7 Summary; Historical Notes; Exercises.

**What it is**: Textbook chapter that goes from sparse term-vector retrieval (tf-idf, BM25) through retrieval evaluation and dense retrieval, to RAG and question-answering datasets and metrics.

**Key points**
- Sparse retrieval (11.1.2, 11.1.3): tf = 1 + log10(count) (Eq. 11.4); idf = log10(N/df) (Eq. 11.5); tf-idf = tf x idf (Eq. 11.6). BM25 (Eq. 11.12): sum over query terms of idf times a length-normalized tf weight, tf / (k(1 - b + b|d|/|d_avg|) + tf); k balances term frequency vs IDF, b controls length normalization; suggested k 1.2 to 2 and b = 0.75 (citing Manning et al., 2008). Ranking by cosine similarity (Eqs. 11.7 to 11.11), worked example "sweet love" gives cosines 0.747 vs 0.0779. Inverted index for efficiency (11.1.4). READ.
- Retrieval evaluation (11.2): precision = |R|/|T| and recall = |R|/|U| (Eq. 11.13); precision-recall curve, interpolated precision (Eq. 11.14), 11-point curve, average precision (Eq. 11.15), MAP (Eq. 11.16; Fig. 11.7 example AP = 0.6). nDCG and MRR are NOT defined in this chapter (the tool said it could not find them). READ.
- Dense retrieval (11.3): sparse methods suffer vocabulary mismatch. Cross-encoder (BERT on query+doc together, Eq. 11.17) is accurate but used for reranking a shortlist; bi-encoder (separate encoders, dot product of [CLS] vectors, Eq. 11.18) allows precomputed document vectors; ColBERT (per-token embeddings, sum of max similarities, Eq. 11.19, query capped at 32 tokens); training with negatives sampled from a system's top-1000; nearest-neighbor search with approximate methods such as Faiss. Passages chunked e.g. ~100-token non-overlapping, must fit BERT's 512-token window. READ.
- RAG definition (11.4): add IR to an LM: a retriever pulls passages from a document store, then an LLM generates an answer conditioned on those passages and the original query. Two components: retriever and generator (historically "reader"); Fig. 11.13 shows the pipeline (user prompt, indexed documents, relevant documents, LLM generator, optional knowledge citations). READ.
- Problems RAG addresses (11.4): grounding answers in trusted documents can reduce hallucination; access to private data (email, health records, corporate files); information newer than the training data. READ.
- Basic algorithm (11.4): (1) retrieve top-k passages, (2) build a prompt with the retrieved passages first, then an instruction to answer based on them, then the question, (3) call the LLM. READ.
- Extensions and limits (11.4): agent-based RAG (decide when and where to retrieve), rerankers, multi-hop retrieval; options to instruction-tune on question+passages+answer, to prompt the model to reflect on which passages helped, and to train retriever and LLM end to end; knowledge citations (numbered URLs/references) requested via the prompt. Limits: basic version has no training, passages can be noisy or badly ordered, off-the-shelf retrievers can mismatch the task. READ.
- QA datasets and metrics (11.5, 11.6): Natural Questions, MS MARCO, TyDi QA, MMLU (open-book vs closed-book); exact match for multiple choice, token F1 for free text. No human or LLM-as-judge evaluation is described in this chapter. READ.

**Relevance to our project**: high for the Expert's knowledge access; none for conversation-level evaluation.
- Citable for: RAG definition and the retrieve-then-prompt setup (11.4), the stated motivation of grounding answers in documents to reduce hallucination (11.4), and BM25/tf-idf versus dense (bi-encoder) retrieval as the choice for retrieving reviews (11.1.2, 11.3). Supports giving the Expert a review knowledge base while the Beginner has none.
- Agent-based RAG (11.4: model decides when to retrieve) lines up with an Expert deciding whether to look up reviews (OURS).
- Retrieval metrics (precision, recall, MAP, 11.2) could evaluate review retrieval if relevance labels exist (DSTC11 Track 5 provides labels, but this chapter says nothing about that data, OURS).
- Not usable for: LLM-judge or human evaluation, dialogue evaluation, or conversational (multi-turn) retrieval; the chapter covers single-question QA.

**Caveats**: Chapter is on single-turn factual QA. Its RAG metrics (exact match, token F1) do not fit free-form hotel recommendations. nDCG/MRR missing.

---

## Sections where I am least sure
1. Ch 25 names only the relevance maxim: from the summarizer, not checked in raw text. Check before writing that the chapter omits quantity, quality, manner.
2. Ch 25 grounding example turn numbers (A8/A10 vs A12/A16/A20) were flagged inconsistent; do not cite turn labels.
3. Ch K: "user satisfaction/PARADISE not discussed" is an absence claim from the summarizer; a quick Ctrl-F in the PDF would confirm.
4. Ch 11: "nDCG and MRR not defined" is likewise an absence claim.
5. Author names are not read from the PDFs; take them from the book's title page.


---

<!-- file: B-slp3-embeddings-llms.md -->

# Batch B: SLP3 (Jurafsky & Martin) Jan 2026 draft, Ch 5, 7, 10

Method note: WebFetch returns a small model's answers, not raw text. All READ tags below mean "stated in the WebFetch answer about the PDF", not verified against raw page text. Each PDF was returned in full (all pages through references), used 4 / 3 / 2 fetches. Section titles and numbers were read for all three.
Header on all three: draft of January 6, 2026. Book: Speech and Language Processing, 3rd ed. draft, Dan Jurafsky and James H. Martin (authors taken from the series/book, not printed in the fetch answers: OURS, check the PDF cover before citing). Published draft, not a final print edition.

## Ch 5 "Embeddings"  (https://web.stanford.edu/~jurafsky/slp3/old_jan26/5.pdf)
Access: opened fully.
Sections (READ): 5.1 Lexical Semantics; 5.2 Vector Semantics: The Intuition; 5.3 Simple count-based embeddings; 5.4 Cosine for measuring similarity; 5.5 Word2vec (5.5.1 The classifier, 5.5.2 Learning skip-gram embeddings, 5.5.3 Other kinds of static embeddings); 5.6 Visualizing Embeddings; 5.7 Semantic properties of embeddings (5.7.1 Embeddings and Historical Semantics); 5.8 Bias and Embeddings; 5.9 Evaluating Vector Models; 5.10 Summary. Then Historical Notes, Exercises (heading only), references.
Key points:
- 5.4: cosine = dot product divided by vector lengths (Eqs. 5.7-5.10); 1 same direction, 0 orthogonal, -1 opposite; for non-negative count vectors range is 0-1; for unit vectors dot product = cosine. Worked example cos(cherry,information)=.018, cos(digital,information)=.996 (READ).
- 5.2: distributional idea, similar contexts imply similar meaning; Fig. 5.1 neighbours of "sweet" (READ).
- 5.1: distinguishes similarity (cat/dog) from relatedness (coffee/cup) (READ). 5.9 says SimLex-999 measures similarity, not relatedness (READ).
- 5.5: word2vec vectors are static, one vector per word; contrasted with contextual embeddings. Intro and 5.5 only point to Chapters 8 and 9 for "BERT-like" contextual embeddings; no mechanics here (READ).
- 5.7: parallelogram analogy model (Fig. 5.8, Eq. 5.28), Fig. 5.9; says the method often returns an input word and fails for some relations (READ).
- 5.9: extrinsic task evaluation called most important; intrinsic = correlation with human ratings (WordSim-353, SimLex-999), TOEFL, analogies, WiC/SCWS; STS mentioned at sentence level (READ).
- Absent (READ, per fetch): methods for sentence or document embeddings, retrieval, BERTScore. End of 5.2 says cosine can compare two sentences or documents, only as a remark.
Relevance: medium for the Expert's review retrieval, only as background: cite 5.4 for what cosine similarity is and 5.5 for the static vs contextual distinction. It does NOT support "use sentence embeddings to retrieve reviews" (OURS).
Caveats: static word vectors, not sentence encoders. Cross-reference chapter numbers inside the text (8, 9) may not match this edition's numbering (see mismatches).

## Ch 7 "Large Language Models"  (https://web.stanford.edu/~jurafsky/slp3/old_jan26/7.pdf)
Access: opened fully (about 30 pages, 7 fetches' worth of targeted questions; 5 used).
Sections (READ): 7.1 Three architectures for language models; 7.2 Conditional Generation of Text: The Intuition; 7.3 Prompting; 7.4 Generation and Sampling (7.4.1 Greedy decoding, 7.4.2 Random sampling, 7.4.3 Temperature sampling); 7.5 Training Large Language Models (7.5.1 Self-supervised training algorithm for pretraining, 7.5.2 Pretraining corpora for large language models, 7.5.3 Finetuning); 7.6 Evaluating Large Language Models (7.6.1 Perplexity, 7.6.2 Downstream tasks: Reasoning and world knowledge, 7.6.3 Other factors for evaluating language models); 7.7 Ethical and Safety Issues with Language Models; 7.8 Summary. Then Historical Notes, references.
Key points by topic:
- Prompting, 7.3 (READ): prompt = text given to the model; finding good ones = prompt engineering. Instruction-tuned models follow prompts better (details deferred). Demonstrations = labeled examples in the prompt; text argues they mainly show task and output format, and even wrong-answer demos can help. Fig. 7.6 = 2-shot MMLU example. Zero-shot = instructions without examples; few-shot = with demonstrations. In-context learning = learning during prompting with no weight change.
- System prompts, 7.3 (READ): a system prompt is an instruction silently prepended to all user input that sets role and tone; minimal example uses <system> and <user> metatokens; a long real-world system prompt is described in unnumbered blocks (no figure number). Chapter does not use the term "chat template".
- Chain-of-thought: does NOT appear in 7.2 or 7.3 (READ). Not checked in the rest of the chapter (OURS: assume absent, verify before claiming).
- Decoding, 7.4 (READ): greedy = argmax (Eq. 7.2), generic and repetitive, deterministic, not used with LLMs in practice (7.4.1). Random sampling gives odd text because the tail mass adds up (7.4.2). Temperature: y = softmax(u/tau) (Eq. 7.4); low tau (0,1] sharpens, approaches greedy as tau goes to 0; tau>1 flattens toward uniform; Fig. 7.11 top candidate .45 at tau=1, .59 at .5, .95 at .1, near uniform at 10 and 100. No recommended default or typical range given. Beam search only named in 7.4.1 (details "Chapter 12"). Top-k and top-p only named in 7.4.3 as coming "in the next chapter", not described. Min-p not mentioned.
- Evaluation, 7.6 (READ): perplexity (7.6.1) = inverse probability of test set normalised by token count, lower is better, depends on tokenisation so compare models with the same tokenizer. 7.6.2: MMLU (15,908 multiple-choice questions, 57 areas) as proxy for knowledge and reasoning; data contamination flagged. 7.6.3: size, time, memory, energy (kWh, CO2); fairness benchmarks StereoSet, RealToxicityPrompts, BBQ; leaderboards Dynabench, HELM. LLM-as-a-judge is NOT mentioned. No quantitative hallucination metric.
- Harms, 7.7 (READ): hallucination (false statements, training does not enforce truth, risky in medical or emergency use); sycophancy (agreeing with user errors); toxicity and stereotypes (Tay example); privacy leakage; disinformation, fraud, phishing; emotional dependence; copyright and consent; bias amplification. Mitigation (RAG) deferred to a later chapter.
- Pretraining data, 7.5.2 (READ): Common Crawl, C4 (about 156B filtered English tokens), The Pile (825 GB), Dolma (3T tokens); quality filtering, dedup; toxicity filtering has mixed results and can wrongly flag African American English; copyright and opt-out (robots.txt) unclear; skew to US and developed-country authors. 7.5.1: self-supervised next-token prediction, cross-entropy, teacher forcing. 7.5.3: finetuning = continued training on new domain. Training stages: pretraining, instruction tuning (SFT), preference alignment; the term "RLHF" is not used.
- 7.1 (READ): decoder (GPT, Claude, Llama, Mistral), encoder (BERT, RoBERTa; not for generation), encoder-decoder (MT, ASR).
Relevance: HIGH for the Expert/Beginner design. Cite 7.3 for system prompts, zero-shot vs few-shot, demonstrations, in-context learning; 7.4.3 for temperature (Eq. 7.4, Fig. 7.11), and 7.4.1 for why greedy is avoided; 7.6.1 for perplexity; 7.7 for hallucination and sycophancy (sycophancy is directly relevant to two agents agreeing with each other, OURS); 7.5.2 for pretraining data.
Caveats: no advice on picking a temperature value; top-k/top-p not explained here so do not cite this chapter for them; no chain-of-thought, self-consistency, or LLM-as-a-judge (cite other readings); 7.5 gives no LoRA or DPO detail.

## Ch 10 "Masked Language Models"  (https://web.stanford.edu/~jurafsky/slp3/old_jan26/10.pdf)
Access: opened fully (2 fetches).
Sections (READ): 10.1 Bidirectional Transformer Encoders (10.1.1 The architecture for bidirectional masked models); 10.2 Training Bidirectional Encoders (10.2.1 Masking Words, 10.2.2 Next Sentence Prediction, 10.2.3 Training Regimes); 10.3 Contextual Embeddings (10.3.1 Contextual Embeddings and Word Sense, 10.3.2 Contextual Embeddings and Word Similarity); 10.4 Fine-Tuning for Classification (10.4.1 Sequence Classification, 10.4.2 Sequence-Pair Classification); 10.5 Fine-Tuning for Sequence Labeling: Named Entity Recognition (10.5.1-10.5.4); 10.6 Summary. Historical Notes says "History TBD". Only 10.1-10.5 are assigned.
Key points:
- 10.2.1: of selected tokens, 80% become [MASK], 10% random, 10% unchanged; loss only on selected tokens; Fig. 10.3 (READ).
- 10.3: token representation = final-layer output; averaging last four layers also suggested; Fig. 10.5 (READ).
- 10.3.1: UMAP of "die" (Fig. 10.6), nearest-neighbour word sense disambiguation (Eqs. 10.6-10.7, Figs. 10.7-10.8) (READ).
- 10.3.2: word-in-context similarity via cosine on contextual embeddings; anisotropy and z-score standardisation (Eqs. 10.8-10.10) (READ).
- 10.4.1: [CLS] output vector into classifier head (Eq. 10.11, Fig. 10.9); sum or mean of token outputs mentioned as an alternative for classification only. 10.4.2: pairs joined with [SEP], MultiNLI example (READ).
- Absent (READ, per fetch): BERTScore, Sentence-BERT or sentence embeddings for similarity, retrieval, text-level similarity.
Relevance: medium-low. Cite for contextual vs static embeddings (10.3) and cosine between contextual vectors (10.3.2). Does NOT support BERTScore or sentence-embedding retrieval; cite BERTScore's own paper or the evaluation lecture for that.
Caveats: encoder models, classification, NER; none of it is about generation or dialogue.

## Mismatches and flags
- Titles and numbers match the reading list's labels: Ch 5 Embeddings, Ch 7 Large Language Models, Ch 10 Masked Language Models (READ). Ch 5 and Ch 7 include 10.x and other chapter numbers in cross-references that look inconsistent with this edition: Ch 7 says encoder models/BERT come in "Chapter 9", instruction tuning and safety tuning in "Chapter 10", top-k/top-p in "next chapter", RAG in Chapter 11; yet Ch 10 in this edition is Masked Language Models. So in-text cross-references appear stale relative to the file numbers (OURS, from the fetch's list of cross-references). Do not cite "Chapter 10 covers instruction tuning" for this edition; verify in the PDF.
- Lecture slides cite the August 2026 manuscript with different numbering; cite sections by title plus "Jan 2026 draft" to be safe.


---

<!-- file: C-slp3-transformers-posttraining.md -->

# SLP3 Jan 2026 draft: Ch. 8 Transformers and Ch. 9 Post-training

Method: 3 WebFetch calls per document (WebFetch returns a small model's answers, not raw text). Tags: READ = in the text returned; OURS = inference.
Both fetches reported full-chapter coverage.

## 1. Chapter 8 "Transformers"
- Verified citation: Jurafsky & Martin, Speech and Language Processing, 3rd ed. draft, Chapter 8 "Transformers", "Draft of January 6, 2026". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/8.pdf (draft, not published). Authors/year taken from the series, not from the fetch output (OURS).
- Access: opened fully (READ, complete chapter incl. references).
- Sections (READ): 8.1 Attention (8.1.1 Attention more formally); 8.2 Transformer Blocks; 8.3 Parallelizing computation using a single matrix X; 8.4 The input: embeddings for token and position; 8.5 The Language Modeling Head; 8.6 More on Sampling (8.6.1 Top-k; 8.6.2 Nucleus/top-p); 8.7 Training; 8.8 Dealing with Scale (8.8.1 Scaling laws; 8.8.2 KV Cache; 8.8.3 Parameter Efficient Fine Tuning); 8.9 Interpreting the Transformer (8.9.1 In-Context Learning and Induction Heads; 8.9.2 Logit Lens); 8.10 Summary; unnumbered Historical Notes.
- Key points
  - Attention: Eq. 8.6-8.8 simplified attention; Eq. 8.9-8.14 single head (scaled by sqrt(d_k) in 8.11, softmax 8.12, output projection W_O 8.14); multi-head Eq. 8.15-8.20. Figs 8.3-8.6. (READ)
  - Block: FFN Eq. 8.21; layer norm Eq. 8.22-8.25; block Eq. 8.26-8.31; prenorm; Figs 8.7, 8.8. (READ)
  - Decoding: 8.5 mentions greedy (take highest-probability word). 8.6 says sampling methods trade quality against diversity. 8.6.1 top-k is a procedure in steps, no numbered equation; k=1 equals greedy. 8.6.2 top-p: Eq. 8.48 defines V(p) as smallest set with cumulative probability >= p. (READ)
  - TEMPERATURE: the chapter does not say. The word "temperature" does not appear (confirmed by a second dedicated search question). No recommended k or p values. Intro says Chapter 7 already covered how tokens are generated by sampling (so temperature, if covered, would be there, not here; we did not read Ch. 7). (READ for absence; OURS for the Ch. 7 hint)
  - Maximum generation length / stopping / EOS for generation: the chapter does not say. Only a training-time end-of-text token between packed documents (8.7). (READ)
  - Context window: 8.1 "context window of input vectors"; lengths given inconsistently: 8.1.1 "thousands of tokens", 8.3 N commonly 1K-32K (128K or millions possible with special mechanisms not described), 8.5 about 32K for large models, 8.7 4096 (GPT-4) and 8192 (Llama 3), 8.10 summary "200K or more". (READ)
  - KV cache 8.8.2, Fig 8.18, Eq. 8.53: reuse keys/values at inference; no numbers on memory or speedup. (READ)
  - LoRA, 8.8.3, Fig 8.19, Eq. 8.54: h = xW + xAB. W (pretrained) frozen; only A [k x r] and B [r x d] trained; r << min(d,k), no value given; original applied to W_Q, W_K, W_V, W_O, many variants exist. Stated advantages: less hardware (no gradients for most parameters), AB same size as W so can be merged with no inference cost, LoRA modules swappable per domain. (READ)
  - In-context learning, 8.9.1: term credited to Brown et al. 2020; learning during forward pass without gradient updates; demonstrations can teach a new task; induction heads (Fig 8.20). No number of shots, no few-shot results. (READ)
- Relevance: high for decoding (cite 8.5, 8.6.1, 8.6.2 for greedy/top-k/top-p and the quality-diversity trade-off; NOT for temperature or max tokens), context window (8.1, 8.3), LoRA mechanics (8.8.3, Eq. 8.54, Fig 8.19), in-context/few-shot prompting rationale (8.9.1) for the prompted Expert.
- Caveats: draft with broken cross-references ("??"); internal inconsistency on context length (8.3 vs 8.10). No guidance on choosing temperature/top-p values or max_new_tokens; justify those from the model docs or Ch. 7, not this chapter.

## 2. Chapter 9 "Post-training"
- Verified citation: Jurafsky & Martin, SLP 3rd ed. draft, Chapter 9 "Post-training: Instruction Tuning, Alignment, and Test-Time Compute", "Draft of January 6, 2026". URL: https://web.stanford.edu/~jurafsky/slp3/old_jan26/9.pdf (draft). Course page just says "Post-training"; full title is longer (minor mismatch).
- Access: opened fully (about 18 pages, READ).
- Sections (READ): 9.1 Instruction Tuning (9.1.1 Instructions as Training Data; 9.1.2 Evaluation of Instruction-Tuned Models); 9.2 Learning from Preferences (9.2.1 LLM Preference Data; 9.2.2 Modeling Preferences; 9.2.3 Learning to Score Preferences); 9.3 LLM Alignment via Preference-Based Learning (9.3.1 RL with Preference Feedback (PPO); 9.3.2 Direct Preference Optimization; 9.3.3 Evaluation of Preference-Aligned Models; 9.3.4 Limitations of Preference-Based Learning); 9.4 Test-time Compute (9.4.1 Chain-of-Thought Prompting); 9.5 Summary; Historical Notes (heading only).
- UNFINISHED: 9.3.1 body is just "TBD"; 9.3.3 and 9.3.4 are headings with no text. (READ)
- Key points
  - Intro: post-training = steps after pretraining, namely instruction tuning and preference alignment, to make models more helpful and less harmful. (READ)
  - SFT / instruction tuning, 9.1: finetune base LLM on instruction-response pairs; same next-token cross-entropy as pretraining, no numbered equation. Four data sources: human-written (Aya, Fig 9.2), templated NLP datasets (Figs 9.3, 9.4), reused annotator guidelines (Fig 9.5), LLM-generated (e.g. about 500 safety examples reduced harmfulness, Bianchi et al. 2024). Fig 9.1 contrasts with other finetuning. (READ)
  - Evaluation 9.1.2: leave-one-out by task cluster (SuperNaturalInstructions has 76 clusters); no metric named. (READ)
  - LoRA/PEFT: only in 9.1 (text around Fig 9.1): A and B adapted, pretrained parameters frozen. No equation here; the forward-pass equation is Eq. 8.54 in Ch. 8. Text points back to "Chapter 7" for continued pretraining and PEFT. (READ)
  - Preferences 9.2: data from human annotators, implicit online votes (Fig 9.6), synthetic LLM annotators (9.2.1); scalar ratings on helpfulness, honesty, correctness, complexity, verbosity on a 0-4 scale. Bradley-Terry: Eq. 9.1-9.3 (probability, reward form, cross-entropy loss). Reward model = pretrained LLM with LM head replaced by a linear layer (9.2.3, Fig 9.7). (READ)
  - RLHF objective: Eq. 9.4 (maximize reward), 9.5 and 9.6 (KL penalty, coefficient beta). PPO itself is not described (TBD). Fig 9.8. (READ)
  - DPO 9.3.2: derivation Eq. 9.7-9.12; DPO loss is an unnumbered display equation; reference model = starting policy; beta typically 0.1 to 0.01; DPO needs 2 LLMs in training vs 4 for PPO. Fig 9.9. (READ)
  - Test-time compute 9.4: inference-time computation after post-training; the chapter covers only chain-of-thought prompting (9.4.1): few-shot demos augmented with reasoning steps help on hard reasoning (Wei et al. 2022; Suzgun et al. 2023). Figs 9.10 (GSM8K), 9.11 (BIG-Bench-Hard). (READ)
  - Does NOT say: RLVR / verifiable rewards / reasoning models / rule-based rewards (none appear); self-consistency; budget forcing; sycophancy. Side effects covered: hallucination and unsafe outputs as motivation (9.2), toxicity and stereotypes (intro/9.2), verbosity only as a rating dimension. (READ for absence)
- Relevance: high. Cite 9.1 (SFT as the way to fine-tune the Expert on instruction-style data, Fig 9.1 vs other finetuning) with Eq. 8.54/8.8.3 for LoRA; 9.4.1 for few-shot and CoT prompting as the cheaper prompted alternative; 9.2-9.3.2 only if we add a DPO variant (DPO pitfalls: needs preference pairs, reference model). Nothing here supports a claim that LoRA beats prompting; the chapter makes no such comparison (OURS).
- Caveats: unfinished draft; no RLVR, no sycophancy; LoRA equation lives in Ch. 8 not Ch. 9.

## 3. Numbering inconsistency resolved
- The Jan 2026 files: Ch. 8 = Transformers, Ch. 9 = Post-training (READ, both title pages). The slides' "Aug 19, 2026" manuscript (Transformers = Ch. 7, Post-training = Ch. 8) is a different, later draft; we did not read it (OURS).
- Slide items vs Jan 2026 files: Ch. 9 has no Eq. 8.1 and no Figs 8.1, 8.8, 8.10-8.12 (it does not reference them, READ). Ch. 8 has Fig 8.8 (attention moving info between token streams) and Fig 8.1 does not match post-training; Ch. 8 Eq. 8.1 not verified. So the slide numbers must NOT be matched to these files. Jan 2026 equivalents: LoRA = Eq. 8.54 / Fig 8.19 (Ch. 8.8.3); instruction tuning = Fig 9.1 to 9.5; Bradley-Terry = Eq. 9.1-9.3; DPO = Eq. 9.7-9.12 + Fig 9.9; CoT = Figs 9.10, 9.11.
- Cite as "Jurafsky & Martin, SLP3 draft of January 6, 2026, Section X" and state the edition explicitly.
- Odd: Ch. 9 text says "Chapters 7 and 9" for other finetuning methods, probably a draft error (READ; OURS on the error).


---

<!-- file: D-slp3-ch02-15.md -->

# D: Jurafsky & Martin, Speech and Language Processing (3rd ed. draft, Jan 2026), skim of chapters 2, 3, 4, 6, 12, 13, 14, 15

Source URLs (all WebFetch, base https://web.stanford.edu/~jurafsky/slp3/old_jan26/):
2.pdf, 3.pdf, 4.pdf, 6.pdf, 12.pdf, 13.pdf, 14.pdf, 15.pdf

Note on the reading-list entries: the batch brief gives only the chapter numbers, not the list's own titles or author lines, so I could not check the list for mismatches beyond the chapter numbers. The chapter numbers in the PDFs match the batch for all eight. Chapter titles below are as printed in the PDF text.

All claims below are READ unless tagged SEARCH or OURS.

---

## Chapter 2: "Words and Tokens"

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, 6 Jan 2026, Chapter 2 "Words and Tokens". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/2.pdf. Draft, not the published edition.

**Access**: opened partly. The tool returned characters 0 to 100000 of 110133 (about 91%). The cut falls in the Historical Notes. Exercises and bibliography were not read.

**What it is**: The chapter on what counts as a word and how text is split into tokens. It covers word types and instances, morphology, Unicode, and subword tokenization. It also covers regular expressions, rule-based tokenization, and minimum edit distance.

**Sections** (numbered headings): 2.1 Words; 2.2 Morphemes: Parts of Words; 2.3 Unicode (2.3.1 Code Points, 2.3.2 UTF-8 Encoding); 2.4 Subword Tokenization: Byte-Pair Encoding (2.4.1 BPE training, 2.4.2 BPE encoder, 2.4.3 BPE in practice); 2.5 Corpora; 2.6 Regular Expressions (2.6.1 to 2.6.9); 2.7 Simple Unix Tools for Word Tokenization; 2.8 Rule-based tokenization (2.8.1 Sentence Segmentation); 2.9 Minimum Edit Distance; 2.10 Summary.

**Key points** (skim):
- Defining "words" is hard across languages; word types versus instances and Heaps' Law are introduced (Section 2 opening, READ).
- Section 2.4 explains Byte-Pair Encoding for learning subword tokens, which is the tokenizer family behind many LLMs (READ).
- Section 2.6.7 covers ELIZA and its regex substitutions, the chatbot used as a historical example (READ).
- Section 2.9 covers minimum edit distance and alignment by dynamic programming. The text links it to word error rate in speech recognition (READ).

**Relevance to our project**: low. The only plausible use is OURS: the objective metric "conversation length in tokens" depends on which tokenizer is used, and Section 2.4 is a textbook explanation of subword tokenization that could support a footnote on that point. The ELIZA section (2.6.7) is historical background for chatbots and is not something we would cite for design.

**Caveats**: nothing on evaluation, prompting, or dialogue design. The truncated part (Historical Notes end, exercises, bibliography) was not read.

---

## Chapter 3: "N-gram Language Models"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 3 "N-gram Language Models". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/3.pdf. Draft.

**Access**: opened fully. The tool returned what appears to be the full chapter, with no truncation notice.

**What it is**: The classic n-gram language model chapter. It covers the Markov assumption, maximum likelihood estimation, smoothing and backoff, and perplexity as the intrinsic evaluation for language models.

**Sections**: 3.1 N-Grams (3.1.1 The Markov assumption; 3.1.2 How to estimate probabilities; 3.1.3 Dealing with scale in large n-gram models); 3.2 Evaluating Language Models: Training and Test Sets; 3.3 Evaluating Language Models: Perplexity (3.3.1 Perplexity as Weighted Average Branching Factor); 3.4 Sampling sentences from a language model; 3.5 Generalizing vs. overfitting the training set; 3.6 Smoothing, Interpolation, and Backoff (3.6.1 Laplace, 3.6.2 Add-k, 3.6.3 Interpolation, 3.6.4 Stupid Backoff); 3.7 Advanced: Perplexity's Relation to Entropy; 3.8 Summary.

**Key points** (skim):
- Section 3.3 uses perplexity as the evaluation metric for language models (READ).
- Section 3.2 describes train, dev, and test splits and says the test set must be large enough to show a "statistically significant difference" between models. It describes no significance test (READ).
- Section 3.1.2 describes the Berkeley Restaurant Project as "a dialogue system" used as a data source (READ).
- Section 3.4 covers sampling sentences from a language model, which is a generation technique (READ).

**Relevance to our project**: low. Perplexity is not one of our metrics, and our LLMs are not n-gram models. Section 3.2 could back a general point that the test set should be big enough, but Section 4.10 covers the same point for classifiers. Not a citation for the Expert or Beginner design.

**Caveats**: n-gram models and perplexity are a different setting from prompted LLMs. The chapter does not discuss generated-text metrics such as BLEU, human judgments, or LLM judges.

---

## Chapter 4: "Logistic Regression and Text Classification"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 4 "Logistic Regression and Text Classification". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/4.pdf. Draft.

**Access**: opened mostly. The tool returned characters 0 to 100000 of 100700 (about 99%). The cut falls near the end of the reference list. The targeted second read covered Sections 4.9 to 4.11 in full, as far as the tool returned them.

**What it is**: A textbook chapter on binary and multiclass text classification with logistic regression, using sentiment as the main example. It covers cross-entropy loss, gradient descent, classifier evaluation, cross-validation, and the paired bootstrap significance test.

**Sections**: 4.1 Machine learning and classification; 4.2 The sigmoid function; 4.3 Classification with Logistic Regression (4.3.1 to 4.3.3); 4.4 Learning in Logistic Regression; 4.5 The cross-entropy loss function; 4.6 Gradient Descent (4.6.1 to 4.6.4); 4.7 Multinomial logistic regression (4.7.1 Softmax, 4.7.2, 4.7.3); 4.8 Learning in Multinomial Logistic Regression; 4.9 Evaluation: Precision, Recall, F-measure (4.9.1 Evaluating with more than two classes); 4.10 Test sets and Cross-validation; 4.11 Statistical Significance Testing (4.11.1 The Paired Bootstrap Test); 4.12 Avoiding Harms in Classification; 4.13 Interpreting models; 4.14 Advanced: Regularization; 4.15 Advanced: Deriving the Gradient Equation; 4.16 Summary.

**Key points** (deep read on 4.9 to 4.11, skim elsewhere):
- Section 4.9: classifier evaluation uses a confusion matrix against human gold labels, with precision, recall, and F-measure. The text says accuracy is misleading for rare classes (READ).
- Section 4.9.1: macroaveraging versus microaveraging. The worked example gives a macro precision of .60 and a micro precision of .73 (READ, from the worked example in 4.9.1).
- Section 4.10: train, dev, and test split; 10-fold cross-validation run inside the training set; the text calls cross-validation over the full corpus "cheating." It gives no minimum test-set size (READ).
- Section 4.11: the null hypothesis is that A is not better than B. The text mentions approximate randomization (Noreen, 1989) and the bootstrap test (Efron and Tibshirani, 1993), but develops only the paired bootstrap (READ).
- Section 4.11.1: the paired bootstrap resamples the test set with replacement, about 10^5 virtual sets. The p-value counts how often the resampled difference reaches twice the original difference. The worked example gives p = .0047 (47 of 10,000 sets, READ).
- None of 4.9 to 4.11 mentions inter-annotator agreement or Cohen's kappa. The text refers to "gold labels" without measuring labeler consistency (READ, absence in 4.9 to 4.11).
- Section 4.1 notes that language models can be used by "prompting the model to give a label to some text" and mentions hallucination as a weakness (READ, one sentence in 4.1).

**Relevance to our project**:
- Section 4.11.1 (paired bootstrap) is medium relevance. It is a citable, standard method for testing whether one Expert version beats the other on per-conversation scores. It is a textbook for this, not a source for LLM-judge reliability.
- Section 4.9 is low to medium: precision, recall, and F-measure apply to the "was the request fulfilled" outcome if it is coded as a binary label. Macro versus micro averaging applies if the outcome is coded by category.
- Section 4.10 is low: the point that the test set must be held out is useful background for the Expert comparison.
- Section 4.1 is low: a single sentence mentioning prompting for classification.
- Nothing in this chapter covers generated-text evaluation, LLM judges, or human agreement.

**Caveats**: the chapter is about classifiers, not generated dialogue. Its paired bootstrap example uses n = 10 for illustration and says real test sets are much larger. It gives no guidance on how many conversations to run. Section 4.11 says the bootstrap assumes items are independent, which may not hold for multi-turn conversations, but the chapter does not discuss this (OURS).

---

## Chapter 6: "Neural Networks"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 6 "Neural Networks". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/6.pdf. Draft. The chapter's printed title is "Neural Networks".

**Access**: opened fully. The tool returned what appears to be the full chapter, with no truncation notice.

**What it is**: An introduction to feedforward neural networks. It covers units and activations, the XOR motivation for hidden layers, classification with embeddings, and training by backpropagation over computation graphs.

**Sections**: 6.1 Units; 6.2 The XOR problem (6.2.1 The solution: neural networks); 6.3 Feedforward Neural Networks (6.3.1 More details); 6.4 Feedforward networks for NLP: Classification (6.4.1, 6.4.2); 6.5 Embeddings as the input to neural net classifiers; 6.6 Training Neural Nets (6.6.1 Loss function; 6.6.2 Computing the Gradient; 6.6.3 Computation Graphs; 6.6.4 Backward differentiation; 6.6.5 More details on learning); 6.7 Summary.

**Key points** (skim):
- Section 6.1 covers sigmoid, tanh, and ReLU activations (READ).
- Section 6.2 explains why XOR requires a hidden layer (READ).
- Section 6.5 covers embeddings as input to classifiers and a feedforward neural language model. The text says the next chapter introduces neural large language models (READ, introduction and 6.5).
- Section 6.6 covers cross-entropy loss, gradient descent, and backpropagation (READ).

**Relevance to our project**: low. This is background for the neural machinery underneath LoRA and fine-tuning, but the chapter does not discuss LoRA, fine-tuning, or LLMs. Not a citation for any design choice.

**Caveats**: the chapter says the LLM material comes in later chapters. We should not cite it for LLM behaviour.

---

## Chapter 12: "Machine Translation"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 12 "Machine Translation". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/12.pdf. Draft. The PDF prints "CHAPTER 12 Machine Translation".

**Access**: opened fully, then a targeted second read of Section 12.6 and its subsections. The first read returned what appears to be the full chapter, with no truncation notice. The second read returned the 12.6 material and the significance section.

**What it is**: The machine translation chapter. It covers the encoder-decoder transformer, subword tokenization, beam search and minimum Bayes risk decoding, low-resource methods, and bias. Section 12.6 gives the standard evaluation toolkit for generated text: human ratings, chrF, BLEU, BERTScore, and significance testing.

**Sections**: 12.1 Language Divergences and Typology; 12.2 Machine Translation using Encoder-Decoder; 12.3 Details of the Encoder-Decoder Model; 12.4 Decoding in MT: Beam Search; 12.5 Translating in low-resource situations; 12.6 MT Evaluation (12.6.1 Using Human Raters; 12.6.2 Automatic Evaluation, including chrF, BLEU, BERTScore, and significance testing); 12.7 Bias and Ethical Issues; 12.8 Summary.

**Key points** (deep read on 12.6):
- Section 12.6 evaluates along two dimensions: adequacy (preserving meaning) and fluency. It says human evaluation is most accurate, and automatic metrics are used because they are cheaper and faster (READ, 12.6 opening).
- Section 12.6.1 lists human rating methods: fluency and adequacy scales (1 to 5 or 1 to 100), pairwise ranking, and training raters to separate the two dimensions (READ).
- Section 12.6.1 says raters often disagree, gives no agreement statistic, and suggests removing outlier raters and normalizing scores. It also mentions post-editing edit distance as a quality measure, citing Nekoto et al. (2020) and Bentivogli et al. (2018) (READ; those two citations are in-chapter references only, not verified by us).
- Section 12.6.2, chrF: character n-gram precision and recall combined in an F-score, with beta = 2 weighting recall more heavily. The chapter says chrF is simple, robust, and correlates well with human judgments across many languages (READ, Eq. 12.20 and the text after it).
- Section 12.6.2, BLEU: a precision-based word n-gram metric with a brevity penalty. The chapter says it is sensitive to tokenization and recommends SacreBLEU for standard tokenization (READ).
- Section 12.6.2, BERTScore: BERT embeddings with greedy token matching, reported as precision, recall, and F1 (Eqs. 12.21 and nearby). The chapter also mentions COMET and BLEURT as learned metrics trained on human quality labels. It states no limitations for BERTScore (READ).
- Section 12.6.2 limitations of overlap metrics: chrF is very local, cannot judge discourse coherence, and performs poorly when comparing very different systems. Overlap metrics suit single-system changes best (READ).
- Section 12.6.2 significance: a bootstrap over the test set gives a 95% confidence interval for one system. For two systems, the same resamples are used and the chapter reports how often system A beats system B. The chapter also mentions randomization. It does not give a resample count or threshold beyond the 95% interval (READ).
- ROUGE is not mentioned in this chapter (READ, absence in 12.6).
- Dialogue is mentioned once in 12.4.1, as one of the generation tasks minimum Bayes risk decoding has been applied to (READ).

**Relevance to our project**: high for the subjective and objective evaluation sections of the project.
- Section 12.6.1 (human rating scales, pairwise ranking, rater training, rater disagreement) supports the design of the human evaluation on a small subset. It can be cited for the claim that rater disagreement is expected and that raters need training. It gives no agreement statistic, so it does not support a choice of kappa or any other specific agreement measure.
- Section 12.6.2 (chrF, BLEU, BERTScore) is directly relevant to the course's Notebook 3 metric set. It can be cited for what each metric measures, and for the stated limitation that overlap metrics are weak at judging discourse coherence. This matters for our multi-turn conversations.
- Section 12.6.2 (bootstrap and randomization) is relevant to comparing two Expert versions.
- The chapter does not cover LLM-as-a-judge, so it cannot support that part of the design.

**Caveats**: MT evaluation compares a candidate to a reference translation. Our task has no single reference: a good dialogue outcome can take many forms, so reference-based overlap metrics (BLEU, chrF) do not map directly onto it. The chapter does not discuss dialogue. The chapter predates LLM-as-a-judge work, so it does not discuss judge bias or agreement with human raters (OURS, based on what the chapter omits). The chapter's rater agreement remark is a qualitative statement; we should not treat it as a measured result.

---

## Chapter 13: "RNNs and LSTMs"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 13 "RNNs and LSTMs". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/13.pdf. Draft.

**Access**: opened fully. The tool returned what appears to be the full chapter, with no truncation notice.

**What it is**: A chapter on recurrent neural networks and LSTMs, covering their use in language modelling, sequence labelling, and sequence classification. It ends with encoder-decoder models and attention.

**Sections**: 13.1 Recurrent Neural Networks (13.1.1 Inference, 13.1.2 Training); 13.2 RNNs as Language Models (13.2.1 to 13.2.3); 13.3 RNNs for other NLP tasks (13.3.1 to 13.3.3); 13.4 Stacked and Bidirectional RNNs (13.4.1, 13.4.2); 13.5 The LSTM (13.5.1 Gated Units); 13.6 Summary: Common RNN NLP Architectures; 13.7 The Encoder-Decoder Model with RNNs (13.7.1 Training); 13.8 Attention; 13.9 Summary.

**Key points** (skim):
- Section 13.1 covers simple recurrent networks that carry a hidden state through a sequence (READ).
- Section 13.5 covers LSTM gating for longer context (READ).
- Section 13.7 says encoder-decoder models "have been applied to a very wide range of applications including summarization, question answering, and dialogue" (READ, quoted fragment under 15 words; this is the only dialogue and QA mention beyond a passing remark).
- Section 13.8 introduces attention (READ).

**Relevance to our project**: low. Background on the architectures that transformers replaced. Section 13.8 (attention) is background for the transformer material the course already covers. Not a citation for the Expert or Beginner design.

**Caveats**: the chapter does not discuss evaluation, prompting, or any of our topics beyond the passing mention in 13.7.

---

## Chapter 14: "Phonetics and Speech Feature Extraction"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 14 "Phonetics and Speech Feature Extraction". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/14.pdf. Draft.

**Access**: opened fully. The tool returned what appears to be the full chapter. Some figure labels and equation references are garbled in extraction ("Section ??"), but the body text reads fully.

**What it is**: An introduction to phonetics and speech signal processing for recognition. It covers phonetic transcription, articulation, prosody, acoustic analysis, and MFCC features.

**Sections**: 14.1 Speech Sounds and Phonetic Transcription; 14.2 Articulatory Phonetics; 14.3 Prosody; 14.4 Acoustic Phonetics and Signals; 14.5 Feature Extraction for Speech Recognition: Log Mel Spectrum; 14.6 MFCC; 14.7 Summary.

**Key points** (skim):
- Section 14.1 covers ARPAbet and IPA transcription, and corpora such as TIMIT (READ).
- Section 14.3 mentions "managing turn-taking in conversation" only as a prosodic function (READ).
- Sections 14.5 and 14.6 cover mel filter banks and MFCCs (READ).

**Relevance to our project**: not relevant. Speech signal processing has no bearing on a text-based agent-to-agent system.

**Caveats**: the only item that touches conversation is a single phrase about turn-taking in prosody.

---

## Chapter 15: "Automatic Speech Recognition"

**Verified citation**: Jurafsky and Martin, SLP3 draft Jan 2026, Chapter 15 "Automatic Speech Recognition". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/15.pdf. Draft.

**Access**: opened fully. The tool returned what appears to be the full chapter, including references. The "Exercises" heading is present with no items after it.

**What it is**: The speech recognition chapter. It covers the ASR task, CNN feature extraction, encoder-decoder ASR (Whisper-style), self-supervised HuBERT, CTC, and word error rate.

**Sections**: 15.1 The Automatic Speech Recognition Task; 15.2 Convolutional Neural Networks; 15.3 The Encoder-Decoder Architecture for ASR; 15.4 Self-supervised models: HuBERT; 15.5 CTC; 15.6 ASR Evaluation: Word Error Rate; 15.7 Summary.

**Key points** (skim):
- Section 15.6 uses word error rate as the main metric and covers significance tests MAPSSWE and McNemar's test. It says McNemar's test is not suitable for continuous speech recognition (READ).
- Section 15.1 notes speech is a natural interface for "digital assistants or chatbots" and contrasts ASR with dialogue systems (READ).
- Section 15.3 covers the encoder-decoder architecture for ASR (READ).

**Relevance to our project**: none for the core design. Word error rate is not a metric for generated dialogue. The significance tests in 15.6 are of interest only as alternatives to the bootstrap in 4.11 and 12.6.2. Do not cite for our metrics.

**Caveats**: the chapter does not discuss text generation evaluation, LLMs, prompting, or dialogue design.

---

## Coverage summary

| Chapter | Access | Fully read? |
|---|---|---|
| 2 Words and Tokens | partly, about 91% | no, Historical Notes end, exercises, and bibliography missing |
| 3 N-gram Language Models | full | yes |
| 4 Logistic Regression and Text Classification | mostly, about 99%; 4.9 to 4.11 read in full | references end missing |
| 6 Neural Networks | full | yes |
| 12 Machine Translation | full, plus targeted read of 12.6 | yes |
| 13 RNNs and LSTMs | full | yes |
| 14 Phonetics and Speech Feature Extraction | full | yes |
| 15 Automatic Speech Recognition | full | yes |

---

## Links and sources I could not open

None. All eight URLs returned text. Partial coverage is noted above for Chapters 2 and 4.

## Citation mismatches

Not checked against the reading list, since the batch gives only chapter numbers. Chapter numbers and titles in the PDFs match the batch. Chapter 6 is printed "Neural Networks". No other mismatches.

## The five claims I am least sure of

1. The statement that the BERTScore section states no limitations. The tool's summary says so, but it may have missed a passage. Worth checking the PDF directly before citing a limitation.
2. That the chapter's rater-agreement remark (12.6.1) is purely qualitative. The tool gave no agreement number, and I did not verify the full subsection text.
3. The paired bootstrap p-value description in 4.11.1 (the 2 times original difference rule). The tool's paraphrase is accurate in outline, but I did not read the equation itself.
4. That Section 4.11 applies to multi-turn conversations. I flagged the independence issue as my own inference (OURS), not as something the chapter says.
5. That the in-chapter citations Nekoto et al. (2020) and Bentivogli et al. (2018) are real and say what the chapter reports. I have not verified these references. They are only what the chapter cites.


---

<!-- file: E-slp3-ch16-24.md -->

# Batch E: Jurafsky & Martin, Speech and Language Processing (3rd ed. draft, January 2026), chapters 16 to 24 (skim)

Source for all nine: the book website's old_jan26 PDFs (web.stanford.edu/~jurafsky/slp3/old_jan26/NN.pdf).
Access for all nine: opened partly or fully through WebFetch, one call each. Each PDF is a single chapter. Page headers read "Draft of January 6, 2026". The reading-list entry is not in my batch, so I have no list entry to compare against. The chapter titles below are the ones printed in the PDFs.
Note: the course does not assign these chapters (per the batch instructions), so relevance is judged only as possible background.

---

## Chapter 16: Text-to-Speech

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 16 "Text-to-Speech". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/16.pdf. Draft, not the published version.

**Access**: opened fully (text returned covered the chapter through summary, historical notes and references; exercises are a heading only). Some figures garbled by extraction.

**What it is**: A chapter on modern TTS, mapping text to a waveform. It covers audio codecs that turn speech into discrete tokens, and the VALL-E two-stage language-model approach to zero-shot voice cloning. Section 16.6 (Spoken Language Models) is marked "TBD".

**Key points** (skim):
- 16.2 (with 16.2.1 to 16.2.4) explains the EnCodec encoder/decoder, vector quantization and residual VQ as the discrete audio tokens. READ
- 16.3 describes VALL-E, a two-stage language model over codec tokens. READ
- 16.4 TTS evaluation uses human MOS and CMOS ratings, plus automatic checks such as ASR word error rate and speaker verification. It mentions paired t-tests for comparing systems. READ
- The "in-context learning" phrase appears only in a quoted VALL-E related-work excerpt, not as a topic. READ

**Relevance to our project**: Not relevant. TTS and speech evaluation are outside the text-based hotel/restaurant booking agents. The MOS/CMOS material concerns speech audio, not generated text, so it does not fit our subjective metrics. The paired t-test remark is a general point, but chapter 17 covers it more directly.

**Caveats**: Speech domain only. Its evaluation section does not cover BLEU, ROUGE, BERTScore, chrF or LLM judges.

---

## Chapter 17: Sequence Labeling for Parts of Speech and Named Entities

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 17 "Sequence Labeling for Parts of Speech and Named Entities". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/17.pdf. Draft, not the published version.

**Access**: opened fully (full chapter text returned, about 27 pages of extracted text). Page boundaries could not be confirmed from the extraction.

**What it is**: An introduction to POS tagging and named entity recognition as sequence labeling. It covers BIO tagging, the generative HMM (decoded with Viterbi) and the discriminative linear-chain CRF with hand-designed features. It ends with NER evaluation and rule-based methods.

**Key points** (skim):
- 17.4 (HMM tagging, Viterbi) and 17.5 (CRFs and their features) are the two classic models. READ
- 17.6 Evaluation of NER: comparing the F1 scores of two NER systems needs a paired bootstrap or randomization test. READ
- 17.3 mentions sentiment analysis and question answering only as downstream uses of NER. READ

**Relevance to our project**: Low. The only point that could be cited is 17.6's statement that comparing two systems' F1 needs a paired test (bootstrap or randomization). That could support a significance-testing sentence if we compare two Expert versions on a labeled metric. The chapter itself is about tagging and NER, not about dialogue or generated text. Otherwise not relevant.

**Caveats**: NER F1 on labeled spans. It does not discuss generated-text metrics, human agreement, or LLM judges. The significance-test details are deferred to a later section that is outside this batch's skim.

---

## Chapter 18: Context-Free Grammars and Constituency Parsing

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 18 "Context-Free Grammars and Constituency Parsing". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/18.pdf. Draft, not the published version.

**Access**: opened fully (full text returned, about 26 pages).

**What it is**: The chapter introduces constituency structure and context-free grammars. It covers treebanks, ambiguity, the CKY dynamic-programming parser (which needs Chomsky normal form) and span-based neural parsing. It ends with the PARSEVAL metrics for parser accuracy.

**Key points** (skim):
- 18.2 defines context-free grammars, and 18.6 covers CKY parsing. READ
- 18.7 covers span-based neural constituency parsing. READ
- 18.8 Evaluating Parsers uses PARSEVAL precision, recall, F1 and crossing brackets. These measure parser accuracy, not generated text. READ

**Relevance to our project**: Not relevant. None of the listed topics appear. The only evaluation content is for parsers.

**Caveats**: Syntax and parsing only.

---

## Chapter 19: Dependency Parsing

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 19 "Dependency Parsing". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/19.pdf. Draft, not the published version.

**Access**: opened fully (chapter body, historical notes and references returned; exercise questions not in the text).

**What it is**: The chapter presents dependency grammar as typed head-dependent relations between words. It covers Universal Dependencies relations, projectivity and treebanks. It then gives transition-based and graph-based (maximum spanning tree) parsers, and evaluates them with LAS, UAS and related scores.

**Key points** (skim):
- 19.1 covers dependency formalisms, projectivity and treebanks. READ
- 19.2 covers transition-based parsing, with oracles and feature-based and neural classifiers. READ
- 19.4 Evaluation covers exact match, LAS, UAS and per-relation precision and recall. These measure parser accuracy. READ
- Question answering and sentiment analysis appear only in passing, in the 19 introduction and summary. READ

**Relevance to our project**: Not relevant.

**Caveats**: Parser evaluation only. Nothing on generated text.

---

## Chapter 20: Information Extraction: Relations, Events, and Time

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 20 "Information Extraction: Relations, Events, and Time". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/20.pdf. Draft, not the published version.

**Access**: opened fully (full chapter, pages 1 to 28 by its markers, including exercises and references).

**What it is**: An overview of information extraction, turning unstructured text into structured data. It covers relation extraction (pattern-based, supervised, bootstrapping, distant supervision, unsupervised), event extraction, time representation and normalization, and template filling.

**Key points** (skim):
- 20.2 lists the relation-extraction algorithms, from patterns to distant supervision. READ
- 20.2.6 Evaluation of Relation Extraction uses precision, recall and F-measure. READ
- 20.7 covers temporal expression extraction, normalization and event ordering. READ

**Relevance to our project**: Not relevant. The project's knowledge base is review text, but the course has not yet reached retrieval or extraction, and the chapter does not bear on dialogue or agent evaluation. A reviewer might ask about extracting structured facts (price, cuisine) from reviews. If so, 20.1 to 20.2 is the place to look, but the chapter does not address that use case.

**Caveats**: Extraction is pre-LLM in framing. Evaluation is extraction accuracy, not generated text.

---

## Chapter 21: Semantic Role Labeling

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 21 "Semantic Role Labeling". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/21.pdf. Draft, not the published version.

**Access**: opened fully (full chapter text, about pages 1 to 20 plus references through about page 22; exercises a heading only).

**What it is**: The chapter introduces semantic roles (agent, theme, instrument and so on). It compares thematic roles with PropBank and FrameNet labels, describes feature-based and neural SRL, and covers selectional restrictions and preferences.

**Key points** (skim):
- 21.4 (PropBank) and 21.5 (FrameNet) compare role inventories. READ
- 21.6.3 Evaluation of SRL uses exact-match precision, recall and F on CoNLL data. READ
- 21.7 selectional restrictions. READ
- Dialogue, question answering and sentiment appear only in the historical notes. READ

**Relevance to our project**: Not relevant.

**Caveats**: Predicate-argument structure. No generated-text metrics.

---

## Chapter 22: Lexicons for Sentiment, Affect, and Connotation

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 22 "Lexicons for Sentiment, Affect, and Connotation". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/22.pdf. Draft, not the published version.

**Access**: opened fully (chapter body, figures, historical notes, exercises and references returned). The text gives no page numbers. Figure text is partly garbled.

**What it is**: The chapter defines emotion, mood and attitude, and surveys sentiment and affect lexicons. It covers how to build lexicons by human labeling, semi-supervised seed methods and supervised signals, how lexicons feed sentiment and affect classifiers, and connotation frames.

**Key points** (skim):
- 22.2 surveys available sentiment and affect lexicons. READ
- 22.3 describes human labeling and reports split-half reliability for the NRC VAD lexicon. READ
- 22.5 covers supervised word sentiment, with the log-odds ratio informative Dirichlet prior. READ
- 22.6 covers using lexicons for sentiment recognition. READ

**Relevance to our project**: Medium, for the sentiment side of our data. Our knowledge base is customer reviews with opinions, so 22.3's note on split-half reliability could support a sentence on annotator agreement for a small human-labeled set, if we label one. It is background only. It is not a source for LLM-judge agreement.

**Caveats**: Lexicon-based sentiment, not LLM-based. Its agreement discussion is about how lexicons were built, not about judging generated dialogue. It does not bear on generated-text metrics. The chapter does not formally test significance.

---

## Chapter 23: Coreference Resolution and Entity Linking

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 23 "Coreference Resolution and Entity Linking". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/23.pdf. Draft, not the published version.

**Access**: opened partly. The tool covered characters 0 to 100000 of 113548. The text is cut off partway through the bibliography. Exercises are a heading only. Sections 23.1 to 23.11 were all visible in the returned text, so I did not need the remainder for the headings or for the evaluation section.

**What it is**: The chapter covers how discourse entities are referred to and how systems detect mentions and cluster them into coreference chains. It surveys mention-pair, mention-ranking and entity-based architectures, linking mentions to knowledge-base entities, Winograd-style problems and gender bias.

**Key points** (skim):
- 23.8 Evaluation of Coreference Resolution covers MUC, B-cubed, CEAF, BLANC and LEA. READ
- 23.7 covers entity linking, including applying it to questions. READ
- The introduction cites a question-answering example and a dialogue reference such as "the second one" as motivation. READ

**Relevance to our project**: Low. If the Expert's reviews or the dialogue ever need coreference (for example "the second one" in a turn), the chapter explains the problem. The evaluation section is for coreference clusters, not generated text, so it does not fit our metrics.

**Caveats**: Coreference metrics measure cluster overlap, not conversational quality.

---

## Chapter 24: Discourse Coherence

**Verified citation**: Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, 3rd ed. draft, January 2026, Chapter 24 "Discourse Coherence". URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/24.pdf. Draft, not the published version.

**Access**: opened fully (full chapter text returned, including exercises and references). Figures and tables are garbled, so some diagram detail may be lost.

**What it is**: The chapter explains what makes a text coherent, both locally (coherence relations, entity-based coherence, lexical cohesion) and globally (genre structure such as argumentation and scientific discourse). It covers RST, PDTB, Centering Theory, the entity grid and neural self-supervised coherence models.

**Key points** (skim):
- 24.1 covers coherence relations, with RST (24.1.1) and PDTB (24.1.2). READ
- 24.3 covers Centering and the entity grid, and 24.3.3 covers evaluating neural and entity-based coherence. READ
- 24.3.3 says humans rated document coherence to train classifiers. This is about human-written text, not generated text. READ
- 24.2.2 mentions RST-Pareval F1 for parser evaluation. READ

**Relevance to our project**: Medium, if we score coherence. The entity grid (24.3.2) and the self-supervised coherence tasks (24.3.3) are concrete, citable baselines for "is this conversation coherent?" Our subjective metrics could draw on them. The chapter does not evaluate LLM-generated dialogue, so any use should say so.

**Caveats**: Written for monologic text (documents, papers). It does not cover dialogue coherence with turn-taking or LLM outputs. Its coherence models are not LLM judges.

---

## Summary table (for the caller)

| Chapter | Title (as printed) | Access | Relevance to project |
|---|---|---|---|
| 16 | Text-to-Speech | opened fully | none |
| 17 | Sequence Labeling for Parts of Speech and Named Entities | opened fully | low (17.6 paired bootstrap or randomization test for comparing F1) |
| 18 | Context-Free Grammars and Constituency Parsing | opened fully | none |
| 19 | Dependency Parsing | opened fully | none |
| 20 | Information Extraction: Relations, Events, and Time | opened fully | none |
| 21 | Semantic Role Labeling | opened fully | none |
| 22 | Lexicons for Sentiment, Affect, and Connotation | opened fully | medium for sentiment data; 22.3 split-half reliability as background for annotation agreement |
| 23 | Coreference Resolution and Entity Linking | opened partly (about 88%) | low (23.8 coreference metrics, not generated text) |
| 24 | Discourse Coherence | opened fully | medium if we score coherence (24.3.2 entity grid, 24.3.3 self-supervised coherence) |

## Citation mismatches

None checked against a reading-list entry, since my batch gave chapter URLs and not list entries. Chapter numbers and titles in the PDFs match the batch's chapter numbers. The PDFs' running headers read "Draft of January 6, 2026", which is consistent with the January 2026 edition named in the batch.

## Links I could not open

None.

## The five claims I am least sure of

1. That 17.6 recommends a paired bootstrap or randomization test for comparing NER F1 is what the extracted text said. Section 17.6 is the only place I read it. I did not read the later section that gives the details.
2. The 22.3 split-half reliability claim for the NRC VAD lexicon comes from a summary of extracted text. I did not confirm the exact figure or table.
3. Chapter 23 was read only up to character 100000 of 113548. Its evaluation section (23.8) and headings are visible in that part, but I did not read the rest of the bibliography.
4. The chapter 24 claim that humans rated coherence to train classifiers (24.3.3) comes from one summary. I did not check the wording.
5. The page counts I give (for example "about 27 pages" for ch.17 and "pages 1 to 28" for ch.20) are estimates from running headers or extraction, not checked against the printed PDFs.


---

<!-- file: F-slp3-appendices-toc.md -->

# F. Jurafsky & Martin SLP3 appendices A to J, index page, and full-book title and TOC

Batch: appendices A to J (not assigned in the course), the index of https://web.stanford.edu/~jurafsky/slp3/old_jan26/, and the full book ed3book_jan26.pdf (title page and TOC only).

Source tags: READ = in the text WebFetch returned for that document. SEARCH = snippet only (none used here). OURS = my inference.
Caveat for the whole file: every "READ" item comes from a WebFetch answer (a small model summarizing the PDF), not from the raw PDF. Section numbers and titles were consistent across two or more calls where I re-checked, but exact wording should be checked against the PDF before anything is cited.

## Summary table

| File | Printed label and title | Access | Relevance |
|---|---|---|---|
| A.pdf | Appendix A, Hidden Markov Models | opened fully | none |
| B.pdf | Appendix B, Naive Bayes, Text Classification, and Sentiment | opened fully (two passes) | low to medium (significance testing B.9; metrics B.7 and B.8; lexicons B.4) |
| C.pdf | Labelled "CHAPTER B" / "APPENDIX B", Kneser-Ney Smoothing | opened fully | none (label mismatch, see below) |
| D.pdf | Chapter/Appendix D, Spelling Correction and the Noisy Channel | opened fully | none |
| E.pdf | Appendix E, Statistical Constituency Parsing | opened fully | none |
| F.pdf | Appendix F, Constituency Grammars | opened fully | none (one passing dialogue mention) |
| G.pdf | Appendix G, Combinatory Categorial Grammar | opened fully | none |
| H.pdf | Appendix H, Logical Representations of Sentence Meaning | opened fully (H.1 re-checked) | low (restaurant KB example, H.1) |
| I.pdf | none | file is empty (0 bytes), no text returned | could not open |
| J.pdf | Appendix J, Pointwise Mutual Information (PMI) | opened fully | none |
| index page | "Index of /~jurafsky/slp3/old_jan26" | opened fully | n/a (see index notes) |
| ed3book_jan26.pdf | Speech and Language Processing, Third Edition draft, Jan 6 2026 | partly (title page and first 100,000 of about 1.9M characters; second pass at offset 100,000 for appendix list) | low to medium (chapter 22 and 25 titles; see TOC) |

---

## Appendix A (A.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix A, "Hidden Markov Models," draft of January 6, 2026 (date from the book's title page). Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/A.pdf. Draft, not a published edition.

**Access:** opened fully (whole document, including historical notes and references).

**What it is:** A standalone appendix on Markov chains and hidden Markov models, with the forward, Viterbi and forward-backward algorithms. It is a background chapter on sequence models and does not touch dialogue or evaluation.

**Key points (skim):**
- Numbered sections: A.1 Markov Chains; A.2 The Hidden Markov Model; A.3 Likelihood Computation: The Forward Algorithm; A.4 Decoding: The Viterbi Algorithm; A.5 HMM Training: The Forward-Backward Algorithm; A.6 Summary. (READ)
- Covers the Markov assumption and the three HMM problems: likelihood, decoding, learning. (READ, A.2)
- Uses an ice-cream and weather example for forward-backward training. (READ, A.5)
- None of the project-relevant topics (dialogue, QA, generated-text evaluation, human evaluation, significance testing, kappa, sentiment lexicons) appear in the text. (READ)

**Relevance to our project:** not relevant.

**Caveats:** none for our purposes.

---

## Appendix B (B.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix B, "Naive Bayes, Text Classification, and Sentiment," draft of January 6, 2026. Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/B.pdf. Draft.

**Label check:** The first page prints "CHAPTER B"; running headers print "APPENDIX B". Consistent.

**Access:** opened fully (first pass for the whole document, second targeted pass for B.4, B.7, B.8, B.9, B.9.1).

**What it is:** A classification chapter that introduces multinomial naive Bayes, applies it to sentiment and spam, and then covers the evaluation toolkit (precision, recall, F-measure, cross-validation, bootstrap significance testing). Dialogue, QA, generated-text evaluation and inter-annotator agreement are not covered.

**Key points (deep read of the relevant parts):**
- B.7 (Evaluation: Precision, Recall, F-measure): accuracy is misleading with unbalanced classes; the text's example is a classifier labelling every tweet "not about pie" that scores 99.99% accuracy with zero recall. (READ)
- B.7: macroaveraging versus microaveraging for multiclass; the worked example gives macro precision .60 and micro precision .73. (READ, Figs. B.5 to B.6)
- B.8 (Test Sets and Cross-validation): train, tune on a devset, test once; 10-fold cross-validation is the common choice; warns that full CV can leak test information and recommends CV inside the training set with a fixed test set. (READ, Fig. B.7)
- B.9 (Statistical Significance Testing): a single observed gap does not prove A is better; null hypothesis and p-value; NLP typically uses non-parametric sampling tests (approximate randomization or bootstrap) rather than t-tests. (READ)
- B.9.1 (The Paired Bootstrap Test): pairs each test item's result for system A with system B on the same test set; the text says bootstrapping works for any metric, including precision, recall, F1 and BLEU. (READ)
- B.9.1: the worked example uses a 10-document test set and resamples it; the text says real test sets are much larger and suggests b around 10^5 resamples. Fig. B.9 gives the algorithm and the worked example reports p = .0047 (47 of 10,000 sets). (READ)
- B.4 (Optimizing for Sentiment Analysis): binarized counts, NOT_ negation marking, and sentiment lexicons (General Inquirer, LIWC, Hu and Liu opinion lexicon, MPQA with 6,885 words) used as features when labelled data is scarce. (READ)
- B.10 (Avoiding Harms in Classification) recommends model cards. (READ, section present; not read in detail)

**Relevance to our project:**
- Subjective and objective metric comparison between the two Expert versions: B.9 and B.9.1 (paired bootstrap on the same test set) could support a claim that a difference between two Expert versions is not just noise. Medium. The example is about classifiers, and the text itself mentions BLEU only as a metric the bootstrap can apply to, so we would have to justify applying it to dialogue outcomes ourselves (OURS).
- Task-success rate and per-metric precision/recall: B.7 could be cited for why accuracy alone misleads when most conversations succeed or fail in one direction (OURS applied to our setting). Low.
- Test-set and cross-validation design for the judge comparison: B.8. Low.
- Sentiment lexicons (B.4): our knowledge base is customer reviews, but the lexicon material is about classifying sentiment with lexicon features, not about our Expert's retrieval or reasoning. Low; citing it for "sentiment-based review filtering" would stretch it.
- Not relevant: dialogue systems, chatbots, QA, generated-text evaluation, human evaluation, inter-annotator agreement and Cohen's kappa are not in this appendix. Kappa is not here; do not cite B for it.

**Caveats:** Classifier and test-set setting, not dialogue. The bootstrap section is about a fixed test set of items with per-item scores; applying it to LLM conversations needs an explicit justification.

---

## Appendix C (C.pdf): label mismatch

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix B (as printed), "Kneser-Ney Smoothing," draft of January 6, 2026. Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/C.pdf.

**Label mismatch (confirmed in a second fetch):** The file is C.pdf, but the PDF prints "CHAPTER B" on the first page and "APPENDIX B" in every running header. A second WebFetch quoted the opening lines and found no other letter. Two files therefore claim Appendix B (B.pdf is Naive Bayes). Cite this as "Appendix B" with the title, and flag that the file is named C.

**Access:** opened fully (whole document, first page to references).

**What it is:** An n-gram smoothing appendix on absolute discounting and Kneser-Ney (interpolated and modified) discounting. It is about language-model probability estimation.

**Key points (skim):**
- B.1 Absolute Discounting; B.2 Kneser-Ney Discounting. (READ)
- Continuation probability: the unigram is based on how many different contexts a word appears in; the example is "Kong", which is frequent but follows only "Hong". (READ, B.2)
- Modified Kneser-Ney uses three discounts for counts of 1, 2, and 3 or more. (READ, B.2)
- No project-relevant topics are mentioned. The held-out corpus in B.1 is for estimating discounts, not for evaluation. (READ)

**Relevance to our project:** not relevant (n-gram smoothing; course uses neural LMs, so at most background for the N-gram chapter).

---

## Appendix D (D.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix D, "Spelling Correction and the Noisy Channel," draft of January 6, 2026. Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/D.pdf. First page prints "CHAPTER D"; running headers "APPENDIX D". Consistent.

**Access:** opened fully.

**What it is:** Spelling correction using the noisy channel model, covering non-word and real-word errors and later refinements (edit-model partitions, pronunciation keys). It is a classic NLP application with no dialogue component.

**Key points (skim):**
- D.1 The Noisy Channel Model (Bayes' rule, language model prior, confusion-matrix channel, worked example). (READ)
- D.2 Real-word spelling errors (sentence-level candidates with a trigram LM). (READ)
- D.3 Noisy Channel Model: The State of the Art; D.3.1 Improved Edit Models: Partitions and Pronunciation. (READ)
- D.1 says spelling correction is evaluated by holding out training, development and test sets from lists of errors. (READ)

**Relevance to our project:** not relevant. The only evaluation mention is a held-out split for spelling errors.

**Caveats:** none.

---

## Appendix E (E.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix E, "Statistical Constituency Parsing," draft of January 6, 2026. First page prints "CHAPTER E". Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/E.pdf.

**Access:** opened fully (including figures and tables as extracted).

**What it is:** PCFGs and probabilistic CKY parsing, plus their known weaknesses and the lexicalized Collins parser. It is parsing theory.

**Key points (skim):**
- Numbered sections E.1 to E.7, including E.1.1 PCFGs for Disambiguation, E.1.2 PCFGs for Language Modeling, E.4 Problems with PCFGs, E.6.1 The Collins Parser. (READ)
- Probabilistic CKY finds the most probable parse; rule probabilities are learned from treebanks or with inside-outside. (READ, E.2 and E.3)
- Names the independence and lexical-dependency weaknesses of PCFGs. (READ, E.4)

**Relevance to our project:** not relevant.

**Caveats:** none.

---

## Appendix F (F.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix F, "Constituency Grammars," draft of January 6, 2026. First page prints "CHAPTER F"; running headers "APPENDIX F". Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/F.pdf.

**Access:** opened fully.

**What it is:** Context-free grammars, English constituency rules, treebanks (mainly Penn Treebank), head-finding and Chomsky normal form. It is syntax background.

**Key points (skim):**
- Sections F.1 Constituency; F.2 Context-Free Grammars; F.3 Some Grammar Rules for English; F.4 Treebanks (F.4.1 Penn Treebank); F.5 Grammar Equivalence and Normal Form. (READ)
- The unnumbered chapter introduction names "dialogue understanding" as a CFG application and describes ATIS as an early spoken system for booking flights. (READ, passing mention)
- F.4 says treebank parses were produced by parsers and then hand-corrected by linguists. This is annotation, not evaluation. (READ, F.4)

**Relevance to our project:** not relevant. The dialogue mention is one passing sentence in the introduction, about grammar applications; it would not support any claim about our agents.

**Caveats:** none.

---

## Appendix G (G.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix G, "Combinatory Categorial Grammar," draft of January 6, 2026. First page prints "CHAPTER G". Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/G.pdf.

**Access:** opened fully.

**What it is:** The CCG formalism: categories, lexicon, combination rules, CCGbank and CCG parsing with supertagging and A* search. It is parsing theory.

**Key points (skim):**
- Sections G.1 CCG Categories through G.6 CCG Parsing (G.6.1 Supertagging; G.6.2 A* parsing). (READ)
- Describes CCGbank as derived from the Penn Treebank. (READ, G.4)
- Does not mention any project-relevant topic. (READ)

**Relevance to our project:** not relevant.

**Caveats:** none.

---

## Appendix H (H.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix H, "Logical Representations of Sentence Meaning," draft of January 6, 2026. First page prints "CHAPTER H"; running headers "APPENDIX H". Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/H.pdf.

**Access:** opened fully; section H.1 re-checked in a targeted second call.

**What it is:** Meaning representation with first-order logic, lambda notation, event representations and description logics. It is formal semantics background.

**Key points (deep read of H.1 only):**
- H.1 Computational Desiderata for Representations uses a restaurant advice system with a knowledge base of facts about restaurants. The central question is whether a restaurant serves vegetarian food, answered by matching a logical form against the knowledge base. (READ, H.1)
- The text says the system must answer "No" when its knowledge is complete and must say it does not know when knowledge is incomplete. (READ, H.1)
- The Inference and Variables subsection (inside H.3) adds common-sense facts, such as what vegetarians eat, and uses requests like "Can vegetarians eat at Maharani?". (READ, H.1 and H.3.5)
- H.1 does not discuss dialogue or multi-turn interaction. The word "question-answering" is not used in the section. (READ)
- OURS: the "No" versus "I don't know" distinction under incomplete knowledge is a possible background point for how our Expert should answer requests the reviews cannot settle. This is my inference, not the appendix's claim about our design.

**Relevance to our project:** low. Possible background for knowledge-base answering and for the difference between a negative answer and an unknown answer (knowledge-base design, low). Not a source for retrieval, dialogue or evaluation claims.

**Caveats:** The example is a logic-based KB, not a review corpus or an LLM. Do not cite it for retrieval-augmented generation.

---

## Appendix I (I.pdf): could not open

**Access:** could not open as text. The file is listed on the index as 0 bytes. WebFetch returned that the document is empty or cannot be read and contains no machine-readable text. Tried once, as instructed.

**Relevance to our project:** unknown; nothing to read.

---

## Appendix J (J.pdf)

**Verified citation:** Daniel Jurafsky and James H. Martin, "Speech and Language Processing," 3rd ed. draft, Appendix J, "Pointwise Mutual Information (PMI)," draft of January 6, 2026. First page prints "CHAPTER" and "J"; running headers "APPENDIX J". Page numbers not captured. URL read: https://web.stanford.edu/~jurafsky/slp3/old_jan26/J.pdf.

**Access:** opened fully (about four pages, one chapter excerpt).

**What it is:** A short note on pointwise mutual information for word co-occurrence, positive PMI and smoothing choices, used for word vectors. Not about dialogue or evaluation.

**Key points (skim):**
- Defines PMI and the positive variant PPMI, which replaces negative values with zero. (READ)
- Worked example with co-occurrence counts for "cherry", "digital" and "information". (READ)
- Smoothing options: context smoothing with alpha = 0.75 and Laplace smoothing; Levy et al. (2015) are cited for alpha = 0.75 improving embedding tasks. (READ)
- In the opening discussion it asks whether negative PMI scores of "unrelatedness" can be checked with human judgments. This is an aside, not an evaluation method. (READ)

**Relevance to our project:** not relevant. It could only bear on the Embeddings material in the course, not on our agents or metrics.

**Caveats:** none.

---

## Index page

**Access:** opened fully.

**Observations (READ from the index listing):**
- Title line "Index of /~jurafsky/slp3/old_jan26", last modified 2026-01-06, between 08:31 and 08:32. No book title printed on the page.
- Numbered PDFs listed: 2.pdf to 25.pdf (no 1.pdf appears in the listing). The chapter count (25) matches the TOC below. OURS: the missing 1.pdf is worth a check if someone needs chapter 1 from this set.
- Lettered PDFs listed: A.pdf to K.pdf. K.pdf (592K) is not in my batch. The full book also cites "Appendix K" for text classification, so someone should check K.pdf.
- Full-book files: ed3book.pdf and ed3book_jan26.pdf, both about 25M.
- Also listed: thanks.html (16K). The column headers are sort controls, not files.
- I.pdf is listed at 0 bytes, which matches what I found.

---

## Full book (ed3book_jan26.pdf): title page and TOC

**Access:** partly. I read the title page and the first 100,000 characters (of about 1.9M) where the TOC sits. A second call at offset 100,000 looked for an appendix list and found none in that part. The TOC answer is WebFetch's summary of that part, so check the exact titles against the PDF.

**Title page (READ):**
- Full title: "Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models"
- Authors: Daniel Jurafsky (Stanford University) and James H. Martin (University of Colorado at Boulder)
- Edition: "Third Edition draft"
- Date: "Draft of January 6, 2026", "Copyright 2026".

**Table of contents (READ; from front matter after the Summary of Contents, printed pages about 3 to 8):**

Part I: Large Language Models
1. Introduction
2. Words and Tokens
3. N-gram Language Models
4. Logistic Regression
5. Embeddings
6. Neural Networks
7. Large Language Models
8. Transformers
9. Masked Language Models
10. Post-training: Instruction Tuning, Alignment, and Test-Time Compute
11. Retrieval-based Models
12. Machine Translation
13. RNNs and LSTMs
14. Phonetics and Speech Feature Extraction
15. Automatic Speech Recognition
16. Text-to-Speech

Part II: Annotating Linguistic Structure
17. Sequence Labeling for Parts of Speech and Named Entities
18. Context-Free Grammars and Constituency Parsing
19. Dependency Parsing
20. Information Extraction: Relations, Events, and Time
21. Semantic Role Labeling
22. Lexicons for Sentiment, Affect, and Connotation
23. Coreference Resolution and Entity Linking
24. Discourse Coherence
25. Conversation and its Structure

Appendices: the TOC lists no appendix letters or titles. The only back matter named is the Bibliography and the Subject Index (READ, from the TOC answer). The second call found no appendix list in characters 100,000 to 200,000. In-text cross-references mention "Appendix D" and "Appendix K" (READ), which fits the existence of those files.

**Mismatch and check notes for the course citations:**
- Chapter 25 is titled "Conversation and its Structure". Our course lecture is titled "Conversation and Its Structure". The chapter number in this draft is 25. We cannot check which edition the course cites from this file alone; that is for whoever compares the reading list.
- Chapter 22 (Lexicons for Sentiment, Affect, and Connotation) and Chapter 11 (Retrieval-based Models) are relevant topic titles. They are outside my batch; I only report the titles here, not their content.

---

## Caveats across the batch

- All claims are from WebFetch summaries of PDFs. Section numbers and titles were checked by a second call only for B, H, C and the TOC. Others are single-pass.
- Draft (January 2026) text, not a published edition. Page numbers were not captured.
- Nothing here supports a claim about our Expert agent, the DSTC11 data or LLM judges. Appendix B is the only one with evaluation tools a reader might cite, and it is for classifiers.

## Five claims I am least sure of

1. That the TOC has exactly 25 chapters with no appendix list (the TOC was a model summary of the first 100,000 characters).
2. That C.pdf is labelled Appendix B (confirmed by one quote, but the summary model could have misread the header).
3. That the B.9.1 p-value example (47 of 10,000, p = .0047) is reported as written.
4. That chapter 1 is absent from the index listing rather than hidden by the listing.
5. That the H.1 "No" versus "don't know" point applies to our Expert design. This is my inference, not the appendix's claim.


---

<!-- file: G-papers-dialogue-data.md -->

# G: Papers behind the dialogue data (MultiWOZ, SK-TOD / DSTC11-T5, Baez Santamaria et al.)

Method note: all reading was through WebFetch, which returns a small model's answer, not raw text. Numbers below are what that answer reported. Items marked READ were in returned text; OURS is my inference. Nothing was filled from memory.

---

## 1. MultiWOZ (Budzianowski et al., EMNLP 2018)

**Verified citation** (READ, from https://aclanthology.org/D18-1547.pdf, published ACL Anthology version): Pawel Budzianowski, Tsung-Hsien Wen, Bo-Hsiang Tseng, Inigo Casanueva, Stefan Ultes, Osman Ramadan, Milica Gasic. 2018. MultiWOZ - A Large-Scale Multi-Domain Wizard-of-Oz Dataset for Task-Oriented Dialogue Modelling. Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pp. 5016-5026, Brussels, Belgium. ACL.

**Mismatch with course page**: the course page says 2020. The paper says 2018 (the proceedings are EMNLP 2018). Author list matches (7 authors, same order). The course page did not give pages; they are 5016-5026.

**Access**: PDF opened fully (one fetch, structured answer covering all sections). DOI link not separately opened (it resolves to the same paper). The .mp4 is a talk video, not read. The VU Library link was not tried for this paper (expected login wall).

**What it is**: The paper that introduced MultiWOZ, a human-human written dialogue corpus collected with crowd workers in a Wizard-of-Oz setup. It spans 7 domains, is labelled with belief states and dialogue acts, and ships with baselines for state tracking and response generation.

**Key points**
- Collection (Sec 3): Wizard-of-Oz on Amazon Mechanical Turk. One worker plays the user and another plays the clerk (wizard). Tasks are templates sampled from an ontology, single- and multi-domain, some with booking, some deliberately with no matching database entry. User goals are revealed gradually. The wizard queries the database through a GUI form. Because form constraints persist across turns, the belief state is annotated implicitly. READ.
- Dialogue acts were annotated in a separate second phase (Sec 3.4); act set grew from 8 to 13 during qualification trials. Weighted kappa 0.884 over 291 turns (0.704 in initial trials). 1,249 workers in total. READ.
- Domains (Sec 3.1 / 4): 7 domains: Attraction, Hospital, Police, Hotel, Restaurant, Taxi, Train. Hotel, Restaurant, Taxi, Train have a booking sub-task. Dialogues cover 1 to 5 domains. READ.
- Size (Sec 4.1, Table 1): 10,438 dialogues (about 8,438 train, 1,000 val, 1,000 test); 3,406 single-domain and 7,032 multi-domain; 115,434 turns. Average turns per dialogue 8.93 (single-domain) and 15.39 (multi-domain); Table 1 gives 13.68 for the training split. Average utterance length 11.75 tokens (user) and 15.12 (wizard). Train vocabulary 24,071 types, 1,520,970 tokens. READ.
- Annotations (Sec 4.2, Table 2): belief state per turn, dialogue acts (13 act types, universal and domain slots), database pointer used by the response generator. About 60% of system turns carry more than one act. READ.
- Restaurant slots (Table 2): area, price range, food type, name, number of choices. Hotel slots: the same core slots plus internet, parking, stars. Shared slots: address, postcode, phone. Booking slots: people, day, reference number, and for hotels number of days. READ (via summary of Table 2).
- The paper does not report entity counts for the hotel or restaurant databases. READ (absence). If we need them, do not cite this paper for it.
- Benchmarks (Sec 5): (a) dialogue state tracking, restaurant subset only (Table 3): joint goal accuracy 85.5 on WOZ 2.0 vs 80.9 on MultiWOZ, overall accuracy 96.5 vs 89.7. (b) dialogue-context-to-text generation (Table 4), seq2seq with oracle belief state and DB pointer, metrics Inform / Success / BLEU: on MultiWOZ Inform 71.29 / 71.33, Success 60.29 / 60.96, BLEU 0.188 / 0.189 (without / with attention); on Cam676 Inform 99.17 / 99.58. (c) dialogue-act-to-text (Table 5), SC-LSTM on restaurant: SER 4.378, BLEU 0.616 vs SFX 0.46 and 0.731. READ.
- Stated limitations: validation and test keep only fully successful dialogues; some dialogues are incoherent; turns longer than speech; the generation baseline uses oracle belief state so it is not end-to-end; DST and act-to-text are restricted to restaurant. READ (the paper has no dedicated limitations section; some of these are implied).

**Relevance**
- Data (DSTC11-T5 / MultiWOZ): high. Cite for "MultiWOZ is a crowd-sourced Wizard-of-Oz corpus of about 10k dialogues in 7 domains, including Hotel and Restaurant with booking" and for Inform / Success as the standard task-completion metrics for task-oriented dialogue.
- Conversation design: medium. Its Inform and Success metrics are one precedent for our "was the request fulfilled" measure (OURS; the paper defines them for system-vs-corpus evaluation, not for LLM agents).
- Frame-based dialogue course material: the belief-state-with-slots design ties directly to the frame-based TOD lecture (OURS).

**Caveats**: Our project uses the DSTC11 version, which is built on MultiWOZ 2.1 (per the SK-TOD paper), not the original 2018 release this paper describes. Counts here are for original MultiWOZ, not for the hotel+restaurant subset used in DSTC11-T5.

---

## 2. SK-TOD / DSTC11 Track 5 (Zhao et al., SIGDIAL 2023)

**Verified citation** (READ, from the arXiv copy https://arxiv.org/pdf/2305.12091, which is a preprint; I did NOT read the SIGDIAL PDF, so table numbers below are from the arXiv version and could differ from the published one): Chao Zhao, Spandana Gella, Seokhwan Kim, Di Jin, Devamanyu Hazarika, Alexandros Papangelis, Behnam Hedayatnia, Mahdi Namazifar, Yang Liu, Dilek Hakkani-Tur. "What do others think?": Task-Oriented Conversational Modeling with Subjective Knowledge. SIGDIAL 2023 (venue and year from the reading-list entry and DOI 10.18653/v1/2023.sigdial-1.28; page numbers not seen). The repo README tells users to cite arXiv:2305.12091.

**Access**: arXiv PDF read through two targeted fetches, covering the full paper including appendices D and E at summary level. SIGDIAL PDF and DOI not opened. VU Library link: fetch returned INVALID_URL, not readable. Repo pages: see 2b.

**What it is**: Defines subjective-knowledge task-oriented dialogue (SK-TOD): when a user in a hotel or restaurant dialogue asks for opinions (for example about WiFi quality), the system must find relevant review sentences and answer by summarising them, including minority views. The paper builds a dataset on MultiWOZ, gives baselines for each sub-task, and a small human evaluation.

**Key points**
- Task (Sec 3): given dialogue context, decide whether the last user turn seeks subjective information; if so select all relevant review sentences and generate a response that reflects the diversity and proportion of opinions. READ.
- Subtasks (Sec 5): Knowledge-Seeking Turn Detection (5.1, binary), Entity Tracking (5.2, extra step before selection), Knowledge Selection (5.3, bi- and cross-encoders), Response Generation (5.4, with ABSA sentiment cues). The DSTC repo lists the three official subtasks (KTD, KS, RG); entity tracking is a pipeline step in the paper, not an official track subtask. READ.
- Construction (Sec 4.1, App A): base is MultiWOZ hotel and restaurant dialogues (ethics section names MultiWOZ 2.1). Mechanical Turk workers wrote reviews: 10 reviews for each of 33 hotels and 110 restaurants. Each writer got a sampled persona, aspects and sentiments, sampled to follow real rating distributions; writers were pre-qualified English speakers from US, CA, GB. For each MultiWOZ dialogue, another worker was given an aspect and inserted a subjective user request at a chosen position, with the dialogue truncated there. Workers marked the gold entity; review sentences matching the aspect are the relevant snippets. Workers then wrote a response summarising all relevant snippets (including minority opinions) using only the given reviews. READ.
- Negatives (Sec 4.2): 18,383 dialogues with non-subjective requests sampled from original MultiWOZ. READ.
- Size (Sec 4.2, Table 2): 19,696 subjective instances in total; train / val / test = 14,768 / 2,129 / 2,799. Seen vs unseen: val 1,471 / 658, test 1,547 / 1,252 (train all seen). Multi-entity instances 412 / 199 / 436 (1,047 total). Average snippets per instance 3.80 / 4.07 / 4.21 (3.88 overall). Average utterances per instance about 9.3 to 9.4; request about 9 tokens; response about 24 tokens. Knowledge overall: 143 entities, 1,430 reviews, 8,013 sentences. READ.
- NOT in the paper: per-split counts of entities, reviews, sentences, and any split by domain (hotel vs restaurant). The only domain breakdown is the entity count 33 hotels + 110 restaurants. READ (absence, per the fetch answer; I did not see the appendices in full, so a domain table there cannot be fully excluded).
- Baselines (Sec 6): KTD (Table 3) BERT/RoBERTa/ALBERT/DeBERTa all around 99.5 to 99.7% accuracy. Entity tracking (6.2) fuzzy n-gram match, 92.18% instance accuracy (1.8% missed a gold entity, 7.6% spurious entity). Knowledge selection (Table 4): TF-IDF mAP 45.97, BM25 mAP 45.42; best bi-encoder DeBERTa mAP 83.43; best cross-encoder DeBERTa instance F1 84.6, snippet F1 84.18, mAP 91.84; seen vs unseen aspects F1 89.93 vs 78.03. Response generation (Table 5): EXT, GPT-2, DialoGPT, BART, BART_ABSA, T5, T5_ABSA; metrics BLEU, ROUGE-1/2/L, METEOR, BERTScore. T5_ABSA best BLEU 10.97 and ROUGE-L 28.88; BART_ABSA best BERTScore 41.75; random extractive baseline BLEU 2.89; encoder-decoder beat GPT-style. READ.
- Human evaluation of RG (Sec 6.4, Table 6, App D): three criteria on a 5-point Likert scale: Appropriateness (fluent and fits the context), Aspect Accuracy (gives relevant useful information about the asked aspect), Sentiment Accuracy (sentiment proportion of the response matches the snippets). 240 test instances, three crowd workers each. Gwet's gamma 0.7270 / 0.7535 / 0.6239. Table 6: Reference 4.70 / 4.77 / 4.50; T5_ABSA 4.49 / 4.67 / 3.98; T5 4.40 / 4.63 / 3.87; BART_ABSA 4.58 / 4.66 / 3.80; GPT-2 4.55 / 4.54 / 3.20. READ. These are summary-level definitions; the exact annotation wording is in Appendix D, which I only saw summarised.
- End-to-end (Sec 7, Table 8): gold knowledge BLEU 10.80 / ROUGE-L 28.52 / BERTScore 41.12; with predicted knowledge (KS) BLEU 10.20 / ROUGE-L 27.78 / BERTScore 40.64; adding ET and KTD barely changes (BLEU about 10.27 to 10.29). Knowledge-selection errors hurt generation more than ET or KTD errors. READ.
- Fact-TOD comparison (Sec 8, Table 9): models trained on FAQ-grounded data do worse on SK-TOD: KTD acc 87.62 vs 99.71, KS macro-F 59.55 vs 84.60, BLEU 6.15 vs 10.80. They tend to copy a single snippet. READ.
- Findings and challenges: large gap between human and machine responses, mainly in sentiment proportion; ABSA cues help but do not close it; hard parts are aggregating diverse or contradictory opinions, generalising to unseen aspects, and error propagation from selection. READ.
- Limitations (stated): only two domains; crowd-written reviews are fewer and shorter than real ones; LLMs not explored. READ.
- Agree vs disagree: the paper does NOT report what share of instances have agreeing vs disagreeing reviews. It only says annotators were told to describe minority opinions and that responses should reflect proportions. READ (absence). Multi-entity count is 1,047, which is a different quantity.

**Relevance**
- Data: high. Cite for dataset construction, size, the claim that reviews are crowd-written with sampled personas, and that responses are meant to cover minority opinions.
- Expert agent / knowledge access: high. Cite for "knowledge selection must return all relevant sentences (recall matters), and selection errors propagate to the response" (Sec 7).
- Subjective metrics: high. The three human criteria (Appropriateness, Aspect Accuracy, Sentiment Accuracy) with 5-point Likert and Gwet's gamma are a ready template for our LLM-judge rubric and human-agreement step. Note they report Gwet's gamma, not Cohen's kappa.
- Objective metrics: medium. BLEU, ROUGE, METEOR, BERTScore as the reference-based metrics on this data.
- Fine-tuning: medium. T5/BART baselines (about 220M to 400M parameter encoder-decoder) show fine-tuning on this data works; no LLM baselines.

**Caveats**: Preprint read. No agent-agent setting; evaluation is single-turn response generation against a human-written reference. Models are 2022-era seq2seq, no LLM prompting. No hotel/restaurant split of stats.

### 2b. Repository pages

**https://github.com/alexa/dstc11-track5** (READ, landing page + raw data/README.md). Organisers listed: Kim, Gella, Zhao, Jin, Papangelis, Hedayatnia, Liu, Hakkani-Tur. Task: three subtasks (KTD: binary label; KS: list of candidates; knowledge-grounded RG). Data: augmented MultiWOZ 2.1 with added subjective knowledge-seeking turns; splits data/train, data/val, data/test; test may contain unseen domains, entities, locales. Metrics: KTD P/R/F; KS P/R/F/accuracy; RG BLEU, ROUGE, METEOR; KS and RG scores weighted by KTD performance (scripts/scores.py). Final ranking by human evaluation of selected systems on appropriateness and relevance to the given knowledge. Licences: code Apache 2.0, data CDLA-Sharing 1.0. Folders: baseline, bin, data, results, scripts. Timeline: train data 19 Dec 2022, test 24 Mar 2023. Baseline scores are not on the landing page (they are in baseline/README.md, not read). The landing page does not describe the file formats; those come from data/README.md.

**Data format** (READ from raw data/README.md of alexa repo; note the fetch tool said the README contains no sample records and that its JSON examples were illustrative, so do NOT cite the example values as real data):
- logs.json: list of instances; each instance is a list of turns `{speaker: "U" or "S", text}`. The instance is a partial dialogue ending at the target user turn.
- labels.json: list in the same order as logs. Fields: `target` (bool, is the last user turn knowledge-seeking; always present); `knowledge` (list, only if target is true) with items `{domain, entity_id (int), doc_type ("review" or "faq"), doc_id (int), sent_id (int, reviews only)}`; `response` (string, human-written knowledge-grounded reply, only if target is true). Same format is required for submissions (scripts.check_results validates).
- knowledge.json: domain ("hotel" or "restaurant") -> entity_id -> {name (entity-specific entries), reviews -> review_id -> {sentences -> sent_id -> sent, metadata (such as traveler type, dishes, drinks)}, faqs -> faq_id -> {question, answer}}. Labels point into it via domain, entity_id, doc_id (review_id or faq_id), sent_id.
- Uncertainty: whether `sentences` is a dict keyed by sent_id or a list was not clear in the returned text. Check the actual file in the notebook before relying on it. FAQs exist in the format; the SK-TOD paper focuses on reviews.

**https://github.com/lkra/dstc11-track5** (READ, landing page + data/README.md + CLTeamL/README.md via raw URLs; the github.com/tree/CLTeamL page was blocked by robots rules). The landing page is a copy of the alexa README with the same task text, data description and metrics, plus extra folders `CLTeamL` and `pred/val`. It never mentions the alexa repo, and the data README has the same format as above with no extra files. What it adds is CLTeamL:
- Authors: four CLTL PhD students named in its README: Lea Krause, Selene Baez Santamaria, Michiel van der Meer, Urja Khurana (all of VU/CLTL). Note Krause and Baez Santamaria are authors of document 3.
- Approach: split each response into a "summary" part (answer to the user based on knowledge) and a "questions" part (dialogue management, e.g. offering more help); enrich the dataset with dialogue acts for context utterances, sentiment per knowledge item and its average, and sentiment of the reference summary; hypothesis that summary sentiment should track the average knowledge sentiment; GPT-3 prompting (prompt style 1 best); post-prompting to extract the answer from step-by-step outputs; question manipulation (remove the question, or add the most frequent train question).
- Augmented files: CSV written by dataset_analysis.py to CLTeamL/data_analysis/output/analysis_$DATASET$.csv, with columns including `ref_know_avg_sentiment` and `ref_response_summary_sentiment`. The full column list was not documented in what I read. They are not new knowledge.json files.
- Scripts: prompting.py, post_prompting.py, manipulate_questions.py, analysis/ (dataset_analysis.py, sentiment_analysis.py, question_analysis.py, error_analysis.py, case_analysis.py, plot_trends.py). Needs an OpenAI API key. The README warns requirements.txt may be outdated.
- No results are given in the README text I saw.

**Relevance of 2b**: data format is needed for the Expert's knowledge loader and for deciding which fields the Beginner can never see (knowledge). The CLTeamL README is a close precedent for ours: prompting an LLM, splitting summary vs follow-up questions, sentiment of knowledge vs response. OURS: cite it as a course-group precedent, not as evidence of performance (no results seen). It is a code repository, not a paper.

---

## 3. Baez Santamaria et al. (BNAIC/BeNeLearn 2023)

**Verified citation** (READ from https://bnaic2023.tudelft.nl/static/media/BNAICBENELEARN_2023_paper_23.a7a48c6078e92bcb7550.pdf, the conference-site PDF; the URL name says BNAIC/BeNeLearn 2023 paper 23): Selene Baez Santamaria, Lea Krause, Lucia Donatelli, Piek Vossen (all Vrije Universiteit Amsterdam; Krause and Baez Santamaria marked as equal contributors). Title as printed in the PDF: "The Role of Personal Perspectives in Open-Domain Dialogue". The running header reads "Baez et al.". The text itself does not state venue, date or page range (no BNAIC/BeNeLearn mention inside the document); venue comes from the URL and the reading-list entry (SEARCH-level for venue).

**Mismatch / checks**
- Author order: Baez Santamaria, Krause, Donatelli, Vossen is the order printed in the paper. That matches the order in the task description. If a lecture slide gives a different order, the paper's order is the one above.
- Title: the PDF has no subtitle. The reading-list title ("... Towards Enhanced Data Modelling and Long-term Memory") was not found in the PDF; a web search for the long title only returned this same PDF. A subtitle may exist on another version (for example the conference programme), but I could not confirm that. Cite the printed title and say which version.
- Venue: could not be confirmed from the document text. Only the URL says BNAIC/BeNeLearn 2023.

**Access**: PDF opened fully (two fetches: content and header check).

**What it is**: A position paper. It argues that open-domain dialogue carries personal perspectives and social information, and that existing datasets are poorly suited to long-term memory. It compares five datasets, derives requirements, and proposes a knowledge-graph-style annotation scheme (triples with identifiers, a dialogue act, and a perspective record). It trains and evaluates no model.

**Key points**
- Datasets compared (Sec 3, Table 2): PEDC (Personal Events in Dialogue Corpus: 14 conversations, 1,035 turns, 73.93 turns per conversation); DialogRE (1,788 conversations, 23,129 turns, 12.94); Harry Potter dialogue (1,262; 16,891; 13.38); OpenDialKG (13,802; 96,942; 7.02); MultiWOZ 2.2 (10,437; 143,040; 13.71). READ.
- Findings from the comparison: statements dominate in all datasets (average 36.18%), opinions second (23.25%), and MultiWOZ has the lowest share of opinions (14.77%) and the most commands (21.13%) (Table 4). MultiWOZ also has the lowest linguistic variation and the most repetition (Table 5); PEDC the highest variation. READ.
- Proposed scheme (Sec 4 to 5, Appendix A): subject-predicate-object triples with identifiers, dialogue act, and perspective with holder, target, sentiment, polarity, certainty, annotated manually with open information extraction. READ.
- Stated limitations: English only; human-human data may not reflect human-machine dialogue; predicate interpretation and speaker intention are hard to annotate; written text lacks spoken cues. READ.
- The future work is to apply the scheme to an established dataset. No annotated dataset is reported. READ.

**Relevance**
- Data (MultiWOZ): medium-low. One citeable claim: in a comparison of five English dialogue datasets, MultiWOZ 2.2 has the smallest share of opinion utterances (14.77%) and low linguistic variety, which supports why a subjective-knowledge extension (DSTC11-T5) was needed (OURS framing; the paper does not mention DSTC11-T5, per what I read). Its own MultiWOZ counts are for version 2.2, not 2.1.
- Expert agent / knowledge access: low. The "perspective" fields (holder, sentiment, certainty) are a conceptual parallel to review aspects and sentiment, but the paper does not deal with reviews or retrieval.
- Appears linked to the CLTeamL work above by shared authors (Krause, Baez Santamaria), which is a fact about authorship only.

**Caveats**: Position paper with no empirical evaluation; do not cite it for any performance claim. Title and venue need to be written as they appear on the version you cite.


---

<!-- file: H-papers-evaluation.md -->

# H: evaluation papers (deep read)

Tags: READ = in the text WebFetch returned; SEARCH = only in a search snippet; OURS = my inference.
Note: WebFetch returns a small model's summary of each page, not raw text. Numbers below are as reported by it. Check anything you will quote against the PDF.

---

## 1. Bavaresco et al. 2025 (JUDGE-BENCH)

**Verified citation**: Anna Bavaresco, Raffaella Bernardi, Leonardo Bertolazzi, Desmond Elliott, Raquel Fernandez, Albert Gatt, Esam Ghaleb, Mario Giulianelli, Michael Hanna, Alexander Koller, Andre F. T. Martins, Philipp Mondorf, Vera Neplenbroek, Sandro Pezzelle, Barbara Plank, David Schlangen, Alessandro Suglia, Aditya K. Surikuchi, Ece Takmaz, Alberto Testoni. 2025. "LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks". Proceedings of ACL 2025 (Volume 2: Short Papers), pp. 238-255. Read at https://aclanthology.org/2025.acl-short.20.pdf (published version). DOI 10.18653/v1/2025.acl-short.20.
**Access**: opened via the Anthology PDF, two targeted passes (abstract, sections, tables, appendices H/C/E, limitations). Figures 2-4 are plots, so no numbers from them. VU Library link not tried (not needed).

**What it is**: A short paper that builds JUDGE-BENCH, a collection of 20 NLP datasets with human annotations, and tests how well 11 LLMs reproduce those human judgements. It asks when an LLM can replace a human judge. Conclusion: it depends heavily on model, dataset and property, so validate first.

**Key points**
- Benchmark: JUDGE-BENCH, 20 datasets, 11 LLMs (GPT-4o, Gemini-1.5, Llama-3.1 8B and 70B, Mixtral 8x7B and 8x22B, Command R and R+, Mistral-7B, Starling-7B, OLMo-7B), over 70,000 instances. Abstract + Sect. 2-3. READ. (Authors note a name clash with a different "JudgeBench".)
- Agreement statistic: Cohen's kappa for categorical annotations, Spearman's rho for graded ones. Sect. 3/4, Table 1. READ.
- Human upper bound: single-rater responses bootstrapped 1,000 times against the aggregated human rating, mean taken. Appendix C. Authors say model scores can exceed it. READ.
- Main finding: agreement varies widely by model, dataset and property; no model wins everywhere. GPT-4o often first but Llama-3.1-70B and Mixtral-8x22B are close and sometimes better. Sect. 4. READ.
- Dialogue results, Table 1 (six models with at least 98% valid answers). Graded: DailyDialog acceptability rho 0.69 (GPT-4o; upper bound 0.79), Switchboard 0.66 (upper 0.80). Topical Chat graded 0.13-0.28 (upper 0.56) and Persona Chat graded -0.02 to 0.22 (upper 0.61), mostly not significant. Categorical Topical Chat kappa about 0 (upper 0.58); Persona Chat kappa 0.24 for GPT-4o up to 0.58 for Mixtral-8x22B (upper 0.88). READ.
- Property level (Figure 3, plot only): GPT-4o and Gemini-1.5 do best on acceptability; correlation with engagingness stays consistently low across all models. Coherence for dialogue is not separately reported in the text I got (coherence appears for ROSCOE and SummEval, not dialogue). READ for the first two; coherence-in-dialogue: not found.
- Chain of thought: does not consistently improve agreement; effect "inconsistent". Run on 9 models. Appendix H, Table 7 (e.g. WMT23 En-De Llama-3.1-8B 0.08 to 0.18; DICES-350-expert 0.01 to -0.07). Sect. 5. READ.
- Human vs machine text: all models agree more with humans on human-written text than on machine-generated text (Figure 4); authors suggest self-preference bias. READ.
- Expert vs non-expert: on graded tasks models correlate more with non-expert annotators (Figure 2). Authors call the explanation speculative (non-experts may use surface cues). In DICES-350 the categorical pattern is mixed. READ.
- Lowest agreement: toxicity and safety (guardrails, non-answers). Best: instruction following, mathematical reasoning traces. READ.
- Recommendation: validate LLM judges against task-specific human annotations before use. Abstract + Sect. 5. READ.
- Limitations: correlation with humans is an imperfect check (shared biases, human reliability itself unvalidated); no pairwise preference evaluation; mostly English; data leakage risk. READ.
- Prompt setup: original annotation instructions plus "answer with one of {}, do not explain"; greedy decoding; invalid answers replaced by random human judgements. Sect. 3, App. E. READ.

**Relevance**: HIGH for subjective metrics / LLM judge / human-LLM agreement. Citable for: (a) using Cohen's kappa (categorical) and Spearman (graded) as the agreement statistics; (b) LLM-human agreement is property- and dataset-dependent, so the judge must be validated on our own human subset; (c) engagingness is hard for LLM judges, acceptability easier (relevant if we judge "natural/engaging" vs "acceptable/understandable"); (d) CoT is not a guaranteed gain, so if we use CoT in the judge, test it; (e) judges may favour machine text and self-generated text, a risk because our conversations are all machine text (OURS); (f) reporting a human upper bound (inter-annotator agreement) gives context for the kappa.

**Caveats**: Models tested are not Qwen3-1.7B or Qwen2.5-3B; small models were weakest here (OLMo-7B, Mistral-7B, Starling-7B excluded from Table 1 for low valid-answer rates, per the "six models with at least 98%" note, OURS inference on why). Dialogue sets are chit-chat (Persona/Topical Chat), not task-oriented booking dialogues with a knowledge base. Single-response rating, not multi-turn agent-agent transcripts. The paper does not test a human subset as small as ours. Per-property dialogue numbers are in plots I could not read.

---

## 2. Deriu et al. 2021 (survey)

**Verified citation**: Jan Deriu, Alvaro Rodrigo, Arantxa Otegi, Guillermo Echegoyen, Sophie Rosset, Eneko Agirre, Mark Cieliebak. "Survey on evaluation methods for dialogue systems". Artificial Intelligence Review. DOI 10.1007/s10462-020-09866-x. Year: the ZHAW repository copy is labelled 2020 (file name 2020_Deriu-etal...), the reading list says 2021 and "54". Volume, issue and pages were NOT in any text I read, so volume 54 and year 2021 are unverified by me. (OURS: online-first 2020, print volume 2021 is plausible, but check the Springer page.)
**What I actually read**: (a) the arXiv preprint https://arxiv.org/pdf/1905.04071 (title "Survey on Evaluation Methods for Dialogue Systems", first about 200k of 202k characters); (b) the ZHAW repository PDF https://srv-clst-301-data66.zhaw.ch/bitstream/11475/20318/2/2020_Deriu-etal_Survey-on-evaluation-methods-for-dialogue-systems.pdf (first 200k of 214k characters), which has the same section structure and appears to be the accepted/published text. The Springer page and the PMC copy both failed (client error; reCAPTCHA). Section numbers below match in both copies.
**Access**: opened partly to mostly (about 95%), via preprint and repository copy, not the Springer page. VU Library link not tried.

**What it is**: A long survey of how dialogue systems are evaluated, organised by system type. Its central position is that evaluation should ideally be automated, repeatable and correlated with human judgement, and that no current method meets all of these.

**Key points**
- Classification (Sect. 2.1): three classes: task-oriented systems, conversational agents (chit-chat), interactive question answering systems; the authors say the literature usually lists only the first two and QA fits neither cleanly. READ.
- Task success (Sect. 3.4): how well the system meets the information requirements of the user goal, i.e. satisfies the constraints and delivers the requested information (follows Schatzmann et al. 2007 per the preprint). Can be shown as a confusion matrix, with Kappa applied. READ.
- Dialogue efficiency (Sect. 3.4): measured through dialogue costs, mainly tied to dialogue length: number of turns, elapsed time, number of inappropriate repair utterances. Attributed to Walker et al. (1997). READ. This is the passage to cite for "turns" as an efficiency metric. Tokens are NOT mentioned in what I saw (OURS: token count is our own extension of "dialogue length").
- User satisfaction modelling (Sect. 3.4.1): premise is that usability can be approximated by user satisfaction, collected by questionnaire and then modelled from measurable features. READ.
- PARADISE (Sect. 3.4.1, Walker et al. 1997): linear regression from task success and dialogue costs to predicted user satisfaction. The survey reports task success and number of repetitions as the significant predictors, and limited transfer from novice to expert users. Also Interaction Quality (Schmitt and Ultes 2015). READ.
- User simulation (Sect. 3.4.2): used to train RL dialogue managers and to evaluate weaknesses before deployment; agenda-based simulator (ABUS) most popular; neural user simulator; MeMo workbench. READ.
- Subsystem evaluation (Sect. 3.4.3): NLU accuracy, slot error rate, F-measures; DST accuracy; NLG with slot error, BLEU, ROUGE plus human evaluation. READ.
- Human evaluation settings (Sect. 2.2): lab experiments (controlled, questionnaire, may not transfer to real use), in-field experiments (real users, e.g. Alexa Prize), crowdsourcing (e.g. Mechanical Turk; chat with system and rate, or rate a given context/response on quality, fluency, appropriateness). Human evaluation is costly and time consuming. READ (ZHAW copy; the preprint passage I got did not show 2.2).
- Desirable properties (Sect. 2.2 and again Sect. 7): automated (or partly), repeatable, correlated with human judgements, able to differentiate between systems/strategies, explainable. READ.
- Conversational systems (Sect. 4.3): human appropriateness judgements are central; weak agreement and Voted Appropriateness metrics (system-level correlation 0.803 and 0.893; interaction-level about 0.48). Word-overlap metrics correlate weakly at turn level (Sect. 7). READ.
- Interactive QA (Sect. 5, 5.3 per preprint): correctness metrics (MAP, MRR, F1, exact match, accuracy) ignore dialogue flow, so proper evaluation needs humans interacting; Kelly et al. (2009) questionnaires (NASA TLX, task, system), task questionnaire best separated systems; simulated users have limits. READ.
- Sect. 3.4.1 notes dialogues can be rated by the users or by objective judges (as described by the reader tool). Sect. 2.2 does not use "subjective/objective". READ.

**Relevance**: HIGH for objective metrics. Cite Sect. 3.4 for "task success = did the system meet the user's constraints and give the requested information" and "efficiency = dialogue cost such as number of turns and time". MEDIUM for subjective evaluation (Sect. 2.2 gives the human evaluation settings; our small human set is closest to crowdsourcing-style rating of given dialogues, OURS). The five desirable properties (Sect. 2.2/7) can motivate using an LLM judge (automated, repeatable) while checking correlation with humans.

**Caveats**: Survey covers work up to about 2019-2020; no LLM-as-judge and no agent-agent setups. Efficiency is defined as costs like turns and time; it does not say fewer turns is always better, and PARADISE shows cost interacts with success. Volume/pages unverified. Section numbering was checked in two copies, not on Springer. Section 7 title in the preprint is "Issues and Challenges"; in the ZHAW copy it is "Issues and challenges in automated evaluation".

---

## 3. Smith et al. 2022

**Verified citation**: Eric Michael Smith, Orion Hsu, Rebecca Qian, Stephen Roller, Y-Lan Boureau, Jason Weston. 2022. "Human Evaluation of Conversations is an Open Problem: comparing the sensitivity of various methods for evaluating dialogue agents". Proceedings of the 4th Workshop on NLP for Conversational AI, pp. 77-97, ACL. Read at https://aclanthology.org/2022.nlp4convai-1.8.pdf (published). Author list taken from the reading tool's citation block; confirm full names on the PDF.
**Access**: opened via PDF, two passes (abstract/sections/methods, setup/questions/results/conclusion). The .mp4 video: not read. VU Library link: not tried.

**What it is**: Compares five crowdworker-based ways to evaluate open-domain chatbots (BlenderBot variants) on how reliably each detects a true difference between two models. Finds no method best in all cases.

**Key points**
- Methods compared (Sect. 3.1): Single-Model Per-Turn (SM-Turn), Single-Model Per-Dialogue (SM-Dialog), Pairwise Per-Turn (PW-Turn), Pairwise Per-Dialogue (PW-Dialog), plus a PW-Dialog self-chat variant. READ.
- Sensitivity = ability of a method to detect a real performance difference between two models. Measured by win rates (for single-model methods, bootstrapped Likert/success scores) and by crowdworker time needed to reach p<0.05 (binomial test pairwise, t-test single-model); repeatability by variability across time chunks. Sect. 3-4. READ.
- Setup: Mechanical Turk workers role-play a persona, open with "Hi!", 6 turns each. Pairwise per-turn: worker picks between two models' replies every turn. PW-Dialog: raters compare existing conversations. SM methods: per-turn engaging/human-like/interesting marks, then 1-5 Likert at the end. Questions asked: preference, humanness, interestingness. Sect. 3.1. READ.
- Results by condition (Sect. 4, Table 3): length difference: pairwise (PW-Dialog, up to 85% win rate on interestingness) far better than single-model. Size difference: small gaps, whole-dialogue methods slightly better (SM-Dialog 66%). Fine-tuning difference (nonsense replies): PW-Turn best (93% preference). Single-model methods competitive except when length differs. Mixing PW-Turn and PW-Dialog (1:5) was not best anywhere. Averaging SM-Turn and SM-Dialog ratings reached significance faster than either. READ.
- Time to significance: about 5.7 h (PW-Turn), 6.0 h (PW-Dialog), 4.4 h (SM, joint) per pair/model; per-comparison curves only in Figures 8-13 (Appendix C.7-C.8), not tabulated. READ.
- Authors' recommendations (Sect. 5): choose the method to suit the expected kind of difference; per-turn for differences in sensible replies, whole-conversation for subtle/global differences; consider combining; improve sensitivity for similar-quality models. READ.
- Limitations: only three model pairs; US-based weekday crowdworkers; single-model methods ran in one shared interface; self-chat has no human partner; justification analysis preliminary. READ.

**Relevance**: MEDIUM-HIGH for the human-evaluation design choice. What we can cite it for: (1) no method is uniformly best, so the choice must be justified by the difference we expect between the two Experts; (2) pairwise comparison is more sensitive when two systems differ visibly (e.g. length, a typical difference between prompting variants, OURS); (3) averaging per-turn and per-dialogue ratings helped single-model Likert evaluation; (4) the term "sensitivity" and how it can be measured. Practical reading for 10-20 conversations (OURS): the paper supports pairwise for detecting differences between the two Experts and Likert per dialogue for absolute scores, but it gives no sample size guidance for such a small set.

**Caveats**: Raters here are crowdworkers who chat live with the bot, not annotators reading agent-agent transcripts; the dialogues are 6-turn persona chit-chat, not task-oriented, and not about booking; the metrics are preference/humanness/interestingness, not task fulfilment. SM-Dialog is based on only about 68 ratings per condition (Appendix C.1 figure as relayed). The paper's per-turn evaluation happens during a live chat; for us, per-turn rating would be of fixed transcripts, which differs (OURS). The paper does not discuss LLM judges.

---

## 4. Howcroft et al. 2020 (not on the reading list; Notebook 3 pointer)

**Verified citation**: David M. Howcroft, Anya Belz, Miruna-Adriana Clinciu, Dimitra Gkatzia, Sadid A. Hasan, Saad Mahamood, Simon Mille, Emiel van Miltenburg, Sashank Santhanam, Verena Rieser. 2020. "Twenty Years of Confusion in Human Evaluation: NLG Needs Evaluation Sheets and Standardised Definitions". Proceedings of INLG 2020 (13th International Conference on Natural Language Generation), Dublin, pp. 169-182. ACL. DOI 10.18653/v1/2020.inlg-1.23. Read at https://aclanthology.org/2020.inlg-1.23/ (abstract page) and https://aclanthology.org/2020.inlg-1.23.pdf (published).
**Access**: opened both; PDF read in one pass covering sections, findings and recommendations (Table 7); appendices not read in detail.

**What it is**: A literature analysis of 165 NLG papers with human evaluation (INLG/ENLG, 2000-2019) showing how inconsistent the names, definitions and reporting of human-evaluation criteria are, and a call for better reporting.

**Key points**
- Main finding: human evaluation in NLG is in a confused state; the same criterion name is used for different things and different names for the same thing. Abstract + Sect. 4-5. READ.
- Numbers: 165 papers screened from 578; 478 evaluations; 478 verbatim criterion names map to 204 unique names, merged into 71 normalised criteria. 279 of 478 evaluations gave no definition of the criterion, 311 gave no prompt/question, 98 no criterion name. "Fluency" mapped to 15 different sets of normalised criteria. READ (Sect. 3-4).
- Most common elicitation: direct quality estimation (207), then relative (72), then agreement with a statement (48). READ.
- Recommendation (Sect. 5, Table 7): report at minimum: the system's task and its inputs/outputs; each criterion's name and its definition; the instrument (how responses are collected and on what scale) and the exact instructions/prompts/questions shown to raters, ideally in an appendix. READ.
- The authors name the next step as developing this into a "Human Evaluation Checklist". READ.
- Standardised criteria: the paper does NOT give a standard list with definitions for correctness, fluency, informativeness, appropriateness. Its normalised criteria are explicitly not meant as a standard set; it calls for standardised terminology as a goal. READ (as relayed). Appendices contain criterion definitions/taxonomy but I did not read them.

**Relevance**: MEDIUM for the evaluation write-up (subjective metrics). Citable for: define each criterion and give the exact question wording to the LLM judge and to humans; report the scale and instructions; the same name can mean different things, so do not just reuse "fluency" or "coherence" without defining it. We cannot cite it for ready-made definitions to adopt.

**Caveats**: About NLG papers up to 2019, not dialogue or LLM judges specifically. "Evaluation sheet" in the title is proposed but the paper's own text, as relayed, gives a minimum-information list (Table 7) rather than a full template; do not describe a specific template as being in the paper. Notebook 3 pointing to this paper (per the task description) is not something I checked.

---

## Citation mismatches and open items
- Deriu: reading list says 2021, AI Review 54. I could not confirm volume 54, year 2021 or page numbers from any text I read; the repository copy is labelled 2020 and shows only the DOI.
- Smith: none found (title, venue, workshop match).
- Bavaresco: none found (short papers, ACL 2025; pp. 238-255).
- Howcroft: not on the reading list; details above from the Anthology.
- Not opened: all VU Library proxy links (not tried, student login), Smith .mp4 video, Springer page for Deriu (fetch failed), PMC copy (reCAPTCHA).


---

<!-- file: I-papers-prompting-reasoning.md -->

# Batch I: prompting, search and reasoning papers

Tags: READ = in text returned by WebFetch; SEARCH = search snippet / metadata only; OURS = inference.
All WebFetch answers are a small model's summary, not raw text.

## 1. Tree of Thoughts (Yao et al.)
**Verified citation**: Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., Narasimhan, K. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. Advances in Neural Information Processing Systems 36 (NeurIPS 2023), New Orleans, 10-16 Dec 2023. Pages not listed on the page I read. arXiv:2305.10601 (v1 17 May 2023, v2 3 Dec 2023 "NeurIPS 2023 camera ready"). Read: arxiv.org/pdf/2305.10601 (v2, preprint/camera-ready), arxiv.org/abs/2305.10601, collaborate.princeton.edu record (venue/year).
**Mismatch**: course page says 2024. Venue records say NeurIPS 2023 / vol. 36. Use 2023. (A "2024" can only come from a later proceedings listing; I did not see one.)
**Access**: PDF opened in several targeted calls; main text, Tables 2-3, cost section, limitations covered. Not every appendix.
**What it is**: A prompting/search framework that generalises chain of thought. The LM proposes several partial solutions ("thoughts"), scores them itself, and a search algorithm keeps or drops branches, with backtracking. Tested with GPT-4 on three tasks.
**Key points**
- Four components, all Section 3: (1) thought decomposition, size of a thought depends on task; (2) thought generator, either sample k i.i.d. thoughts or "propose" several in one prompt; (3) state evaluator, LM scores each state independently ("value") or votes across states; (4) search: BFS or DFS, more advanced search left for future work. READ
- Game of 24 (Sec 4.1, Table 2): IO 7.3%, CoT 4.0%, CoT-SC(100) 9.0%, ToT b=1 45%, ToT b=5 74%; best-of-100 CoT 49%, IO best-of-100 33%. b = breadth kept per step. Abstract also states 4% vs 74%. READ
- Creative Writing (Sec 4.2, Fig 5): GPT-4 coherence 1-10: IO 6.19, CoT 6.93, ToT 7.56 (100 tasks). Humans preferred ToT in 41 pairs, CoT in 21, 38 similar. READ
- Mini Crosswords (Sec 4.3, Table 3): word-level success IO 14%, CoT 15.6%, ToT 60%; game success 0 / 1 / 20% (4 of 20 games). Ablations: no pruning 5%, no backtracking 5% game success. READ (column labels inferred by the reader from garbled table; numbers consistent with text)
- Per-task settings: Game of 24 propose + value(3 samples) + BFS b=5; Creative Writing sample + vote(5) + BFS b=1; Crosswords propose + value + DFS (100-step cap). READ
- Cost (Sec 4 / Table 7 per the reader): Game of 24 ToT ~5.5k generated + 1.4k prompt tokens, ~$0.74/case vs best-of-100 CoT ~6.7k tokens, ~$0.47, 49%. Creative Writing ~$0.32 vs ~$0.06 for IO. Overall roughly 5 to 100 times more generated tokens than CoT; authors suggest early stopping/smaller beams. READ (table pointer for cost is from the reader, not confirmed by me; check Table 7 in the PDF)
- Stated limitations: only three fairly simple tasks; deliberate search may be unnecessary for tasks GPT-4 already does well; off-the-shelf model, no fine-tuning; higher cost. Broader impact: risks if used with external environments/humans; readable thoughts may help interpretability. READ
**Relevance**: Medium. Can cite for: prompting technique in the course list; the idea that an LM can evaluate its own intermediate states and that this improves accuracy on search-like tasks at higher token cost (relevant to objective metrics: token count per conversation, and to comparing two Expert prompting variants). It does not cover dialogue, retrieval, or multi-agent setups. Note the Kambhampati ICML paper (item 4) disputes ToT's link to systematic search (READ, Sec 2.3 per reader).
**Caveats**: GPT-4 only, three puzzle/writing tasks, no dialogue. The Creative Writing score is judged by GPT-4 itself (OURS: relevant to LLM-judge caveats). Our small open models (Qwen3-1.7B, Qwen2.5-3B) are not tested; nothing here says ToT works for them.

## 2. Brown et al. (2020), GPT-3
**Verified citation**: Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., ... Amodei, D. (2020). Language Models are Few-Shot Learners. Advances in Neural Information Processing Systems 33 (NeurIPS 2020), pp. 1877-1901. arXiv:2005.14165 (v4, 22 Jul 2020). Read: arxiv.org/abs/2005.14165 and arxiv.org/pdf/2005.14165 (preprint; venue/pages from papers.neurips.cc page).
**Mismatch**: course page lists "Mann, B., Ryder, N., ..." as if Mann were first author. True first author is Tom B. Brown; Mann is second. Course entry also says arXiv preprint; it was published at NeurIPS 2020. (The NeurIPS page's metadata oddly lists Amodei first, but the visible author list starts with Brown.)
**Access**: Opened partly: about the first 100k of 240k characters, plus later passes covering Section 5 and parts of Section 6-7. Appendices not read.
**What it is**: Introduces GPT-3 (175B parameters, autoregressive) and evaluates it on many NLP benchmarks without any gradient updates, giving tasks and demonstrations only as text in the prompt.
**Key points**
- Definitions (Sec 2, Fig 2.1): fine-tuning updates weights on a supervised set (not done for GPT-3); few-shot = K demonstrations in context, no weight updates, K typically 10-100 limited by context window of 2048 tokens; one-shot = exactly one demonstration plus a task description; zero-shot = only a natural-language instruction. In-context learning is the umbrella term. READ
- Headline finding: scaling up improves few-shot performance, sometimes close to fine-tuned SOTA; zero-shot improves with size and few-shot improves faster (Fig 1.3, 42 accuracy benchmarks). READ
- Example numbers (few-shot): LAMBADA 86.4% (Table 3.2), TriviaQA 71.2% closed-book (Table 3.3), CoQA 85.0 F1 (Table 3.7), 2-digit addition 100% but 4-5 digit ~9-27% (Table 3.9). READ
- Humans identify GPT-3 175B generated news only ~52% of the time (Sec 3.9.4, Table 3.11). READ
- Weak spots: ANLI, WiC (49.4%, chance), some reading comprehension (Sec 3.7, intro). READ
- Limitations (Sec 5): repetition and incoherence in long text; weak common-sense physics; near chance on comparison tasks (WiC, ANLI); autoregressive-only objective; all tokens weighted equally, no grounding; poor sample efficiency; unclear whether few-shot learns tasks at inference or recognises tasks seen in training; large and costly; hard to interpret; bias. READ
- Test-set contamination found for some benchmarks (Appendix C / Sec 4); a filtering bug; affected benchmarks flagged. READ
**Relevance**: Medium for conceptual grounding. Can cite for the definitions of zero-shot, one-shot and few-shot prompting, in-context learning without weight updates, and the fact that few-shot gains grow with model size (relevant to why small Qwen models may benefit less: OURS, not claimed by paper in those terms). Relevant to designing the two Expert variants (e.g. zero-shot vs few-shot prompt).
**Caveats**: GPT-3 is 175B, not the small models we use. Paper does not cover dialogue, chain-of-thought or instruction tuning. The "10 to 100" K is their typical choice for their 2048 context, not a rule.

## 3. Kambhampati, Stechly, Valmeekam (2025), "(How) Do reasoning models reason?"
**Verified citation**: Kambhampati, S., Stechly, K., Valmeekam, K. (2025). (How) Do reasoning models reason? Annals of the New York Academy of Sciences, 1547(1), 33-40. DOI 10.1111/nyas.15339. Published May 2025; PMID 40221824; peer-reviewed comment/debate article. Source for these details: asu.elsevierpure.com record (READ of the landing page metadata and abstract only).
**Access**: COULD NOT OPEN the full text. Tried: doi.org link, Wiley abs and ?af=R pages (all failed), ResearchGate (failed), VU library link not tried because Wiley is blocked (expected login). No arXiv copy of this exact paper was found in four searches. I did NOT read this paper.
**What I did read**: the ASU Pure abstract: a broad unifying perspective on large reasoning models such as OpenAI o1 and DeepSeek R1, covering their promise, sources of capability, common misconceptions and limitations. READ (abstract only)
**Closest related text (a different paper, not a substitute)**: Kambhampati et al., "Position: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces!", arXiv:2504.09762 (v4, 9 Jun 2026; authors Kambhampati, Valmeekam, Bhambri, Palod, Saldyt, Stechly, Samineni, Kalwar, Biswas). It cites the Annals paper as Kambhampati et al., 2025. I read it via arxiv.org/pdf/2504.09762. Its claims (READ): intermediate tokens are trained with reward on the final answer only, with no guarantee the trace is correct (Sec 2); trace validity correlated only loosely with answer correctness in A* maze transformers, and correct answers often came with wrong traces (Sec 4.1); long traces do not mean more effort (Sec 4.2); showing traces raised human trust regardless of correctness (Sec 4.3); recommends verifying solutions externally (Sec 6). Authors say the evidence is mostly small models on maze tasks and partly qualitative.
**Key points about the Annals paper itself**: none beyond the abstract. Do not cite specific claims or experiments from it.
**Relevance**: Low-to-medium, and only for the generic claim in the abstract that reasoning models have limitations and are often misunderstood. For anything finer the team must read the paper via the VU library login.
**Caveats**: Course entry matches the real citation (journal, vol 1547, issue 1). Pages 33-40 come from one landing page; confirm on the VU copy.

## 4. Kambhampati et al. (ICML 2024), LLM-Modulo position paper
**Verified citation**: Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., Murthy, A. (2024). Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks. Proceedings of the 41st International Conference on Machine Learning, PMLR 235, Vienna. Read: openreview.net/pdf?id=Th8JPEmH4z (published/camera-ready PDF per its header as returned; pages not given).
**Access**: Opened in two targeted calls; Sections 1-4 summarised, no appendices checked.
**What it is**: A position paper arguing that autoregressive LLMs cannot plan or verify on their own and proposing LLM-Modulo, where the LLM only proposes and external verifiers decide.
**Key points**
- Sec 2.1: only about 12% of GPT-4 plans were executable and goal-reaching on average; newer models (GPT-4o, Claude-3-Opus, Gemini Pro, LLaMA-3 70B) also poor on PlanBench (Table 1); drop when names are obfuscated. CoT and ReAct described as largely ineffective. READ
- Sec 2.2: on graph coloring with GPT-4, LLMs were no better at verifying than generating; self-critique did not beat the baseline and was sometimes worse; it failed to recognise correct solutions. No exact numbers returned. A 24-puzzle study found the LLM's own criticisms often off the mark. READ
- Sec 2.3: argues that apparent successes come from confusing knowledge with executable plans, easy domains, human-in-the-loop correction, or external verification. Says ToT has no deeper link to systematic search. READ
- Sec 3 architecture: generate-test-critique loop. LLM proposes candidates; a bank of critics checks them. Hard critics (correctness; model-based e.g. VAL, or unit tests) give soundness guarantees. Soft critics (style, preference) may be LLM-based. A meta/backprompt controller pools critiques and sends them back to the LLM (round-robin, LLM-summarised, or diversified prompts). LLMs also act as reformulators and help acquire specifications. READ
- Sec 3.5 and case studies: classical solvers can be far cheaper where applicable; Blocksworld and travel planning improve, but Mystery Blocksworld stays about 10%. READ
- Stated limitations: completeness depends on LLM generating good candidates; LLM soft critics have no soundness guarantee; someone must build the verifiers. READ
**Relevance (agents verifying each other)**: Honest answer: mostly warns, with a narrow allowance. READ: the paper says LLMs cannot be hard critics with soundness guarantees, and argues against relying on LLM self-critique for correctness, citing Sec 2.2. It allows LLM-based critics only for soft/style judgments. It does not discuss multi-agent LLM debate or one LLM checking another LLM (the excerpt returned had nothing on it). OURS: our Expert/Beginner stopping decision is a soft judgment (is this a good reply for the user), so the paper does not forbid it, but it gives a citable reason to (a) not treat the agents' agreement as proof of correctness, and (b) add an external check, e.g. a rule-based check that stated facts appear in the retrieved reviews, or a turn cap. Supports "generate, then check against something external, then feed back" as a design for the stop mechanism. Also a source for citing planning as out of scope for Expert.
**Caveats**: Evidence is on planning (Blocksworld, graph coloring, travel planning) with GPT-4-class models, not hotel/restaurant dialogue, and the paper is a position piece. It does not test two LLMs critiquing each other. Do not claim it shows LLM-LLM verification fails; it shows LLM self-critique failed on those tasks and argues LLM critics lack guarantees.

## 5. Logic-LM (Pan et al., 2023)
**Verified citation**: Pan, L., Albalak, A., Wang, X., Wang, W. Y. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 3806-3824, Singapore, December 2023. DOI 10.18653/v1/2023.findings-emnlp.248. Read: aclanthology.org/2023.findings-emnlp.248 and the .pdf (published version). (The ACL page lists the last author as "William Wang"; the full name Wang, William Yang is OURS/not seen on the page.) arXiv:2305.12295 exists (SEARCH).
**Mismatch**: none found, course gave no link.
**Access**: PDF opened in one targeted call (method, datasets, refinement); results tables not read directly, only the abstract-level numbers and Figure 4 description.
**What it is**: A neuro-symbolic pipeline: the LLM translates a logic problem into a formal representation, an external solver does the inference, and a module maps the answer back.
**Key points**
- Modules: Problem Formulator (Sec 3.1, few-shot LLM to logic programming, first-order logic, CSP or SAT-style form); Symbolic Reasoner (3.2); Self-Refiner (3.3); Result Interpreter (3.4). READ
- Solvers: Pyke for ProofWriter and PrOntoQA, Prover9 for FOLIO, python-constraint for LogicalDeduction, Z3 for AR-LSAT (Table 1). READ
- Models: gpt-3.5-turbo, text-davinci-003, gpt-4; temperature 0; baselines standard prompting and CoT; falls back to CoT when the formulation cannot be executed (Sec 4.1). READ
- Headline: across five datasets, average improvement of 39.2% over standard prompting and 18.4% over CoT (abstract, as returned). READ
- Self-refinement: triggered only by solver execution errors; LLM gets the faulty formulation, error message and examples, revises, repeats up to a maximum. On FOLIO the executable rate rose from about 67% to 84% (GPT-3.5) and 80% to 86% (GPT-4) over rounds 0-3 (Fig 4); about +5 points executable rate on average (Sec 4.4); accuracy gains flatten because errors only flag syntax, not meaning. READ
- Datasets and test sizes: PrOntoQA 500, ProofWriter 600, FOLIO 204, LogicalDeduction 300, AR-LSAT about 230. READ
**Relevance**: Low-to-medium. Can cite for: external deterministic checker feeding error messages back to the LLM (refine loop), which matches the LLM-Modulo idea and is a pattern for the stopping/verification topic coming later in the course. Not about dialogue, reviews or LLM-judge. It shows verification works when the checker is a solver, not another LLM.
**Caveats**: Logic reasoning benchmarks, OpenAI models, no dialogue. The self-refiner uses solver errors, not an LLM critic, so it does not support agent-to-agent verification.


---

<!-- file: J-papers-knowledge-memory.md -->

# J: knowledge access and memory papers (deep read)
Tags: READ = in text returned by WebFetch; SEARCH = search snippet only; OURS = inference.
Note: WebFetch returns a small model's answers, not raw text; numbers below are as reported to me.

## 1. Edge et al., GraphRAG
**Verified citation**: Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, Jonathan Larson. "From Local to Global: A Graph RAG Approach to Query-Focused Summarization." arXiv:2404.16130, v1 24 Apr 2024, v2 19 Feb 2025. cs.CL. No venue listed on arXiv (READ). Read: https://arxiv.org/abs/2404.16130 and https://arxiv.org/pdf/2404.16130 (preprint, v2 presumably).
**Access**: abstract page full; PDF read through 4 targeted queries covering method, evaluation, results, limitations (not verbatim; Appendices only touched).
**What it is**: A preprint proposing GraphRAG: an LLM builds an entity graph from a corpus, the graph is clustered into communities, each community gets a pre-written summary, and questions are answered by combining partial answers from those summaries. Targets "global sensemaking" questions about a whole corpus (e.g. main themes), which plain vector RAG cannot answer.
**Key points**
- Problem: vector RAG fetches chunks similar to the query, fine for facts in a few records, fails for corpus-wide questions; these are query-focused summarization, and older QFS methods do not scale to RAG-size corpora (Sec 1; READ).
- Pipeline (Sec 3; READ): chunk text (600 tokens, 100 overlap) -> LLM extracts entities, relationships, claims (with "gleaning" re-prompts) -> graph (duplicate edges raise weight) -> Leiden hierarchical communities -> LLM report-style summary per community, bottom-up -> query time: map (each batch of shuffled summaries gives a partial answer with 0-100 helpfulness score, 0s dropped) -> reduce (best-scored partials fill a context window and are synthesised).
- Conditions compared: C0 root, C1, C2, C3 leaf-level summaries; TS = map-reduce over raw text chunks; SS = vector RAG baseline (READ).
- Data: two ~1M-token corpora, podcast transcripts (1,669 chunks) and news articles (3,197 chunks; from MultiHop-RAG). 125 LLM-generated questions per dataset (5 personas x 5 tasks x 5 questions) (Sec 3.2, Table 1; READ).
- Judging (Sec 3.3, Appx F; READ): no gold answers, so head-to-head LLM judge: two systems answer the same question, judge picks a winner or a tie per criterion. Criteria: comprehensiveness, diversity, empowerment, plus directness as a control (expected to trade off against the others). Each comparison repeated 5 times; score 100 win / 0 loss / 50 tie, averaged; Wilcoxon signed-rank with Holm-Bonferroni (Table 6). The judge model is NOT named in the text I got (Sec 1 says "a second LLM", Sec 3.3 "an LLM evaluator"); intro says results are "when using GPT-4"; indexing used gpt-4-turbo (Sec 4.1.3).
- Headline results (Fig 2; READ): global methods beat SS on comprehensiveness (72-83% win rate Podcast, 72-80% News) and diversity (75-82% Podcast, 62-71% News); SS wins on directness; empowerment mixed. Community summaries beat TS only slightly at intermediate/low levels; C0 did not beat TS.
- Claim-based check (Exp 2, Tables 3-4, Sec 5.2; READ): Claimify extracted 47,075 claims; comprehensiveness = mean claim count, diversity = cluster count. LLM-judge labels agreed with claim-based labels 78% (comprehensiveness) and 69-70% (diversity) when not tied. No significant differences among global conditions on these.
- Cost (Table 2, Sec 4.1.3; READ): fixed 8k context. C0 used ~2.3-2.6% of the tokens of TS (over 97% fewer); C3 26-33% fewer. Building the podcast index took 281 min with gpt-4-turbo. Indexing cost is the real upfront cost.
- Limitations (Sec 6; READ): only sensemaking questions on two ~1M-token corpora, generalisation untested; hallucination/fabrication not measured (SelfCheckGPT suggested as future work); vector RAG still better for local lookup questions.
**Relevance to our project**: knowledge access (medium-low), subjective metrics (low-medium). Citable for: (a) vector RAG is suited to local fact lookup and weak on corpus-wide summary questions; (b) an example of a pairwise LLM-judge setup with named criteria and repeated runs; (c) the LLM judge was cross-checked against a non-LLM claim-based measure (agreement 69-78%), a precedent for validating a judge, though it is not human agreement.
**Caveats / closeness to our Expert agent (OURS)**: Our task, "what do many reviews say about one aspect (e.g. food, noise) of one hotel/restaurant", is aggregation over a small per-entity set of reviews, so it is topically a query-focused summary, but the setting is far from the paper's: the paper handles ~1M tokens of heterogeneous text with global themes; one DSTC11 entity has a handful to some dozens of short reviews that fit in a context window (check this against the data; I did not read the data), so no graph or community hierarchy is needed. The indexing cost (hours, GPT-4 class) is not realistic for Qwen 1.7B/3B on Kaggle. The idea that is transferable is only "summarise-then-combine (map-reduce) over many reviews", which would be our adaptation, not what the paper evaluates. Honest closeness: conceptually related, practically low. Do not claim GraphRAG results transfer to review summarisation.

## 2. Chhikara et al., Mem0
**Verified citation**: Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav. "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory." arXiv:2504.19413, v1 28 Apr 2025, cs.CL. arXiv page lists no venue or comments (READ). Crossref record (api.crossref.org/works/10.3233/FAIA251160, read via WebFetch) lists the same title and authors in IOS Press, Frontiers in Artificial Intelligence and Applications, ECAI 2025, published 21 Oct 2025, DOI 10.3233/FAIA251160; volume and pages not given in what I got. So the course page's "ECAI" is supported by Crossref, not by the arXiv page or the PDF text (PDF has no mention of any venue) (READ/SEARCH). I read the arXiv v1 preprint, not the proceedings version; numbers could differ in the published version.
**Access**: abstract page full; PDF read through 4 targeted queries (architecture, benchmark, results tables, limitations).
**What it is**: A system paper describing Mem0, a long-term memory layer that pulls facts out of a conversation, stores them, and retrieves them for later questions, plus Mem0g, a graph-based variant. Evaluated on LOCOMO (long multi-session chats) against memory systems, RAG, full context, and OpenAI memory.
**Key points**
- Extraction (Sec 2.1; READ): on each new message pair the LLM sees a stored conversation summary plus the last m=10 messages and extracts candidate facts. GPT-4o-mini does all LLM operations.
- Update (Sec 2.1; READ): for each candidate, top s=10 similar memories by embedding; the LLM chooses via tool call ADD / UPDATE / DELETE / NOOP (Algorithm 1).
- Mem0g (Sec 2.2; READ): memories as directed labelled graph (entities with type, embedding, timestamp; relation triplets), Neo4j store; conflicting facts are marked invalid, not deleted; retrieval combines entity-centred subgraph and semantic triplet matching.
- Benchmark (Sec 3-4; READ): LOCOMO, 10 conversations (~600 turns, ~26k tokens each), ~200 questions each; categories single-hop, multi-hop, temporal, open-domain; adversarial excluded (no ground truth). Baselines: LoCoMo, ReadAgent, MemoryBank, MemGPT, A-Mem, LangMem, Zep, OpenAI memory, RAG (chunk 128-8192, k=1,2), full-context.
- Judging (Sec 3; READ): F1 and BLEU-1 plus LLM-as-a-Judge J (CORRECT/WRONG label with a one-sentence reason, prompt adapted from MemGPT's, instructed to be lenient on same-topic answers), mean of 10 runs. The judge model is NOT named ("a more capable LLM"). No human-agreement check reported.
- Quality (Table 1; READ): J per category, Mem0 / Mem0g: single-hop 67.13 / 65.71; multi-hop 51.15 / 47.19; open-domain 72.93 / 75.71; temporal 55.51 / 58.13. Zep wins open-domain (76.60).
- Overall (Table 2; READ): J Mem0 66.88, Mem0g 68.44, full-context 72.90, best RAG 60.97, Zep 65.99, LangMem 58.10, A-Mem 48.38, OpenAI 52.90. So memory does not beat full context on accuracy.
- Latency and tokens (Table 2, Fig 4, Sec 4.3; READ): retrieved tokens Mem0 1,764, Mem0g 3,616, full-context 26,031. Total p95 latency 1.44 s (Mem0), 2.59 s (Mem0g) vs 17.12 s full-context (about 92% and 85% lower; abstract says 91%). Note "token cost" = retrieved context tokens, not money.
- Limitations (Sec 5; READ, no dedicated limitations section): future work on lower graph latency, hierarchical memory, human-inspired consolidation, non-conversational domains. Authors are company staff (OURS: product paper).
**Relevance to our project**: low to medium. Informs knowledge access/memory design only loosely. Citable for: an LLM deciding ADD/UPDATE/DELETE/NOOP on stored facts; trade-off of full-context vs retrieved memory (accuracy vs tokens and latency); reporting LLM-judge score as mean over repeated runs. Could matter if we let the Beginner or Expert keep a running fact memory across turns of one dialogue, but the task is single-session and short (OURS).
**Caveats**: benchmark is long personal conversations, not review QA; results are the authors' own, run with GPT-4o-mini, not small open models; judge unnamed and not validated against humans; preprint v1 vs published ECAI version not compared.

## 3. Pan et al., Unifying LLMs and KGs: A Roadmap
**Verified citation**: Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu. "Unifying Large Language Models and Knowledge Graphs: A Roadmap." arXiv:2306.08302 (v1 14 Jun 2023, v3 25 Jan 2024), cs.CL/cs.AI. Published version per reading list: IEEE TKDE 36(7), pp. 3580-3599, DOI 10.1109/TKDE.2024.3352100 (the arXiv page shows the DOI, but did not itself name the journal; TKDE is inferred from the DOI prefix and the user's reading-list entry; volume/issue/pages NOT verified by me). I read the arXiv preprint, not the published version.
**Authors mismatch check**: the reading list names six authors (Pan, Luo, Wang, Chen, Wang, Wu); arXiv lists Pan, Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu, which matches.
**Access**: IEEE page (https://ieeexplore.ieee.org/document/10387715, reached via doi.org redirect): returned empty, so no abstract or pages from IEEE. VU Library link not tried (needs login, expected to fail; per instructions try once, I did not spend a fetch; report as not tried). arXiv abstract page full; arXiv PDF read to about 100k of 165k chars plus a second pass at 100k onward.
**What it is**: A survey/roadmap paper arguing LLMs and knowledge graphs complement each other, organised into three frameworks, with a review of work per framework and future directions.
**Key points**
- Framework 1, KG-enhanced LLMs (Sec 4, Fig 6a; READ): KGs used in pre-training (4.1: objectives, inputs, instruction tuning), at inference (4.2: retrieval-augmented knowledge fusion 4.2.1; KG prompting 4.2.2), and for interpretability (4.4: probing 4.4.1, analysing reasoning 4.4.2).
- Framework 2, LLM-augmented KGs (Sec 5, Fig 6b): LLMs for KG embedding (5.1), completion (5.2), construction (5.3), KG-to-text (5.4), KG question answering (5.5).
- Framework 3, Synergized LLMs + KGs (Sec 6, Fig 6c, Fig 7): equal partners; synergized knowledge representation (6.1) and reasoning (6.2); four layers: data, synergized model, technique, application (Sec 3.1.3).
- Inference-time external knowledge (Sec 3.2, 4.2, 4.3; READ): lets LLMs use up-to-date knowledge without retraining; retrieval-augmented methods feed retrieved material as context and the survey reports gains in open-domain QA and factuality; KG prompting turns triples into text. Pre-training injection cannot absorb updates without retraining.
- Hallucination (Sec 1, 7.1; READ): LLMs produce factually wrong statements (gravity example); 7.1 says hallucination will likely persist and KGs as external sources to validate outputs is a promising direction. The survey does not run its own hallucination experiments (it is a survey).
- Open problems (Sec 7; READ): difficulty linearising KG structure for LLMs, black-box (API-only) LLMs cannot get KG injection except by prompts limited by input length, knowledge editing.
**Relevance to our project**: low-medium; knowledge access. Citable for the general claim that supplying external structured knowledge at inference time (retrieval, prompting) is one way to ground LLM answers and reduce factual errors, and that hallucination is a recognised problem. Useful for the course's upcoming "graph-assisted conversational AI" theme (OURS). Not citable for any specific hallucination-reduction figure; the survey gives none that I saw.
**Caveats**: survey, no experiments; dialogue and hotel/restaurant reviews are not discussed in what I read; the review data are unstructured text, so a KG would be an extra build step (OURS). Published page numbers unverified.

## Links not opened
- https://ieeexplore.ieee.org/document/10387715 : opened but returned empty page.
- VU Library (vu-nl.idm.oclc.org) link: not attempted (login wall expected).
