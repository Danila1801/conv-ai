"""Find on which page (= slide) of a lecture PDF a phrase appears.

Usage: python3 -I find_in_slides.py <pdf> <phrase> [<phrase> ...]
Uses pdftotext. Prints page number and a short piece of the text around the phrase.
"""
import re
import subprocess
import sys

pdf, phrases = sys.argv[1], sys.argv[2:]
text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
pages = text.split("\f")
print(f"== {pdf.split('/')[-1]}: {len(pages) - 1} pages")
for phrase in phrases:
    hits = []
    for n, page in enumerate(pages, 1):
        flat = re.sub(r"\s+", " ", page)
        m = re.search(re.escape(phrase), flat, re.IGNORECASE)
        if m:
            start = max(0, m.start() - 60)
            hits.append((n, flat[start:m.end() + 110].strip()))
    if not hits:
        print(f"  [{phrase}] not found")
    for n, snippet in hits[:3]:
        print(f"  [{phrase}] p.{n}: {snippet}")
    if len(hits) > 3:
        print(f"  [{phrase}] also on pages {[n for n, _ in hits[3:]]}")
