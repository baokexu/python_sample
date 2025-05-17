import json
import os

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_student(group, name, scores):
    data = load_data()
    if group not in data:
        data[group] = {}
    data[group][name] = scores
    save_data(data)
    print(f"Added {name} to {group}.")


def show_scores(group=None):
    data = load_data()
    if group:
        if group in data:
            print(f"Scores in {group}:")
            for name, scores in data[group].items():
                print(f"  {name}: {scores}")
        else:
            print(f"Group {group} not found.")
    else:
        print("All Scores:")
        for grp, students in data.items():
            print(f"Group {grp}:")
            for name, scores in students.items():
                print(f"  {name}: {scores}")


def update_score(group, name, subject, new_score):
    print('TODO: please provide code to update score')


def delete_student(group, name):
    print('TODO: please provide code to delete student')


def show_student(group, name):
    print('TODO: please provide code to show the score for a student')


def show_students_count(group):
    print('TODO: please provide code to show the count of  students in a group')


def get_average(subject, group=None):
    data = load_data()
    total = 0
    count = 0
    groups = [group] if group else data.keys()
    for grp in groups:
        for scores in data.get(grp, {}).values():
            if subject in scores:
                total += scores[subject]
                count += 1
    if count > 0:
        print(f"Average {subject} score: {total / count:.2f}")
    else:
        print(f"No scores found for subject {subject}.")


def get_top_student(subject, group=None):
    data = load_data()
    top_name = None
    top_score = -1
    groups = [group] if group else data.keys()
    for grp in groups:
        for name, scores in data.get(grp, {}).items():
            if subject in scores and scores[subject] > top_score:
                top_score = scores[subject]
                top_name = name
    if top_name:
        print(f"Top student in {subject}: {top_name} ({top_score})")
    else:
        print(f"No scores found for subject {subject}.")
