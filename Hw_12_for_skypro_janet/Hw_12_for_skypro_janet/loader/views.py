import logging
from flask import Blueprint, render_template, request, send_from_directory
from functions import load_post, save_uploaded_picture
from logger import file_handler
import os
# Затем создаем новый блюпринт, выбираем для него имя

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates') #добавим настройку папки с шаблонами

# Создаем вьюшку, используя в декораторе блюпринт вместо app

@loader_blueprint.route("/post/", methods=["GET"])
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route("/post_uploaded/", methods=["POST"])
def page_post_upload():
    # Получаем объект картинки и текст из форм
    picture = request.files.get("picture")
    content = request.form.get("content")
    # проверка на существование картинки
    if not picture or content:
        return "Ошибка загрузки"

    try:
        picture_path = save_uploaded_picture(picture)

    except FileNotFoundError:
        return "Не удалось сохранить файл, путь не найден"

    picture_url = "/"+picture_path
    #начинаем работу с текстом от юзера
    #создаем словарь с постом и добавим его в posts.json
    post = {'pic': picture_url, 'content': content}
    load_post(post)
    return render_template('post_uploaded.html', filename=picture_url, content=content)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
