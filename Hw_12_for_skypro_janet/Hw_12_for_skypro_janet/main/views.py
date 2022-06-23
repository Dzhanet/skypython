# Сперва импорттируем класс блюпринта
from flask import Blueprint, render_template, request
from functions import search_posts
from logger import file_handler
# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates') #добавим настройку папки с шаблонами

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def page_index():

    return render_template("index.html")

@main_blueprint.route('/search/')
def page_tag():
    s = request.args.get('s') #получаем данные из адресной строки (переменную, переда-ю из index.html в адр методом гет
    if s:
        posts_with_tag = search_posts(s) #получаем список словарей с постами по тегу от юзера
        return render_template("post_list.html", s=s, items=posts_with_tag) #items-словарь, к-й пребирает в шаблоне
    else:
        file_handler.info('Пользователь ничего не ввел')