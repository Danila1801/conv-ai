"""Ask Kimi K3.1 Pro (Nebius) to review the Group 7 deck like a strict TA.
Needs NEBIUS_API_KEY in the environment (never commit it).
Run from the repo root: python presentation/tools/kimi_grill.py > presentation/qa/kimi_grill.md"""
import json
import os
import sys
import urllib.request
from pathlib import Path

import pymupdf as fitz

URL = "https://api.tokenfactory.nebius.com/v1/chat/completions"
ROOT = Path(__file__).resolve().parents[2]
key = os.environ.get("NEBIUS_API_KEY") or sys.exit("set NEBIUS_API_KEY first")

paper = "".join(p.get_text() for p in fitz.open(ROOT / "course/papers/peter-devlin-2025-decentralising-llm-alignment.pdf"))
deck = "".join(f"--- PAGE {i + 1} ---\n{p.get_text()}\n" for i, p in enumerate(fitz.open(ROOT / "presentation/deck/Group7-v3.pdf")))
scripts = json.loads((ROOT / "presentation/deck/scripts.json").read_text(encoding="utf-8"))
notes = "\n".join(f"Slide {k} ({v[0]}): {v[2]}" for k, v in scripts.items())
qa = (ROOT / "presentation/qa/extra_qa.md").read_text(encoding="utf-8")

prompt = f"""You are a strict TA for the VU course Conversational AI. Group 7 (3 bachelor students, non-native English) presents
Peter & Devlin (AIES 2025) for 10 min + 5 min Q&A. Below: the paper, the slides, the speaker scripts and the prepared Q&A.
Be short. Use only keyboard characters (write -> for arrows, plain hyphens).
1. FACT CHECK: any slide or script claim the paper or the cited source does not support (slide number, exact phrase, what is true).
2. 10 HARD QUESTIONS not covered by the prepared Q&A, each with a 2-3 sentence answer and which presenter takes it (P1 slides 1-3, P2 4-6, P3 7-9).
3. THREE WEAK SPOTS in the talk with a one-line fix each.

=== PAPER ===
{paper}

=== SLIDES ===
{deck}

=== SCRIPTS ===
{notes}

=== PREPARED Q&A ===
{qa}
"""
body = {"model": "moonshotai/Kimi-K3.1-Pro", "temperature": 0.3, "max_tokens": 32000, "reasoning_effort": "low",
        "messages": [{"role": "user", "content": prompt}]}
req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                             headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
r = json.load(urllib.request.urlopen(req, timeout=900))
print(r["choices"][0]["message"].get("content") or "(no answer)")
