# файл с функциями

import json


def load_candidates_from_json():
    """возвращает список всех кандидатов из candidates.json"""

    file = open("candidates.json", "r", encoding="utf-8")
    candidates = json.load(file)
    file.close()
    return candidates


def get_candidate(candidate_id):
    """возвращает одного кандидата по ключу'id'"""

    candidates = load_candidates_from_json()
    for item in candidates:
        if item['id'] == int(candidate_id):
            return item




def get_candidates_by_name(candidate_name):
    """возвращает кандидата/ов по имени, по ключу 'name'"""

    candidates = load_candidates_from_json()
    each_candidate_list = []
    for item in candidates:
        if candidate_name.lower() in item['name'].lower():
            each_candidate_list.append(item)
    return each_candidate_list



def get_candidates_by_skill(skill_name):
    """возвращает кандидата/кандидатов по навыку по ключу 'skills'"""

    candidates = load_candidates_from_json()
    each_candidate_list = []
    for item in candidates:
        if skill_name.lower() in item['skills'].lower():
            each_candidate_list.append(item)
    return each_candidate_list