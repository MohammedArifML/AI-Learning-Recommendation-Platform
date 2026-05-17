import pandas as pd

def load_courses():

    df = pd.read_csv("data/courses.csv")

    return df


def recommend_courses(
    career_track,
    selected_skills,
    learning_style,
    selected_difficulty="All",
    selected_category="All"
):

    df = load_courses()

    filtered_df = df[
        df["career_track"] == career_track
    ]

    if learning_style != "All":

        filtered_df = filtered_df[
            filtered_df["learning_style"]
            == learning_style
        ]

    if selected_skills:

        filtered_df = filtered_df[
            filtered_df["skill"].isin(selected_skills)
        ]
    
    if selected_difficulty != "All":

        filtered_df = filtered_df[
            filtered_df["difficulty_level"]
            == selected_difficulty
        ]

    if selected_category != "All":

        filtered_df = filtered_df[
            filtered_df["platform_category"]
            == selected_category
        ]

    return filtered_df