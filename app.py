import streamlit as st
from logic.recommender import recommend_courses
from logic.roadmap import generate_roadmap

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="NPC DataPath",
    layout="wide"
)

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
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Header / Branding
# -----------------------------------

st.markdown("""
<div style='display:flex; align-items:center; gap:12px;'>

<div style='font-size:40px;'>
📘
</div>

<div style='font-size:30px; font-weight:700;'>
NPC DataPath
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------
# Session State Defaults
# -----------------------------------

if "career_track" not in st.session_state:
    st.session_state.career_track = "Data Engineering"

if "experience_level" not in st.session_state:
    st.session_state.experience_level = "Choose an option"

if "selected_skills" not in st.session_state:
    st.session_state.selected_skills = []

if "goal" not in st.session_state:
    st.session_state.goal = "Choose an option"

if "learning_style" not in st.session_state:
    st.session_state.learning_style = "Choose an option"

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.header("Learner Profile")

career_track = st.sidebar.selectbox(
    "Select Career Track",
    [
        "Data Engineering",
        "Data Analysis",
        "Business Intelligence",
        "Machine Learning",
        "Statistical Analysis"
    ],
    key="career_track"
)

experience_level = st.sidebar.selectbox(
    "Experience Level",
    [
        "Choose an option",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    key="experience_level"
)

skills_mapping = {
    "Data Engineering": [
        "SQL",
        "Python",
        "Spark",
        "Databricks",
        "Airflow",
        "Azure",
        "Snowflake"
    ],
    "Data Analysis": [
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "Python",
        "Statistics"
    ],
    "Business Intelligence": [
        "Power BI",
        "Tableau",
        "SQL",
        "Data Modeling"
    ],
    "Machine Learning": [
        "Python",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "MLOps"
    ],
    "Statistical Analysis": [
        "R",
        "Python",
        "Statistics",
        "Hypothesis Testing",
        "Regression"
    ]
}

selected_skills = st.sidebar.multiselect(
    "Current Skills",
    skills_mapping[career_track],
    key="selected_skills"
)

goal = st.sidebar.selectbox(
    "Learning Goal",
    [
        "Choose an option",
        "Job Switch",
        "Promotion",
        "Certification",
        "Project Building",
        "Interview Preparation"
    ],
    key="goal"
)

learning_style = st.sidebar.selectbox(
    "Preferred Learning Style",
    [
        "Choose an option",
        "Video Courses",
        "Hands-on Labs",
        "Documentation",
        "Books",
        "YouTube Tutorials"
    ],
    key="learning_style"
)

# -----------------------------------
# Validation
# -----------------------------------

is_valid = (
    experience_level != "Choose an option"
    and goal != "Choose an option"
    and learning_style != "Choose an option"
)

# -----------------------------------
# Buttons
# -----------------------------------

col1, col2 = st.sidebar.columns(2)

with col1:
    generate = st.button("Generate", disabled=not is_valid)

with col2:

    reset = st.button("Reset")

    if reset:

        keys_to_clear = [
        "career_track",
        "experience_level",
        "selected_skills",
        "goal",
        "learning_style"
    ]

        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]

        st.rerun()

if not is_valid:

    st.sidebar.warning(
        "Please complete all required selections."
    )

# -----------------------------------
# Main Section
# -----------------------------------

st.markdown(
    '<div class="main-title">AI Learning Recommendation Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-text">Personalized learning roadmap generator for data professionals.</div>',
    unsafe_allow_html=True
)

st.markdown("")

# -----------------------------------
# Generate Results
# -----------------------------------

if generate:

    st.subheader("Learner Summary")

    st.write(f"**Career Track:** {career_track}")
    st.write(f"**Experience Level:** {experience_level}")
    st.write(f"**Current Skills:** {', '.join(selected_skills) if selected_skills else 'None'}")
    st.write(f"**Goal:** {goal}")
    st.write(f"**Learning Style:** {learning_style}")

    recommended_courses = recommend_courses(
        career_track,
        selected_skills,
        learning_style
    )

    roadmap = generate_roadmap(
    career_track,
    experience_level
    )

    st.subheader("Learning Roadmap")

    if roadmap:

        for phase in roadmap:

            st.markdown(f"""
            ### {phase['phase']}
            """)

            for skill in phase["skills"]:

                st.markdown(f"- {skill}")

    else:

        st.warning("No roadmap available.")

    st.subheader("Recommended Courses")

    if recommended_courses.empty:

        st.warning("No matching courses found.")

    else:

        for _, row in recommended_courses.iterrows():

            st.markdown(f"""
            ### {row['course_name']}

            - Provider: {row['provider']}
            - Skill: {row['skill']}
            - Level: {row['level']}
            - Learning Style: {row['learning_style']}

            [Open Course]({row['url']})
            """)