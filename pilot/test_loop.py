"""Check the conversation loop of the pilot without a GPU.

It runs pilot.py with the fake model (canned replies) and checks that every stopping case
ends the way DESIGN.md section 5 says, for both ways of writing the final reply.

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

# 6 dialogues x 2 writers x 2 Experts. The fake behaviours cycle per dialogue.
assert len(records) == 24, len(records)
behaviours = ["quick", "followup", "never", "early", "quick", "followup"]

# (number of messages, how it stopped) we expect for each case
EXPECTED = {
    ("beginner", "quick"): (3, "answer_tag"),      # ask, answer, reply
    ("beginner", "followup"): (5, "answer_tag"),   # one follow-up in between
    ("beginner", "never"): (7, "cap"),             # never writes the tag
    ("beginner", "early"): (3, "answer_tag"),      # <answer> in message 1 is ignored
    ("expert", "quick"): (4, "answer_tag"),        # ask, answer, "covers it", reply
    ("expert", "followup"): (6, "answer_tag"),
    ("expert", "never"): (8, "cap"),               # Beginner never agrees, Expert is told to finish
    ("expert", "early"): (4, "answer_tag"),
}

for i, record in enumerate(records):
    behaviour = behaviours[i // 4]
    writer = record["final_writer"]
    case = (writer, behaviour, record["expert_version"])
    agents = [m["agent"] for m in record["messages"]]

    # the Beginner always speaks first, the agents alternate, the writer speaks last
    assert agents[0] == "beginner", case
    assert all(a != b for a, b in zip(agents, agents[1:])), case
    assert agents[-1] == writer, case
    # message 1 quotes the dialogue with the user word for word
    assert record["history"][-1]["text"] in record["messages"][0]["text"], case
    # every conversation ends with a reply, and the reply has no tags in it
    assert record["final_reply"] and "<answer>" not in record["final_reply"], case
    assert (record["n_messages"], record["stop_reason"]) == EXPECTED[(writer, behaviour)], (case, record["n_messages"])

    first = record["messages"][0]
    if behaviour == "early":
        assert first["format_ok"] is False and "<answer>" not in first["text"], case
    else:
        assert first["format_ok"] is True, case
    if (writer, behaviour) == ("beginner", "never"):
        assert record["messages"][-1]["format_ok"] is False, case      # no tag even when told to finish
    if (writer, behaviour) == ("expert", "never"):
        assert record["messages"][-1]["format_ok"] is True, case       # finished when told to

    first_expert_message = record["messages"][1]
    if record["expert_version"] == "B":
        # only the <output> part reaches the Beginner, the steps are kept as hidden
        assert "Step 1" not in first_expert_message["text"] and "Step 1" in first_expert_message["hidden"], case
    else:
        assert first_expert_message["hidden"] == "", case

    assert record["config"]["model"] and record["config"]["max_messages"] in (7, 8), case
    assert record["gold_reviews"] and record["reference_response"], case

domains = [r["domain"] for r in records[::4]]
assert domains.count("hotel") == 3 and domains.count("restaurant") == 3, domains
print(f"OK: {len(records)} conversations checked, all stopping cases behave as designed")
