# %% [markdown]
# # Pilot: a Beginner and an Expert talk about a user request
#
# This is a small test run for our final project. It is **not** the final notebook.
# It runs 6 dialogues from the DSTC11 Track 5 test split. Each dialogue is run four times:
# with Expert A and Expert B, and with two ways of ending the conversation. So 24 conversations.
#
# We want to see six things (DESIGN.md, section 11):
#
# 1. Do the agents keep their roles?
# 2. Does Expert B keep to its steps and the `<output>` tag?
# 3. Does the conversation end with the `<answer>` tag, and after how many messages?
# 4. How many seconds does a conversation take?
# 5. How many tokens is the Expert's prompt with all reviews of a place?
# 6. Which ending gives the better final reply: the Beginner writes it, or the Expert writes it
#    after the Beginner says the answer covers the request?
#
# **On Kaggle:** the account has to be phone verified. Then turn on the GPU
# (Settings -> Accelerator -> GPU T4 x2) and the internet (right panel), and press "Run All".
# At the end there is a summary table and a file `pilot_conversations.jsonl`.

# %%
import json
import os
import random
import re
import subprocess
import time

# ---- settings: our own choices, explained in DESIGN.md ----
N_DIALOGUES = 6                     # half hotel, half restaurant
MODEL_NAME = "Qwen/Qwen3-1.7B"      # the model of the course notebooks
SEED = 3407                         # same seed as the course notebooks
TEMPERATURE, TOP_P, TOP_K = 0.7, 0.8, 20   # the Qwen3 model card's values for non-thinking mode

# Who writes the reply for the user. We test both and decide after the pilot.
FINAL_WRITERS = ["beginner", "expert"]
# The last message has to come from the writer, so the cap differs by one.
MAX_MESSAGES = {"beginner": 7, "expert": 8}
# The writer may only finish after the other agent has spoken at least once in reply.
FIRST_MESSAGE_THAT_MAY_FINISH = {"beginner": 3, "expert": 4}

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
# Each prompt has a fixed part (who the agent is) and a part that depends on who writes the final reply.
#
# - The Beginner never gets the reviews. Its prompt is the same for Expert A and Expert B.
# - Expert A and Expert B get the same reviews. They differ only in how they are told to work:
#   A answers directly, B works in steps first (chain-of-thought, as in Notebook 4).

# %%
BEGINNER_ROLE = """You are a new assistant at a booking service for hotels and restaurants.
A user asked something you cannot answer yourself, because you have not read the customer reviews.
You are talking to an Expert colleague who has read them. The user does not see this conversation.
Never invent facts about the place."""

BEGINNER_STEPS = {
    "beginner": """How to work:
1. First, say in one sentence what the user wants, and ask the Expert what you need to know. Do not answer the user yet.
2. When the Expert has answered, check that it covers what the user asked. If something is missing, ask one short follow-up question.
3. When you know enough, write the reply for the user between <answer> and </answer>. Use only what the Expert told you. One to three sentences.""",
    "expert": """How to work:
1. First, say in one sentence what the user wants, and ask the Expert what you need to know.
2. When the Expert has answered, check that it covers what the user asked. If something is missing, ask one short follow-up question.
3. When the Expert's answer covers everything, say so in one short sentence, so the Expert can write the reply for the user.
You never write the reply for the user yourself.""",
}

EXPERT_ROLE = """You are an Expert assistant at a booking service. You have read all customer reviews of {name}.
A Beginner colleague asks you for help with a user request. The user does not see this conversation.

Customer reviews of {name}:
{reviews}"""

EXPERT_STYLE = {
    # Expert A: direct (zero-shot)
    "A": """Answer the Beginner's question using only these reviews. Say what the reviewers think about the thing the user asks about, and say so if their opinions differ. If the reviews do not mention it, say that. Two or three sentences.""",
    # Expert B: step by step (chain-of-thought with tags)
    "B": """Work in steps before you answer the Beginner's question:
Step 1: Name the thing the user asks about.
Step 2: Copy every review sentence that is about it. After each one write (positive) or (negative).
Step 3: Count the positive and the negative sentences.
Then write your answer to the Beginner between <output> and </output>. Use only these reviews. Say what the reviewers think, and say so if their opinions differ. If the reviews do not mention it, say that. Two or three sentences.""",
}

EXPERT_ENDING = {
    "beginner": "Do not write the reply for the user, the Beginner does that.",
    "expert": "When the Beginner says your answer covers the user's question, write the reply for the user between <answer> and </answer>. One to three sentences, only from the reviews. Not before.",
}

# Everything that differs between the two Expert versions is in this table.
EXPERT_CONFIG = {
    "A": {"max_new_tokens": 300, "uses_output_tag": False},
    "B": {"max_new_tokens": 600, "uses_output_tag": True},
}
BEGINNER_MAX_NEW_TOKENS = 300

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
FAKE_BEHAVIOUR = "quick"   # "quick", "followup", "never" or "early"; set per dialogue in the run below


def fake_generate(messages, max_new_tokens):
    """Canned replies in the same format as the real model. Lets us test the loop."""
    system, last = messages[0]["content"], messages[-1]["content"]
    own_messages = sum(m["role"] == "assistant" for m in messages)
    n_prompt = sum(len(m["content"].split()) for m in messages)
    forced = "last message" in last
    if system.startswith("You are a new assistant"):                      # the Beginner
        writes_reply = "You never write the reply" not in system
        if own_messages == 0:
            text = "The user wants to know if the wifi is good. What do the reviews say about it?"
            if FAKE_BEHAVIOUR == "early":
                text += " <answer>The wifi is great.</answer>"
        elif FAKE_BEHAVIOUR == "never" or (FAKE_BEHAVIOUR == "followup" and own_messages == 1):
            text = "I am not sure." if forced else "Is it also free?"
        elif writes_reply:
            text = "Thanks. <answer>Most guests say the wifi is fast, one found it slow.</answer>"
        else:
            text = "That covers it."
    else:                                                                  # the Expert
        if "Not before." in system and ("covers it" in last or forced):
            text = "<answer>Most guests say the wifi is fast, one found it slow.</answer>"
        elif "Work in steps" in system:
            text = ("Step 1: wifi.\nStep 2: \"Fast wifi.\" (positive) \"Slow wifi.\" (negative)\n"
                    "Step 3: 1 positive, 1 negative.\n<output>Reviewers are split on the wifi.</output>")
        else:
            text = "Most reviewers say the wifi is fast, one says it is slow."
    return text, len(text.split()), n_prompt


generate = fake_generate if USE_FAKE_MODEL else model_generate

# %% [markdown]
# ## The agents and one conversation
# Both agents are the same small class. An agent keeps its own view of the conversation:
# what it said itself is "assistant", what it is told is "user". The only differences between
# the Beginner and the Expert are the system prompt and the token limit.
#
# **Message 1** is the Beginner's. Code puts the dialogue with the user into it word for word,
# and the Beginner model adds what the user wants and its question. Then they take turns.
#
# **Stopping.** After every message of the writer, code looks for `<answer>...</answer>`.
# If it is there, the conversation stops and the text inside is the final reply.
# At the cap the writer is told to write the reply now, and the conversation is marked "cap".
# An `<answer>` that comes too early, or from the agent that is not the writer, is cut out and counted
# as a format problem.

# %%
ANSWER_TAG = re.compile(r"<answer>(.*?)</answer>", re.DOTALL)
OUTPUT_TAG = re.compile(r"<output>(.*?)</output>", re.DOTALL)


class Agent:
    def __init__(self, name, system_prompt, max_new_tokens):
        self.name = name
        self.max_new_tokens = max_new_tokens
        self.view = [{"role": "system", "content": system_prompt}]

    def hear(self, text):
        self.view.append({"role": "user", "content": text})

    def speak(self):
        start = time.time()
        text, new_tokens, prompt_tokens = generate(self.view, self.max_new_tokens)
        self.view.append({"role": "assistant", "content": text})
        return text, new_tokens, prompt_tokens, round(time.time() - start, 2)


def run_conversation(history, entity_name, reviews_text, expert_version, final_writer):
    quoted = format_history(history)
    beginner = Agent("beginner", BEGINNER_ROLE + "\n\n" + BEGINNER_STEPS[final_writer], BEGINNER_MAX_NEW_TOKENS)
    expert = Agent("expert",
                   EXPERT_ROLE.format(name=entity_name, reviews=reviews_text) + "\n\n"
                   + EXPERT_STYLE[expert_version] + "\n" + EXPERT_ENDING[final_writer],
                   EXPERT_CONFIG[expert_version]["max_new_tokens"])
    beginner.hear(f"Dialogue with the user:\n{quoted}\n\nWrite your first message to the Expert.")

    messages = []                       # what we save: one entry per message
    final_reply, stop_reason, expert_prompt_tokens = "", None, 0
    cap = MAX_MESSAGES[final_writer]

    while stop_reason is None:
        n = len(messages) + 1
        speaker, listener = (beginner, expert) if n % 2 == 1 else (expert, beginner)
        is_writer = speaker.name == final_writer
        is_last_allowed = n == cap      # the cap is set so that this message is the writer's
        if is_last_allowed:
            speaker.view[-1]["content"] += ("\n\nThis is your last message. Write the reply for the user now, "
                                            "between <answer> and </answer>.")
        text, new_tokens, prompt_tokens, seconds = speaker.speak()
        if speaker.name == "expert":
            expert_prompt_tokens = max(expert_prompt_tokens, prompt_tokens)

        answer = ANSWER_TAG.search(text)
        may_finish = is_writer and n >= FIRST_MESSAGE_THAT_MAY_FINISH[final_writer]
        format_ok = True
        visible, hidden = text, ""

        if answer and not may_finish:
            # too early, or not the writer: the answer does not count and is cut out
            visible, format_ok = ANSWER_TAG.sub("", text).strip(), False
        if speaker.name == "expert" and EXPERT_CONFIG[expert_version]["uses_output_tag"] and not (answer and may_finish):
            # Expert B: only the part inside <output> goes to the Beginner. The steps stay hidden but are counted.
            output = OUTPUT_TAG.search(visible)
            if output:
                visible, hidden = output.group(1).strip(), OUTPUT_TAG.sub("", visible).strip()
            else:
                format_ok = False       # no tag: the Beginner gets the whole message
        if n == 1:
            visible = f"Here is my conversation with the user:\n{quoted}\n\n" + (visible or "What do the reviews say about this?")

        messages.append({"n": n, "agent": speaker.name, "text": visible, "hidden": hidden,
                         "new_tokens": new_tokens, "seconds": seconds, "format_ok": format_ok})

        if answer and may_finish:
            final_reply = answer.group(1).strip()
            stop_reason = "cap" if is_last_allowed else "answer_tag"
        elif is_last_allowed:
            # still no tag in the last message: we take the whole message as the reply
            final_reply = text.replace("<answer>", "").replace("</answer>", "").strip()
            messages[-1]["format_ok"] = False
            stop_reason = "cap"
        else:
            listener.hear(visible)

    return {
        "expert_version": expert_version,
        "final_writer": final_writer,
        "config": {"model": MODEL_NAME, "seed": SEED, "temperature": TEMPERATURE, "top_p": TOP_P, "top_k": TOP_K,
                   "max_messages": cap, "beginner_max_new_tokens": BEGINNER_MAX_NEW_TOKENS,
                   "expert_max_new_tokens": EXPERT_CONFIG[expert_version]["max_new_tokens"]},
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
    print(f"dialogue {record['dialogue_id']} | {record['domain']} | {record['entity_name']} | "
          f"Expert {record['expert_version']} | reply written by the {record['final_writer']}")
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
    FAKE_BEHAVIOUR = fake_behaviours[position % len(fake_behaviours)]   # only used by the fake model
    for final_writer in FINAL_WRITERS:
        for expert_version in EXPERT_CONFIG:
            record = run_conversation(history, entity_name, reviews_text, expert_version, final_writer)
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
# One line per combination. "format problems" counts messages where a tag was missing,
# came too early, or came from the wrong agent.

# %%
out_path = os.path.join(WORK_DIR, "pilot_conversations.jsonl")
with open(out_path, "w") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

print(f"{'writer':10}{'Expert':8}{'convs':>7}{'messages':>10}{'new tokens':>12}{'seconds':>9}{'ended by tag':>14}"
      f"{'by cap':>8}{'format problems':>17}{'Expert prompt tokens':>22}")
for final_writer in FINAL_WRITERS:
    for expert_version in EXPERT_CONFIG:
        rows = [r for r in records if r["expert_version"] == expert_version and r["final_writer"] == final_writer]
        n = len(rows)
        print(f"{final_writer:10}{expert_version:8}{n:>7}"
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
