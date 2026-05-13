import streamlit as st
import pandas as pd
import json
import random

if "assessment_started" not in st.session_state:
    st.session_state.assessment_started = False

if "assessment_completed" not in st.session_state:
    st.session_state.assessment_completed = False

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Skill Assessment",
    layout="wide"
)

# -----------------------------------
# Header
# -----------------------------------

st.title("🧠 Skill Assessment")

st.markdown("""
Evaluate your technical competency through AI-generated assessments.
""")

st.markdown("---")

# -----------------------------------
# Load Data
# -----------------------------------

courses_df = pd.read_csv("data/courses.csv")

with open(
    "data/generated_questions.json",
    "r"
) as file:

    question_bank = json.load(file)

start_test = False

if not st.session_state.get("assessment_started"):
    
    # -----------------------------------
    # Learner Information
    # -----------------------------------

    learner_name = st.text_input(
        "Learner Name"
    )

    learner_email = st.text_input(
        "Email ID"
    )
    
    # -----------------------------------
    # Learning Track Selection
    # -----------------------------------

    learning_tracks = sorted(
        courses_df["career_track"].dropna().unique()
    )

    selected_track = st.selectbox(
        "Select Learning Track",
        learning_tracks
    )

    # -----------------------------------
    # Skill Selection
    # -----------------------------------

    available_skills = sorted(
        courses_df[
            courses_df["career_track"] == selected_track
        ]["skill"].dropna().unique()
    )

    selected_skill = st.selectbox(
        "Select Skill",
        available_skills
    )

    # -----------------------------------
    # Question Count
    # -----------------------------------

    question_count = st.selectbox(
        "Number of Questions",
        [5, 10, 15, 20]
    )

    st.markdown("---")

    # -----------------------------------
    # Start Assessment
    # -----------------------------------

    start_test = st.button(
        "Start Assessment"
    )

# -----------------------------------
# Generate Assessment
# -----------------------------------

if start_test:

    if not learner_name.strip():

        st.error(
            "Please enter learner name."
        )

    elif not learner_email.strip():

        st.error(
            "Please enter email ID."
        )

    elif "@" not in learner_email:

        st.error(
            "Please enter valid email ID."
        )

    elif selected_skill not in question_bank:

        st.error(
            "No assessment questions available for this skill."
        )

    else:

        questions = question_bank[selected_skill]

        random.shuffle(questions)

        selected_questions = questions[:question_count]

        st.session_state.assessment_questions = selected_questions

        st.session_state.current_question = 0

        st.session_state.user_answers = {}

        st.session_state.assessment_completed = False

        st.session_state.selected_track = selected_track

        st.session_state.selected_skill = selected_skill

        st.session_state.learner_name = learner_name

        st.session_state.learner_email = learner_email
        
        st.session_state.assessment_started = True

        st.success(
            "Assessment generated successfully."
        )

# -----------------------------------
# Assessment Engine
# -----------------------------------

if (
    st.session_state.get("assessment_started")
    and not st.session_state.get("assessment_completed")
):

    questions = st.session_state.assessment_questions

    current_index = st.session_state.current_question

    current_question = questions[current_index]

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            f"📘 Learning Track: {st.session_state.selected_track}"
        )

    with col2:
        st.info(
            f"🛠 Skill: {st.session_state.selected_skill}"
        )
    
    with col3:
        st.info(
            f"👤 Learner: {st.session_state.learner_name}"
        )

    st.subheader(
        f"Question {current_index + 1} of {len(questions)}"
    )

    progress = (current_index + 1) / len(questions)

    st.progress(progress)

    st.markdown("")

    st.markdown(f"**{current_question['question']}**")

    previous_answer = st.session_state.user_answers.get(
    current_index
    )

    if previous_answer in current_question["options"]:

        default_index = current_question["options"].index(
            previous_answer
        )

    else:

        default_index = None

    selected_answer = st.radio(
        "Select your answer",
        current_question["options"],
        key=f"question_{current_index}",
        index=default_index
    )

    st.session_state.user_answers[current_index] = selected_answer

    st.markdown("")

    col1, col2, col3 = st.columns(3)

    # -----------------------------------
    # Previous Button
    # -----------------------------------

    with col1:

        if current_index > 0:

            if st.button("Previous"):

                st.session_state.current_question -= 1

                st.rerun()

    # -----------------------------------
    # Next Button
    # -----------------------------------

    with col2:

        if current_index < len(questions) - 1:

            if st.button("Next"):

                st.session_state.current_question += 1

                st.rerun()

    # -----------------------------------
    # Finish Button
    # -----------------------------------

    with col3:

        if st.button("Finish Assessment"):

            score = 0

            results = []

            for index, question in enumerate(questions):

                user_answer = st.session_state.user_answers.get(index)

                correct_answer = question["correct_answer"]

                is_correct = (
                    user_answer == correct_answer
                )

                if is_correct:
                    score += 1

                results.append({
                    "question": question["question"],
                    "user_answer": user_answer,
                    "correct_answer": correct_answer,
                    "is_correct": is_correct,
                    "explanation": question["explanation"]
                })

            st.session_state.final_score = score

            st.session_state.assessment_results = results

            st.session_state.assessment_completed = True

            st.rerun()

def render_result_action_buttons(position):

    col1, col2 = st.columns(2)

    # -----------------------------------
    # Retake Assessment
    # -----------------------------------

    with col1:

        if st.button(
            "🔄 Retake Assessment",
            use_container_width=True,
            type="primary",
            key=f"retake_{position}"
        ):

            st.session_state.assessment_started = True

            st.session_state.assessment_completed = False

            st.session_state.current_question = 0

            st.session_state.user_answers = {}

            st.rerun()

    # -----------------------------------
    # Back To Setup Page
    # -----------------------------------

    with col2:

        if st.button(
            "🏠 Back To Assessment Setup",
            use_container_width=True,
            key=f"setup_{position}"
        ):

            keys_to_remove = [
                "assessment_started",
                "assessment_completed",
                "assessment_questions",
                "current_question",
                "user_answers",
                "assessment_results",
                "final_score",
                "selected_track",
                "selected_skill",
                "learner_name",
                "learner_email"
            ]

            for key in keys_to_remove:

                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()

# -----------------------------------
# Results Screen
# -----------------------------------

if st.session_state.get("assessment_completed"):

    st.markdown("---")

    st.header("📊 Assessment Results")

    score = st.session_state.final_score

    total = len(
        st.session_state.assessment_questions
    )

    percentage = round(
        (score / total) * 100,
        2
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Score",
            f"{score}/{total}"
        )

    with col2:
        st.metric(
            "Percentage",
            f"{percentage}%"
        )

    with col3:

        if percentage >= 80:
            performance = "Excellent"

        elif percentage >= 60:
            performance = "Good"

        else:
            performance = "Needs Improvement"

        st.metric(
            "Performance",
            performance
        )

    render_result_action_buttons("top")

    st.markdown("---")

    st.subheader("Question Review")

    for index, result in enumerate(st.session_state.assessment_results,start=1):

        with st.container(border=True):

            st.markdown(f"**Question {index}:** {result['question']}")

            if result["is_correct"]:

                st.markdown(
                    f"**🟢 Your Answer:** {result['user_answer']}"
                )

                st.markdown(
                    f"**🟢 Correct Answer:** {result['correct_answer']}"
                )

            else:

                st.markdown(
                    f"**🔴 Your Answer:** {result['user_answer']}"
                )

                st.markdown(
                    f"**🟢 Correct Answer:** {result['correct_answer']}"
                )

            if result["is_correct"]:

                st.success("Correct")

            else:

                st.error("Incorrect")

            st.info(result["explanation"])

    st.markdown("---")

    render_result_action_buttons("bottom")

