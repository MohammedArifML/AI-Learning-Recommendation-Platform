import streamlit as st
from logic.ai_assistant import ask_ai_assistant

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

#-----------------------------------
# Page Config
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
# HEADER
# -----------------------------------

st.title("🔮 ALIP Chatbot")

st.markdown("""
AI assistant for workforce learning, assessments, analytics, and platform intelligence.
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
            use_container_width=True,
            key=question
        ):

            st.session_state.selected_prompt = question

# -----------------------------------
# CLEAR CHAT
# -----------------------------------

clear_col1, clear_col2 = st.columns([1, 5])

with clear_col1:

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.pending_question = None

        st.rerun()

st.markdown("---")

# -----------------------------------
# CHAT INPUT
# -----------------------------------

user_question = st.chat_input(
    "Ask SSD ALIP AI Assistant..."
)

# -----------------------------------
# SAVE QUESTION IMMEDIATELY
# -----------------------------------

if user_question:

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    st.session_state.pending_question = (
        user_question
    )

    st.rerun()

# -----------------------------------
# RENDER CHAT HISTORY
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------------------
# HANDLE SUGGESTED PROMPTS
# -----------------------------------

if "selected_prompt" in st.session_state:

    selected_question = (
        st.session_state.selected_prompt
    )

    st.session_state.messages.append({
        "role": "user",
        "content": selected_question
    })

    st.session_state.pending_question = (
        selected_question
    )

    del st.session_state.selected_prompt

    st.rerun()

# RENDER CHAT HISTORY

# -----------------------------------
# PROCESS PENDING QUESTION
# -----------------------------------

if st.session_state.pending_question:

    pending_question = (
        st.session_state.pending_question
    )

    with st.chat_message("assistant"):

        with st.spinner("Analyzing request..."):

            try:

                response = ask_ai_assistant(
                    pending_question,
                    st.session_state.messages
                )

            except Exception as e:

                response = f"""
AI Assistant encountered an error.

Details:
{str(e)}
"""

        st.write(response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Clear pending state
    st.session_state.pending_question = None

    st.rerun()

