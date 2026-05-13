import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------------------
# Load Assessment Sources
# -----------------------------------

df = pd.read_csv("data/assessment_sources.csv")

# -----------------------------------
# Generate Questions
# -----------------------------------

def generate_questions(skill,knowledge_text,question_count=20,difficulty="Advanced"):

    prompt = f"""
    Generate {question_count} multiple choice assessment questions.

    Skill: {skill}

    Knowledge Base:
    {knowledge_text}

    Requirements:
    - Questions must be technical and accurate
    - Include 4 options
    - Include correct answer
    - Include short explanation for correct answer
    - Difficulty Level: Primarily Intermediate Professional
    - Most questions should evaluate practical working knowledge
    - Include one advanced challenge question
    - Avoid beginner definitions or trivial memorization
    - Focus on implementation, troubleshooting, optimization, governance, and enterprise usage concepts where relevant
    - Include scenario-based reasoning where appropriate
    - Ensure answer options are plausible and technically meaningful
    - Questions should resemble professional technical assessments
    - Prefer applied enterprise-oriented questions over academic theory

    Return valid JSON array only.

    JSON format:
    [
      {{
        "question": "...",
        "options": ["...", "...", "...", "..."],
        "correct_answer": "...",
        "explanation": "..."
      }}
    ]
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

# -----------------------------------
# Generate Questions For Each Skill
# -----------------------------------

all_questions = {}

for _, row in df.iterrows():

    skill = row["skill"]

    print(f"Generating questions for {skill}...")

    try:

        questions = generate_questions(
            skill,
            row["knowledge_text"],
            question_count=20,
            difficulty="Advanced"
        )

        all_questions[skill] = json.loads(questions)

    except Exception as e:

        print(f"ERROR for {skill}: {e}")

# -----------------------------------
# Save Output
# -----------------------------------

with open(
    "data/generated_questions.json",
    "w"
) as file:

    json.dump(
        all_questions,
        file,
        indent=4
    )

print("Question generation complete.")