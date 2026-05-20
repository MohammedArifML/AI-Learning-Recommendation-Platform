from openai import OpenAI
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

courses_df = pd.read_csv("data/courses.csv")


def load_knowledge_base():

    with open(
        "data/full_platform_knowledge.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()

# -----------------------------------
# LOAD ANALYTICS SUMMARY
# -----------------------------------

def load_analytics_summary():

    try:

        analytics_df = pd.read_csv(
            "data/assessment_history.csv"
        )

        if analytics_df.empty:

            return "No assessment analytics available."

        total_assessments = len(analytics_df)

        total_learners = analytics_df[
            "selected_user"
        ].nunique()

        avg_score = round(
            analytics_df["percentage"].mean(),
            1
        )

        top_skill = (
            analytics_df["skill"]
            .value_counts()
            .idxmax()
        )

        return f"""
Assessment Analytics Summary:

Total Assessments:
{total_assessments}

Unique Learners:
{total_learners}

Average Assessment Score:
{avg_score}%

Most Assessed Skill:
{top_skill}
"""

    except Exception:

        return "Analytics data unavailable."




# -----------------------------------
# ASK ASSISTANT
# -----------------------------------

def ask_ai_assistant(user_question, chat_history):

    knowledge_base = load_knowledge_base()
    
    analytics_summary = load_analytics_summary()

    system_prompt = f"""
You are SSD ALIP AI Assistant.

You are an enterprise AI learning assistant.

Your responsibilities include helping users understand:

- learning tracks
- technical skills
- available courses
- assessment capabilities
- workforce analytics
- platform functionality
- AI features

Only answer questions related to SSD ALIP.

If asked unrelated questions,
politely redirect the conversation back to SSD ALIP.

Use concise professional enterprise language.

When recommending courses:
- include course names
- include provider
- include course URLs
- include AI recommendation reasoning
- explain why the recommendation is relevant
- suggest logical learning progression

Platform Knowledge:
{knowledge_base}

Analytics Summary:
{analytics_summary}
"""

    # -----------------------------------
    # BUILD CHAT HISTORY
    # -----------------------------------

    conversation_messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Add previous messages
    for message in chat_history[-8:]:

        conversation_messages.append({
            "role": message["role"],
            "content": message["content"]
        })

    # Add current question
    conversation_messages.append({
        "role": "user",
        "content": user_question
    })

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=conversation_messages,
        temperature=0.3
    )

    return response.choices[0].message.content