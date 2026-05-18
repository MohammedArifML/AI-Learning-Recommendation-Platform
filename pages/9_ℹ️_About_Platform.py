import streamlit as st
import pandas as pd

# Page Config
# -----------------------------------

st.set_page_config(
    page_title="SSD DataPath",
    page_icon="🧭",
    layout="wide"
)

# ------------------------------------------------------
# LOAD GOVERNMENT THEME CSS
# ------------------------------------------------------

with open("styles/government_theme.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
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

# ------------------------------------------------------
# CUSTOM HEADER
# ------------------------------------------------------

st.markdown(
    """
    <div style='padding: 1rem 0;'>
        <h1 style='color:#8A1538;'>AI-powered learning intelligence platform</h1>
        <h4 style='color:gray;'>Pilot AI-Powered Workforce Learning & Assessment Ecosystem</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    "Current Status: Pilot / Proof of Concept Demonstration Platform"
)

# ------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------

st.markdown("## Executive Summary")

summary_col1, summary_col2 = st.columns([2, 1])

with summary_col1:
    st.markdown(
        """
        This platform demonstrates how Artificial Intelligence can be utilized to modernize organizational learning, employee upskilling, intelligent assessments, and workforce capability development.

        The application combines AI-powered assessment generation, personalized learning recommendations, analytics, and employee-focused learning workflows into a unified pilot ecosystem.

        The primary objective of the platform is to showcase the future potential of AI-assisted learning systems within enterprise and government environments.
        """
    )

with summary_col2:
    st.container(border=True)

    st.metric("Platform Type", "AI Pilot")
    st.metric("Frontend", "Streamlit")
    st.metric("Primary Language", "Python")
    st.metric("AI Integration", "OpenAI GPT")

st.divider()

# ------------------------------------------------------
# PLATFORM CAPABILITIES
# ------------------------------------------------------

st.markdown("## Core Platform Capabilities")

cap_col1, cap_col2, cap_col3 = st.columns(3)

with cap_col1:
    st.container(border=True)

    st.markdown("### 🎯 Learning Recommendations")

    st.markdown(
        """
        - Personalized learning suggestions
        - Skill-based recommendations
        - Career-aligned courses
        - Difficulty-based filtering
        - Category-wise learning paths
        - Learning style customization
        """
    )

with cap_col2:
    st.container(border=True)

    st.markdown("### 🧠 AI Assessment Engine")

    st.markdown(
        """
        - AI-generated assessments
        - Dynamic question generation
        - Multi-level difficulty support
        - Instant evaluation
        - Assessment scoring
        - Interactive workflows
        """
    )

with cap_col3:
    st.container(border=True)

    st.markdown("### 📊 Analytics & Insights")

    st.markdown(
        """
        - Learner performance metrics
        - Recommendation insights
        - Assessment analytics
        - Skill tracking
        - Learning dashboards
        - Future predictive analytics
        """
    )

st.divider()

# ------------------------------------------------------
# AI FEATURES TABLE
# ------------------------------------------------------

st.markdown("## AI Feature Matrix")

ai_features = pd.DataFrame({
    "AI Capability": [
        "Assessment Generation",
        "Recommendation Engine",
        "Adaptive Learning Logic",
        "Skill Mapping",
        "Future AI Mentor",
        "Predictive Analytics"
    ],
    "Current Status": [
        "Implemented",
        "Implemented",
        "Pilot Logic",
        "Planned",
        "Planned",
        "Planned"
    ],
    "Business Objective": [
        "Automated Assessments",
        "Personalized Learning",
        "Adaptive Learning Experience",
        "Competency Development",
        "Employee Guidance",
        "Learning Intelligence"
    ]
})

st.dataframe(
    ai_features,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ------------------------------------------------------
# TECH STACK SECTION
# ------------------------------------------------------

st.markdown("## Technology Stack")

tech_df = pd.DataFrame({
    "Layer": [
        "Frontend",
        "Backend",
        "AI Integration",
        "Data Processing",
        "UI Styling",
        "Deployment"
    ],
    "Technology": [
        "Streamlit",
        "Python",
        "OpenAI GPT Models",
        "Pandas",
        "Custom CSS",
        "Streamlit Community Cloud"
    ],
    "Purpose": [
        "Interactive UI",
        "Application Logic",
        "AI Question Generation",
        "Data Manipulation",
        "Government Theme Styling",
        "Pilot Hosting"
    ]
})

st.dataframe(
    tech_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ------------------------------------------------------
# ARCHITECTURE OVERVIEW
# ------------------------------------------------------

st.markdown("## Solution Architecture")

arch_col1, arch_col2 = st.columns([1, 1])

with arch_col1:
    st.markdown("### Application Flow")

    st.code(
        """
User Interaction
       ↓
Streamlit Frontend
       ↓
Recommendation Engine
       ↓
AI Assessment Generator
       ↓
Analytics & Evaluation
       ↓
Result Dashboard
        """
    )

with arch_col2:
    st.markdown("### Modular Components")

    st.code(
        """
/pages
/logic
/data
/styles
/utils
/assets
        """
    )

st.divider()

# ------------------------------------------------------
# BUSINESS VALUE
# ------------------------------------------------------

st.markdown("## Organizational Value")

value_col1, value_col2 = st.columns(2)

with value_col1:
    st.container(border=True)

    st.markdown("### 🚀 Strategic Benefits")

    st.markdown(
        """
        - Supports workforce upskilling
        - Accelerates digital transformation
        - Enhances learning experiences
        - Reduces manual assessment efforts
        - Encourages continuous learning culture
        - Enables AI-assisted capability development
        """
    )

with value_col2:
    st.container(border=True)

    st.markdown("### 🏛️ Potential Government Use Cases")

    st.markdown(
        """
        - Employee training programs
        - Technical skill development
        - Internal learning ecosystems
        - AI-assisted assessments
        - Department-level learning analytics
        - Workforce capability intelligence
        """
    )

st.divider()

# ------------------------------------------------------
# ROADMAP SECTION
# ------------------------------------------------------

st.markdown("## Future Roadmap")

roadmap_data = {
    "Enhancement": [
        "Microsoft Teams Integration",
        "Single Sign-On (SSO)",
        "Learning Management System Integration",
        "Arabic Language Support",
        "AI Learning Assistant",
        "Skill Gap Analysis",
        "Advanced Analytics Dashboard",
        "Certification Tracking"
    ],
    "Priority": [
        "High",
        "High",
        "High",
        "Medium",
        "Medium",
        "High",
        "Medium",
        "Medium"
    ],
    "Planned Phase": [
        "Phase 2",
        "Phase 2",
        "Phase 3",
        "Phase 3",
        "Phase 3",
        "Phase 2",
        "Phase 2",
        "Phase 3"
    ]
}

roadmap_df = pd.DataFrame(roadmap_data)

st.dataframe(
    roadmap_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ------------------------------------------------------
# GOVERNANCE SECTION
# ------------------------------------------------------

st.markdown("## Governance & Security Considerations")

gov_col1, gov_col2, gov_col3 = st.columns(3)

with gov_col1:
    st.container(border=True)

    st.markdown("### 🔐 Security")

    st.markdown(
        """
        - Enterprise authentication
        - Secure API handling
        - Access management
        - Session controls
        """
    )

with gov_col2:
    st.container(border=True)

    st.markdown("### 📜 Governance")

    st.markdown(
        """
        - AI governance policies
        - Audit logging
        - Compliance alignment
        - Responsible AI usage
        """
    )

with gov_col3:
    st.container(border=True)

    st.markdown("### ☁️ Scalability")

    st.markdown(
        """
        - Cloud deployment readiness
        - Modular architecture
        - Expandable AI services
        - Enterprise integration support
        """
    )

st.divider()

# ------------------------------------------------------
# DEVELOPMENT METRICS
# ------------------------------------------------------

st.markdown("## Platform Snapshot")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Pages", "8+")

with metric_col2:
    st.metric("AI Features", "5+")

with metric_col3:
    st.metric("Architecture", "Modular")

with metric_col4:
    st.metric("Status", "Pilot")

st.divider()

# -----------------------------------
# Footer
# -----------------------------------

st.caption(
    "SSD DataPath • AI-Powered Learning Intelligence Platform"
)