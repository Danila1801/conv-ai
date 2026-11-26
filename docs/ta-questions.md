# Questions for the TAs

Office hours: Fri 27 Nov and Fri 4 Dec, 13:00 to 14:00, NU-2B17. Canvas Discussions also works (answers within 24 hours for questions posted Monday to Wednesday).

Write the answer and the date under each question. If we get no answer, we go with the default.

1. **The Expert and the reviews.** The assignment says the Expert "should be aware of the knowledge base with reviews". May we give the Expert the review sentences that the dataset marks as relevant for a dialogue (the `knowledge` field in `labels.json`), or should the Expert find the relevant reviews itself, for example with retrieval?
   - Default if no answer: the Expert gets the reviews of the hotel or restaurant in question and has to find the relevant ones itself. That is fine under both readings.
   - Answer:

2. **Models.** Is it fine to use the two models from the notebooks (Qwen3-1.7B and Qwen2.5-3B), for example one for the agents and the other one as the judge? Are other open models allowed?
   - Default if no answer: only the two notebook models.
   - Answer:

3. **50 conversations.** With two Expert versions, do we need 50 conversations in total, or 50 per version?
   - Default if no answer: at least 50 dialogues, each run with both versions.
   - Answer:

4. **Running the notebook.** Will you run our notebook, or read it with the saved outputs? If you run it, is it fine if a switch at the top loads our saved conversations so the run takes minutes and not hours?
   - Default if no answer: it runs top to bottom on Kaggle, and we hand it in with the outputs saved.
   - Answer:

5. **Human evaluation.** Is it enough if the three of us rate about 15 to 20 conversations each?
   - Default if no answer: yes, three raters, same sample.
   - Answer:

6. **Rubric.** Is there a rubric that shows how the points are divided over the parts of the notebook?
   - Answer:

7. **Fine-tuning.** If one Expert version is fine-tuned, may we reuse the adapter from Notebook 2, or must we train a new one?
   - Only ask this if we decide on a fine-tuned Expert.
   - Answer:
