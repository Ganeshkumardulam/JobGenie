from schemas.interview import AnswerResponse
from utils.ollama_client import ask_ollama
from utils.prompt_templates import FEEDBACK_TEMPLATE

def evaluate_answer(data: AnswerResponse) -> str:
    prompt = FEEDBACK_TEMPLATE.format(
        question=data.question,
        answer=data.answer,
        role=data.context.role,
        round_type=data.context.round_type
    )
    return ask_ollama(prompt)