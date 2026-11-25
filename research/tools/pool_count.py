"""Count how many instances could serve as agent-agent conversation seeds.

Usage: python3 -I pool_count.py <path to dstc11-track5/data>
A "seed" = a knowledge-seeking instance (target=True) whose gold knowledge is review sentences only.
"""
import json
import sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1])
for split in ["train", "val", "test"]:
    logs = json.load(open(root / split / "logs.json"))
    labels = json.load(open(root / split / "labels.json"))
    pool = Counter()
    n_rev_bins = Counter()
    for d, l in zip(logs, labels):
        if not l.get("target"):
            continue
        ks = l["knowledge"]
        types = {k.get("doc_type", "review") for k in ks}
        ents = {(k["domain"], k["entity_id"]) for k in ks}
        if types != {"review"}:
            continue
        dom = "+".join(sorted({e[0] for e in ents}))
        key = ("single-entity" if len(ents) == 1 else "multi-entity", dom)
        pool[key] += 1
        if len(ents) == 1:
            n = len(ks)
            n_rev_bins["1" if n == 1 else "2-3" if n <= 3 else "4-6" if n <= 6 else "7+"] += 1
    print(split, "review-only target instances:", sum(pool.values()))
    for k, v in sorted(pool.items()):
        print("   ", k, v)
    print("    single-entity, by number of gold review sentences:", dict(sorted(n_rev_bins.items())))
