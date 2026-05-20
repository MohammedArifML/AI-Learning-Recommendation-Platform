import streamlit as st
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="SSD DataPath",
    page_icon="🧭",
    layout="wide"
)

# -----------------------------------
# SIDEBAR BRANDING
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
# LOAD CSS
# -----------------------------------

# def load_css():
#     with open("styles/government_theme.css") as f:
#         st.markdown(
#             f"<style>{f.read()}</style>",
#             unsafe_allow_html=True
#         )

# load_css()

# -----------------------------------
# CUSTOM CSS
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
# HEADER / BRANDING
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
# PAGE HEADER
# -----------------------------------

st.title("📊 Learning Analytics")

st.markdown("""
AI-powered workforce learning insights and competency analytics.
""")

st.markdown("---")

# -----------------------------------
# LOAD ANALYTICS DATA
# -----------------------------------

history_file = "data/assessment_history.csv"

try:

    analytics_df = pd.read_csv(history_file)

except FileNotFoundError:

    st.warning(
        "Assessment history file not found."
    )

    st.stop()

# -----------------------------------
# EMPTY STATE
# -----------------------------------

if analytics_df.empty:

    st.warning(
        "No assessment analytics available."
    )

    st.stop()

# -----------------------------------
# DATA CLEANING
# -----------------------------------

analytics_df["timestamp"] = pd.to_datetime(
    analytics_df["timestamp"],
    errors="coerce"
)

analytics_df["percentage"] = pd.to_numeric(
    analytics_df["percentage"],
    errors="coerce"
)

# -----------------------------------
# EXECUTIVE METRICS
# -----------------------------------

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:

    st.metric(
        "Assessments",
        len(analytics_df)
    )

with metric_col2:

    avg_score = round(
        analytics_df["percentage"].mean(),
        1
    )

    st.metric(
        "Average Score",
        f"{avg_score}%"
    )

with metric_col3:

    st.metric(
        "Learners",
        analytics_df["selected_user"].nunique()
    )

with metric_col4:

    top_score = analytics_df["percentage"].max()

    st.metric(
        "Top Score",
        f"{top_score}%"
    )

st.markdown("---")

# -----------------------------------
# CHARTS
# -----------------------------------

chart_col1, chart_col2 = st.columns(2)

# -----------------------------------
# ASSESSMENTS BY SKILL
# -----------------------------------

with chart_col1:

    with st.container(border=True):

        st.subheader("📚 Assessments by Skill")

        skill_counts = (
            analytics_df["skill"]
            .value_counts()
        )

        st.bar_chart(skill_counts)

# -----------------------------------
# LEARNER PERFORMANCE
# -----------------------------------

with chart_col2:

    with st.container(border=True):

        st.subheader("🏆 Average Learner Performance")

        learner_scores = (
            analytics_df.groupby(
                "selected_user"
            )["percentage"]
            .mean()
            .sort_values(ascending=False)
        )

        st.bar_chart(learner_scores)

# -----------------------------------
# PERFORMANCE DISTRIBUTION
# -----------------------------------

st.markdown("---")

with st.container(border=True):

    st.subheader("🎯 Performance Distribution")

    performance_counts = (
        analytics_df["performance_band"]
        .value_counts()
    )

    st.bar_chart(performance_counts)

# -----------------------------------
# LEADERBOARD
# -----------------------------------

st.markdown("---")

st.subheader("🥇 Top Learners")

leaderboard_df = (
    analytics_df.groupby(
        "selected_user"
    )["percentage"]
    .mean()
    .reset_index()
)

leaderboard_df.columns = [
    "Learner",
    "Average Score"
]

leaderboard_df = leaderboard_df.sort_values(
    by="Average Score",
    ascending=False
)

st.dataframe(
    leaderboard_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# RECENT ACTIVITY
# -----------------------------------

st.markdown("---")

st.subheader("🕒 Recent Assessment Activity")

recent_df = analytics_df.sort_values(
    by="timestamp",
    ascending=False
).head(10)

display_columns = [
    "timestamp",
    "selected_user",
    "learning_track",
    "skill",
    "score",
    "percentage",
    "performance_band"
]

st.dataframe(
    recent_df[display_columns],
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# SKILL INSIGHTS
# -----------------------------------

st.markdown("---")

st.subheader("🚀 Skill Insights")

skill_summary = (
    analytics_df.groupby("skill")
    .agg(
        Assessments=("skill", "count"),
        Avg_Score=("percentage", "mean")
    )
    .reset_index()
)

skill_summary["Avg_Score"] = (
    skill_summary["Avg_Score"]
    .round(1)
)

skill_summary = skill_summary.sort_values(
    by="Assessments",
    ascending=False
)

st.dataframe(
    skill_summary,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------
# PLATFORM OBSERVATIONS
# -----------------------------------

st.markdown("---")

with st.container(border=True):

    st.subheader("🧠 AI Learning Observations")

    top_skill = (
        analytics_df["skill"]
        .value_counts()
        .idxmax()
    )

    strongest_learner = (
        leaderboard_df.iloc[0]["Learner"]
    )

    st.info(f"""
Most assessed skill area: **{top_skill}**

Top performing learner: **{strongest_learner}**

Average workforce competency score:
**{avg_score}%**

The analytics indicate growing engagement with AI-assisted
enterprise learning and competency evaluation workflows.
""")

# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "SSD DataPath • AI-Powered Learning Intelligence Platform"
)