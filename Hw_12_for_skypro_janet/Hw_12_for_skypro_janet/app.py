from flask import Flask
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging
import logger


logger = logging.getLogger('basiq')

# Импортируем блюпринты из их пакетов

app = Flask(__name__)

#конфигурация
app.config['POST_PATH'] = "posts.json"
app.config['UPLOAD_FOLDER'] = "uploads/images"

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
