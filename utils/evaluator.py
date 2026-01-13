import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def evaluate_answers(questions, user_answers):
    prompt = f"""
You are an evaluator.

Questions:
{questions}

User Answers:
{user_answers}

Return ONLY valid JSON in this format:
{{
  "score": number,
  "total_questions": number
}}
"""

    response = model.generate_content(prompt)
    result_text = response.text.strip()

    return json.loads(result_text)
