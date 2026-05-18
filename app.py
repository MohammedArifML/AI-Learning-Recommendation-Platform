import streamlit as st
import pandas as pd

# redeploy refresh

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="SSD DataPath",
    page_icon="🧭",
    layout="wide"
)

# -----------------------------------
# Load CSS
# -----------------------------------

def load_css():
    with open("styles/government_theme.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -----------------------------------
# Load Dataset
# -----------------------------------

courses_df = pd.read_csv(
    "data/courses.csv"
)

# -----------------------------------
# Dynamic Platform Metrics
# -----------------------------------

total_courses = len(courses_df)

total_skills = (
    courses_df["skill"]
    .nunique()
)

total_tracks = (
    courses_df["career_track"]
    .nunique()
)

total_providers = (
    courses_df["provider"]
    .nunique()
)

# -----------------------------------
# Sidebar Branding
# -----------------------------------

st.sidebar.image(
    "assets/logo.png",
    width=260
)

st.sidebar.markdown("---")

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
    width=100
)

st.sidebar.title("SSD DataPath")

st.sidebar.markdown("""
AI-powered learning intelligence platform
for SSD data professionals.
""")

st.sidebar.markdown("---")

st.sidebar.success(
    "Use the navigation menu to access platform modules."
)

# -----------------------------------
# Hero Section
# -----------------------------------

st.markdown("""
# 🧭 SSD DataPath

### AI-Powered Learning Intelligence Platform
""")

st.markdown("""
Personalized learning recommendations, AI-powered assessments,
and enterprise skill intelligence for SSD data professionals.
""")

st.markdown("---")

# -----------------------------------
# Platform Metrics
# -----------------------------------

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric(
        "Courses",
        total_courses
    )

with metric_col2:
    st.metric(
        "Skills",
        total_skills
    )

with metric_col3:
    st.metric(
        "Learning Tracks",
        total_tracks
    )

with metric_col4:
    st.metric(
        "Providers",
        total_providers
    )

st.markdown("---")

# -----------------------------------
# Platform Overview Cards
# -----------------------------------

col1, col2 = st.columns(2)

# -----------------------------------
# Learning Recommendations Card
# -----------------------------------

with col1:

    with st.container(border=True):

        st.markdown("## 🧭 Learning Recommendations")

        st.markdown("""
Discover personalized learning paths, curated courses,
and AI-enriched recommendations across modern data
engineering, analytics, cloud, and enterprise platforms.
""")

        st.info("""
✔ AI-generated course summaries

✔ Personalized learning guidance

✔ Curated enterprise learning resources

✔ Metadata-driven learning intelligence
""")

# -----------------------------------
# Skill Assessment Card
# -----------------------------------

with col2:

    with st.container(border=True):

        st.markdown("## 🧠 Skill Assessment")

        st.markdown("""
Evaluate technical competency through AI-generated
professional assessments across enterprise technologies
and modern data platforms.
""")

        st.info("""
✔ AI-generated assessment questions

✔ Enterprise-oriented competency evaluation

✔ Skill-gap identification

✔ Persistent learner assessment tracking
""")

st.markdown("---")

# -----------------------------------
# Supported Learning Domains
# -----------------------------------

st.markdown("## 🚀 Supported Learning Domains")

skills = sorted(
    courses_df["skill"]
    .dropna()
    .unique()
)

skill_chunks = [
    skills[i:i + 5]
    for i in range(0, len(skills), 5)
]

cols = st.columns(3)

for idx, chunk in enumerate(skill_chunks):

    with cols[idx % 3]:

        with st.container(border=True):

            for skill in chunk:

                st.markdown(f"✔ {skill}")

# -----------------------------------
# Platform Categories
# -----------------------------------

st.markdown("---")

st.markdown("## 🏷️ Platform Categories")

categories = sorted(
    courses_df["platform_category"]
    .dropna()
    .unique()
)

category_cols = st.columns(len(categories))

for idx, category in enumerate(categories):

    with category_cols[idx]:

        st.info(category)

# -----------------------------------
# Difficulty Coverage
# -----------------------------------

st.markdown("---")

st.markdown("## 📚 Learning Difficulty Coverage")

levels = sorted(
    courses_df["difficulty_level"]
    .dropna()
    .unique()
)

level_cols = st.columns(len(levels))

for idx, level in enumerate(levels):

    count = len(
        courses_df[
            courses_df["difficulty_level"]
            == level
        ]
    )

    with level_cols[idx]:

        st.metric(
            level,
            count
        )

# -----------------------------------
# Certification Statistics
# -----------------------------------

st.markdown("---")

certification_count = len(
    courses_df[
        courses_df[
            "certification_related"
        ]
        .astype(str)
        .str.lower()
        == "yes"
    ]
)

st.success(
    f"🏅 {certification_count} certification-related learning resources available."
)

# -----------------------------------
# Platform Vision
# -----------------------------------

st.markdown("---")

with st.container(border=True):

    st.markdown("## 🎯 Platform Vision")

    st.markdown(
        f"""
SSD DataPath is an AI-powered workforce learning intelligence platform
built to support enterprise upskilling, assessment, and capability development
for SSD professionals.

The platform currently supports:

- {total_courses} curated learning resources
- {total_skills} technical skill domains
- {total_tracks} enterprise learning tracks
- AI-generated learning recommendations
- AI-generated competency assessments
- Metadata-driven learning intelligence

SSD DataPath combines learning guidance, AI-powered assessment,
and learner intelligence into a unified enterprise learning ecosystem.
"""
    )

st.markdown("---")

# -----------------------------------
# Footer
# -----------------------------------

st.caption(
    "SSD DataPath • AI-Powered Learning Intelligence Platform"
)