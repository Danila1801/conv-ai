"""Group 7 deck v2: 7 plain slides, simple spoken scripts in the presenter notes.
Run: python build_deck.py   -> Group7-v2.pptx (+ PDF via export_pdf.ps1)
Content lives in SLIDES below. Edit the text there, not in PowerPoint, so the cards stay in sync."""
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Pt

BG = RGBColor(0xF6, 0xF3, 0xEC)      # warm paper
INK = RGBColor(0x1F, 0x22, 0x28)
MUTED = RGBColor(0x6B, 0x6B, 0x6B)
ACCENT = RGBColor(0xB4, 0x4A, 0x22)  # one accent, used sparingly
LINE = RGBColor(0xD9, 0xD3, 0xC7)
SERIF, SANS = "Georgia", "Segoe UI"

W, H = Emu(12192000), Emu(6858000)   # 13.333 x 7.5 in
M = Emu(700000)                      # side margin

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]


def text(slide, x, y, w, h, s, size=24, font=SANS, color=INK, bold=False, italic=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, spacing=1.15):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(s.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        r = p.add_run()
        r.text = line
        f = r.font
        f.size, f.name, f.bold, f.italic = Pt(size), font, bold, italic
        f.color.rgb = color
    return tb


def rich(slide, x, y, w, h, paras, anchor=MSO_ANCHOR.TOP):
    """paras: list of (text, size, font, color, bold, italic, space_before_pt)"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, (t, size, font, color, bold, italic, sb) in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.line_spacing = 1.2
        p.space_before = Pt(sb)
        r = p.add_run()
        r.text = t
        r.font.size, r.font.name, r.font.bold, r.font.italic = Pt(size), font, bold, italic
        r.font.color.rgb = color
    return tb


def rect(slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    s.shadow.inherit = False
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(1.25)
    return s


def base(title=None, kicker=None, page=None):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    if kicker:
        text(s, M, Emu(520000), Emu(9000000), Emu(300000), kicker.upper(), 12, SANS, ACCENT, bold=True)
    if title:
        text(s, M, Emu(820000), W - 2 * M, Emu(900000), title, 38, SERIF, INK)
    if page:
        text(s, W - M - Emu(600000), H - Emu(520000), Emu(600000), Emu(250000), str(page), 11, SANS, MUTED,
             align=PP_ALIGN.RIGHT)
        text(s, M, H - Emu(520000), Emu(6000000), Emu(250000), "Group 7, Peter & Devlin (2025)", 11, SANS, MUTED)
    return s


def notes(s, who, secs, script):
    s.notes_slide.notes_text_frame.text = f"[{who}, ~{secs} s]\n{script}"


# ---------------------------------------------------------------- slides
SCRIPTS = {}

# 1 title
s = base()
text(s, M, Emu(1500000), Emu(9000000), Emu(300000), "CONVERSATIONAL AI, PAPER PRESENTATION, GROUP 7", 12, SANS,
     ACCENT, bold=True)
text(s, M, Emu(1900000), Emu(10500000), Emu(1800000), "Decentralising\nLLM Alignment", 60, SERIF, INK, spacing=1.0)
text(s, M, Emu(3850000), Emu(10000000), Emu(500000), "Who gets to decide how a chatbot behaves?", 24, SERIF, MUTED,
     italic=True)
text(s, M, Emu(5450000), Emu(10000000), Emu(700000),
     "Oriane Peter & Kate Devlin, King's College London, AIES 2025\n"
     "Antonia Bulai, Danila Popusoi, Goktug Yildirim", 15, SANS, INK, spacing=1.3)
SCRIPTS[1] = ("P1", 20, "Hi, we're Group 7. Our paper is Decentralising LLM Alignment, by Oriane Peter and Kate Devlin "
              "from King's College London. The question behind it is simple: who gets to decide how a chatbot "
              "behaves? I'll explain the problem, then we'll show how they argue it, what they found, and what we "
              "think about it.")

# 2 the problem: flow diagram
s = base("Aligned with whom?", "1, The problem", 2)
steps = [("A small group of raters", "ranks the model's answers"),
         ("The model learns their taste", "this is RLHF"),
         ("Millions of users", "get that same taste")]
bw, bh, gap, y = Emu(3300000), Emu(1700000), Emu(560000), Emu(2250000)
x = M
for i, (a, b) in enumerate(steps):
    rect(s, x, y, bw, bh, fill=RGBColor(0xFF, 0xFF, 0xFF), line=LINE)
    rich(s, x + Emu(280000), y, bw - Emu(560000), bh,
         [(a, 21, SANS, INK, True, False, 0), (b, 17, SANS, MUTED, False, False, 6)], anchor=MSO_ANCHOR.MIDDLE)
    if i < 2:
        text(s, x + bw + Emu(100000), y + Emu(550000), gap - Emu(200000), Emu(500000), "->", 30, SANS, ACCENT,
             align=PP_ALIGN.CENTER)
    x += bw + gap
text(s, M, Emu(4500000), W - 2 * M, Emu(1200000),
     "Those raters are mostly from WEIRD societies: Western, Educated, Industrialised, Rich, Democratic.\n"
     "And RLHF makes answers more alike. That's called mode collapse.", 19, SANS, INK, spacing=1.35)
SCRIPTS[2] = ("P1", 75,
              "You all know ChatGPT. What made it actually useful was a step called RLHF, reinforcement learning from "
              "human feedback. It works like this: a small group of people rate the model's answers, the model learns "
              "what they like, and then millions of users get that same taste. OpenAI reportedly called this their "
              "secret sauce. The problem is: whose taste? The raters and the training data lean towards WEIRD "
              "societies: Western, Educated, Industrialised, Rich and Democratic. And RLHF also makes the answers more "
              "alike. That's called mode collapse: the model gets less varied and closer to what those raters "
              "preferred. Even OpenAI's own RLHF paper says it aligned to one specific group, not to everyone.")

# 3 power + prior work
s = base("More voices is not the same as more power", "1, Why it matters", 3)
col = (W - 2 * M - Emu(600000)) // 2
text(s, M, Emu(2100000), col, Emu(400000), "Earlier fixes asked more people", 18, SANS, ACCENT, bold=True)
text(s, M, Emu(2600000), col, Emu(2400000),
     "Collective Constitutional AI: ~1,000 Americans\n"
     "PRISM: 1,500 people\n"
     "Rose et al.: ~15,000 people, 5 countries\n\n"
     "But the company still made the final call.", 19, SANS, INK, spacing=1.4)
x2 = M + col + Emu(600000)
text(s, x2, Emu(2100000), col, Emu(400000), "The authors' point", 18, SANS, ACCENT, bold=True)
text(s, x2, Emu(2600000), col, Emu(2400000),
     "Whoever aligns the model decides what counts as \"harmful\" or \"helpful\".\n\n"
     "That view is then copied to millions of users. (Foucault: power and knowledge feed each other.)",
     19, SANS, INK, spacing=1.4)
SCRIPTS[3] = ("P1", 70,
              "People already tried to fix this by asking more people. Collective Constitutional AI asked about a "
              "thousand Americans to help write the rules for a model. PRISM collected preferences from 1,500 people. "
              "Rose and colleagues went to fifteen thousand people in five countries. The authors like this work, but "
              "they say it doesn't change who has power. People give input, and the company still decides. For "
              "example, Anthropic used only one of the rules that the public voted for. Their bigger point comes from "
              "Foucault: power and knowledge feed each other. Training big models needs huge resources, so mostly a "
              "few companies do the aligning, and they decide what counts as harmful or helpful. Then that view is "
              "copied to millions of people. So their question is: how do we spread that power out? Over to "
              "Presenter 2.")

# 4 the three principles
s = base("Their answer: three requirements", "2, The idea", 4)
items = [("Context", "Align for one use and one group, not for a \"general human\"."),
         ("Pluralism", "Keep disagreement. Don't force one consensus."),
         ("Participation", "The people affected get real control, not just a survey.")]
cw = (W - 2 * M - 2 * Emu(400000)) // 3
x = M
for name, desc in items:
    rect(s, x, Emu(2300000), cw, Emu(60000), fill=ACCENT)
    text(s, x, Emu(2550000), cw, Emu(600000), name, 32, SERIF, INK)
    text(s, x, Emu(3300000), cw, Emu(1300000), desc, 19, SANS, INK, spacing=1.35)
    x += cw + Emu(400000)
text(s, M, Emu(5150000), W - 2 * M, Emu(500000),
     "Position paper: no experiments, no dataset. They test the idea on two made-up cases.", 18, SANS, MUTED,
     italic=True)
SCRIPTS[4] = ("P2", 65,
              "Thanks. The authors' answer is that alignment needs three things. First, context: you align a model for "
              "one specific use and one group of people, because there's no general human that fits everyone. Second, "
              "pluralism: people disagree about values, and that's normal, so the model shouldn't squash everything "
              "into one consensus. Third, participation: the people who are affected should get real control, not "
              "just fill in a survey. One important thing about the method: this is a position paper. There are no "
              "experiments, no dataset and no metrics. Instead, they test their idea by applying it to two made-up "
              "use cases that are very different from each other.")

# 5 the two cases
s = base("Two made-up cases, on purpose very different", "2, How they argue it", 5)
cases = [("A voter chatbot", "Explains an election to citizens.",
          "Risk: people already ask ChatGPT how to vote, and it was never built to be neutral."),
         ("A game character (NPC)", "One LLM plays many characters in a game.",
          "Risk: studios lack diverse teams, so stereotypes of real communities can get worse.")]
cw = (W - 2 * M - Emu(600000)) // 2
x = M
for t, a, b in cases:
    rect(s, x, Emu(2150000), cw, Emu(2900000), fill=RGBColor(0xFF, 0xFF, 0xFF), line=LINE)
    rich(s, x + Emu(350000), Emu(2420000), cw - Emu(700000), Emu(2500000),
         [(t, 26, SERIF, INK, False, False, 0), (a, 19, SANS, INK, False, False, 14),
          (b, 18, SANS, MUTED, False, False, 14)])
    x += cw + Emu(600000)
text(s, M, Emu(5350000), W - 2 * M, Emu(400000),
     "For each case: what's at stake -> who has the power -> how alignment could fix it", 18, SANS, ACCENT)
SCRIPTS[5] = ("P2", 70,
              "The first case is a voter advice chatbot, like a chat version of StemWijzer. People already ask "
              "ChatGPT about elections, but it was never built or tested to give neutral advice. So the power to "
              "inform voters slowly moves from democratic institutions to private companies. The second case is a "
              "character in a video game, an NPC, where one language model plays many characters. Game studios often "
              "don't have diverse teams, so stereotypes of real communities risk getting worse when you add an "
              "already biased model. For each case they ask the same three things: what's at stake, who has the "
              "power, and how alignment could fix it. Presenter 3 will show what came out.")

# 6 the result table
s = base("Same framework, opposite answers", "3, Result", 6)
rows = [("", "Voter chatbot", "Game character"),
        ("How to train it", "RLHF: same answers for everyone", "LoRA: a small add-on per community"),
        ("Which kind of pluralism", "Show all parties' views in one answer", "Each character true to its own community"),
        ("Who decides", "State, parties and citizens together", "Each community, no global consensus")]
c0, cw = Emu(3000000), (W - 2 * M - Emu(3000000)) // 2
y, rh = Emu(2000000), Emu(860000)
for i, r in enumerate(rows):
    if i:
        rect(s, M, y - Emu(60000), W - 2 * M, Emu(12000), fill=LINE)
    for j, cell in enumerate(r):
        cx = M if j == 0 else M + c0 + (j - 1) * cw
        w_ = c0 if j == 0 else cw - Emu(200000)
        style = dict(size=17, font=SANS, color=MUTED) if j == 0 else dict(size=18, font=SANS, color=INK)
        if i == 0:
            style = dict(size=22, font=SERIF, color=ACCENT)
        text(s, cx, y + Emu(80000), w_, rh, cell, **style)
    y += rh if i else Emu(620000)
text(s, M, Emu(5450000), W - 2 * M, Emu(500000),
     "Mode collapse: a bug for game characters, a feature for a voter chatbot.", 21, SERIF, INK, italic=True)
SCRIPTS[6] = ("P3", 80,
              "Thanks. The main result is that the same framework gives opposite answers. For the voter chatbot, they "
              "pick RLHF, because you want every voter to get consistent answers. Here mode collapse may actually "
              "help. They also want retrieval from trusted sources, so answers stick to the real party programmes. "
              "For the game character, they pick LoRA: a small add-on trained on top of the model. It's much cheaper, "
              "so a community could train its own and even take it back if a studio misuses it. Pluralism also "
              "flips: the voter bot should show all parties' views in one answer, while each game character should "
              "stay true to its own community. And who decides: for the voter bot it's the state, parties and "
              "citizens together. For the game, each community decides for itself. So the same technique can be a "
              "bug in one place and a feature in another. That's their whole point: there's no one-size-fits-all "
              "alignment.")

# 7 our view + question
s = base("What we think", "3, Discussion", 7)
col = (W - 2 * M - Emu(600000)) // 2
text(s, M, Emu(2000000), col, Emu(400000), "Convincing", 18, SANS, ACCENT, bold=True)
text(s, M, Emu(2450000), col, Emu(2000000),
     "It connects ethics to real techniques: RLHF, LoRA, retrieval.\n\n"
     "It's honest: alignment alone can't fix inequality.", 19, SANS, INK, spacing=1.35)
x2 = M + col + Emu(600000)
text(s, x2, Emu(2000000), col, Emu(400000), "Still open", 18, SANS, ACCENT, bold=True)
text(s, x2, Emu(2450000), col, Emu(2000000),
     "Nothing is tested yet.\n\n"
     "Who speaks for a \"community\"?\n\n"
     "A state-run voter bot gives power to governments. Is that always safer?", 19, SANS, INK, spacing=1.35)
rect(s, M, Emu(5250000), W - 2 * M, Emu(750000), fill=RGBColor(0xFF, 0xFF, 0xFF), line=LINE)
text(s, M + Emu(300000), Emu(5250000), W - 2 * M - Emu(600000), Emu(750000),
     "Question for you: how would you test if a voter chatbot shows all sides fairly?", 21, SERIF, INK,
     anchor=MSO_ANCHOR.MIDDLE)
SCRIPTS[7] = ("P3", 75,
              "What convinced us: the paper connects ethics to real techniques like RLHF, LoRA and retrieval, and it's "
              "honest that alignment alone can't fix inequality in society. What's still open: first, nothing is "
              "tested yet, both cases are made up. Second, who speaks for a community? Communities aren't one person. "
              "And this one is our own view: if the state runs the voter chatbot, power moves from companies to "
              "governments. Is that always safer? Not under every government. The authors themselves say the next "
              "step is to build and test these ideas. That fits today's lecture on evaluation, so we'll end with a "
              "question for you: how would you test if a voter chatbot shows all sides fairly? Thank you, we're "
              "happy to take questions.")

# 8 backup: references + disclosure
s = base("Sources", "Backup, not presented", 8)
text(s, M, Emu(2000000), W - 2 * M, Emu(3200000),
     "Peter, O. & Devlin, K. (2025). Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation. "
     "AIES 2025, 8(2), 1988-1999. doi:10.1609/aies.v8i2.36690\n\n"
     "Also mentioned: Ouyang et al. 2022 (RLHF), Huang et al. 2024 (Collective Constitutional AI), "
     "Kirk et al. 2024 (PRISM), Rose et al. 2025, Sorensen et al. 2024 (kinds of pluralism), Hu et al. 2021 (LoRA)\n\n"
     "GenAI disclosure: we used Claude (Anthropic) and Kimi (Moonshot) to help draft and check the slides and "
     "speaker notes. All content was checked against the paper by the group.", 16, SANS, INK, spacing=1.4)
SCRIPTS[8] = ("-", 0, "Not presented. Keep it ready for Q&A.")

for i, sl in enumerate(prs.slides, start=1):
    who, secs, sc = SCRIPTS[i]
    notes(sl, who, secs, sc)

prs.save("Group7-v2.pptx")
total = sum(v[1] for v in SCRIPTS.values())
words = {p: sum(len(v[2].split()) for v in SCRIPTS.values() if v[0] == p) for p in ("P1", "P2", "P3")}
print("saved Group7-v2.pptx | planned", total // 60, "min", total % 60, "s | words", words)

import json
json.dump(SCRIPTS, open("scripts.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
