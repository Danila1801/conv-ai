"""Group 7 deck v3: assertion-evidence slides with real data, diagrams and mockups.
Run: python charts.py; python build_deck.py; powershell -File export_pdf.ps1; python build_cards.py
Every number has its source on the slide. Edit text here, not in PowerPoint."""
import json
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Pt, Inches

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

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]
SCRIPTS = {}


def rich(slide, x, y, w, h, paras, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT, spacing=1.2):
    """paras: list of tuples (text, size, font, color, bold, italic, space_before)"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, para in enumerate(paras):
        t, size, font, color, bold, italic, sb = (list(para) + [False, False, 0])[:7] if len(para) < 7 else para
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
        s.adjustments[0] = 0.18
    return s


def slide(title=None, kicker=None, n=None, source=None):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    if kicker:
        text(s, M, Inches(0.5), Inches(9), Inches(0.3), kicker, 14, SANS, ACCENT, bold=True)
    if title:
        text(s, M, Inches(0.82), W - 2 * M, Inches(1.2), title, 32, SERIF, INK, spacing=1.05)
    if n:
        text(s, W - M - Inches(0.6), H - Inches(0.5), Inches(0.6), Inches(0.25), str(n), 11, SANS, MUTED,
             align=PP_ALIGN.RIGHT)
    if source:
        text(s, M, H - Inches(0.5), Inches(10.5), Inches(0.25), "Source: " + source, 11, SANS, MUTED)
    return s


def bubble(s, x, y, w, t, who="bot", size=15, h=None):
    h = h or Inches(0.75)
    fill, col = (WHITE, INK) if who == "bot" else (DARK, WHITE)
    box(s, x, y, w, h, fill=fill, line=LINE if who == "bot" else None, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    rich(s, x + Inches(0.18), y, w - Inches(0.36), h, [(t, size, SANS, col, False, False, 0)],
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.1)


def picture(s, path, x, y, w=None, h=None):
    return s.shapes.add_picture(path, x, y, width=w, height=h)


# 1 - title, with the "everyone gets the same answer" motif
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
text(s, Inches(8.4), Inches(6.0), Inches(4), Inches(0.4), "Different people, very similar answers", 12, SANS, MUTED,
     italic=True)
SCRIPTS[1] = ("P1", 35,
              "Hi, we're Group 7. Our paper is Decentralising LLM Alignment by Oriane Peter and Kate Devlin. The "
              "mock-up shows the problem: different questions get almost the same careful answer. So who decides how "
              "a chatbot behaves? I'll cover the problem, Presenter 2 will explain their solution, and Presenter 3 "
              "the results and our view.")

# 2 - WEIRD: real correlation
s = slide("GPT's values are closest to the US, and to the Netherlands", "Part 1: The problem", 2,
          "Atari et al. (2023), Which Humans? World Values Survey, 94,278 people in 65 countries. Cited in the paper.")
rich(s, M, Inches(2.15), Inches(4.2), Inches(2.6),
     [("r = -0.70", 60, SERIF, ACCENT, False, False, 0),
      ("The further a country is culturally from the US, the less GPT's answers match its people.", 18, SANS, INK,
       False, False, 8)])
rich(s, Inches(5.4), Inches(2.25), Inches(7.1), Inches(2.4),
     [("WEIRD", 22, SERIF, INK, False, False, 0),
      ("Western, Educated, Industrialised, Rich, Democratic.", 17, SANS, MUTED, False, False, 4),
      ("The paper's claim: training data starts this skew, and alignment makes it stronger.", 18, SANS, INK, False,
       False, 14)])
picture(s, "charts/weird_strip.png", M, Inches(4.75), w=W - 2 * M)
SCRIPTS[2] = ("P1", 60,
              "First, a real number. Atari and colleagues gave GPT the World Values Survey, the same questions "
              "answered by almost a hundred thousand people in 65 countries. GPT's answers were closest to the "
              "United States, and also to countries like Canada, Germany and, yes, the Netherlands. They were "
              "furthest from countries like Ethiopia and Pakistan. The correlation is minus 0.70: the more a culture "
              "differs from the US, the worse GPT matches it. These are called WEIRD societies: Western, Educated, "
              "Industrialised, Rich and Democratic. The authors say the training data starts this bias, and "
              "alignment makes it stronger.")

# 3 - RLHF + mode collapse: real chart
s = slide("RLHF made answers 5 to 11 times less varied", "Part 1: The problem", 3,
          "Kirk et al. (2024), ICLR, Table 11: per-input diversity (EAD), OPT models, summarisation. Cited in the paper.")
steps = ["Raters rank answers", "A reward model learns their taste", "The LLM is trained to please it"]
x = M
for i, st in enumerate(steps):
    box(s, x, Inches(2.05), Inches(3.55), Inches(0.62), fill=WHITE, line=LINE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, x, Inches(2.05), Inches(3.55), Inches(0.62), st, 15, SANS, INK, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE)
    if i < 2:
        text(s, x + Inches(3.55), Inches(2.1), Inches(0.42), Inches(0.5), "->", 22, SANS, ACCENT,
             align=PP_ALIGN.CENTER)
    x += Inches(3.97)
picture(s, "charts/rlhf_diversity.png", M, Inches(2.95), h=Inches(3.85))
rich(s, Inches(8.3), Inches(3.3), Inches(4.3), Inches(3.2),
     [("Mode collapse", 22, SERIF, INK, False, False, 0),
      ("After RLHF the model keeps giving the same kind of answer. It moves towards what its raters liked.", 17,
       SANS, INK, False, False, 6),
      ("Bigger model, same effect.", 17, SANS, ACCENT, False, False, 14)])
SCRIPTS[3] = ("P1", 70,
              "How does alignment make it stronger? Through RLHF, the step that made ChatGPT useful. People rank "
              "answers, a reward model learns their taste, and the language model is trained to please that reward "
              "model. This chart is from Kirk and colleagues, a paper our authors cite. The light bars show the model "
              "before RLHF, the green bars show it after. The score measures how different the answers are when you "
              "ask the same question several times. It drops from about 0.8 to between 0.07 and 0.16, so five to "
              "eleven times less variety, and a bigger model doesn't fix it. This is called mode collapse: the model "
              "keeps giving one kind of answer, the kind its raters liked. Over to Presenter 2.")

# 4 - prior work + power: participants + CCAI funnel
s = slide("Asking more people did not change who makes the final call", "Part 2: Why it matters", 4,
          "Peter & Devlin (2025), Prior work, Anthropic (2023), Collective Constitutional AI, Anthropic (2024)")
text(s, M, Inches(2.0), Inches(5.6), Inches(0.35), "Earlier attempts asked the public", 15, SANS, ACCENT, bold=True)
picture(s, "charts/prior_participants.png", M, Inches(2.45), h=Inches(2.85))
text(s, Inches(7.0), Inches(2.0), Inches(5.6), Inches(0.35), "What happened to the public's input", 15, SANS,
     ACCENT, bold=True)
picture(s, "charts/ccai_funnel.png", Inches(7.0), Inches(2.4), h=Inches(3.0))
text(s, M, Inches(5.45), Inches(5.8), Inches(1.1),
     "Foucault: power and knowledge feed each other. Whoever aligns the model decides what counts as \"harmful\".",
     16, SANS, INK, italic=True)
SCRIPTS[4] = ("P2", 65,
              "Thanks. People already tried to fix this by asking the public. On the left: from 44 people in focus "
              "groups up to fifteen thousand people in five countries. The highlighted one is Anthropic's Collective "
              "Constitutional AI. On the right is what happened there. About a thousand Americans cast more than "
              "38,000 votes on 1,127 statements. That became a public constitution of 75 principles. According to "
              "our paper, Anthropic then adopted just one of them in its later models. That's the authors' point: "
              "asking more people does not give them the final say. They use Foucault: power and knowledge feed each "
              "other, so whoever aligns the model decides what counts as harmful or helpful.")

# 5 - three principles + participation spectrum
s = slide("Their fix: context, pluralism and participation", "Part 2: The idea", 5,
          "Peter & Devlin (2025), participation levels after Delgado et al. (2023)")
cols = [("Context", "Align for one use and one group. There is no \"general human\"."),
        ("Pluralism", "Keep disagreement. Don't force one consensus."),
        ("Participation", "The people affected get real control, not just a survey.")]
cw = (W - 2 * M - Inches(0.8)) // 3
x = M
for name, d in cols:
    box(s, x, Inches(2.05), cw, Inches(0.06), fill=ACCENT)
    rich(s, x, Inches(2.25), cw, Inches(1.4), [(name, 24, SERIF, INK), (d, 16, SANS, INK, False, False, 6)])
    x += cw + Inches(0.4)
# spectrum
y0 = Inches(4.75)
levels = ["Consult", "Include", "Collaborate", "Own"]
lw_ = (W - 2 * M) // 4
for i, lv in enumerate(levels):
    shade = [RGBColor(0xE3, 0xEC, 0xE8), RGBColor(0xBF, 0xD6, 0xCD), RGBColor(0x7F, 0xAE, 0x9F), ACCENT][i]
    box(s, M + i * lw_, y0, lw_, Inches(0.5), fill=shade)
    text(s, M + i * lw_, y0, lw_, Inches(0.5), lv, 15, SANS, WHITE if i >= 2 else INK, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, M, Inches(4.25), Inches(8), Inches(0.4), "Who has control? From \"people give input\" -> to \"people decide\"", 14, SANS,
     MUTED)
marks = [(0, "CCAI, PRISM\n(earlier work)"), (2, "Voter chatbot\n(their proposal)"), (3, "Game communities\n(their proposal)")]
for i, lab in marks:
    cx = M + i * lw_ + lw_ // 2
    box(s, cx - Inches(0.09), y0 + Inches(0.58), Inches(0.18), Inches(0.16), fill=INK, shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
    text(s, cx - Inches(1.4), y0 + Inches(0.8), Inches(2.8), Inches(0.7), lab, 13, SANS, INK, align=PP_ALIGN.CENTER)
SCRIPTS[5] = ("P2", 65,
              "Their solution is three requirements. Context: you align a model for one specific use and one group "
              "of people, because there's no general human. Pluralism: people disagree about values, that's normal, "
              "so don't squash it into one answer. And participation: the affected people get real control. The bar "
              "at the bottom goes from 'consult', where you just ask people, to 'own', where people decide. Earlier "
              "projects like PRISM sit at 'consult'. For these cases, the authors put the voter bot near 'collaborate' "
              "and game communities at 'own'. But 'own' is not always best; it depends on the context. This is a "
              "position paper, so there are no experiments. They illustrate the idea with two fictional use cases.")

# 6 - the two cases as mockups
s = slide("Two made-up chatbots, picked to be opposites", "Part 2: How they argue it", 6,
          "Peter & Devlin (2025), use cases, mock-ups made by us")
# voter app mockup
px, py, pw, ph = M, Inches(2.0), Inches(5.6), Inches(3.75)
box(s, px, py, pw, ph, fill=WHITE, line=LINE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, px, py, pw, Inches(0.5), fill=DARK)
text(s, px + Inches(0.25), py, pw, Inches(0.5), "Voter advice chatbot", 14, SANS, WHITE, bold=True,
     anchor=MSO_ANCHOR.MIDDLE)
bubble(s, px + Inches(1.6), py + Inches(0.75), Inches(3.75), "What do parties say about housing?", "user", 14,
       Inches(0.55))
bubble(s, px + Inches(0.25), py + Inches(1.5), Inches(4.4),
       "Party A wants more social housing. Party B wants lower taxes for builders. Party C...", "bot", 14, Inches(0.95))
text(s, px + Inches(0.25), py + Inches(2.55), Inches(5), Inches(0.35), "Sources: party programmes 2026", 12, SANS,
     ACCENT)
text(s, px + Inches(0.25), py + Inches(3.0), pw - Inches(0.5), Inches(0.6),
     "Risk: people already ask ChatGPT how to vote, and it was never built to be neutral.", 13, SANS, MUTED)
# NPC mockup
qx = Inches(6.95)
box(s, qx, py, pw, ph, fill=DARK, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, qx + Inches(0.35), py + Inches(0.4), Inches(0.9), Inches(0.9), fill=ACCENT, shape=MSO_SHAPE.OVAL)
text(s, qx + Inches(0.35), py + Inches(0.4), Inches(0.9), Inches(0.9), "NPC", 14, SANS, WHITE, bold=True,
     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
rich(s, qx + Inches(1.45), py + Inches(0.45), Inches(3.9), Inches(0.9),
     [("Village elder", 15, SANS, WHITE, True), ("one LLM voices every character", 12, SANS, SOFT)])
box(s, qx + Inches(0.35), py + Inches(1.5), pw - Inches(0.7), Inches(1.15), fill=RGBColor(0x2A, 0x3D, 0x38),
    shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, qx + Inches(0.55), py + Inches(1.5), pw - Inches(1.1), Inches(1.15),
     "\"Our people have fished this river for generations. Sit, traveller, I will tell you how.\"", 15, SERIF,
     WHITE, italic=True, anchor=MSO_ANCHOR.MIDDLE)
text(s, qx + Inches(0.35), py + Inches(3.0), pw - Inches(0.7), Inches(0.6),
     "Risk: studios lack diverse teams, so stereotypes of real communities can get worse.", 13, SANS, SOFT)
SCRIPTS[6] = ("P2", 60,
              "Here are the two cases, drawn as mock-ups. On the left, a voter advice chatbot, like a chat version of "
              "StemWijzer. People already ask ChatGPT how to vote, but it was never built to be neutral, so the "
              "power to inform voters moves to private companies. On the right, a character in a video game, where "
              "one language model plays every character. Studios often lack diverse teams, so stereotypes of real "
              "communities risk getting worse. For both, they ask the same three things: what's at stake, who has "
              "the power, and how alignment could fix it. Presenter 3 will show what came out.")

# 7 - three kinds of pluralism (Sorensen et al.)
s = slide("Three ways to answer a question people disagree on", "Part 3: The toolkit", 7,
          "Kinds of pluralism: Sorensen et al. (2024), as used in Peter & Devlin (2025). Example answers written by us.")
bubble(s, M + Inches(3.3), Inches(1.95), Inches(5.3), "Should the Netherlands build more nuclear plants?", "user",
       15, Inches(0.55))
kinds = [("Overton", "One answer that shows all reasonable views.",
          "\"Some parties say yes, for the climate. Others say no, because of cost and waste.\"", "-> Voter chatbot"),
         ("Steerable", "Takes the view you ask for.",
          "\"As a Green voter: no, invest in wind and solar instead.\"", "-> Game characters"),
         ("Distributional", "Answers match how common each view is.",
          "Says yes in 55% of answers and no in 45%.", "-> Rejected for both")]
cw = (W - 2 * M - Inches(0.8)) // 3
x = M
for i, (k, d, ex, use) in enumerate(kinds):
    box(s, x, Inches(2.8), cw, Inches(3.5), fill=WHITE, line=LINE)
    rich(s, x + Inches(0.25), Inches(2.95), cw - Inches(0.5), Inches(3.2),
         [(k, 22, SERIF, INK), (d, 14, SANS, MUTED, False, False, 4), (ex, 15, SANS, INK, False, True, 12)])
    text(s, x + Inches(0.25), Inches(5.7), cw - Inches(0.5), Inches(0.4), use, 15, SANS,
         MUTED if i == 2 else ACCENT, bold=True)
    x += cw + Inches(0.4)
SCRIPTS[7] = ("P3", 45,
              "Thanks. To understand the results you need one more tool: three kinds of pluralism. Take a question "
              "people disagree on: should the Netherlands build more nuclear plants? An Overton answer shows all the "
              "reasonable views in one reply. A steerable answer takes the view you ask for. A distributional model "
              "answers yes or no as often as the population does. The authors pick Overton for the voter chatbot, "
              "steerable for game characters, and reject distributional for both.")

# 8 - result table
s = slide("Same framework, opposite answers", "Part 3: Result", 8, "Adapted from Peter & Devlin (2025), Table 1")
rows = [("", "Voter chatbot", "Game character"),
        ("How to train it", "RLHF: consistent answers for everyone", "SFT + LoRA: an add-on per community"),
        ("Kind of pluralism", "Overton: show a spectrum of party views", "Steerable: true to its own community"),
        ("Who decides", "State, parties and citizens together", "Each community, no global consensus")]
c0 = Inches(3.1)
cw = (W - 2 * M - c0) // 2
y = Inches(2.05)
box(s, M + c0, y - Inches(0.1), cw - Inches(0.15), Inches(3.55), fill=WHITE)
box(s, M + c0 + cw, y - Inches(0.1), cw - Inches(0.15), Inches(3.55), fill=WHITE)
for i, r in enumerate(rows):
    for j, cell in enumerate(r):
        cx = M if j == 0 else M + c0 + (j - 1) * cw + Inches(0.2)
        ww = c0 - Inches(0.2) if j == 0 else cw - Inches(0.55)
        if i == 0:
            text(s, cx, y, ww, Inches(0.5), cell, 22, SERIF, ACCENT)
        else:
            text(s, cx, y, ww, Inches(0.8), cell, 17 if j else 16, SANS, INK if j else MUTED)
    y += Inches(0.65) if i == 0 else Inches(0.95)
box(s, M, Inches(5.85), W - 2 * M, Inches(0.7), fill=TINT)
text(s, M + Inches(0.3), Inches(5.85), W - 2 * M - Inches(0.6), Inches(0.7),
     "Mode collapse can be a bug for game characters and useful for a voter chatbot.", 19, SERIF, INK, italic=True,
     anchor=MSO_ANCHOR.MIDDLE)
SCRIPTS[8] = ("P3", 70,
              "Here is the main result. The same framework gives opposite answers. The voter chatbot gets RLHF, "
              "because every voter should get consistent answers, so here mode collapse may actually help. It also "
              "retrieves from trusted sources, the real party programmes. The game character uses supervised "
              "fine-tuning with LoRA, a small add-on to the base model. It's much cheaper, so a community could train "
              "its own, and take it back if a studio misuses it, although the authors admit many communities still "
              "lack the money and skills. Who decides? For the voter bot, the state, parties and citizens together. "
              "For the game, each community for itself. So mode collapse can be a bug in one case and useful in the "
              "other: there is no one-size-fits-all alignment.")

# 9 - our view + a metric
s = slide("Their proposal is convincing, but still untested", "Part 3: Discussion", 9,
          "Metric example and opinions are ours. Party names are placeholders.")
rich(s, M, Inches(2.0), Inches(5.6), Inches(3.4),
     [("Convincing", 15, SANS, ACCENT, True),
      ("Links ethics to real techniques: RLHF, LoRA, retrieval.", 16, SANS, INK, False, False, 4),
      ("Still open", 15, SANS, ACCENT, True, False, 16),
      ("No experiments. Both cases are made up.", 16, SANS, INK, False, False, 4),
      ("Who speaks for a \"community\"?", 16, SANS, INK, False, False, 4),
      ("A state-run voter bot gives power to governments. Always safer?", 16, SANS, INK, False, False, 4)])
rich(s, Inches(6.9), Inches(2.0), Inches(5.7), Inches(0.9),
     [("How we would measure it", 15, SANS, ACCENT, True),
      ("Overton coverage: which parties' positions does one answer mention?", 16, SANS, INK, False, False, 4)])
picture(s, "charts/overton_metric.png", Inches(6.9), Inches(3.05), w=Inches(5.6))
box(s, M, Inches(5.65), W - 2 * M, Inches(0.8), fill=WHITE, line=LINE)
text(s, M + Inches(0.3), Inches(5.65), W - 2 * M - Inches(0.6), Inches(0.8),
     "Question for you: what else would you measure to know if a voter chatbot is fair?", 19, SERIF, INK,
     anchor=MSO_ANCHOR.MIDDLE)
SCRIPTS[9] = ("P3", 65,
              "What convinced us is that the paper links ethics to real techniques like RLHF, LoRA and retrieval. "
              "What's still open: there are no experiments, both cases are made up. Who speaks for a community? And "
              "our own view: if the state runs the voter chatbot, power moves from companies to governments, and "
              "that's not always safer. The authors say the next step is to test their ideas, which fits today's "
              "lecture on evaluation. Here's how we would start: Overton coverage. Ask the bot a question and count "
              "which parties' positions it mentions. Four out of six is 67 percent. So our question for you: what "
              "else would you measure to know if a voter chatbot is fair? Thank you.")

# 10 - backup
s = slide("Sources", "Backup, not presented", 10)
text(s, M, Inches(2.0), W - 2 * M, Inches(4.5),
     "Peter, O. & Devlin, K. (2025). Decentralising LLM Alignment: A Case for Context, Pluralism, and Participation. "
     "Proceedings of AIES 2025, pp. 1988-1999.\n"
     "Atari, M. et al. (2023). Which Humans? PsyArXiv.\n"
     "Kirk, R. et al. (2024). Understanding the Effects of RLHF on LLM Generalisation and Diversity. ICLR.\n"
     "Huang, S. et al. (2024) and Anthropic (2023). Collective Constitutional AI.\n"
     "Kirk, H. R. et al. (2024). PRISM.\n"
     "Sorensen, T. et al. (2024). A Roadmap to Pluralistic Alignment.\n"
     "Delgado, F. et al. (2023). The Participatory Turn in AI Design.\n\n"
     "GenAI disclosure: we used Claude (Anthropic) and Kimi (Moonshot) to help draft and check slides, charts and "
     "speaker notes. Every number was checked against its source by the group.", 15, SANS, INK, spacing=1.35)
SCRIPTS[10] = ("-", 0, "Not presented. Keep it ready for Q&A.")

tot = sum(v[1] for v in SCRIPTS.values())
if tot > 9 * 60:
    raise ValueError(f"Planned talk is {tot} seconds. Reduce it to 9:00 or less to leave time for transitions.")
for i, sl in enumerate(prs.slides, start=1):
    who, secs, sc = SCRIPTS[i]
    sl.notes_slide.notes_text_frame.text = f"[{who}, about {secs} s]\n{sc}"
prs.save("Group7-v3.pptx")
json.dump(SCRIPTS, open("scripts.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
words = {p: sum(len(v[2].split()) for v in SCRIPTS.values() if v[0] == p) for p in ("P1", "P2", "P3")}
print(f"saved Group7-v3.pptx | planned {tot // 60}:{tot % 60:02d} | words {words} | total {sum(words.values())}")
