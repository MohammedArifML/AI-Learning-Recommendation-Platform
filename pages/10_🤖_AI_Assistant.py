import streamlit as st
from logic.ai_assistant import ask_ai_assistant
import pandas as pd

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

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

st.sidebar.success(
    "Use the navigation menu to access platform modules."
)

# -----------------------------------
# LOAD CSS
# -----------------------------------

def load_css():
    with open("styles/government_theme.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

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

/* Chat container spacing */
[data-testid="stChatMessage"] {
    padding-top: 10px;
    padding-bottom: 10px;
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

st.title("🤖 SSD ALIP AI Assistant")

st.markdown("""
Ask questions about:
- learning tracks
- technical skills
- learning recommendations
- assessments
- workforce analytics
- SSD ALIP platform capabilities
""")

st.info("""
Welcome to SSD ALIP AI Assistant.

This enterprise AI assistant can help you understand:
- supported learning tracks
- platform capabilities
- AI-powered assessments
- learning analytics
- workforce learning intelligence
""")

st.markdown("---")

# -----------------------------------
# SUGGESTED QUESTIONS
# -----------------------------------

st.subheader("💡 Suggested Questions")

suggestions = [
    "What learning tracks are available?",
    "Recommend beginner Azure learning paths.",
    "What assessment capabilities exist?",
    "Which skills are supported?",
    "What AI features are available?",
    "What analytics capabilities exist?"
]

col1, col2 = st.columns(2)

for index, question in enumerate(suggestions):

    target_col = col1 if index % 2 == 0 else col2

    with target_col:

        if st.button(
            question,
            use_container_width=True
        ):

            st.session_state.selected_prompt = question

# -----------------------------------
# CLEAR CHAT
# -----------------------------------

clear_col1, clear_col2 = st.columns([1, 5])

with clear_col1:

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

st.markdown("---")

# -----------------------------------
# CHAT INPUT
# -----------------------------------

user_question = st.chat_input(
    "Ask SSD ALIP AI Assistant..."
)

# -----------------------------------
# HANDLE SUGGESTED PROMPTS
# -----------------------------------

if "selected_prompt" in st.session_state:

    user_question = st.session_state.selected_prompt

    del st.session_state.selected_prompt

# -----------------------------------
# PROCESS USER QUESTION
# -----------------------------------

if user_question:

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.spinner("Analyzing request..."):

        try:

            response = ask_ai_assistant(user_question)
            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })

        except Exception as e:

            response = f"""
AI Assistant encountered an error.

Details:
{str(e)}
"""

# -----------------------------------
# RENDER CHAT HISTORY
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
# -----------------------------------
# FOOTER
# -----------------------------------

st.markdown("---")

st.caption(
    "SSD DataPath • AI-Powered Learning Intelligence Platform"
)