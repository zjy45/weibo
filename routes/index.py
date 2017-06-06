from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    session,
    send_from_directory,
)
from werkzeug.utils import secure_filename
from config import user_file_director
import os
from models.user import User
from utils import log


def current_user():
    uid = session.get('user_id', -1)
    u = User.find_by(id=uid)
    return u


main = Blueprint('index', __name__)


@main.route('/')
def index():
    u = current_user()
    return render_template('index.html', user=u)


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        return redirect(url_for('.index'))
    else:
        print('u', u)
        session['user_id'] = u.id
        print('session', session)
        return redirect(url_for('weibo.index'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User.validate_register(form)
    return redirect(url_for('.index'))


@main.route('/123')
def one():
    return render_template('123.html')


@main.route('/profile')
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    return render_template('profile.html', user=u)


def allow_file(filename):
    suffix = filename.split('.')[-1]
    from config import accept_user_file_type
    return suffix in accept_user_file_type


@main.route('/addimg', methods=["POST"])
def add_img():
    u = current_user()

    if u is None:
        return redirect(url_for(".profile"))

    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if allow_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(user_file_director, filename))
        u.user_image = filename
        u.save()

    return redirect(url_for(".profile"))


# send_from_directory
# nginx 静态文件
@main.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(user_file_director, filename)


@main.context_processor
def include_user_class():
    return {'User': User}