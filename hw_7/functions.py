import json


def load_students():
    """load students from students.json"""

    file = open("students.json")
    students = json.load(file)
    file.close()
    return students


def load_professions():
    """load professions from professions.json"""

    file = open("professions.json")
    professions = json.load(file)
    file.close()
    return professions


def get_student_by_pk(pk):
    """find student with pk and return dict with information"""

    student_dict = load_students()
    for student in student_dict:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title):
    """find profession with title and return dict with information"""

    profession_dict = load_professions()
    for profession in profession_dict:
        if profession["title"] == title:
            return profession


def check_fitness(student_skills, profession_skills):
    """check intersection and return in key has, luks, fit_percent"""


    has = student_skills.intersection(profession_skills)
    lucks = profession_skills.difference(student_skills)
    percent_fit = round(((len(has)) / len(profession_skills) * 100))

    return {"has": list(has),
            "lucks": list(lucks),
            "percent_fit": percent_fit
            }



