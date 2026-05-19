import pandas as pd

courses_df = pd.read_csv("data/courses.csv")

# -----------------------------------
# Extract Metadata
# -----------------------------------

skills = sorted(
    courses_df["skill"]
    .dropna()
    .unique()
)

tracks = sorted(
    courses_df["career_track"]
    .dropna()
    .unique()
)

categories = sorted(
    courses_df["platform_category"]
    .dropna()
    .unique()
)

providers = sorted(
    courses_df["provider"]
    .dropna()
    .unique()
)

# -----------------------------------
# Generate Metadata Text
# -----------------------------------

metadata_text = f"""
SSD ALIP Platform Metadata

Available Learning Tracks:
{', '.join(tracks)}

Supported Skills:
{', '.join(skills)}

Platform Categories:
{', '.join(categories)}

Learning Providers:
{', '.join(providers)}

Total Courses Available:
{len(courses_df)}
"""

# -----------------------------------
# Save Metadata
# -----------------------------------

with open(
    "data/generated_platform_metadata.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(metadata_text)

print("Platform metadata generated successfully.")