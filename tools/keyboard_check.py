"""Fail if a deck/PDF/text file contains any character Danil can't type on a normal keyboard.
Allowed: printable ASCII plus newline/tab. Banned examples: the middle dot, en and em dashes,
arrow symbols (write -> instead), curly quotes, ellipsis, the math minus, check marks, triangles.
Usage: python keyboard_check.py deck.pptx deck.pdf notes.md ...   (exit 1 if anything is found)"""
import sys
from pathlib import Path

# Real keys on Danil's keyboard (AltGr+5 gives the euro sign)
ALLOWED = "€"

FIX = {
    "\u00b7": ", ",
    "\u2013": "-",
    "\u2014": "-",
    "\u2192": "->",
    "\u2190": "<-",
    "\u2026": "...",
    "\u2212": "-",
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u00d7": "x",
    "\u2260": "!=",
    "\u2264": "<=",
    "\u2265": ">=",
    "\u2022": "-",
    "\u00a0": " ",
}


def texts(path):
    p = Path(path)
    if p.suffix == ".pptx":
        from pptx import Presentation
        for i, s in enumerate(Presentation(p).slides, 1):
            for sh in s.shapes:
                if sh.has_text_frame:
                    yield f"slide {i}", sh.text_frame.text
            if s.has_notes_slide:
                yield f"slide {i} notes", s.notes_slide.notes_text_frame.text
    elif p.suffix == ".pdf":
        import pymupdf
        import unicodedata
        for i, pg in enumerate(pymupdf.open(p), 1):
            # NFKC folds font ligatures (U+FB00 ff, U+FB01 fi) back to plain letters; those are rendering, not typed
            yield f"page {i}", unicodedata.normalize("NFKC", pg.get_text())
    else:
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            yield f"line {i}", line


def main(paths):
    bad = 0
    for path in paths:
        for where, t in texts(path):
            for ch in sorted(set(c for c in t if (ord(c) > 126 or ord(c) < 32) and c not in "\n\t\r" + ALLOWED)):
                bad += 1
                ctx = t[max(0, t.find(ch) - 25): t.find(ch) + 25].replace("\n", " ")
                print(f"{path} {where}: U+{ord(ch):04X} -> use {FIX.get(ch, 'plain ASCII')!r} | ...{ctx}...")
    print("OK: keyboard-only" if not bad else f"FAIL: {bad} non-keyboard characters")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
