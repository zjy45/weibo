from .index import *
from models.user import User
from models.reply import Reply
from utils import log


def current_user():
    uid = session.get('user_id', -1)
    u = User.find_by(id=uid)
    return u

main = Blueprint('reply', __name__)


@main.route('/add/<int:w_id>', methods=['post'])
def add(w_id):
    u = current_user()
    form = request.form
    Reply.new(form, user_id=u.id, weibo_id=w_id)
    return redirect(url_for('weibo.index'))


@main.route('/delete')
def delete():
    id = int(request.args.get('reply_id'))
    r = Reply.find(id)
    if current_user().id == r.user_id:
        r.delete()
    return redirect(url_for('weibo.index'))


@main.route('/update/<int:reply_id>', methods=["post"])
def update(reply_id):
    r = Reply.find(reply_id)
    if current_user().id == r.user_id:
        form = request.form
        r.update(form)
    return redirect(url_for('weibo.index'))