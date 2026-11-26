"""Measure the DSTC11 Track 5 data the course notebooks use.

Usage: python3 -I inspect_data.py <path to dstc11-track5/data>
Reads only JSON. Prints counts; writes nothing.
"""
import json
import statistics as st
import sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1])


def q(xs):
    xs = sorted(xs)
    n = len(xs)
    if n == 0:
        return "n=0"
    return (f"n={n} min={xs[0]} q1={xs[n // 4]} median={st.median(xs)} "
            f"q3={xs[(3 * n) // 4]} max={xs[-1]} mean={st.mean(xs):.2f}")


kb = json.load(open(root / "knowledge.json"))
print("== knowledge.json ==")
for dom, ents in kb.items():
    n_rev = [len(e.get("reviews") or {}) for e in ents.values()]
    n_sent = [sum(len(r["sentences"]) for r in (e.get("reviews") or {}).values()) for e in ents.values()]
    n_faq = [len(e.get("faqs") or {}) for e in ents.values()]
    print(f"domain={dom}: entities={len(ents)} reviews total={sum(n_rev)} "
          f"review sentences total={sum(n_sent)} faqs total={sum(n_faq)}")
    print("   reviews per entity:", q(n_rev))
    print("   review sentences per entity:", q(n_sent))
    print("   faqs per entity:", q(n_faq))
    ex = next(iter(ents.values()))
    r0 = next(iter((ex.get("reviews") or {}).values()), None)
    print("   example entity keys:", list(ex.keys()), "| name:", ex.get("name"))
    if r0:
        print("   example review keys:", list(r0.keys()), "| metadata:", r0.get("metadata"))

for split in ["train", "val", "test"]:
    logs = json.load(open(root / split / "logs.json"))
    labels = json.load(open(root / split / "labels.json"))
    print(f"\n== {split} ==")
    print("instances:", len(logs), "| labels:", len(labels))
    target = [l for l in labels if l.get("target")]
    with_resp = [l for l in labels if "response" in l]
    print("target=True:", len(target), "| with response:", len(with_resp))
    turns_all = [len(d) for d in logs]
    print("turns per instance (all):", q(turns_all))
    turns_t = [len(d) for d, l in zip(logs, labels) if l.get("target")]
    print("turns per instance (target):", q(turns_t))
    last_speaker = Counter(d[-1]["speaker"] for d in logs)
    print("last speaker:", dict(last_speaker))
    words_t = [sum(len(t["text"].split()) for t in d) for d, l in zip(logs, labels) if l.get("target")]
    print("words in dialogue history (target):", q(words_t))
    n_k, n_rev_sent, n_faq, doms, n_ent, only_review, only_faq, mixed = [], [], [], Counter(), [], 0, 0, 0
    missing = 0
    for l in target:
        ks = l.get("knowledge", [])
        n_k.append(len(ks))
        types = Counter(k.get("doc_type", "review") for k in ks)
        n_rev_sent.append(types.get("review", 0))
        n_faq.append(types.get("faq", 0))
        if types.get("review") and not types.get("faq"):
            only_review += 1
        elif types.get("faq") and not types.get("review"):
            only_faq += 1
        elif types.get("faq") and types.get("review"):
            mixed += 1
        ents = {(k["domain"], str(k["entity_id"])) for k in ks}
        n_ent.append(len(ents))
        for d, _ in ents:
            doms[d] += 1
        for k in ks:
            try:
                e = kb[str(k["domain"])][str(k["entity_id"])]
                if k.get("doc_type", "review") == "review":
                    e["reviews"][str(k["doc_id"])]["sentences"][str(k["sent_id"])]
                else:
                    e["faqs"][str(k["doc_id"])]
            except Exception:
                missing += 1
    print("knowledge snippets per target instance:", q(n_k))
    print("  review sentences per target instance:", q(n_rev_sent))
    print("  faq items per target instance:", q(n_faq))
    print(f"  only reviews={only_review} only faqs={only_faq} both={mixed}")
    print("entities per target instance:", dict(Counter(n_ent)))
    print("domains (entity mentions):", dict(doms))
    print("knowledge references not found in knowledge.json:", missing)
    resp_words = [len(l["response"].split()) for l in with_resp]
    print("reference response length in words:", q(resp_words))
    # first target example
    for d, l in zip(logs, labels):
        if l.get("target") and any(k.get("doc_type") == "review" for k in l["knowledge"]):
            print("example last user turn:", d[-1]["text"])
            print("example response:", l["response"])
            print("example knowledge refs:", l["knowledge"][:3], "... total", len(l["knowledge"]))
            break
