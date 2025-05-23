from fastapi import APIRouter, HTTPException
from schemas.interview import InterviewRequest, AnswerResponse
from services.question_generator import generate_question
from services.feedback_evaluator import evaluate_answer

router = APIRouter()

@router.post("/question")
def get_question(request: InterviewRequest):
    try:
        question = generate_question(request)
        return {"question": question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/answer")
def evaluate_user_answer(answer: AnswerResponse):
    try:
        feedback = evaluate_answer(answer)
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))