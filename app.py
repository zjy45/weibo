from flask import Flask
import config


app = Flask(__name__)
app.secret_key = config.secret_key

from routes.index import main as index_routes
from routes.weibo import main as weibo_routes
from routes.reply import main as reply_routes
from routes.api import main as api_routes

app.register_blueprint(index_routes)
app.register_blueprint(weibo_routes, url_prefix='/weibo')
app.register_blueprint(reply_routes, url_prefix='/reply')
app.register_blueprint(api_routes, url_prefix='/api')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )

app.run(**config)



'''
1.登录页
2.weibo主页面
    1.添加weibo
    2.显示weibo 删除
    3.用户栏
    4.评论

3.个人主页
    1.信息
    2.上传图片



<!-- <div>
    {% for w in weibo %}
    <div class="weibo-list">
        <a>
            <img class=head-img src={{ '/uploads/' + w.user().user_image + '?v=3&amp;s=120' }}title="atian25"/>
        </a>
        {{w.user().username}}
        <div>
            {{w.title}}
        </div>
        <div>
            {{w.content}}
        </div>
        <form method="post" action={{url_for('reply.add', w_id=w.id)}}>
            <input type="text" name="content" placeholder="评论内容">
            <button>评论</button>
        </form>
        {% for r in w.replys() %}
        <div>
            {{r.content}} @ {{ r.user().username }}
            <form method="post" action={{url_for('reply.update', reply_id=r.id)}}>
                <input type="text" name="content" placeholder="编辑评论">
                <button>编辑</button>
            </form>
            <a href={{ url_for('reply.delete', reply_id=r.id)}}>删除评论</a>
        </div>
        <a href="{{ url_for('.delete', id=w.id)}}">删除</a>
        {% endfor %}
    </div> -->
    {% endfor %}
'''