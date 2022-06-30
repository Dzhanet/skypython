import json
from json import JSONDecodeError


def load_data_json():
    """загружает данные из data.json в список"""

    try:
        with open('data/data.json', encoding='utf-8') as f:
            data = json.load(f)

    except(FileNotFoundError, JSONDecodeError):
        return "Не удается получить данные из data.json"

    return data

def load_comments_json():
    """загружает данные из comments.json в список"""
    try:
        with open('data/comments.json', encoding='utf-8') as f:
            data = json.load(f)

    except(FileNotFoundError, JSONDecodeError):
        return "Не удается получить данные из data.json"

    return data

def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""

    data = load_data_json()
    post_of_user = []

    if user_name is not None:
        for post in data:
            if user_name == post['poster_name']:
                post_of_user.append(post)
        return post_of_user
    if user_name is None:
        raise ValueError

def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""

    data = load_comments_json()
    comments_by_post_id = []

    if post_id is not None:
        for comments in data:
            if post_id == comments['post_id']:
                comments_by_post_id.append(comments)
            else:
                raise ValueError
        return comments_by_post_id
    if post_id is None:
        raise ValueError

def search_for_posts(query):
    """возвращает список постов по ключевому слову"""

    posts = load_data_json()
    posts_with_query = []
    for post in posts:
        if query in post['content']:
            posts_with_query.append(post)

    return posts_with_query

def single_post(id):
    """Возвращает пост с определенным pk"""

    posts = load_data_json()
    single_post = []
    for post in posts:
        if id == post["pk"]:
            single_post.append(post)
    return single_post
