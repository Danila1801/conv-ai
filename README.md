# Conversational AI (VU, XB_0119), Group 7

Everything for the course in one place: our paper presentation, the notebooks, the lectures and the final project.
Group: Antonia Bulai, Danila Popusoi, Goktug Yildirim.

## What's coming up

| When | What | Where |
|---|---|---|
| Fri 13 Nov 2026, 11:00 | **Our paper presentation** (10 min + 5 min Q&A) | HG-10A33 |
| Wed 18 Nov, 25 Nov, 2 Dec | Quizzes 3, 4, 5 (best 4 of 5 count) | in class |
| Fri 20 Nov 2026 | Midterm progress form | Canvas |
| **Wed 9 Dec 2026, 23:59** | **Final project notebook** (Canvas says 18 Dec, Filip still has to confirm) | Canvas |
| 10-11 Dec 2026 | Oral defence of the project | |
| Mon 14 Dec 2026, 15:30 | Exam | |

## The presentation (start here)

Paper: Peter & Devlin (2025), *Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation*, AIES.
PDF in `course/papers/`.

| File | What it is |
|---|---|
| `presentation/deck/Group7-v4.pdf` | **The deck we present.** 12 slides + backup (v4, 12 Nov 2026, after Antonia's review) |
| `presentation/deck/Group7-v4.pptx` | Same deck, editable. Your script is in the speaker notes |
| `presentation/deck/Group7-v4-speaker-cards.pdf` | Script per presenter, print it or keep it on your phone |
| `presentation/qa/extra_qa.md` | Hard questions with answers, and who answers them |
| `presentation/qa/group7-study-guide.pdf` | Paper explained, glossary, basic Q&A |
| `presentation/qa/kimi_grill.md` | A second AI model reviewed the deck like a strict TA |

**Who presents what:** P1 = slides 1-5 (why RLHF exists, its cost, the paper's claim), P2 = slides 6-8 (context, the workers, the table of earlier fixes), P3 = slides 9-12 (the two cases, pluralism, result, our view). Decide between us who is P1, P2 and P3.

**Before Friday:** read your part out loud twice, then say it in your own words. Do one timed run on Thursday evening. Current planned narration: 8:40 (727 words, slow pace). Keep the full run under 9:30.

### Changing the deck

The slide text lives in `presentation/deck/build_deck.py`, so the deck and the speaker cards stay in sync. To rebuild (Windows with PowerPoint):

```
cd presentation/deck
pip install python-pptx matplotlib pymupdf
python charts.py
python build_deck.py
powershell -ExecutionPolicy Bypass -File export_pdf.ps1
python build_cards.py
python ../tools/keyboard_check.py Group7-v4.pptx Group7-v4.pdf
```

Small edits straight in the .pptx are fine too. Just tell the group in the chat.

**House rules for slides:** a claim as the title, real numbers with a source line, a chart or diagram on every slide, a cool green palette, and only characters you can type on a keyboard (write `->`, not arrow symbols). `keyboard_check.py` has to print `OK`.

## Folders

```
presentation/   deck (current), qa, tools, archive (v1, v2, v3)
course/         lectures, papers, Canvas notes
notebooks/      weekly notebooks (a1 has a filled version)
project/        final project (tutorial-style notebook, due 9 Dec)
```

## Working together

- Pull before you start: `git pull`
- Commit small: `git add -A`, `git commit -m "what you changed"`, `git push`
- Never commit API keys or `.env` files
- Big binary files (videos, model weights) do not go in here
