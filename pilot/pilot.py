# %% [markdown]
# # Pilot: a Beginner and an Expert talk about a user request
#
# This is a small test run for our final project. It is **not** the final notebook.
# It runs 6 dialogues from the DSTC11 Track 5 test split with two versions of the Expert,
# so 12 conversations. We want to see five things (DESIGN.md, section 11):
#
# 1. Do the agents keep their roles?
# 2. Does Expert B keep to its steps and the `<output>` tag?
# 3. Does the Beginner end with the `<answer>` tag, and after how many messages?
# 4. How many seconds does a conversation take?
# 5. How many tokens is the Expert's prompt with all reviews of a place?
#
# **On Kaggle:** turn on the GPU (Settings -> Accelerator -> GPU T4 x2) and the internet, then "Run All".
# It takes a few minutes. At the end there is a summary table and a file `pilot_conversations.jsonl`.

# %%
import json
import os
import random
import re
import subprocess
import time

# ---- settings: our own choices, explained in DESIGN.md ----
N_DIALOGUES = 6                 # half hotel, half restaurant
EXPERT_VERSIONS = ["A", "B"]    # A = direct, B = step by step
MODEL_NAME = "Qwen/Qwen3-1.7B"  # the model of the course notebooks
SEED = 3407                     # same seed as the course notebooks
MAX_MESSAGES = 7                # Beginner, Expert, Beginner, Expert, Beginner, Expert, Beginner
MAX_NEW_TOKENS = {"beginner": 300, "expert_A": 300, "expert_B": 600}
TEMPERATURE, TOP_P, TOP_K = 0.7, 0.8, 20   # the Qwen3 model card's values for non-thinking mode

# Only for testing the loop without a GPU: canned replies in place of the model.
USE_FAKE_MODEL = os.environ.get("PILOT_FAKE") == "1"

# %% [markdown]
# ## Data
# Same repository as in the course notebooks. We use the **test** split, because in this
# repository the train split also contains the validation dialogues.

# %%
ON_KAGGLE = os.path.exists("/kaggle/working")
WORK_DIR = "/kaggle/working" if ON_KAGGLE else os.environ.get("PILOT_WORK_DIR", os.getcwd())
DATA_DIR = os.environ.get("PILOT_DATA_DIR", os.path.join(WORK_DIR, "dstc11-track5", "data"))

if not os.path.exists(DATA_DIR):
    subprocess.run(["git", "clone", "--depth", "1", "https://github.com/lkra/dstc11-track5.git",
                    os.path.join(WORK_DIR, "dstc11-track5")], check=True)

with open(os.path.join(DATA_DIR, "test", "logs.json")) as f:
    logs = json.load(f)            # the dialogues with the user
with open(os.path.join(DATA_DIR, "test", "labels.json")) as f:
    labels = json.load(f)          # reference answer and the relevant review sentences
with open(os.path.join(DATA_DIR, "knowledge.json")) as f:
    knowledge_base = json.load(f)  # all reviews

print(len(logs), "test dialogues loaded")


# %%
def is_usable(label):
    """We use a dialogue if it has a reference answer, its knowledge is reviews only,
    and it is about one hotel or restaurant."""
    if not label.get("target"):
        return False
    knowledge = label["knowledge"]
    if any(k.get("doc_type", "review") != "review" for k in knowledge):
        return False
    places = {(k["domain"], str(k["entity_id"])) for k in knowledge}
    return len(places) == 1


def pick_dialogues(n, seed):
    """Draw n usable dialogues at random, half hotel and half restaurant."""
    rng = random.Random(seed)
    by_domain = {"hotel": [], "restaurant": []}
    for i, label in enumerate(labels):
        if is_usable(label):
            domain = label["knowledge"][0]["domain"]
            if domain in by_domain:
                by_domain[domain].append(i)
    n_restaurant = n // 2
    picked = rng.sample(by_domain["hotel"], n - n_restaurant) + rng.sample(by_domain["restaurant"], n_restaurant)
    return sorted(picked)


def place_reviews(domain, entity_id):
    """The name of the place and all its reviews as text. This is what the Expert gets."""
    place = knowledge_base[domain][str(entity_id)]
    lines = []
    for n, review in enumerate(place["reviews"].values(), 1):
        lines.append(f"Review {n}: " + " ".join(review["sentences"].values()))
    return place["name"], "\n".join(lines)


def gold_review_sentences(label):
    """The review sentences the dataset marks as relevant (like knowledge2sources in Notebook 4).
    The agents never see these. We keep them for the evaluation."""
    sentences = []
    for k in label["knowledge"]:
        review = knowledge_base[k["domain"]][str(k["entity_id"])]["reviews"][str(k["doc_id"])]
        sentences.append(review["sentences"][str(k["sent_id"])])
    return sentences


def format_history(history):
    """The dialogue with the user as plain text."""
    return "\n".join(("User: " if turn["speaker"] == "U" else "Assistant: ") + turn["text"] for turn in history)


# %% [markdown]
# ## The prompts
# The Beginner does not get the reviews. The Expert does. Expert A and Expert B get the same
# reviews and differ only in how they are told to work.

# %%
BEGINNER_SYSTEM = """You are a new assistant at a booking service for hotels and restaurants.
A user asked something you cannot answer yourself, because you have not read the customer reviews.
You are talking to an Expert colleague who has read them. The user does not see this conversation.

How to work:
1. First, ask the Expert what you need to know to answer the user's last message. One or two sentences. Do not answer the user yet.
2. When the Expert has answered, check that it covers what the user asked. If something is missing, ask one short follow-up question.
3. When you know enough, write the reply for the user between <answer> and </answer>. Use only what the Expert told you. One to three sentences.

Never invent facts about the place."""

EXPERT_A_SYSTEM = """You are an Expert assistant at a booking service. You have read all customer reviews of {name}.
A Beginner colleague asks you for help with a user request. The user does not see this conversation.

Customer reviews of {name}:
{reviews}

Answer the Beginner's question using only these reviews. Say what the reviewers think about the thing the user asks about, and say so if their opinions differ. If the reviews do not mention it, say that. Two or three sentences. Do not write the reply for the user, the Beginner does that."""

EXPERT_B_SYSTEM = """You are an Expert assistant at a booking service. You have read all customer reviews of {name}.
A Beginner colleague asks you for help with a user request. The user does not see this conversation.

Customer reviews of {name}:
{reviews}

Work in steps before you answer:
Step 1: Name the thing the user asks about.
Step 2: Copy every review sentence that is about it. After each one write (positive) or (negative).
Step 3: Count the positive and the negative sentences.

Then write your answer to the Beginner between <output> and </output>. Use only these reviews. Say what the reviewers think, and say so if their opinions differ. If the reviews do not mention it, say that. Two or three sentences. Do not write the reply for the user, the Beginner does that."""

# %% [markdown]
# ## The model
# Qwen3-1.7B with thinking switched off, as in the course notebooks.

# %%
if not USE_FAKE_MODEL:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    torch.manual_seed(SEED)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype="auto", device_map="auto")


def model_generate(messages, max_new_tokens):
    """One model call. Returns the text, the number of new tokens, and the number of prompt tokens."""
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True,
                                         enable_thinking=False)
    inputs = tokenizer([text], return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True,
                                temperature=TEMPERATURE, top_p=TOP_P, top_k=TOP_K)
    new_ids = output[0][inputs.input_ids.shape[1]:]
    return tokenizer.decode(new_ids, skip_special_tokens=True).strip(), len(new_ids), inputs.input_ids.shape[1]


# %%
# ---- only for testing without a GPU ----
FAKE_BEHAVIOUR = "quick"   # "quick", "followup", "never" or "early"; set per conversation in the test


def fake_generate(messages, max_new_tokens):
    """Canned replies that follow the same format as the real model. Lets us test the loop."""
    system, last = messages[0]["content"], messages[-1]["content"]
    own_messages = sum(m["role"] == "assistant" for m in messages)
    n_prompt = sum(len(m["content"].split()) for m in messages)
    if system.startswith("You are a new assistant"):          # the Beginner
        if own_messages == 0:
            text = "The user asks about the wifi. What do the reviews say about it?"
            if FAKE_BEHAVIOUR == "early":
                text += " <answer>The wifi is great.</answer>"
        elif "last message" in last:
            text = "<answer>Guests are split about the wifi.</answer>" if FAKE_BEHAVIOUR != "never" else "I am not sure."
        elif FAKE_BEHAVIOUR == "never" or (FAKE_BEHAVIOUR == "followup" and own_messages == 1):
            text = "Is it also free?"
        else:
            text = "Thanks. <answer>Most guests say the wifi is fast, one found it slow.</answer>"
    elif "Work in steps" in system:                           # Expert B
        text = ("Step 1: wifi.\nStep 2: \"Fast wifi.\" (positive) \"Slow wifi.\" (negative)\n"
                "Step 3: 1 positive, 1 negative.\n<output>Reviewers are split on the wifi.</output>")
    else:                                                     # Expert A
        text = "Most reviewers say the wifi is fast, one says it is slow."
    return text, len(text.split()), n_prompt


generate = fake_generate if USE_FAKE_MODEL else model_generate

# %% [markdown]
# ## One conversation
# The Beginner speaks first. Code puts the dialogue with the user into message 1 word for word,
# and the Beginner model adds its question. Then Expert and Beginner take turns.
#
# **Stopping.** After every Beginner message, code looks for `<answer>...</answer>`. If it is there,
# the conversation stops and the text inside is the final reply. The 7th message is the last one
# allowed: the Beginner is told to write the reply now, and the conversation is marked "cap".

# %%
ANSWER_TAG = re.compile(r"<answer>(.*?)</answer>", re.DOTALL)
OUTPUT_TAG = re.compile(r"<output>(.*?)</output>", re.DOTALL)


def run_conversation(history, entity_name, reviews_text, expert_version):
    quoted = format_history(history)
    expert_system = EXPERT_A_SYSTEM if expert_version == "A" else EXPERT_B_SYSTEM

    # Each agent has its own view of the conversation: its own messages are "assistant",
    # the other agent's messages are "user".
    beginner_view = [
        {"role": "system", "content": BEGINNER_SYSTEM},
        {"role": "user", "content": f"Dialogue with the user:\n{quoted}\n\nWrite your question to the Expert."},
    ]
    expert_view = [{"role": "system", "content": expert_system.format(name=entity_name, reviews=reviews_text)}]

    messages = []               # what we save: one entry per message
    final_reply, stop_reason, expert_prompt_tokens = "", None, 0

    while stop_reason is None:
        # ---------- Beginner ----------
        is_first = len(messages) == 0
        is_last_allowed = len(messages) == MAX_MESSAGES - 1
        if is_last_allowed:
            beginner_view[-1]["content"] += ("\n\nThis is your last message. Write the reply for the user now, "
                                             "between <answer> and </answer>.")
        start = time.time()
        text, new_tokens, _ = generate(beginner_view, MAX_NEW_TOKENS["beginner"])
        seconds = time.time() - start
        beginner_view.append({"role": "assistant", "content": text})
        answer = ANSWER_TAG.search(text)

        if is_first:
            # An answer before the Expert has said anything does not count. We cut it out.
            question = ANSWER_TAG.sub("", text).strip() or "What do the reviews say about this?"
            shown = f"Here is my conversation with the user:\n{quoted}\n\n{question}"
            format_ok = answer is None
        else:
            shown, format_ok = text, True
        messages.append({"n": len(messages) + 1, "agent": "beginner", "text": shown, "hidden": "",
                         "new_tokens": new_tokens, "seconds": round(seconds, 2), "format_ok": format_ok})

        if answer and not is_first:
            final_reply = answer.group(1).strip()
            stop_reason = "cap" if is_last_allowed else "answer_tag"
            break
        if is_last_allowed:
            # Still no tag in the last message: we take the whole message as the reply.
            final_reply = text.replace("<answer>", "").replace("</answer>", "").strip()
            messages[-1]["format_ok"] = False
            stop_reason = "cap"
            break

        # ---------- Expert ----------
        expert_view.append({"role": "user", "content": shown})
        start = time.time()
        text, new_tokens, prompt_tokens = generate(expert_view, MAX_NEW_TOKENS["expert_" + expert_version])
        seconds = time.time() - start
        expert_view.append({"role": "assistant", "content": text})
        expert_prompt_tokens = max(expert_prompt_tokens, prompt_tokens)

        visible, hidden, format_ok = text, "", True
        if expert_version == "B":
            # Only the part inside <output> goes to the Beginner. The steps stay hidden but are counted.
            output = OUTPUT_TAG.search(text)
            if output:
                visible, hidden = output.group(1).strip(), OUTPUT_TAG.sub("", text).strip()
            else:
                format_ok = False       # no tag: the Beginner gets the whole message
        messages.append({"n": len(messages) + 1, "agent": "expert", "text": visible, "hidden": hidden,
                         "new_tokens": new_tokens, "seconds": round(seconds, 2), "format_ok": format_ok})
        beginner_view.append({"role": "user", "content": "Expert: " + visible})

    return {
        "expert_version": expert_version,
        "messages": messages,
        "final_reply": final_reply,
        "stop_reason": stop_reason,
        "n_messages": len(messages),
        "n_new_tokens": sum(m["new_tokens"] for m in messages),
        "seconds": round(sum(m["seconds"] for m in messages), 2),
        "expert_prompt_tokens": expert_prompt_tokens,
    }


# %% [markdown]
# ## Run the pilot

# %%
def print_conversation(record):
    print("=" * 100)
    print(f"dialogue {record['dialogue_id']} | {record['domain']} | {record['entity_name']} | Expert {record['expert_version']}")
    print("USER ASKED:", record["history"][-1]["text"])
    for m in record["messages"]:
        flag = "" if m["format_ok"] else "   [FORMAT PROBLEM]"
        print(f"\n--- message {m['n']}, {m['agent']}, {m['new_tokens']} tokens, {m['seconds']} s{flag}")
        # message 1 starts with the quoted dialogue, which we do not print again
        print(m["text"].split("\n\n")[-1] if m["n"] == 1 else m["text"])
        if m["hidden"]:
            print("   (hidden steps) " + m["hidden"].replace("\n", "\n   "))
    print(f"\nFINAL REPLY ({record['stop_reason']}):", record["final_reply"])
    print("REFERENCE ANSWER:", record["reference_response"])
    print("RELEVANT REVIEW SENTENCES:", record["gold_reviews"])


records = []
picked = pick_dialogues(N_DIALOGUES, SEED)
fake_behaviours = ["quick", "followup", "never", "early"]
for position, dialogue_id in enumerate(picked):
    label, history = labels[dialogue_id], logs[dialogue_id]
    place = label["knowledge"][0]
    entity_name, reviews_text = place_reviews(place["domain"], place["entity_id"])
    for expert_version in EXPERT_VERSIONS:
        FAKE_BEHAVIOUR = fake_behaviours[position % len(fake_behaviours)]   # only used by the fake model
        record = run_conversation(history, entity_name, reviews_text, expert_version)
        record.update({
            "dialogue_id": dialogue_id,
            "domain": place["domain"],
            "entity_id": str(place["entity_id"]),
            "entity_name": entity_name,
            "history": history,
            "gold_reviews": gold_review_sentences(label),
            "reference_response": label["response"],
        })
        records.append(record)
        print_conversation(record)

# %% [markdown]
# ## Summary
# One line per Expert version. "format problems" counts messages where a tag was missing or
# came too early.

# %%
out_path = os.path.join(WORK_DIR, "pilot_conversations.jsonl")
with open(out_path, "w") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

print(f"{'Expert':8}{'convs':>7}{'messages':>10}{'new tokens':>12}{'seconds':>9}{'ended by tag':>14}{'by cap':>8}"
      f"{'format problems':>17}{'Expert prompt tokens':>22}")
for expert_version in EXPERT_VERSIONS:
    rows = [r for r in records if r["expert_version"] == expert_version]
    n = len(rows)
    print(f"{expert_version:8}{n:>7}"
          f"{sum(r['n_messages'] for r in rows) / n:>10.1f}"
          f"{sum(r['n_new_tokens'] for r in rows) / n:>12.0f}"
          f"{sum(r['seconds'] for r in rows) / n:>9.1f}"
          f"{sum(r['stop_reason'] == 'answer_tag' for r in rows):>14}"
          f"{sum(r['stop_reason'] == 'cap' for r in rows):>8}"
          f"{sum(not m['format_ok'] for r in rows for m in r['messages']):>17}"
          f"{sum(r['expert_prompt_tokens'] for r in rows) / n:>22.0f}")
print("\nsaved:", out_path)

# %% [markdown]
# ## What to send back
# The file `pilot_conversations.jsonl` (on Kaggle: Output -> /kaggle/working), or this notebook
# saved with its outputs. Put it in the repo under `results/pilot/`.
