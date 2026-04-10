from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    email_text: str
    sender: str
    subject: str
    step_count: int

class Action(BaseModel):
    category: str  # spam / important / work / personal
    priority: Optional[str] = None
    response: Optional[str] = None
    mark_done: bool = False

class Reward(BaseModel):
    value: float
    reason: str