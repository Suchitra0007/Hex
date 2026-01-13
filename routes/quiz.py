from fastapi import APIRouter
from models.quiz_models import QuizRequest, Submission
from services.ai_service import generate_quiz
from utils.evaluator import evaluate_answers

router = APIRouter()

# temporary in-memory storage
generated_questions = []


@router.post("/generate")
def generate_quiz_api(request: QuizRequest):
    global generated_questions

    generated_questions = generate_quiz(
        request.language,
        request.difficulty,
        request.num_questions
    )

    # remove answers before sending to user
    response = []
    for q in generated_questions:
        response.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"]
        })

    return response


@router.post("/submit")
def submit_quiz(submission: Submission):
    result = evaluate_answers(generated_questions, submission.answers)
    return result