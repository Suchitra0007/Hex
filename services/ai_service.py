import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def extract_json(text: str):
    """
    Extract JSON array from Gemini response safely
    """
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON array found in Gemini response")
    return json.loads(match.group())


def generate_quiz(language: str, difficulty: str, num_questions: int):
    prompt = f"""
Generate {num_questions} multiple-choice questions on {language}.
Difficulty level: {difficulty}.

STRICT RULES:
- Return ONLY JSON
- No explanations
- No markdown
- No text outside JSON
- Exactly this format

[
  {{
    "id": 1,
    "question": "text",
    "options": ["A", "B", "C", "D"],
    "answer": "correct option"
  }}
]
"""

    print("📡 Calling Gemini API...")

    response = model.generate_content(prompt)

    raw_text = response.text
    print("🧠 Gemini raw response:\n", raw_text)

    return extract_json(raw_text)
