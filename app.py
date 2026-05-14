import streamlit as st

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="SSD DataPath",
    page_icon="📘",
    layout="wide"
)

st.sidebar.image(
    "assets/logo.png",
    width=260
)

# -----------------------------------
# Sidebar Branding
# -----------------------------------

st.sidebar.markdown("---")

# -----------------------------------
# Hero Section
# -----------------------------------

st.markdown("""
# 📘 SSD DataPath

### AI-Powered Learning Intelligence Platform
""")

st.markdown("""
Personalized learning recommendations, AI-powered assessments,
and enterprise skill intelligence for SSD data professionals.
""")

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

        st.markdown("## 📚 Learning Recommendations")

        st.markdown("""
Discover personalized learning paths, curated courses,
and AI-enriched recommendations across modern data
engineering, analytics, cloud, and enterprise platforms.
""")

        st.info("""
✔ AI-generated course summaries

✔ Personalized learning guidance

✔ Curated enterprise learning resources

✔ Multi-platform learning ecosystem
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

✔ Personalized assessment workflows
""")

st.markdown("---")

# -----------------------------------
# Supported Technologies
# -----------------------------------

st.markdown("## 🚀 Supported Learning Domains")

domains_col1, domains_col2, domains_col3 = st.columns(3)

with domains_col1:

    st.success("""
- SQL
- Python
- Spark / PySpark
- Databricks
- Informatica IDMC
""")

with domains_col2:

    st.success("""
- Power BI
- Oracle BI
- Statistical Analysis
- Oracle APEX Development
""")

with domains_col3:

    st.success("""
- OCI Core Services
- OCI Architecture
- OCI Autonomous Database
- Oracle AI & Analytics
""")

st.markdown("---")

# -----------------------------------
# Platform Vision
# -----------------------------------

with st.container(border=True):

    st.markdown("## 🎯 Platform Vision")

    st.markdown("""
SSD DataPath is designed to support workforce upskilling,
continuous learning, and enterprise capability development
through AI-powered learning intelligence and competency assessment.

The platform combines:
- learning recommendations
- assessment intelligence
- skill-gap evaluation
- AI-generated educational content

into a unified workforce learning ecosystem.
""")

st.markdown("---")

# -----------------------------------
# Footer
# -----------------------------------

st.caption(
    "SSD DataPath • AI-Powered Learning Intelligence Platform"
)