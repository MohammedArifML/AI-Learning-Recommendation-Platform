import streamlit as st
from logic.recommender import recommend_courses

st.set_page_config(
    page_title="AI Learning Recommendation Platform",
    layout="wide"
)

st.title("AI Learning Recommendation Platform")

st.markdown("Personalized learning roadmap generator for data professionals.")

# -----------------------------
# Sidebar Inputs
# -----------------------------

st.sidebar.header("Learner Profile")

career_track = st.sidebar.selectbox(
    "Select Career Track",
    [
        "Data Engineering",
        "Data Analysis",
        "Business Intelligence",
        "Machine Learning",
        "Statistical Analysis"
    ]
)

experience_level = st.sidebar.selectbox(
    "Experience Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# Conditional skills based on track

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
    skills_mapping[career_track]
)

goal = st.sidebar.selectbox(
    "Learning Goal",
    [
        "Job Switch",
        "Promotion",
        "Certification",
        "Project Building",
        "Interview Preparation"
    ]
)

learning_style = st.sidebar.selectbox(
    "Preferred Learning Style",
    [
        "Video Courses",
        "Hands-on Labs",
        "Documentation",
        "Books",
        "YouTube Tutorials"
    ]
)

# -----------------------------
# Submit Button
# -----------------------------

generate = st.sidebar.button("Generate Learning Plan")

# -----------------------------
# Output Section
# -----------------------------

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