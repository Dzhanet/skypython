# Сперва импорттируем класс блюпринта
from flask import Blueprint, render_template, request, send_from_directory
from ..functions import is_filename_allowed, load_post
from ..logger import file_handler
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
    content = request.values.get("content")
    # проверка на существование картинки
    if picture:
        # Получаем имя файла у загруженного файла
        filename = picture.filename
        if is_filename_allowed(filename):
            # Сохраняем картинку под родным именем в папку uploads
            path_to_save = f"./uploads/images/{filename}"
            picture.save(path_to_save)
            #начинаем работу с текстом от юзера
            #создаем словарь с постом и добавим его в posts.json
            post = {'pic': path_to_save, 'content': content}
            load_post(post)
            return render_template('post_uploaded.html', filename=filename, content=content)
        else:
            file_handler.info('Загружен файл в другом формате')
            return "Загруженный файл не в формате jpeg или png, мы вредные, принимаем только их"
    else:
        file_handler.error('файл не был загружен')
        return "Ошибка загрузки"




@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
