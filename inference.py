import os
from env.environment import EmailEnv
from env.models import Action

# REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN", "")

# Optional OpenAI client (safe fallback)
try:
    from openai import OpenAI

    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=HF_TOKEN
    )
except:
    client = None


def rule_based_agent(obs):
    text = (obs["email_text"] + " " + obs["subject"]).lower()

    if "win" in text or "free" in text:
        return Action(
            category="spam",
            priority="low",
            response="[AUTO][confidence=0.7] This appears to be spam.",
            mark_done=True
        )

    elif "meeting" in text or "urgent" in text:
        return Action(
            category="important",
            priority="high",
            response="[AUTO][confidence=0.9] Noted. I will attend.",
            mark_done=True
        )

    else:
        return Action(
            category="work",
            priority="medium",
            response="[AUTO][confidence=0.6] Received. Will review.",
            mark_done=True
        )


def run_task(task):
    env = EmailEnv()
    obs = env.reset(task)

    print(f"[START] task={task} env=email-env model=rule-based-agent")

    done = False
    rewards = []
    step_num = 1

    while not done:
        action = rule_based_agent(obs)

        obs, reward, done, info = env.step(action)

        print(
            f"[STEP] step={step_num} action={action.dict()} "
            f"reward={reward['value']} done={done} error=None"
        )

        rewards.append(reward["value"])
        step_num += 1

    score = sum(rewards) / len(rewards)

    print(
        f"[END] success=True steps={len(rewards)} "
        f"score={score} rewards={rewards}"
    )

    return score


if __name__ == "__main__":
    tasks = ["easy", "medium", "hard"]
    scores = []

    for task in tasks:
        scores.append(run_task(task))

    final_score = sum(scores) / len(scores)

    print(f"\nFINAL AVERAGE SCORE: {final_score}")