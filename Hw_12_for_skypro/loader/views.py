# Сперва импорттируем класс блюпринта
from flask import Blueprint, render_template, request, send_from_directory
from functions import is_filename_allowed
# Затем создаем новый блюпринт, выбираем для него имя

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates') #добавим настройку папки с шаблонами


# Создаем вьюшку, используя в декораторе блюпринт вместо app

@loader_blueprint.route("/post/", methods=["GET","POST"])
def page_post_form():

    return render_template('post_form.html')


@loader_blueprint.route("/post/", methods=["POST"])
def page_post_upload():
    # Получаем объект картинки и текст из форм
    picture = request.files.get("picture")
    content = request.files.get("content")
    # проверка на существование картинки
    if picture:
        # Получаем имя файла у загруженного файла
        filename = picture.filename
        if is_filename_allowed(filename):
            # Сохраняем картинку под родным именем в папку uploads
            picture.save(f"../uploads/images{filename}")
            return render_template('post_uploaded.html', picture=picture,content=content)
        else:
            return "Загруженный файл не в формате jpeg или png, мы вредные, принимаем только их"
    else:
        return "Ошибка загрузки"



@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)