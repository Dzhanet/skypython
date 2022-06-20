from flask import Flask, request, render_template, send_from_directory


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

# Импортируем блюпринты из их пакетов
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

# Ограничиваем размер файла здесь
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)



if __name__ == "__main__":
    app.run()

