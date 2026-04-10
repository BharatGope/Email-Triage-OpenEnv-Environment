from env.models import Observation, Reward
from env.grader import grade_easy, grade_medium, grade_hard
from env.tasks import load_tasks


class EmailEnv:
    def __init__(self):
        self.tasks = load_tasks()
        self.current_index = 0
        self.step_count = 0
        self.mode = "easy"

    def reset(self, task="easy"):
        self.mode = task
        self.current_index = 0
        self.step_count = 0
        return self._get_observation()

    def _get_observation(self):
        email = self.tasks[self.current_index]

        return Observation(
            email_text=email["email_text"],
            sender=email["sender"],
            subject=email["subject"],
            step_count=self.step_count
        ).dict()

    def step(self, action):
        email = self.tasks[self.current_index]

        if self.mode == "easy":
            reward_value = grade_easy(action, email["label"])

        elif self.mode == "medium":
            reward_value = grade_medium(action, email["priority"])

        else:
            reward_value = grade_hard(action, email["label"])

        reward = Reward(value=reward_value, reason="evaluated")

        self.step_count += 1
        done = True  # single-step environment

        return self._get_observation(), reward.dict(), done, {}

    def state(self):
        return {
            "current_index": self.current_index,
            "step_count": self.step_count,
            "mode": self.mode
        }