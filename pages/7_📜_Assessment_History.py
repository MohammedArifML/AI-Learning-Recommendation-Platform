import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SSD DataPath",
    page_icon="🧭",
    layout="wide"
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

st.title("📜 Assessment History")

st.markdown("""
Historical learner assessment records and competency tracking.
""")

st.markdown("---")

# -----------------------------------
# Load Data
# -----------------------------------

history_df = pd.read_csv(
    "data/assessment_history.csv"
)

if history_df.empty:

    st.warning("No assessment history available.")

    st.stop()

# -----------------------------------
# Filters
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    learner_filter = st.selectbox(
        "Learner",
        ["All"] + sorted(
            history_df["selected_user"]
            .dropna()
            .unique()
            .tolist()
        )
    )

with col2:

    skill_filter = st.selectbox(
        "Skill",
        ["All"] + sorted(
            history_df["skill"]
            .dropna()
            .unique()
            .tolist()
        )
    )

with col3:

    performance_filter = st.selectbox(
        "Performance",
        ["All"] + sorted(
            history_df["performance_band"]
            .dropna()
            .unique()
            .tolist()
        )
    )

# -----------------------------------
# Apply Filters
# -----------------------------------

filtered_df = history_df.copy()

if learner_filter != "All":

    filtered_df = filtered_df[
        filtered_df["selected_user"]
        == learner_filter
    ]

if skill_filter != "All":

    filtered_df = filtered_df[
        filtered_df["skill"]
        == skill_filter
    ]

if performance_filter != "All":

    filtered_df = filtered_df[
        filtered_df["performance_band"]
        == performance_filter
    ]

# -----------------------------------
# Metrics
# -----------------------------------

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:

    st.metric(
        "Assessments",
        len(filtered_df)
    )

with metric_col2:

    st.metric(
        "Average Score",
        f"{round(filtered_df['percentage'].mean(), 1)}%"
    )

with metric_col3:

    st.metric(
        "Top Score",
        f"{filtered_df['percentage'].max()}%"
    )

with metric_col4:

    st.metric(
        "Learners",
        filtered_df["selected_user"].nunique()
    )

st.markdown("---")

# -----------------------------------
# Data Table
# -----------------------------------

st.subheader("Assessment Records")

display_columns = [
    "assessment_id",
    "timestamp",
    "selected_user",
    "learning_track",
    "skill",
    "score",
    "percentage",
    "performance_band"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)