from openai import OpenAI
from dotenv import load_dotenv

import pandas as pd
import json
import os
from pathlib import Path

# -----------------------------------
# LOAD ENV
# -----------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------------------
# FILE PATHS
# -----------------------------------

DATA_FOLDER = "data"

OUTPUT_FILE = (
    f"{DATA_FOLDER}/full_platform_knowledge.txt"
)

# -----------------------------------
# HELPER FUNCTIONS
# -----------------------------------

def safe_read_text(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    except Exception as e:

        return f"Unable to read {file_path}: {str(e)}"


def safe_read_json(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.dumps(
                json.load(f),
                indent=2
            )

    except Exception as e:

        return f"Unable to read JSON {file_path}: {str(e)}"


def safe_read_csv(file_path):

    try:

        df = pd.read_csv(file_path)

        return df.to_string(index=False)

    except Exception as e:

        return f"Unable to read CSV {file_path}: {str(e)}"

# -----------------------------------
# BUILD FULL COURSE CATALOG
# -----------------------------------

# -----------------------------------
# BUILD FULL COURSE CATALOG
# -----------------------------------

def build_full_course_catalog():

    try:

        df = pd.read_csv(
            f"{DATA_FOLDER}/courses.csv"
        )

        catalog_text = (
            "\n\n"
            "==================================================\n"
            "COMPLETE COURSE CATALOG\n"
            "==================================================\n\n"
        )

        for index, row in df.iterrows():

            catalog_text += (
                f"\n\n"
                f"Course #{index + 1}\n\n"
            )

            # -----------------------------------
            # Add ALL Columns Dynamically
            # -----------------------------------

            for column in df.columns:

                value = row.get(column, "N/A")

                # Handle NaN values
                if pd.isna(value):

                    value = "N/A"

                catalog_text += (
                    f"{column}:\n"
                    f"{value}\n\n"
                )

            catalog_text += (
                "--------------------------------------------------\n"
            )

        return catalog_text

    except Exception as e:

        return (
            f"Unable to generate course catalog: {str(e)}"
        )
    

# -----------------------------------
# LOAD PLATFORM FILES
# -----------------------------------

print("Loading platform artifacts...")

courses_data = safe_read_csv(
    f"{DATA_FOLDER}/courses.csv"
)

assessment_history = safe_read_csv(
    f"{DATA_FOLDER}/assessment_history.csv"
)

assessment_sources = safe_read_csv(
    f"{DATA_FOLDER}/assessment_sources.csv"
)

generated_questions = safe_read_json(
    f"{DATA_FOLDER}/generated_questions.json"
)

roadmaps_data = safe_read_json(
    f"{DATA_FOLDER}/roadmaps.json"
)

platform_knowledge = safe_read_text(
    f"{DATA_FOLDER}/platform_knowledge.txt"
)

generated_metadata = safe_read_text(
    f"{DATA_FOLDER}/generated_platform_metadata.txt"
)

full_course_catalog = build_full_course_catalog()

# -----------------------------------
# GENERATE ANALYTICS SUMMARY
# -----------------------------------

try:

    analytics_df = pd.read_csv(
        f"{DATA_FOLDER}/assessment_history.csv"
    )

    total_assessments = len(
        analytics_df
    )

    total_learners = analytics_df[
        "selected_user"
    ].nunique()

    avg_score = round(
        analytics_df["percentage"].mean(),
        1
    )

    top_skills = (
        analytics_df["skill"]
        .value_counts()
        .head(5)
        .to_dict()
    )

    analytics_summary = f"""
Total Assessments:
{total_assessments}

Unique Learners:
{total_learners}

Average Assessment Score:
{avg_score}%

Top Assessed Skills:
{top_skills}
"""

except Exception as e:

    analytics_summary = (
        f"Unable to generate analytics summary: {str(e)}"
    )

# -----------------------------------
# TECH STACK
# -----------------------------------

tech_stack = """
Frontend:
- Streamlit

Backend:
- Python

AI/LLM:
- OpenAI GPT-4o-mini

Data Processing:
- Pandas

Storage:
- CSV persistence
- JSON persistence

Architecture:
- Modular page-based architecture
- Logic layer separation
- AI-powered recommendation workflows
- AI-generated assessment engine
- Workforce analytics layer

Deployment:
- Streamlit Community Cloud
"""

# -----------------------------------
# SYSTEM PROMPT
# -----------------------------------

system_prompt = f"""
You are an enterprise AI knowledge architect.

Your task is to generate a comprehensive
knowledge corpus for the platform:

SSD ALIP
(AI-Powered Learning Intelligence Platform)

The output should become the master
knowledge base used by an AI assistant.

Generate a highly detailed,
well-structured,
professional enterprise knowledge corpus.

The corpus must include:

1. Platform Overview
2. Business Purpose
3. AI Features
4. Technical Architecture
5. Technology Stack
6. Learning Tracks
7. Skills Supported
8. Course Catalog
9. Course Recommendations
10. Course Providers
11. Course URLs
12. Analytics Overview
13. Assessment Engine
14. Sample Assessment Questions
15. Workforce Learning Insights
16. Future Roadmap
17. Platform Modules
18. User Workflows
19. Governance and AI Vision

IMPORTANT:
- Organize content into sections
- Use professional enterprise language
- Include course details and URLs
- Include descriptions and summaries
- Summarize analytics intelligently
- Summarize assessments intelligently
- Avoid raw table dumps
- Avoid JSON formatting
- Convert structured data into narrative enterprise knowledge
- Make the corpus highly useful for a GPT-based assistant
- The assistant should be able to answer:
    - course questions
    - analytics questions
    - AI feature questions
    - platform questions
    - roadmap questions
    - learning path questions

The final output should read like:
- enterprise platform intelligence documentation
- AI assistant operational knowledge
- workforce learning intelligence guide
"""

# -----------------------------------
# USER CONTEXT
# -----------------------------------

user_prompt = f"""
PLATFORM KNOWLEDGE:
{platform_knowledge}

GENERATED PLATFORM METADATA:
{generated_metadata}

TECH STACK:
{tech_stack}

ASSESSMENT HISTORY:
{assessment_history}

ASSESSMENT SOURCES:
{assessment_sources}

GENERATED QUESTIONS:
{generated_questions}

ROADMAP DATA:
{roadmaps_data}

ANALYTICS SUMMARY:
{analytics_summary}
"""

# -----------------------------------
# GENERATE CORPUS
# -----------------------------------

print("Generating enterprise knowledge corpus...")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    temperature=0.3
)

knowledge_corpus = (
    response.choices[0]
    .message.content
)

# -----------------------------------
# APPEND FULL COURSE CATALOG
# -----------------------------------

knowledge_corpus += f"""

==================================================
FULL COURSE INVENTORY
==================================================

{full_course_catalog}
"""

# -----------------------------------
# SAVE CORPUS
# -----------------------------------

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(knowledge_corpus)

print(
    f"\nKnowledge corpus generated successfully:\n{OUTPUT_FILE}"
)