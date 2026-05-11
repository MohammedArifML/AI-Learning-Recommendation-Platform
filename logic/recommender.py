import pandas as pd

def load_courses():

    df = pd.read_csv("data/courses.csv")

    return df


def recommend_courses(
    career_track,
    selected_skills,
    learning_style
):

    df = load_courses()

    filtered_df = df[
        (df["career_track"] == career_track)
        &
        (df["learning_style"] == learning_style)
    ]

    if selected_skills:

        filtered_df = filtered_df[
            filtered_df["skill"].isin(selected_skills)
        ]

    return filtered_df