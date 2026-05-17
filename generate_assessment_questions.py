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

import os

question_bank = {}

if os.path.exists(
    "data/generated_questions.json"
):

    with open(
        "data/generated_questions.json",
        "r"
    ) as file:

        question_bank = json.load(file)

# -----------------------------------
# Load Assessment Sources
# -----------------------------------

df = pd.read_csv("data/courses.csv")

df = df.drop_duplicates(subset=["skill"])

# -----------------------------------
# Generate Questions
# -----------------------------------

def generate_questions(
    skill,
    difficulty_level,
    platform_category,
    tags,
    prerequisites,
    assessment_source_url,
    assessment_knowledge_text,
    course_name,
    question_count=20
):

    prompt = f"""
        Generate {question_count} professional multiple choice assessment questions.

        Skill:
        {skill}

        Difficulty Level:
        {difficulty_level}

        Platform Category:
        {platform_category}

        Tags:
        {tags}

        Prerequisites:
        {prerequisites}

        Knowledge Context:
        {assessment_knowledge_text}

        Reference Documentation:
        {assessment_source_url}

        Course Context:
        {course_name}

        Requirements:

        - Generate enterprise-oriented technical questions
        - Questions should test practical understanding
        - Include conceptual and scenario-based questions
        - Avoid trivial memorization-only questions
        - Include one challenging question
        - Cover different concepts across the skill
        - Questions must not be repetitive
        - Provide 4 options for each question
        - Include correct_answer
        - Include explanation
        - Return ONLY valid JSON array

        Required JSON format:

        [
        {{
            "question": "...",
            "options": ["A", "B", "C", "D"],
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

    response_text = (
        response
        .choices[0]
        .message
        .content
    )

    # -----------------------------------
    # Clean Markdown Wrappers
    # -----------------------------------

    response_text = response_text.strip()

    response_text = response_text.replace(
        "```json",
        ""
    )

    response_text = response_text.replace(
        "```",
        ""
    )

    # -----------------------------------
    # Parse JSON
    # -----------------------------------

    questions = json.loads(response_text)

    return questions

# -----------------------------------
# Generate Questions For Each Skill
# -----------------------------------

all_questions = {}

# added below 4 lines only fr generating questions for SQL & PL/SQL skill, can remove these lines to generate questions for all skills in the dataset
# target_skill = "SQL & PL/SQL"

# filtered_df = df[
#     df["skill"] == target_skill
# ]

# for _, row in filtered_df.iterrows():

for _, row in df.iterrows():

    skill = row["skill"]

    print(f"Generating enterprise assessment questions for {skill}..")

    try:

        questions = generate_questions(
            skill=skill,
            difficulty_level=row["difficulty_level"],
            platform_category=row["platform_category"],
            tags=row["tags"],
            prerequisites=row["prerequisites"],
            assessment_source_url=row["assessment_source_url"],
            assessment_knowledge_text=row["assessment_knowledge_text"],
            course_name=row["course_name"],
            question_count=20
        )

        question_bank[skill] = questions

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
        question_bank,
        file,
        indent=4
    )

print("Question generation complete.")