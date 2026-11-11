"""Turn the 'slides + notes' printout into a clean projector deck.

The source PDF pages are 4K images: a small slide on top, speaker notes below.
This crops the slide out at full resolution, fixes the placeholders, and writes
Group7-slides.pdf (16:9, one slide per page) for the projector.
Run: python build_slides.py
"""
import io
import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont

SRC = "Decentralising LLM Alignment - Group 7 (1).pdf"
OUT = "Group7-slides.pdf"
CLIP = fitz.Rect(288, 32, 672, 248)  # slide area on the printout page (points)
SCALE = 10                            # 384 pt * 10 = 3840 px wide

NAMES = "Presented by Antonia Bulai, Danila Popusoi and Goktug Yildirim"
DISCLOSURE = ("GenAI disclosure: we used Claude (Anthropic) to help outline and draft these slides "
              "and speaker notes. All content was checked against the paper by the group.")


def font(size_px, bold=False):
    for name in (["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]):
        try:
            return ImageFont.truetype(name, size_px)
        except OSError:
            pass
    return ImageFont.load_default()


def px(rect_pts):
    """Page points -> pixel box inside the cropped slide image."""
    return [int((rect_pts[0] - CLIP.x0) * SCALE), int((rect_pts[1] - CLIP.y0) * SCALE),
            int((rect_pts[2] - CLIP.x0) * SCALE), int((rect_pts[3] - CLIP.y0) * SCALE)]


def patch(img, box_pts, text, size_pts, wrap_at=None):
    x0, y0, x1, y1 = px(box_pts)
    bg = img.getpixel((max(x0 - 6, 0), y0 + 2))
    fg = darkest_or_lightest(img, x0, y0, x1, y1, bg)
    d = ImageDraw.Draw(img)
    d.rectangle([x0 - 4, y0 - 4, x1 + 4, y1 + 4], fill=bg)
    f = font(int(size_pts * SCALE))
    lines = [text] if not wrap_at else wrap(text, f, wrap_at, d)
    lh = int(size_pts * SCALE * 1.45)
    for i, ln in enumerate(lines):
        d.text((x0, y0 - int(size_pts * SCALE * 0.15) + i * lh), ln, fill=fg, font=f)


def darkest_or_lightest(img, x0, y0, x1, y1, bg):
    """Pick the existing text colour: the pixel in the box furthest from the background."""
    best, dist = bg, -1
    for x in range(x0, x1, 7):
        for y in range(y0, y1, 3):
            c = img.getpixel((x, y))
            dd = sum(abs(a - b) for a, b in zip(c[:3], bg[:3]))
            if dd > dist:
                best, dist = c, dd
    return best


def wrap(text, f, width_px, d):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > width_px and cur:
            out.append(cur)
            cur = w
        else:
            cur = t
    out.append(cur)
    return out


def main():
    src = fitz.open(SRC)
    out = fitz.open()
    for i, page in enumerate(src):
        pm = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=CLIP)
        img = Image.open(io.BytesIO(pm.tobytes("png"))).convert("RGB")
        if i == 0:
            patch(img, (313.6, 215.4, 470, 221.0), NAMES, 5.63)
        if i == 13:
            box = (319.19, 139.8, 640, 152.0)
            patch(img, box, DISCLOSURE, 4.9, wrap_at=(640 - 319.19) * SCALE)
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=92)
        pg = out.new_page(width=960, height=540)
        pg.insert_image(pg.rect, stream=buf.getvalue())
    out.save(OUT, deflate=True)
    print("wrote", OUT, len(out), "slides")


if __name__ == "__main__":
    main()
