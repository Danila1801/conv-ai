# Extra Q&A: questions the study guide does not cover

Added 11 Nov 2026. The study guide already has the 12 basic questions. These are the ones a TA asks on L6 day (post-training and alignment), or the ones that link back to our own coursework. Lines marked **our view** are not in the paper. Say so out loud when you use them.

| Question | Short answer | Who |
|---|---|---|
| Today's lecture covers DPO. Does the argument still hold without RLHF? | The paper only talks about RLHF. **Our view:** the critique is about whose preferences go into the data, not the optimiser. DPO learns from the same kind of preference pairs, so "aligned to whom" applies just the same. | P2 |
| Isn't mode collapse just a low temperature setting? | No. Temperature reshapes sampling from a fixed distribution. Mode collapse changes the distribution itself after alignment, so a higher temperature makes answers noisier but they stay narrowed toward the labellers' taste. | P2 |
| Why must the VAA use RAG? | So every claim can be traced to a trusted source. **Our view:** we saw the failure mode in Notebook 1. Qwen3 never got the hotel reviews and answered confidently anyway, saying "comfortable beds" when most reviews were negative. A voter chatbot answering from priors would do the same with party positions. | P2 |
| Can a small LoRA adapter really carry a community's identity? | It works well for style and persona with little data, which is why it is cheap enough for communities. The paper aims for a "respectful likeness, not a perfect copy" and admits rigid identity categories and intersectionality stay hard. | P2 |
| Doesn't decentralised alignment let anyone fine-tune away the safety guardrails? | The authors reject naive relativism, so studios keep moderating. **Our view:** keep a shared safety layer in the base model and put community adapters on top. Communities control the representation, not whether harm is allowed. | P3 |
| Is there a real VAA we know? | Yes, the Netherlands has StemWijzer and Kieskompas. **Our view:** that is the obvious pilot. Use the party programmes as the curated source and measure how much of each party's position a chatbot answer covers. That is exactly the evaluation the authors leave for future work. | P3 |
| Who pays for all this participation? | The paper suggests public money, universities and the funders of current VAAs (agencies, media, non-profits), plus Chatbot Arena-style feedback tools. It admits that organisation and funding are still open. | P3 |
| If RLHF centralises power, why not just use a base model? | Base models are unpredictable and often harmful, which is why alignment made LLMs usable as assistants in the first place. The paper does not reject alignment. It asks who does it and for which context. | P1 |
| What would you change in the paper? | **Our view:** add one small empirical pilot, such as the StemWijzer-style coverage test above, so at least one claim gets measured instead of only argued. | P3 |

## From the Kimi K3.1 Pro grill (11 Nov 2026, checked against the paper)

Full output: `kimi_grill.md`. These six were the strongest. The rest overlap with the questions above.

| Question | Short answer | Who |
|---|---|---|
| Does consistent output mean accurate or impartial output? | No. RAG grounds the facts, and RLHF is proposed only for consistent presentation. The paper itself says it needs iterative investigation of consistency *and* accuracy. A model can be consistently biased. | P3 |
| Why RLHF at all, if RAG, templates or SFT could give consistency more cheaply? | The paper compares no implementations. It infers RLHF from the generalisation vs diversity trade-off and leaves testing open. **Our view:** constrained RAG or SFT should be the baseline, and RLHF is only worth it if it adds robust guardrails on top. | P2 |
| Who decides which views are "reasonable" for Overton pluralism? Isn't that centralisation again? | The paper gives curation to democratic institutions, trusted third parties or a consortium of parties, with citizens and independent monitors. **Our view:** that moves the gatekeeping rather than removing it, and the paper gives no criteria for excluding a view. | P3 |
| The VAA uses centralised, consensus-seeking participation. How is that different from the consultative participation the paper criticises? | In prior work, companies kept the final say. The VAA gives parties, citizens and monitors real agency in creation and alignment. **Our view:** voting, veto and appeal rights are not specified, so the difference is underdeveloped. | P1 |
| If the base model stays developer-controlled, how much power do LoRA communities actually gain? | Control over one layer, their own adapter, not the whole stack. The paper itself lists "how much power stays with the developers" as future work. | P3 |
| What does "revoke the licence" mean once a studio has downloaded the adapter? | The paper gives the right but no mechanism. **Our view:** it only works if the adapter is served from the community's side, plus contracts with audit and takedown duties. A downloaded copy can't be recalled. | P3 |

Fixed in the speaker cards after the grill: "secret sauce" was OpenAI's own phrase, not the authors' (slide 2). "Only a few companies can train models" was too absolute (slide 3). NPC bias "risks being amplified" rather than "gets amplified" (slide 9). LoRA is cheaper, but communities still lack resources (slide 10). Mode collapse "may" give consistency (slide 11).

Rejected from the grill: Kimi thought slide 13 was wrong to link Friday's lecture to evaluation. It is not wrong: Filip's 10 Nov announcement moved Evaluation (Notebook 3) to Friday 13 Nov. Kimi also said mode collapse was undefined on slide 2, but the slide 2 script does define it.

## One-liners to fall back on
- "It's a position paper. The contribution is the framework, and testing it is their stated future work."
- "The paper doesn't address that directly, but our view is ..."
- "Same technique, different verdict: that's the whole point of context."
