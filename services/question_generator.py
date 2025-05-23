from schemas.interview import InterviewRequest
from utils.ollama_client import ask_ollama
from utils.prompt_templates import QUESTION_TEMPLATE

def generate_question(request: InterviewRequest) -> str:
    prompt = QUESTION_TEMPLATE.format(
        experience=request.experience_level,
        role=request.role,
        skills=", ".join(request.skills),
        round_type=request.round_type,
        resume=request.parsed_resume or ""
    )
    return ask_ollama(prompt)
