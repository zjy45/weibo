from .index import *
from models.user import User
from models.weibo import Weibo
from utils import log


def current_user():
    uid = session.get('user_id', -1)
    u = User.find_by(id=uid)
    return u

main = Blueprint('weibo', __name__)


@main.route('/')
def index():
    all_weibo = Weibo.find_all(deleted=False)
    return render_template('weibo/weibo.html', weibo=all_weibo)


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
        return redirect(url_for('.index'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User.validate_register(form)
    return redirect(url_for('.index'))


@main.route('/new')
def new():
    return render_template('weibo/weibo_new.html')


@main.route('/add', methods=['post'])
def add():
    u = current_user()
    form = request.form
    Weibo.new(form, user_id=u.id)
    return redirect(url_for('.index'))


@main.route('/delete')
def delete():
    id = int(request.args.get('id'))
    w = Weibo.find(id)
    if current_user().id == w.user_id:
        w.delete()
    return redirect(url_for('.index'))


@main.context_processor
def include_user_class():
    u = current_user()
    return {'U': u}




