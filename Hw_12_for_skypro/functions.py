import json
from pprint import pp

from flask import jsonify


def load_json():
    """загружает данные из posts.json в список"""

    with open('posts.json', encoding='utf-8') as f:
        data = json.load(f)
        return data


def search_posts(tag):
    """Поиск по тегу постов"""

    posts = load_json()  # получили словарь!

    posts_with_tag = []
    for post in posts:
        if tag in post['content']:
            posts_with_tag.append(post)
    return posts_with_tag


# pp(search_posts('с'))

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def is_filename_allowed(filename):
    """Проверяем файл на расширения"""

    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False
