import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv("data/courses.csv")

# -----------------------------------
# Generate AI Summary
# -----------------------------------

def generate_summary(row):

    prompt = f"""
    Generate a professional learning course summary.

    Course Name: {row['course_name']}
    Provider: {row['provider']}
    Learning Track: {row['career_track']}
    Skill: {row['skill']}
    Learning Style: {row['learning_style']}

    Explain:
    - what the learner will learn
    - who the course is suitable for
    - how it helps SSD data professionals

    Keep response under 80 words.
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

    return response.choices[0].message.content.strip()

def generate_recommendation_reason(row):

    prompt = f"""
    Generate a concise explanation for why this course should be recommended.

    Learning Track: {row['career_track']}
    Skill: {row['skill']}
    Learning Style: {row['learning_style']}
    Course Name: {row['course_name']}

    Explain:
    - why this course is valuable
    - who should take it
    - how it benefits SSD professionals

    Keep response under 40 words.
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

    return response.choices[0].message.content.strip()    

# -----------------------------------
# Generate Summaries
# -----------------------------------

summaries = []
recommendation_reasons = []

for index, row in df.iterrows():

    print(f"Generating summary for: {row['course_name']}")

    try:

        summary = generate_summary(row)
        recommendation_reason = generate_recommendation_reason(row)

    except Exception as e:

        summary = f"ERROR: {e}"
        recommendation_reason = f"ERROR: {e}"

    summaries.append(summary)
    recommendation_reasons.append(recommendation_reason)

# -----------------------------------
# Save Results
# -----------------------------------

df["ai_summary"] = summaries
df["ai_recommendation_reason"] = recommendation_reasons

df.to_csv(
    "data/courses_enriched.csv",
    index=False
)

print("AI summaries generated successfully.")