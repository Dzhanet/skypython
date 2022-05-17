import utils
from flask import Flask

app = Flask(__name__)


@app.route("/")
def candidates_data():
    candidates = utils.load_candidates_data()
    all_candidates = ""
    for candidate in candidates:
        all_candidates += f"Имя кандидата - {candidate['name']}\n"
        all_candidates += f"Позиция кандидата - {candidate['position']}\n"
        all_candidates += f"Навыки кандидата - {candidate['skills']}\n"

    return f"<pre>{all_candidates}</pre>"


@app.route("/candidates/<int:user_id>")
def candidate_with_photo(user_id):
    candidates = utils.load_candidates_data()
    candidate = ""
    for item in candidates:
        if item['id'] == user_id:
            candidate += f"<img src='{item['picture']}'>\n"
            candidate += f"Имя кандидата - {item['name']}\n"
            candidate += f"Позиция кандидата - {item['position']}\n"
            candidate += f"Навыки кандидата - {item['skills']}\n"

    return f"<pre>{candidate}</pre>"

@app.route("/skills/<skill>")
def candidate_with_skill(skill):
    candidates = utils.load_candidates_data()
    candidate = ""
    for item in candidates:
        new_skills = item['skills'].split(",")
        if skill in new_skills:
            candidate += f"Имя кандидата - {item['name']}\n"
            candidate += f"Позиция кандидата - {item['position']}\n"
            candidate += f"Навыки кандидата - {item['skills']}\n"

    return f"<pre>{candidate}</pre>"



app.run(debug=True)

