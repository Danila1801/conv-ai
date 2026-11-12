"""Group 7 deck v4: RLHF as the fix -> its cost -> the paper's claim -> context, workers, prior work -> cases -> result.
v4 answers Antonia's review (12 Nov 2026): less US/NL focus at the start, RLHF introduced as a solution first,
a context slide, a workers slide, and a cited comparison table of earlier solutions.
Run (from this folder): ../.venv/Scripts/python charts.py; ../.venv/Scripts/python build_deck.py;
powershell -File export_pdf.ps1; ../.venv/Scripts/python build_cards.py
Every number has its source on the slide. Edit text here, not in PowerPoint."""
import json
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Pt, Inches

BG = RGBColor(0xF2, 0xF5, 0xF3)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x17, 0x23, 0x1F)
MUTED = RGBColor(0x5E, 0x6B, 0x66)
ACCENT = RGBColor(0x2C, 0x6E, 0x5F)
SOFT = RGBColor(0xBC, 0xCF, 0xC8)
LINE = RGBColor(0xD3, 0xDE, 0xD9)
TINT = RGBColor(0xDD, 0xEB, 0xE5)
DARK = RGBColor(0x1C, 0x2B, 0x27)
SERIF, SANS = "Georgia", "Segoe UI"
W, H = Inches(13.333), Inches(7.5)
M = Inches(0.75)
OUT = "Group7-v4"
WORDS_PER_SEC = 1.9  # non-native speaking pace; a script faster than this is too long for its seconds

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]
SCRIPTS = {}


def rich(slide, x, y, w, h, paras, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT, spacing=1.15):
    """paras: list of tuples (text, size, font, color, bold, italic, space_before)"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, para in enumerate(paras):
        t, size, font, color, bold, italic, sb = (list(para) + [False, False, 0])[:7]
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        p.space_before = Pt(sb)
        r = p.add_run()
        r.text = t
        r.font.size, r.font.name, r.font.bold, r.font.italic = Pt(size), font, bold, italic
        r.font.color.rgb = color
    return tb


def text(slide, x, y, w, h, t, size=20, font=SANS, color=INK, bold=False, italic=False, **kw):
    return rich(slide, x, y, w, h, [(t, size, font, color, bold, italic, 0)], **kw)


def box(slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE, lw=1.25):
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
        s.line.width = Pt(lw)
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.14
    return s


def arrow_right(s, x, y, w=Inches(0.45), h=Inches(0.36), color=ACCENT):
    return box(s, x, y, w, h, fill=color, shape=MSO_SHAPE.RIGHT_ARROW)


def arrow_down(s, x, y, w=Inches(0.34), h=Inches(0.3), color=ACCENT):
    return box(s, x, y, w, h, fill=color, shape=MSO_SHAPE.DOWN_ARROW)


def slide(title=None, kicker=None, n=None, source=None):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    if kicker:
        text(s, M, Inches(0.45), Inches(9), Inches(0.3), kicker, 14, SANS, ACCENT, bold=True)
    if title:
        text(s, M, Inches(0.78), W - 2 * M, Inches(1.1), title, 30, SERIF, INK, spacing=1.0)
    if n:
        text(s, W - M - Inches(0.6), H - Inches(0.5), Inches(0.6), Inches(0.25), str(n), 11, SANS, MUTED,
             align=PP_ALIGN.RIGHT)
    if source:
        text(s, M, H - Inches(0.55), Inches(11.2), Inches(0.35), "Source: " + source, 11, SANS, MUTED)
    return s


def bubble(s, x, y, w, t, who="bot", size=15, h=None, italic=False):
    h = h or Inches(0.75)
    fill, col = (WHITE, INK) if who == "bot" else (DARK, WHITE)
    box(s, x, y, w, h, fill=fill, line=LINE if who == "bot" else None, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    rich(s, x + Inches(0.18), y, w - Inches(0.36), h, [(t, size, SANS, col, False, italic, 0)],
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.05)


def picture(s, path, x, y, w=None, h=None):
    return s.shapes.add_picture(path, x, y, width=w, height=h)


def say(n, who, secs, script):
    SCRIPTS[n] = (who, secs, script)


# 1 - title
s = slide()
text(s, M, Inches(1.35), Inches(7), Inches(0.3), "Conversational AI, paper presentation, Group 7", 14, SANS,
     ACCENT, bold=True)
text(s, M, Inches(1.8), Inches(7.2), Inches(2.2), "Decentralising\nLLM Alignment", 54, SERIF, INK, spacing=1.0)
text(s, M, Inches(3.95), Inches(6.8), Inches(0.9), "Who gets to decide how a chatbot behaves?", 22, SERIF, MUTED,
     italic=True)
rich(s, M, Inches(5.55), Inches(7), Inches(0.9),
     [("Oriane Peter & Kate Devlin, King's College London, AIES 2025", 14, SANS, INK),
      ("Antonia Bulai, Danila Popusoi, Goktug Yildirim", 14, SANS, MUTED, False, False, 4)])
asks = ["Is eating meat wrong?", "Should my grandma live with us?", "Who should I vote for?"]
y = Inches(1.45)
for q in asks:
    bubble(s, Inches(8.9), y, Inches(3.7), q, who="user", size=14, h=Inches(0.55))
    bubble(s, Inches(8.1), y + Inches(0.68), Inches(4.5), "It depends. There are good points on both sides...", size=13,
           h=Inches(0.55))
    y += Inches(1.5)
text(s, Inches(8.1), Inches(6.0), Inches(4.5), Inches(0.4), "Mock-up made by us: different questions, one style of answer",
     12, SANS, MUTED, italic=True)
say(1, "P1", 20,
    "Hi, we're Group 7. Our paper is Decentralising LLM Alignment, by Oriane Peter and Kate Devlin from King's "
    "College London. The question behind it is simple: who gets to decide how a chatbot behaves?")

# 2 - RLHF as the solution
s = slide("RLHF fixed a real problem: a raw language model only continues text", "Part 1: Why alignment exists", 2,
          "Ouyang et al. (2022), InstructGPT, cited in the paper: human ratings on OpenAI API prompts. Example "
          "answers from OpenAI's InstructGPT announcement (2022).")
steps = ["People rank a few answers", "A reward model learns their taste", "The LLM is trained for high reward"]
x = M
for i, st in enumerate(steps):
    box(s, x, Inches(1.95), Inches(3.55), Inches(0.62), fill=WHITE, line=LINE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, x, Inches(1.95), Inches(3.55), Inches(0.62), st, 15, SANS, INK, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE)
    if i < 2:
        arrow_right(s, x + Inches(3.6), Inches(2.08))
    x += Inches(4.1)
# before / after mock-up (real example from OpenAI 2022)
px, py, pw = M, Inches(2.95), Inches(7.0)
bubble(s, px + Inches(2.2), py, Inches(4.8), "Explain the moon landing to a 6 year old in a few sentences.", "user",
       14, Inches(0.6))
text(s, px, py + Inches(0.78), Inches(3.3), Inches(0.3), "GPT-3, before RLHF", 13, SANS, MUTED, bold=True)
bubble(s, px, py + Inches(1.1), Inches(3.35),
       "Explain the theory of gravity to a 6 year old. Explain the theory of relativity to a 6 year old...", "bot", 14,
       Inches(1.45))
text(s, px + Inches(3.6), py + Inches(0.78), Inches(3.4), Inches(0.3), "InstructGPT, after RLHF", 13, SANS, ACCENT,
     bold=True)
bubble(s, px + Inches(3.6), py + Inches(1.1), Inches(3.4),
       "People went to the moon, and they took pictures of what they saw, and sent them back to the earth...", "bot", 14,
       Inches(1.45))
rich(s, Inches(8.45), Inches(2.95), Inches(4.15), Inches(3.4),
     [("85%", 60, SERIF, ACCENT),
      ("of the time, people preferred InstructGPT's answers to GPT-3's (same size, 175B).", 17, SANS, INK, False,
       False, 2),
      ("Even a 100x smaller InstructGPT (1.3B) beat GPT-3.", 17, SANS, INK, False, False, 12)])
say(2, "P1", 50,
    "First, the problem RLHF solved. A pre-trained model only continues text. Ask GPT-3 to explain the moon landing "
    "to a six year old, and it writes more questions. Early chatbots also copied toxic language. RLHF fixed this: "
    "people rank answers, a reward model learns what they prefer, and the model is trained to score high. People "
    "preferred the result 85 percent of the time, and even a model a hundred times smaller beat GPT-3.")

# 3 - aligned to whom
s = slide("But RLHF aligns a model to one small group: its labellers, and the people instructing them",
          "Part 1: Aligned to whom?", 3,
          "Ouyang et al. (2022), Sections 3.4 and 5.2, Appendix B (labeller survey, rounded). Atari et al. (2023), "
          "Which Humans? Both cited in the paper.")
chain = [("OpenAI researchers", "write the labelling rules"),
         ("About 40 contractors", "hired for 75% agreement with the researchers' labels"),
         ("One model", "for all of its users")]
x = M
cw = Inches(3.55)
for i, (a, b) in enumerate(chain):
    box(s, x, Inches(2.0), cw, Inches(1.05), fill=DARK if i == 1 else WHITE, line=None if i == 1 else LINE,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    rich(s, x + Inches(0.2), Inches(2.0), cw - Inches(0.4), Inches(1.05),
         [(a, 17, SANS, WHITE if i == 1 else INK, True), (b, 14, SANS, SOFT if i == 1 else MUTED, False, False, 2)],
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    if i < 2:
        arrow_right(s, x + cw + Inches(0.05), Inches(2.35))
    x += cw + Inches(0.55)
# labeller nationality bar (stacked, widths proportional)
text(s, M, Inches(3.4), Inches(8), Inches(0.3), "Who the labellers were (nationality, OpenAI's own survey)", 14, SANS,
     ACCENT, bold=True)
segs = [("Filipino 22%", 22, ACCENT, WHITE), ("Bangladeshi 22%", 22, RGBColor(0x7F, 0xAE, 0x9F), WHITE),
        ("American 17%", 17, SOFT, INK), ("7 other countries, about 5% each", 39, TINT, INK)]
bx, bw_total = M, W - 2 * M
for lab, pct, fill, col in segs:
    ww = int(bw_total * pct / 100)
    box(s, bx, Inches(3.78), ww, Inches(0.6), fill=fill)
    text(s, bx, Inches(3.78), ww, Inches(0.6), lab, 14, SANS, col, bold=True, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE)
    bx += ww
# bottom: OpenAI's admission + WEIRD result
box(s, M, Inches(4.75), Inches(5.75), Inches(1.75), fill=WHITE, line=LINE)
rich(s, M + Inches(0.3), Inches(4.75), Inches(5.2), Inches(1.75),
     [("OpenAI itself:", 14, SANS, ACCENT, True),
      ("this group is \"clearly not representative of the full spectrum of people\" who use the model.", 17, SERIF,
       INK, False, True, 4)], anchor=MSO_ANCHOR.MIDDLE)
box(s, Inches(6.85), Inches(4.75), Inches(5.73), Inches(1.75), fill=TINT)
rich(s, Inches(7.15), Inches(4.75), Inches(5.2), Inches(1.75),
     [("r = -0.70", 34, SERIF, ACCENT),
      ("GPT matches people from WEIRD societies best, and gets worse the further a society is from them.", 15, SANS,
       INK, False, False, 2)], anchor=MSO_ANCHOR.MIDDLE)
say(3, "P1", 45,
    "But whose preferences? OpenAI says it openly. Researchers wrote the labelling rules, and about forty "
    "contractors were hired partly for agreeing 75 percent with the researchers' own labels. The labellers came from "
    "many countries, but OpenAI admits this group is clearly not representative of its users. Atari and colleagues "
    "found GPT fits Western, educated, rich societies best, the so-called WEIRD bias.")

# 4 - mode collapse
s = slide("RLHF also narrows the answers: 5 to 11 times less variety", "Part 1: The side effect", 4,
          "Kirk et al. (2024), ICLR, Table 11: diversity of answers to the same input (EAD), OPT models, "
          "summarisation. Cited in the paper.")
picture(s, "charts/rlhf_diversity.png", M, Inches(1.95), h=Inches(4.75))
rich(s, Inches(9.35), Inches(2.3), Inches(3.25), Inches(3.9),
     [("Mode collapse", 24, SERIF, INK),
      ("Ask the same thing several times: after RLHF you get almost the same answer, the kind its raters liked.", 17,
       SANS, INK, False, False, 6),
      ("Bigger model, same effect.", 17, SANS, ACCENT, True, False, 14)])
say(4, "P1", 40,
    "RLHF has a second effect. This chart is from Kirk and colleagues. Light bars are before RLHF, green bars after. "
    "The score is how different the answers are to the same question. It drops from about 0.8 to between 0.07 and "
    "0.16, and a bigger model does not fix it. This is mode collapse. Keep it in mind, it comes back.")

# 5 - the paper's claim: power/knowledge loop + three requirements
s = slide("The paper's claim: whoever aligns the model gets power over what counts as knowledge",
          "Part 2: The paper's argument", 5, "Peter & Devlin (2025), after Foucault (1975) and Jasanoff (2006)")
nodes = [("Money, data and compute", "only a few companies have them"),
         ("They align the model", "and decide what is \"helpful\" or \"harmful\""),
         ("The model spreads that view", "to everyone, at scale"),
         ("That view becomes normal", "and their power grows")]
nx = [M, Inches(3.95), Inches(3.95), M]
ny = [Inches(2.05), Inches(2.05), Inches(4.35), Inches(4.35)]
nw, nh = Inches(2.75), Inches(1.45)
for i, (a, b) in enumerate(nodes):
    box(s, nx[i], ny[i], nw, nh, fill=DARK if i == 1 else WHITE, line=None if i == 1 else LINE,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    rich(s, nx[i] + Inches(0.15), ny[i], nw - Inches(0.3), nh,
         [(a, 16, SANS, WHITE if i == 1 else INK, True), (b, 13, SANS, SOFT if i == 1 else MUTED, False, False, 3)],
         anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
arrow_right(s, M + nw + Inches(0.02), Inches(2.6))
arrow_down(s, Inches(3.95) + nw // 2 - Inches(0.17), Inches(3.62), h=Inches(0.6))
box(s, M + nw + Inches(0.02), Inches(4.9), Inches(0.45), Inches(0.36), fill=ACCENT, shape=MSO_SHAPE.LEFT_ARROW)
box(s, M + nw // 2 - Inches(0.17), Inches(3.62), Inches(0.34), Inches(0.6), fill=ACCENT, shape=MSO_SHAPE.UP_ARROW)
text(s, M, Inches(5.95), Inches(5.95), Inches(0.35), "Power and knowledge feed each other (Foucault)", 13, SANS, MUTED,
     italic=True, align=PP_ALIGN.CENTER)
box(s, Inches(7.35), Inches(2.05), Inches(0.06), Inches(3.75), fill=ACCENT)
reqs = [("Their answer: decentralise alignment", 20, SERIF, INK)]
for k, (name, d) in enumerate([("1  Context", "align for one use and one group"),
                               ("2  Pluralism", "keep disagreement, don't average it away"),
                               ("3  Participation", "affected people get real control")]):
    reqs += [(name, 20, SANS, ACCENT, True, False, 16), (d, 16, SANS, INK, False, False, 2)]
rich(s, Inches(7.7), Inches(2.05), Inches(4.9), Inches(3.9), reqs)
say(5, "P1", 40,
    "That is the core of the paper. Power and knowledge feed each other. A few companies can afford to align a "
    "model, so they decide what counts as helpful or harmful. The model spreads that view at scale, and their power "
    "grows. Their answer is to decentralise alignment, with three requirements. Over to Presenter 2.")

# 6 - context
s = slide("Context: you can only check an alignment if you know who it is for, and what it is for",
          "Part 2: Requirement 1, context", 6,
          "Peter & Devlin (2025), Context section, citing Gebru & Torres (2024), Chen et al. (2023), Jha et al. (2024). "
          "Cards are a mock-up made by us.")
cards = [("General chatbot", ["Aligned to", "\"humans\" in general", "For", "anything", "Who benefits", "unclear",
                              "Harms", "cannot be defined"], False),
         ("Contextual chatbot: voter information", ["Aligned to", "voters, parties, independent monitors", "For",
                                                    "explaining party positions", "Who benefits", "voters, not one party",
                                                    "Harms", "can be tested: bias, wrong facts"], True)]
cx = M
cwid = Inches(5.75)
for title, fields, good in cards:
    box(s, cx, Inches(2.0), cwid, Inches(3.75), fill=WHITE, line=ACCENT if good else LINE, lw=2.25 if good else 1.25)
    box(s, cx, Inches(2.0), cwid, Inches(0.55), fill=ACCENT if good else SOFT)
    text(s, cx + Inches(0.25), Inches(2.0), cwid, Inches(0.55), title, 16, SANS, WHITE if good else INK, bold=True,
         anchor=MSO_ANCHOR.MIDDLE)
    yy = Inches(2.75)
    for j in range(0, len(fields), 2):
        text(s, cx + Inches(0.3), yy, Inches(1.7), Inches(0.5), fields[j], 14, SANS, MUTED)
        text(s, cx + Inches(2.0), yy, cwid - Inches(2.25), Inches(0.5), fields[j + 1], 16, SANS,
             INK if good else MUTED, bold=good)
        yy += Inches(0.72)
    cx += cwid + Inches(0.33)
box(s, M, Inches(5.95), W - 2 * M, Inches(0.6), fill=TINT)
text(s, M + Inches(0.3), Inches(5.95), W - 2 * M - Inches(0.6), Inches(0.6),
     "Already possible with open-weight models: Meditron for medicine, MemeGuard for memes.", 16, SANS, INK,
     anchor=MSO_ANCHOR.MIDDLE)
say(6, "P2", 45,
    "Thanks. Requirement one is context. A lot of alignment work talks about humans in general. The authors say that "
    "hides whose views are inside the model, and a system for everything can't even define its harms. Compare the "
    "two cards. On the right we know who it serves and what to test. Open-weight models already allow this, for "
    "example Meditron for medicine.")

# 7 - workers
s = slide("The people who label the data, and how they work, shape what the model learns",
          "Part 2: Context includes the workers", 7,
          "Peter & Devlin (2025), Participation section. Miceli & Posada (2022), CSCW. Muldoon et al. (2023), AI & "
          "Society. Diaz et al. (2022), FAccT. All cited in the paper.")
chain = ["Heavy workload and strict quality checks", "Unpaid overtime when targets are missed",
         "Workers label what they think the client wants", "Diverse workers, but one viewpoint in the data"]
yy = Inches(1.95)
for i, c in enumerate(chain):
    last = i == len(chain) - 1
    box(s, M, yy, Inches(5.6), Inches(0.66), fill=ACCENT if last else WHITE, line=None if last else LINE,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, M + Inches(0.25), yy, Inches(5.1), Inches(0.66), c, 16, SANS, WHITE if last else INK, bold=last,
         anchor=MSO_ANCHOR.MIDDLE)
    if not last:
        arrow_down(s, M + Inches(2.63), yy + Inches(0.69), h=Inches(0.24))
    yy += Inches(0.96)
stats = [("210 + 55", "instruction documents and interviews (Venezuela, Argentina): instructions carry the client's "
                      "worldview, and workers who need the pay obey them."),
         ("< $2 an hour", "pay of Sama annotators in Kenya, a company that sells itself as \"ethical AI\".")]
yy = Inches(1.95)
for big, small in stats:
    rich(s, Inches(6.95), yy, Inches(5.65), Inches(1.7),
         [(big, 34, SERIF, ACCENT), (small, 15, SANS, INK, False, False, 2)])
    yy += Inches(1.8)
box(s, Inches(6.95), Inches(5.55), Inches(5.63), Inches(0.95), fill=TINT)
text(s, Inches(7.2), Inches(5.55), Inches(5.2), Inches(0.95),
     "Paper's fix: report who labelled the data, and under what conditions (CrowdWorkSheets).", 15, SANS, INK,
     anchor=MSO_ANCHOR.MIDDLE)
say(7, "P2", 50,
    "Context also includes the workers. Labelling is often outsourced to people in poor conditions. Miceli and Posada "
    "read 210 instruction documents and did 55 interviews: the instructions carry the client's worldview, and workers "
    "who need the pay follow them. Sama annotators in Kenya earned under two dollars an hour. So hiring diverse "
    "workers is not enough. The fix: report who labelled, and how they worked.")

# 8 - comparison table of earlier solutions
s = slide("Earlier fixes added voices, but never the final say", "Part 2: What was tried before", 8,
          "Peter & Devlin (2025), section Context, Pluralism and Participation in Previous Work. Anthropic (2023) for "
          "the CCAI numbers. Cells summarise the paper's own assessment.")
Y, N, P, ND = "yes", "no", "partly", "not discussed"
head = ["Project", "Who took part", "Context:\na specific use?", "Pluralism: keeps\ndisagreement?", "Participation",
        "Workers'\nconditions"]
rows = [("STELA, Bergman 2024", "44, in focus groups", (N, "universal rules"), (P, "debate, then one rule set"),
         ("consult", ""), (Y, "small, well paid")),
        ("Collective Constitutional AI, Huang 2024", "~1,000 Americans", (N, "universal rules"),
         (N, "voting, one set"), ("consult", ""), ("little info", "")),
        ("PRISM, Kirk 2024", "1,500 English speakers", (P, "topic clusters"), (Y, "allows personalisation"),
         ("consult", ""), (ND, "")),
        ("Open RLHF dataset, Rose 2025", "~15,000, 5 countries", (Y, "10 use cases"), (ND, ""), ("consult", ""),
         (ND, "")),
        ("Multilingual Prism, Aakanksha 2024", "900 prompts, 8 languages", (P, "local harms"),
         (P, "noted, not used"), ("consult", ""), ("little info", "")),
        ("LoRA per community, Varshney 2024", "communities (a proposal)", (P, "one size for all"),
         (Y, "one add-on each"), ("own", ""), ("-", ""))]
colw = [Inches(2.75), Inches(2.0), Inches(1.75), Inches(1.95), Inches(1.5), Inches(1.88)]
x0, y0, rh, hh = M, Inches(1.9), Inches(0.52), Inches(0.6)
cx = x0
for j, hd in enumerate(head):
    text(s, cx + Inches(0.06), y0, colw[j] - Inches(0.1), hh, hd, 13, SANS, MUTED, bold=True,
         anchor=MSO_ANCHOR.BOTTOM, spacing=1.0)
    cx += colw[j]
box(s, x0, y0 + hh + Inches(0.04), sum(colw, Inches(0)), Inches(0.03), fill=INK)
yy = y0 + hh + Inches(0.1)
for r in rows:
    cx = x0
    for j, cell in enumerate(r):
        cw_ = colw[j]
        if j < 2:
            text(s, cx + Inches(0.06), yy, cw_ - Inches(0.1), rh, cell, 13 if j == 0 else 14, SANS,
                 INK if j == 0 else MUTED, bold=j == 0, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        else:
            verdict, note = cell
            if verdict in (Y, "own"):
                fill, col = ACCENT, WHITE
            elif verdict == P:
                fill, col = SOFT, INK
            elif verdict in (N, "consult", "little info"):
                fill, col = WHITE, INK
            else:
                fill, col = None, MUTED
            box(s, cx + Inches(0.04), yy + Inches(0.04), cw_ - Inches(0.08), rh - Inches(0.08), fill=fill,
                line=LINE if fill == WHITE else None)
            label = verdict if not note else f"{verdict}: {note}"
            text(s, cx + Inches(0.1), yy, cw_ - Inches(0.2), rh, label, 12, SANS, col, bold=verdict in (Y, "own"),
                 italic=fill is None, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, spacing=0.95)
        cx += cw_
    yy += rh
# CCAI callout
fy = yy + Inches(0.2)
box(s, M, fy, W - 2 * M, Inches(0.7), fill=TINT)
text(s, M + Inches(0.3), fy, Inches(3.3), Inches(0.7), "Collective Constitutional AI:", 15, SANS, ACCENT, bold=True,
     anchor=MSO_ANCHOR.MIDDLE)
funnel = ["1,127 public statements", "75 principles", "1 adopted by Anthropic"]
fx = Inches(3.95)
for i, f in enumerate(funnel):
    text(s, fx, fy, Inches(2.55), Inches(0.7), f, 16, SANS, INK, bold=i == 2, anchor=MSO_ANCHOR.MIDDLE,
         align=PP_ALIGN.CENTER)
    if i < 2:
        arrow_right(s, fx + Inches(2.6), fy + Inches(0.2), w=Inches(0.32), h=Inches(0.3))
    fx += Inches(2.95)
say(8, "P2", 60,
    "How did earlier projects do? This table is the paper's own comparison. Context: most write universal rules; "
    "only Rose and colleagues tie data to specific uses. Pluralism: most vote everything into one rule set. Workers: "
    "only STELA describes good conditions. And all sit at consult: people give input, the company decides. In "
    "Collective Constitutional AI, the public wrote 75 principles, and Anthropic adopted one. Varshney instead lets "
    "each community own a small add-on. Over to Presenter 3.")

# 9 - two cases as mock-ups
s = slide("Two made-up cases, picked to be opposites, show why context matters", "Part 3: How they apply it", 9,
          "Peter & Devlin (2025), use cases. Mock-ups made by us.")
px, py, pw, ph = M, Inches(1.95), Inches(5.6), Inches(3.9)
box(s, px, py, pw, ph, fill=WHITE, line=LINE)
box(s, px, py, pw, Inches(0.5), fill=DARK)
text(s, px + Inches(0.25), py, pw, Inches(0.5), "Voter advice chatbot", 15, SANS, WHITE, bold=True,
     anchor=MSO_ANCHOR.MIDDLE)
bubble(s, px + Inches(1.6), py + Inches(0.75), Inches(3.75), "What do parties say about housing?", "user", 14,
       Inches(0.55))
bubble(s, px + Inches(0.25), py + Inches(1.5), Inches(4.4),
       "Party A wants more social housing. Party B wants lower taxes for builders. Party C...", "bot", 14, Inches(0.95))
text(s, px + Inches(0.25), py + Inches(2.55), Inches(5), Inches(0.35), "Sources: party programmes", 13, SANS, ACCENT)
text(s, px + Inches(0.25), py + Inches(3.0), pw - Inches(0.5), Inches(0.7),
     "Risk: people ask commercial chatbots how to vote, and those were never built to be neutral.", 14, SANS, MUTED)
qx = Inches(6.98)
box(s, qx, py, pw, ph, fill=DARK, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, qx + Inches(0.35), py + Inches(0.4), Inches(0.9), Inches(0.9), fill=ACCENT, shape=MSO_SHAPE.OVAL)
text(s, qx + Inches(0.35), py + Inches(0.4), Inches(0.9), Inches(0.9), "NPC", 14, SANS, WHITE, bold=True,
     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rich(s, qx + Inches(1.45), py + Inches(0.45), Inches(3.9), Inches(0.9),
     [("Village elder", 16, SANS, WHITE, True), ("one LLM voices every character", 13, SANS, SOFT)])
box(s, qx + Inches(0.35), py + Inches(1.5), pw - Inches(0.7), Inches(1.15), fill=RGBColor(0x2A, 0x3D, 0x38),
    shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, qx + Inches(0.55), py + Inches(1.5), pw - Inches(1.1), Inches(1.15),
     "\"Our people have fished this river for generations. Sit, traveller, I will tell you how.\"", 15, SERIF,
     WHITE, italic=True, anchor=MSO_ANCHOR.MIDDLE)
text(s, qx + Inches(0.35), py + Inches(3.0), pw - Inches(0.7), Inches(0.7),
     "Risk: studios lack diverse teams, so stereotypes of real communities can get worse.", 14, SANS, SOFT)
say(9, "P3", 35,
    "Thanks. To show that context changes the answer, the authors use two made-up cases. On the left, a voter advice "
    "chatbot, like a chat version of StemWijzer. On the right, a game where one language model voices every "
    "character, and stereotypes of real communities can get worse.")

# 10 - three kinds of pluralism (Sorensen et al.)
s = slide("Requirement 2, pluralism, comes in three kinds", "Part 3: The toolkit", 10,
          "Kinds of pluralism: Sorensen et al. (2024), as used in Peter & Devlin (2025). Example answers written by us.")
bubble(s, M + Inches(3.3), Inches(1.9), Inches(5.3), "Should we build more nuclear power plants?", "user", 15,
       Inches(0.55))
kinds = [("Overton", "One answer that shows all reasonable views.",
          "\"Some parties say yes, for the climate. Others say no, because of cost and waste.\"", "Voter chatbot"),
         ("Steerable", "Takes the view it is asked for.",
          "\"As a Green voter: no, invest in wind and solar instead.\"", "Game characters"),
         ("Distributional", "Answers match how common each view is.",
          "Says yes in 55% of answers and no in 45%.", "Rejected for both")]
cw = (W - 2 * M - Inches(0.8)) // 3
x = M
for i, (k, d, ex, use) in enumerate(kinds):
    box(s, x, Inches(2.75), cw, Inches(3.6), fill=WHITE, line=LINE)
    rich(s, x + Inches(0.25), Inches(2.9), cw - Inches(0.5), Inches(2.6),
         [(k, 22, SERIF, INK), (d, 15, SANS, MUTED, False, False, 4), (ex, 16, SANS, INK, False, True, 12)])
    box(s, x, Inches(5.75), cw, Inches(0.6), fill=SOFT if i == 2 else ACCENT)
    text(s, x + Inches(0.25), Inches(5.75), cw - Inches(0.5), Inches(0.6), "-> " + use, 16, SANS,
         INK if i == 2 else WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    x += cw + Inches(0.4)
say(10, "P3", 35,
    "Requirement two, pluralism, comes in three kinds. Take a question people disagree on. An Overton answer shows "
    "all the reasonable views. A steerable answer takes the view it is asked for. A distributional model says yes or "
    "no as often as people do. Overton fits the voter bot, steerable fits game characters.")

# 11 - result table (paper's Table 1)
s = slide("Same three requirements, opposite answers", "Part 3: Result", 11,
          "Adapted from Peter & Devlin (2025), Table 1")
rows = [("", "Voter chatbot", "Game character"),
        ("Power gap today", "Private companies vs democratic states", "Game studios vs depicted communities"),
        ("How to train it", "RLHF: consistent answers for everyone", "SFT + LoRA: a cheap add-on per community"),
        ("Kind of pluralism", "Overton: show a spectrum of party views", "Steerable: true to its own community"),
        ("Who decides", "State, parties and citizens together", "Each community, no global consensus")]
c0 = Inches(3.1)
cw = (W - 2 * M - c0) // 2
y = Inches(2.0)
box(s, M + c0, y - Inches(0.1), cw - Inches(0.15), Inches(3.75), fill=WHITE)
box(s, M + c0 + cw, y - Inches(0.1), cw - Inches(0.15), Inches(3.75), fill=WHITE)
for i, r in enumerate(rows):
    for j, cell in enumerate(r):
        cx = M if j == 0 else M + c0 + (j - 1) * cw + Inches(0.2)
        ww = c0 - Inches(0.2) if j == 0 else cw - Inches(0.55)
        if i == 0:
            text(s, cx, y, ww, Inches(0.5), cell, 22, SERIF, ACCENT)
        else:
            text(s, cx, y, ww, Inches(0.8), cell, 18 if j else 16, SANS, INK if j else MUTED)
    y += Inches(0.6) if i == 0 else Inches(0.78)
box(s, M, Inches(5.8), W - 2 * M, Inches(0.7), fill=TINT)
text(s, M + Inches(0.3), Inches(5.8), W - 2 * M - Inches(0.6), Inches(0.7),
     "Mode collapse: a problem for game characters, but it can help a voter chatbot stay consistent.", 19, SERIF, INK,
     italic=True, anchor=MSO_ANCHOR.MIDDLE)
say(11, "P3", 50,
    "Here is the result: the same requirements give opposite answers. The voter chatbot gets RLHF, because every "
    "voter should get consistent answers, so here mode collapse can help. The game uses LoRA, cheap enough for a "
    "community to train, own, and take back if a studio misuses it. Who decides? For the voter bot, state, parties "
    "and citizens together. For the game, each community. No one-size-fits-all alignment.")

# 12 - our view + a metric
s = slide("Their proposal is convincing, but still untested", "Part 3: Discussion", 12,
          "Metric example and opinions are ours. Party names are placeholders.")
rich(s, M, Inches(1.95), Inches(5.6), Inches(3.5),
     [("Convincing", 16, SANS, ACCENT, True),
      ("Links ethics to real techniques: RLHF, LoRA, retrieval.", 17, SANS, INK, False, False, 4),
      ("Still open", 16, SANS, ACCENT, True, False, 16),
      ("No experiments. Both cases are made up.", 17, SANS, INK, False, False, 4),
      ("Who speaks for a \"community\", and who pays?", 17, SANS, INK, False, False, 4),
      ("Our view: a state-run voter bot gives power to governments. Always safer?", 17, SANS, INK, False, False, 4)])
rich(s, Inches(6.9), Inches(1.95), Inches(5.7), Inches(0.9),
     [("How we would measure it", 16, SANS, ACCENT, True),
      ("Overton coverage: which parties' positions does one answer mention?", 17, SANS, INK, False, False, 4)])
picture(s, "charts/overton_metric.png", Inches(6.9), Inches(3.05), w=Inches(5.6))
box(s, M, Inches(5.7), W - 2 * M, Inches(0.8), fill=WHITE, line=LINE)
text(s, M + Inches(0.3), Inches(5.7), W - 2 * M - Inches(0.6), Inches(0.8),
     "Question for you: what else would you measure to know if a voter chatbot is fair?", 19, SERIF, INK,
     anchor=MSO_ANCHOR.MIDDLE)
say(12, "P3", 50,
    "What convinced us: the paper links ethics to real techniques. What's open: there are no experiments, and who "
    "speaks for a community? Our own view: a state-run voter bot moves power to governments, which is not always "
    "safer. We would test it with Overton coverage: count which parties' positions one answer mentions, here four of "
    "six. So, what else would you measure to know if a voter chatbot is fair? Thank you.")

# 13 - backup sources
s = slide("Sources", "Backup, not presented", 13)
left = ("Peter, O. & Devlin, K. (2025). Decentralising LLM Alignment: A Case for Context, Pluralism, and "
        "Participation. AIES 2025, pp. 1988-1999.\n"
        "Ouyang, L. et al. (2022). Training language models to follow instructions with human feedback. NeurIPS.\n"
        "OpenAI (2022). Aligning language models to follow instructions (moon landing example).\n"
        "Atari, M. et al. (2023). Which Humans? PsyArXiv.\n"
        "Kirk, R. et al. (2024). Understanding the Effects of RLHF on LLM Generalisation and Diversity. ICLR.\n"
        "Miceli, M. & Posada, J. (2022). The Data-Production Dispositif. CSCW.\n"
        "Muldoon, J. et al. (2023). The poverty of ethical AI. AI & Society.\n"
        "Diaz, M. et al. (2022). CrowdWorkSheets. FAccT.")
right = ("Bergman, S. et al. (2024). STELA. Scientific Reports.\n"
         "Huang, S. et al. (2024) and Anthropic (2023). Collective Constitutional AI.\n"
         "Kirk, H. R. et al. (2024). The PRISM Alignment Dataset. NeurIPS.\n"
         "Rose, Kroner Dale & Jusko (2025). Open RLHF dataset, 10 use cases.\n"
         "Aakanksha et al. (2024). The Multilingual Alignment Prism. EMNLP.\n"
         "Varshney (2024). Community LoRA repository.\n"
         "Sorensen, T. et al. (2024). A Roadmap to Pluralistic Alignment.\n\n"
         "GenAI disclosure: we used Claude (Anthropic) and Kimi (Moonshot) to help draft and check slides, charts and "
         "speaker notes. Every number was checked against its source.")
text(s, M, Inches(1.85), Inches(5.8), Inches(5.0), left, 13, SANS, INK, spacing=1.25)
text(s, Inches(6.85), Inches(1.85), Inches(5.75), Inches(5.0), right, 13, SANS, INK, spacing=1.25)
say(13, "-", 0, "Not presented. Keep it ready for Q&A.")

# ---- checks + save
problems = []
for k, (who, secs, sc) in SCRIPTS.items():
    if secs and len(sc.split()) / secs > WORDS_PER_SEC:
        problems.append(f"slide {k}: {len(sc.split())} words in {secs} s is too fast")
tot = sum(v[1] for v in SCRIPTS.values())
if tot > 9 * 60:
    problems.append(f"planned talk is {tot} s, must be 540 s or less to leave time for transitions")
if problems:
    raise SystemExit("NOT SAVED:\n" + "\n".join(problems))
for i, sl in enumerate(prs.slides, start=1):
    who, secs, sc = SCRIPTS[i]
    sl.notes_slide.notes_text_frame.text = f"[{who}, about {secs} s]\n{sc}"
prs.save(f"{OUT}.pptx")
json.dump(SCRIPTS, open("scripts.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
words = {p: sum(len(v[2].split()) for v in SCRIPTS.values() if v[0] == p) for p in ("P1", "P2", "P3")}
secs = {p: sum(v[1] for v in SCRIPTS.values() if v[0] == p) for p in ("P1", "P2", "P3")}
print(f"saved {OUT}.pptx | planned {tot // 60}:{tot % 60:02d} | seconds {secs} | words {words} | "
      f"total {sum(words.values())}")
