import json


def load_roadmaps():

    with open("data/roadmaps.json", "r") as file:

        roadmaps = json.load(file)

    return roadmaps


def generate_roadmap(career_track):

    roadmaps = load_roadmaps()

    return roadmaps.get(career_track, [])