"""Speaker cards for deck v4, from scripts.json (written by build_deck.py). Run after build_deck.py."""
import html
import json
import pymupdf as fitz

S = json.load(open("scripts.json", encoding="utf-8"))
NAMES = {"P1": "Presenter 1, slides 1-5: why RLHF exists, its cost, the paper's claim",
         "P2": "Presenter 2, slides 6-8: context, the workers, what was tried before",
         "P3": "Presenter 3, slides 9-12: the two cases, pluralism, result, our view"}
CSS = ("body{font-family:sans-serif;font-size:12.5pt;line-height:1.35} h1{font-size:20pt} "
       "h2{font-size:14pt;margin-top:12pt;color:#2c6e5f} p{margin:4pt 0 8pt 0} .t{color:#666;font-size:11pt}")
body = ""
for i, (p, title) in enumerate(NAMES.items()):
    secs = sum(v[1] for v in S.values() if v[0] == p)
    words = sum(len(v[2].split()) for v in S.values() if v[0] == p)
    page_break = "" if i == 0 else " style='page-break-before:always'"
    body += (f"<h1{page_break}>{title}</h1><p class='t'>~{secs // 60}:{secs % 60:02d}, {words} words. "
             "Don't read it word for word. Read it twice out loud, then just tell it. Look at the audience, "
             "not the slide.</p>")
    for k, (who, s, txt) in S.items():
        if who == p:
            body += f"<h2>Slide {k}, ~{s} s</h2><p>{html.escape(txt)}</p>"
story = fitz.Story(html=f"<style>{CSS}</style>" + body)
w = fitz.DocumentWriter("Group7-v4-speaker-cards.pdf")
mb = fitz.paper_rect("a4")
more = 1
while more:
    dev = w.begin_page(mb)
    more, _ = story.place(mb + (50, 50, -50, -50))
    story.draw(dev)
    w.end_page()
w.close()
print("wrote Group7-v4-speaker-cards.pdf")
