from os import abort
from flask import Blueprint, render_template, request
from werkzeug.exceptions import NotFound

from utils import load_data_json, get_posts_by_user, get_comments_by_post_id, search_for_posts

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

@posts_blueprint.route('/')
def page_index():
    """Страничка со всеми постами"""

    all_posts = load_data_json()
    return render_template("index.html", posts=all_posts)

@posts_blueprint.route('/posts/<int:pk>/')
def single_post(pk):
    """Страничка одного поста"""

    post = single_post(pk)
    if post is None:
        abort(404)
    comments = get_comments_by_post_id(pk)
    len_comments = len(comments)

    return render_template('post.html', post=post, comments=comments, len_comments=len_comments)

@posts_blueprint.route('/search/')
def search_page():
    """Страничка с результатами поиска по ключевому слову"""

    s = request.args.get('s')
    if s:
        posts_with_tag = search_for_posts(s)
        len_posts = len(posts_with_tag)
        return render_template("search.html", s=s, posts=posts_with_tag,len_posts=len_posts)
    else:
        raise NotFound


@posts_blueprint.route('/users/<username>')
def user_posts(username):
    """Страничка с постами конкретного пользователя"""

    