import pandas as pd

# -----------------------------------
# Load Courses
# -----------------------------------

courses_df = pd.read_csv(
    "data/courses.csv"
)

# -----------------------------------
# Filter Assessment Enabled
# -----------------------------------

assessment_df = courses_df[
    courses_df["assessment_enabled"]
    .astype(str)
    .str.lower()
    == "yes"
]

# -----------------------------------
# Select Assessment Columns
# -----------------------------------

assessment_df = assessment_df[[
    "skill",
    "assessment_source_url",
    "assessment_knowledge_text"
]]

# -----------------------------------
# Remove Empty Knowledge Rows
# -----------------------------------

assessment_df = assessment_df.dropna(
    subset=[
        "assessment_knowledge_text"
    ]
)

# -----------------------------------
# Deduplicate By Skill
# -----------------------------------

assessment_df = assessment_df.drop_duplicates(
    subset=["skill"]
)

# -----------------------------------
# Rename Columns
# -----------------------------------

assessment_df = assessment_df.rename(
    columns={
        "assessment_source_url": "source_url",
        "assessment_knowledge_text": "knowledge_text"
    }
)

# -----------------------------------
# Add Source Name
# -----------------------------------

assessment_df["source_name"] = (
    assessment_df["skill"]
    + " Knowledge Base"
)

# -----------------------------------
# Reorder Columns
# -----------------------------------

assessment_df = assessment_df[[
    "skill",
    "source_name",
    "source_url",
    "knowledge_text"
]]

# -----------------------------------
# Export
# -----------------------------------

assessment_df.to_csv(
    "data/assessment_sources.csv",
    index=False
)

print(
    "assessment_sources.csv generated successfully."
)