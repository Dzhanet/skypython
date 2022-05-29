# главный файл, который запускает программу
import hw_11_part_2.utils
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")  # представление всех кандидатов на главной странице
def show_all_candidate():
    all_candidates = hw_11_part_2.utils.load_candidates_from_json()
    return render_template('list.html', all_candidates=all_candidates)

@app.route("/candidates/<int:user_id>") # представление кандидата по номеру id
def search_candidate_id(user_id):
    candidate = hw_11_part_2.utils.get_candidate(user_id)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>") #представление кандидата по имени
def search_candidate_name(candidate_name):
    candidates = hw_11_part_2.utils.get_candidates_by_name(candidate_name)
    len_candidate = len(candidates)
    return render_template('search.html', candidates=candidates, len_candidate=len_candidate)


@app.route("/skill/<skill_name>") #представление кандидата для поиска по скиллу
def search_candidate_with_skill(skill_name):
    candidates = hw_11_part_2.utils.get_candidates_by_skill(skill_name)
    len_candidate = len(candidates)
    skill_from_user = skill_name
    return render_template('skill.html', candidates=candidates, len_candidate=len_candidate, skill_from_user=skill_from_user)



app.run(debug=True)