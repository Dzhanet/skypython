import json


def load_candidates_data():
    """Загружаем все данные из candidates.json в список"""

    file = open("candidates.json","r",encoding="utf-8")
    candidates = json.load(file)
    file.close()
    return candidates

print(load_candidates_data())
