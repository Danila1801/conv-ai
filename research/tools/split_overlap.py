"""Check whether the splits in the course's data repo overlap.

Usage: python3 -I split_overlap.py <path to dstc11-track5/data>
An instance is identified by its full dialogue text (all turns, in order).
"""
import json
import sys
from pathlib import Path

root = Path(sys.argv[1])


def load(split, name="logs.json"):
    logs = json.load(open(root / split / name))
    return logs


def key(d):
    return tuple((t["speaker"], t["text"]) for t in d)


def targets(split):
    logs = load(split)
    labels = json.load(open(root / split / "labels.json"))
    all_keys = [key(d) for d in logs]
    tgt_keys = [k for k, l in zip(all_keys, labels) if l.get("target")]
    return all_keys, tgt_keys


data = {s: targets(s) for s in ["train", "val", "test"]}
for s, (a, t) in data.items():
    print(f"{s}: instances={len(a)} unique={len(set(a))} | target instances={len(t)} unique={len(set(t))}")

for a_name, b_name in [("val", "train"), ("test", "train"), ("test", "val")]:
    a_all, a_t = data[a_name]
    b_all, b_t = data[b_name]
    b_set, b_tset = set(b_all), set(b_t)
    n_all = sum(1 for k in a_all if k in b_set)
    n_t = sum(1 for k in a_t if k in b_tset)
    print(f"{a_name} instances also in {b_name}: {n_all} of {len(a_all)} | target instances: {n_t} of {len(a_t)}")

# where do the val instances sit inside train?
train_all = data["train"][0]
val_set = set(data["val"][0])
pos = [i for i, k in enumerate(train_all) if k in val_set]
if pos:
    print(f"val instances inside train: first index={pos[0]} last index={pos[-1]} "
          f"contiguous block={'yes' if pos[-1] - pos[0] + 1 == len(pos) else 'no'}")

# backup file
bkp = root / "train" / "logs_bkp.json"
if bkp.exists():
    b = json.load(open(bkp))
    bk = [key(d) for d in b]
    print(f"train/logs_bkp.json: instances={len(bk)} | val instances inside it: {sum(1 for k in bk if k in val_set)}")
bdir = root / "train" / "bkp"
if bdir.exists():
    for f in sorted(bdir.iterdir()):
        try:
            j = json.load(open(f))
            n_t = sum(1 for x in j if isinstance(x, dict) and x.get("target")) if j and isinstance(j[0], dict) else "-"
            print(f"train/bkp/{f.name}: items={len(j)} target=True: {n_t}")
        except Exception as e:
            print(f"train/bkp/{f.name}: could not read ({type(e).__name__})")

# does the first-100 slice the notebooks use touch val?
first = [k for k in train_all[:400]]
print("of the first 400 train instances, in val:", sum(1 for k in first if k in val_set))
