import json

#объявим константы
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


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


def load_post(post):
    """Добавит список постов в posts.json"""

    with open('posts.json', 'r', encoding='utf-8') as f:
        dictionary = json.load(f)

    with open('posts.json', 'w', encoding='utf-8') as f:
        dictionary.append(post)
        json.dump(dictionary, f, ensure_ascii=False)


def is_filename_allowed(filename):
    """Проверяем файл на расширения"""

    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False

def save_uploaded_picture(picture):
    """сохраняет картинку от юзера в uploads/images"""

    # Получаем имя файла у загруженного файла
    filename = picture.filename
    if is_filename_allowed(filename):
        # Сохраняем картинку под родным именем в папку uploads
        picture.save(f"./uploads/images/{filename}")
        return f"./uploads/images/{filename}"
    else:
        return "Загруженный файл не в формате jpeg или png, мы вредные, принимаем только их"