<!-- Kimi K3.1 Pro, {'completion_tokens': 8243, 'prompt_tokens': 24825, 'total_tokens': 33068, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 6503, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 64, 'created_cache_tokens': 24704, 'multimodal_tokens': None}} -->

## 1. FACT CHECK

- **Slide 2 notes: "The authors call it the 'secret sauce'."** The paper says **"Self-reportedly"**, citing Ouyang et al. and Heaven. It is reported as OpenAI's self-description, not simply the authors' characterisation. **Section: Introduction.**

- **Slide 3 notes: "Only a few well-resourced companies can train and align these models."** Too absolute. The paper says training **powerful** LLMs is typically accessible only to actors with substantial resources, but also says open-weight models partly enable tailoring by communities. **Sections: LLM Alignment and Power Centralisation; Context.**

- **Slide 9 notes: "stereotypes and erasure ... get amplified by already biased models."** The paper does not demonstrate amplification. It says biased games and biased LLMs already exist, and combining them **risks** even more damaging portrayals. **Section: LLM-Powered Non-Playable Characters, Power Centralisation.**

- **Slide 10 notes: LoRA is "cheap enough for communities."** LoRA significantly reduces training and storage requirements, but the paper explicitly says not all communities have the necessary resources, time or expertise, and that substantial infrastructure investment is needed. **Sections: Diverse NPCs; Community-led NPCs.**

- **Slide 11 notes: "every voter gets consistent answers."** This states a guarantee. The paper says mode collapse **may be desirable** for enforcing consistency and requires iterative investigation into whether RLHF can provide sufficient guarantees of consistency and accuracy. **Section: Consistent VAA.**

## 2. TEN HARD QUESTIONS

### 1. What exactly would annotators prefer during RLHF for the VAA, and why would that reward impartiality rather than fluency or persuasiveness?
**Why hard:** It exposes the missing link between the normative goal and an actual post-training objective.  
**Answer:** The paper does not specify preference labels or a reward model. It says alignment should shape retrieved information to promote dialogue and critical thinking while maintaining consistency. **Our view:** the rubric would need source fidelity, balanced coverage and non-persuasion, with separate testing for reward hacking. **Sections: VAA Alignment Mitigation; Consistent VAA.**  
**Owner: P2**

### 2. Does consistent output imply accurate or impartial output?
**Why hard:** The VAA recommendation can sound as though consistency solves reliability.  
**Answer:** No. RAG supplies source grounding, while RLHF is proposed for consistent presentation; the paper still calls for iterative investigation of consistency and accuracy. A model could consistently reproduce the same biased framing, so consistency is only one requirement. **Section: Consistent VAA.**  
**Owner: P3**

### 3. Why use RLHF at all when RAG, templates, constrained decoding or SFT might provide consistency more cheaply?
**Why hard:** It asks for the missing baseline against which RLHF should be justified.  
**Answer:** The paper infers RLHF's suitability from the reported generalisation-diversity trade-off, but compares no implementations and explicitly leaves testing open. **Our view:** constrained RAG or SFT should be the baseline, and RLHF is justified only if it adds robust presentation guardrails across users and contexts. **Section: Consistent VAA.**  
**Owner: P2**

### 4. Who decides which views count as "reasonable" in Overton pluralism, and why is that not another form of centralisation?
**Why hard:** Overton pluralism still requires gatekeeping before pluralistic generation begins.  
**Answer:** The paper assigns curation to democratic institutions, trusted third parties or a consortium of parties, with participation from parties, citizens and independent monitors. **Our view:** this redistributes gatekeeping rather than eliminating it, and the paper gives no clear legitimacy criteria for excluding a view. **Sections: Overton Pluralistic VAA; Centrally Designed VAAs.**  
**Owner: P3**

### 5. The VAA uses centralised, consensus-seeking participation. How is that different from the consultative participation the paper criticises?
**Why hard:** It reveals a possible tension between the critique of prior work and the VAA proposal.  
**Answer:** In prior work, participants supplied input while companies retained control of the final model. The VAA proposal requires meaningful agency for parties, citizens and independent monitors during creation and alignment, although not full ownership. **Our view:** voting, veto and appeal rights remain unspecified, so the practical difference is underdeveloped. **Sections: Previous Work, Participation; Centrally Designed VAAs.**  
**Owner: P1**

### 6. If the base model and tokenizer remain developer-controlled, how much power do LoRA communities actually gain?
**Why hard:** A swappable adapter does not decentralise the whole technical stack.  
**Answer:** Open weights partly enable tailoring, and communities control their licensed representation matrix. However, the paper requires testing whether LoRA compensates for base-model bias and lists residual developer power as something future work must measure. It therefore decentralises one control layer, not the entire model stack. **Sections: Context; Diverse NPCs; Conclusion.**  
**Owner: P3**

### 7. Does sharing a LoRA matrix instead of raw data guarantee privacy or data sovereignty?
**Why hard:** The presentation may implicitly treat parameter sharing as automatically safe.  
**Answer:** The paper presents matrix sharing as a mechanism for reciprocity and refusal, but provides no privacy analysis. **Our view:** there is no guarantee, because trained parameters can leak information; communities still need data governance, privacy testing and licence enforcement. **Section: Community-led NPCs.**  
**Owner: P2**

### 8. What does revocation mean technically after a game studio has downloaded the adapter?
**Why hard:** A legal right to revoke does not automatically remove deployed copies.  
**Answer:** The paper says communities can rescind representation rights and revoke licences when a storyline is disrespectful, but specifies no enforcement mechanism. **Our view:** credible revocation requires server-side adapter loading, versioned deployments and contractual audit or takedown obligations; downloaded copies cannot simply be recalled. **Sections: NPC Alignment Mitigation; Community-led NPCs.**  
**Owner: P3**

### 9. If combining "elderly" and "working-class" LoRAs is inadequate, how does intersectional representation scale?
**Why hard:** Direct participation for every intersection creates a combinatorial and resource problem.  
**Answer:** The paper warns that arithmetic composition may not produce respectful intersectional representations and says intersectional communities must participate directly. It proposes accessible feedback infrastructure, but does not solve adapter proliferation, participation cost or coverage of sparsely represented groups. **Section: Steerable Pluralistic NPCs.**  
**Owner: P2**

### 10. The paper claims inclusion mediated by powerful institutions cannot dislodge their power. What evidence supports such a strong universal claim?
**Why hard:** It challenges a central premise rather than an implementation detail.  
**Answer:** The paper supports the claim through initiatives where firms retained final control, especially Anthropic adopting only one publicly voted principle, while acknowledging PRISM's empirical value. **Our view:** these cases show the limits of the studied initiatives, not that inclusion can never shift power; the universal claim remains a theoretical position. **Section: The Limits of Inclusion.**  
**Owner: P1**

## 3. THREE WEAK SPOTS

- **Structure:** The main comparative result arrives around **6:10**, while slides 5 and 7 repeat the three principles. **Fix:** preview Table 1 on slide 6, explain the cases through that table, and cut slide 7.
- **Timing:** The script totals about **9:05** before realistic transitions or hesitation. **Fix:** reduce slide 4 to three studies, drop distributional pluralism from slide 8, and rehearse to **8:15**.
- **Jargon and lecture framing:** "Mode collapse" appears on slide 2 but is explained only on slide 8, and slide 13 incorrectly calls L6 "evaluation." **Fix:** define it inline as "a narrower output distribution" and retitle slide 13 **"Link to L6: choosing post-training methods by context."**
