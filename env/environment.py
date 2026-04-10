from env.models import Observation, Action, Reward
from env.tasks import load_tasks
from env.grader import grade_easy, grade_medium, grade_hard

class EmailEnv:
    def __init__(self):
        self.tasks = load_tasks()
        self.index = 0
        self.current = None
        self.step_count = 0
        self.mode = "easy"  

    def reset(self):
        self.index = 0
        self.step_count = 0
        self.current = self.tasks[self.index]
        
        return Observation(
            email_text=self.current["email_text"],
            sender=self.current["sender"],
            subject=self.current["subject"],
            step_count=self.step_count
        )

    def step(self, action: Action):
        self.step_count += 1
        
        correct_label = self.current["label"]
        correct_priority = self.current.get("priority", "low")

        # SWITCH BASED ON MODE
        if self.mode == "easy":
            score = grade_easy(action, correct_label)
            reason = "Correct classification" if score == 1 else "Wrong classification"

        elif self.mode == "medium":
            score = grade_medium(action, correct_priority)
            reason = "Correct priority" if score == 1 else "Wrong priority"

        else:  # HARD
            score = grade_hard(action, correct_label)
            reason = "Full task evaluation"

        reward = Reward(
            value=score,
            reason=reason
        )

        done = True  # single-step for now

        return (
            Observation(
                email_text="",
                sender="",
                subject="",
                step_count=self.step_count
            ),
            reward,
            done,
            {
                "score": score,
                "mode": self.mode
            }
        )

    def state(self):
        return {
            "current_index": self.index,
            "step_count": self.step_count
        }