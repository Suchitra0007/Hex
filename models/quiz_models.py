from pydantic import BaseModel
from typing import List


class QuizRequest(BaseModel):
    language: str
    difficulty: str
    num_questions: int


class Question(BaseModel):
    id: int
    question: str
    options: List[str]


class Answer(BaseModel):
    question_id: int
    selected_option: str


class Submission(BaseModel):
    answers: List[Answer]
