"""Check the conversation loop of the pilot without a GPU.

It runs pilot.py with the fake model (canned replies) and checks that every stopping case
ends the way DESIGN.md section 5 says.

Usage:
    python pilot/test_loop.py <path to dstc11-track5/data>
"""
import json
import os
import subprocess
import sys
import tempfile

data_dir = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
work_dir = tempfile.mkdtemp()
env = dict(os.environ, PILOT_FAKE="1", PILOT_DATA_DIR=data_dir, PILOT_WORK_DIR=work_dir)
run = subprocess.run([sys.executable, os.path.join(here, "pilot.py")], env=env, capture_output=True, text=True)
assert run.returncode == 0, run.stderr[-2000:]

with open(os.path.join(work_dir, "pilot_conversations.jsonl")) as f:
    records = [json.loads(line) for line in f]

# 6 dialogues x 2 Experts. The fake behaviours cycle: quick, followup, never, early, quick, followup.
assert len(records) == 12, len(records)
expected = ["quick", "followup", "never", "early", "quick", "followup"]
checks = 0
for i, record in enumerate(records):
    behaviour = expected[i // 2]
    agents = [m["agent"] for m in record["messages"]]
    # agents always alternate, the Beginner speaks first and last
    assert agents[0] == "beginner" and agents[-1] == "beginner", agents
    assert all(a != b for a, b in zip(agents, agents[1:])), agents
    assert record["n_messages"] <= 7
    assert record["final_reply"], "every conversation must end with a reply"
    assert "<answer>" not in record["final_reply"]
    # message 1 quotes the dialogue with the user word for word
    assert record["history"][-1]["text"] in record["messages"][0]["text"]
    if behaviour == "quick":
        assert (record["n_messages"], record["stop_reason"]) == (3, "answer_tag"), record["n_messages"]
    if behaviour == "followup":
        assert (record["n_messages"], record["stop_reason"]) == (5, "answer_tag"), record["n_messages"]
    if behaviour == "never":
        # never writes the tag: stopped at message 7, marked as cap, last message flagged
        assert (record["n_messages"], record["stop_reason"]) == (7, "cap"), record["n_messages"]
        assert record["messages"][-1]["format_ok"] is False
    if behaviour == "early":
        # an <answer> in message 1 is cut out and flagged, the conversation goes on
        assert record["messages"][0]["format_ok"] is False
        assert "<answer>" not in record["messages"][0]["text"]
        assert record["n_messages"] == 3
    if record["expert_version"] == "B":
        # only the <output> part reaches the Beginner, the steps are kept as hidden
        expert = record["messages"][1]
        assert "Step 1" not in expert["text"] and "Step 1" in expert["hidden"], expert
    else:
        assert record["messages"][1]["hidden"] == ""
    assert record["gold_reviews"] and record["reference_response"]
    checks += 1

domains = [r["domain"] for r in records[::2]]
assert domains.count("hotel") == 3 and domains.count("restaurant") == 3, domains
print(f"OK: {checks} conversations checked, all stopping cases behave as designed")
