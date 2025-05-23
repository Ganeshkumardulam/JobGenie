from enum import Enum


class InterviewRound(str, Enum):
    technical = "technical"
    hr = "hr"
    manager = "manager"
    dsa = "dsa"
