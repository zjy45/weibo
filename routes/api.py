from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    session,
    send_from_directory,
)
from models.user import User
from models.weibo import Weibo
from utils import log


def current_user():
    uid = session.get('user_id', -1)
    u = User.find_by(id=uid)
    return u

main = Blueprint('api', __name__)


@main.route('/')
def index():
    all_weibo = Weibo.find_all(deleted=False)
    return render_template('weibo/weibo.html', weibo=all_weibo)