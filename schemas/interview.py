from pydantic import BaseModel
from typing import Optional
from schemas.enums import InterviewRound

class InterviewRequest(BaseModel):
    experience_level: str
    role: str
    skills: list[str]
    round_type: InterviewRound
    parsed_resume: Optional[str] = None

class AnswerResponse(BaseModel):
    question: str
    answer: str
    context: InterviewRequest