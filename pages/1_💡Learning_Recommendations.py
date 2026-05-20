import streamlit as st
import pandas as pd
from logic.recommender import recommend_courses
import inspect

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="SSD DataPath",
    page_icon="🧭",
    layout="wide"
)

st.sidebar.image(
    "assets/logo.png",
    width=260
)

st.sidebar.markdown("---")

# -----------------------------------
# Load CSS
# -----------------------------------

# def load_css():
#     with open("styles/government_theme.css") as f:
#         st.markdown(
#             f"<style>{f.read()}</style>",
#             unsafe_allow_html=True
#         )

# load_css()

# -----------------------------------
# Custom CSS
# -----------------------------------

st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 0px;
}

.sub-text {
    font-size: 18px;
    color: gray;
    margin-top: 0px;
}

.logo-text {
    font-size: 26px;
    font-weight: bold;
}

section[data-testid="stSidebar"] {
    width: 320px !important;
    background-color: #f5f7fb;
}
            
.main .block-container {
    max-width: 1200px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Header / Branding
# -----------------------------------

st.markdown("""
<div style='display:flex; align-items:center; gap:12px;'>

<div style='font-size:40px;'>
🧭
</div>

<div style='font-size:30px; font-weight:700;'>
SSD DataPath
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------
# Header
# -----------------------------------

st.title("💡 Learning Recommendations")

st.markdown("""
Personalize your learning journey with AI-powered recommendations.
""")

st.markdown("---")

# -----------------------------------
# Session State Defaults
# -----------------------------------

if "career_track" not in st.session_state:
    st.session_state.career_track = "Data Analysis"

if "selected_skills" not in st.session_state:
    st.session_state.selected_skills = []

if "learning_style" not in st.session_state:
    st.session_state.learning_style = "Choose an option"

if "selected_difficulty" not in st.session_state:
    st.session_state.selected_difficulty = "All"

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.header("Learning Requirements")

courses_df = pd.read_csv("data/courses.csv")

career_tracks = sorted(
    courses_df["career_track"].dropna().unique()
)

career_track = st.sidebar.selectbox(
    "Select Learning Track",
    career_tracks,
    index=0,
    key="career_track"
)

available_skills = sorted(
    courses_df[
        courses_df["career_track"] == career_track
    ]["skill"].dropna().unique()
)

skill_options = available_skills

selected_skills = st.sidebar.multiselect(
    "Upskill Areas",
    skill_options,
    key="selected_skills"
)

learning_styles = sorted(
    courses_df["learning_style"].dropna().unique()
)

learning_style_options = [
    "All"
] + learning_styles

learning_style = st.sidebar.selectbox(
    "Learning Format",
    learning_style_options,
    index=0,
    key="learning_style"
)

difficulty_options = [
    "All"
] + sorted(
    courses_df["difficulty_level"]
    .dropna()
    .unique()
)

selected_difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    difficulty_options,
    index=0,
    key="selected_difficulty"
)

category_options = [
    "All"
] + sorted(
    courses_df["platform_category"]
    .dropna()
    .unique()
)

selected_category = st.sidebar.selectbox(
    "Platform Category",
    category_options,
    index=0,
    key="selected_category"
)

# -----------------------------------
# Validation
# -----------------------------------

is_valid = (len(selected_skills) > 0)

# -----------------------------------
# Buttons
# -----------------------------------

col1, col2 = st.sidebar.columns(2)

with col1:
    generate = st.button("Generate", disabled=not is_valid)

with col2:

    reset = st.button("Reset")

    if reset:

        if reset:

            keys_to_clear = [
                "career_track",
                "selected_skills",
                "learning_style",
                "selected_difficulty",
                "selected_category"
            ]

            for key in keys_to_clear:
                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()

if not is_valid:

    st.sidebar.warning("Please select at least one upskill area.")

# -----------------------------------
# Generate Results
# -----------------------------------

if generate:

    st.subheader("🎯 Learner Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Learning Track",
            career_track
        )

    with col2:
        st.metric(
            "Skills Selected",
            len(selected_skills)
        )

    with col3:
        st.metric(
            "Learning Format",
            learning_style
        )

    if selected_skills:

        st.markdown(
            f"**Selected Skills:** {', '.join(selected_skills)}"
        )

    recommended_courses = recommend_courses(
    career_track,
    selected_skills,
    learning_style,
    selected_difficulty,
    selected_category
)

    st.markdown("---")

    st.subheader("📚 Recommended Courses")

    st.write(
        f"Found {len(recommended_courses)} recommended courses."
    )

    if recommended_courses.empty:

        st.warning("No matching courses found.")

    else:

        for _, row in recommended_courses.iterrows():

            left, center, right = st.columns([1, 5, 1])

            with center:

                with st.container(border=True):

                    st.markdown(
                        f"### {row['course_name']}"
                    )
                    st.write(row["ai_summary"])
                    st.info(row["ai_recommendation_reason"])
                    st.markdown("---")

                    col1, col2 = st.columns(2)

                    with col1:

                        with col1:

                            st.caption(f"🏢 Provider: {row['provider']}")
                            st.write(f"**Skill:** {row['skill']}")
                            st.write(f"**Difficulty:** {row['difficulty_level']}")
                            st.write(f"**Category:** {row['platform_category']}")
                            st.write(f"**Learning Style:** {row['learning_style']}")

                    with col2:

                        duration = row['duration_hours']

                        if pd.notna(duration):

                            st.write(
                                f"**Duration:** {duration} Hours"
                            )

                        estimated_weeks = row.get(
                            "estimated_weeks"
                        )

                        if pd.notna(estimated_weeks):

                            st.write(
                                f"**Estimated Weeks:** {estimated_weeks}"
                            )

                        certification = row.get(
                            "certification_related"
                        )

                        if str(certification).lower() == "yes":

                            st.success(
                                "🏅 Certification Related"
                            )

                        badge = (
                            "🟢 Free"
                            if row['is_free']
                            else "🔵 Paid"
                        )

                        st.markdown(badge)

                    
                    prerequisites = row.get(
                        "prerequisites"
                    )

                    if (
                        pd.notna(prerequisites)
                        and str(prerequisites).strip() != ""
                    ):

                        st.warning(
                            f"Prerequisites: {prerequisites}"
                        )

                    st.markdown(f"""
                    <a href="{row['url']}" target="_blank">
                        <button style="
                            background-color:#2563eb;
                            color:white;
                            border:none;
                            padding:10px 18px;
                            border-radius:8px;
                            cursor:pointer;
                            font-weight:600;
                        ">
                            Open Course
                        </button>
                    </a>
                    """, unsafe_allow_html=True)

                    st.markdown("")

st.markdown("---")

# -----------------------------------
# Footer
# -----------------------------------

st.caption(
    "SSD DataPath • AI-Powered Learning Intelligence Platform"
)