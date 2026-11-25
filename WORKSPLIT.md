# Work split

This is a proposal from 25 Nov. If something does not fit, change it here and say so in `coordination/STATUS.md`.

## How we split

- Everyone owns one clear part of the notebook, so in the oral defence each of us can explain our own part without help.
- Goktug and Dan have paid Claude plans. Antonia has the free plan, which is fine for questions but not for long working sessions. So her parts are the ones where a person is needed anyway: the human evaluation, checking the references, and the text that frames the project.
- All three of us rate conversations for the human evaluation. That part cannot be given to one person.
- All three of us read the whole notebook before we hand in.
- Each notebook section is its own file while we work, so two people never edit the same file. One script joins them into the single .ipynb at the end.

## Who owns what

| Part | Owner | What it covers |
| --- | --- | --- |
| Agents and conversations | Goktug | The Beginner, the two Expert versions, how they talk, how a conversation stops, saving the conversations |
| Data and automatic evaluation | Dan | Loading the data, picking the dialogues, the counted metrics, the LLM judge, the plots |
| Human evaluation, references and framing | Antonia | Rating guide, organising our ratings, agreement with the judge, checking every reference, introduction and conclusions |

## Work packages

| # | Work package | Owner | Helps or reviews | Done when | Due |
| --- | --- | --- | --- | --- | --- |
| A | Design decisions written down (`DESIGN.md`) | Goktug | all read it | Every choice has a reason and a link to course material. All three agree | Fri 27 Nov |
| B | Questions to the TAs (`docs/ta-questions.md`) | Antonia | whoever is on campus | Asked at the office hour or on Canvas Discussions. Answers written into the file | Fri 27 Nov |
| C | Data loading and choice of dialogues | Dan | Goktug | At least 50 dialogues from the test split, saved as a fixed list with ids | Sun 29 Nov |
| D | Beginner and two Expert versions | Goktug | Dan | Prompts and settings written and explained. A 5-conversation pilot runs | Sun 29 Nov |
| E | Conversation loop, stopping rule, saving to JSON | Goktug | Dan | Every conversation ends by itself or at the cap. The final reply is cut out by code | Mon 30 Nov |
| F | Counted metrics and plots | Dan | Antonia | Turns, tokens and stop reason per conversation, with one table and one figure | Tue 1 Dec |
| G | LLM judge | Dan | Antonia | Criteria defined in words. Judge gives a score per criterion and "request fulfilled yes or no" for every conversation | Wed 2 Dec |
| H | Full run | Goktug | Dan | All dialogues run with both Experts. Results saved in the repo | Wed 2 Dec |
| I | Rating guide and rating sheet | Antonia | Dan | One page that says what each score means, with two examples. A sheet we can fill in without seeing which Expert it was | Wed 2 Dec |
| J | Human ratings | all three | | Each of us has rated the same sample (about 15 to 20 conversations, about an hour) | Fri 4 Dec |
| K | Agreement between us and with the judge | Antonia | Dan (code) | Numbers and a short text on where we agree and where not | Sat 5 Dec |
| L | Text: introduction and setup | Antonia | Goktug | Written, fits the notebook structure from the assignment | Sat 5 Dec |
| M | Text: methodology | Goktug | Antonia | Each agent described with its reason and parameter values | Sat 5 Dec |
| N | Text: experimental setup and results | Dan | Antonia | Data, stopping, metrics described. Results with figures and tables | Sun 6 Dec |
| O | Text: conclusions (findings, lessons, future work) | Antonia drafts | all | Three paragraphs, as the assignment asks | Sun 6 Dec |
| P | Reference check | Antonia | | Every cited source opened. Authors, year, venue and the claim checked against the source | Mon 7 Dec |
| Q | Final run on Kaggle, top to bottom | Goktug | Dan | "Save & Run All" finishes without errors. Outputs are saved in the file | Mon 7 Dec |
| R | Division of labour paragraph and AI-use statement | all three | | Written together, true to what happened | Mon 7 Dec |
| S | Final read and hand-in | all three | | Each of us has read everything. Uploaded on Canvas | Tue 8 Dec |
| T | Defence practice | all three | | Each of us can answer the questions about our own part, and the basics of the other parts | Wed 9 Dec |

## Timeline

| When | What happens |
| --- | --- |
| Wed 25 and Thu 26 Nov | Repo set up. Design draft. Pilot with 5 conversations |
| Fri 27 Nov | TA office hour, 13:00, NU-2B17. Design fixed |
| Sat 28 to Mon 30 Nov | Build: data (C), agents (D), loop (E). Antonia starts the rating guide and the introduction |
| Tue 1 and Wed 2 Dec | Metrics (F), judge (G), full run (H) |
| Thu 3 and Fri 4 Dec | We rate (J). Second TA office hour on Friday |
| Sat 5 and Sun 6 Dec | Agreement (K), all text (L to O) |
| Mon 7 Dec | Reference check (P), final run (Q), division of labour (R) |
| Tue 8 Dec | Final read, hand in (S) |
| Wed 9 Dec | Spare day. Deadline 23:59. Defence practice (T) |
| Thu 10 or Fri 11 Dec | Oral defence |

## Working in the repo

- One branch per work package, for example `wp-d-agents`. Open a pull request into `main`. One other person looks at it before it is merged.
- Commit messages say what changed in a normal sentence, with the work package letter in front, for example `D: Beginner prompt quotes the dialogue history`.
- If you stop working, write where you are in `coordination/STATUS.md`. The next person (or their Claude) reads that first.
- Do not commit the dataset, model files or any password or token.
