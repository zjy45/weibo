from models.mongua import Mongua


class Weibo(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('title', str, ''),
        ('content', str, ''),
        ('user_id', int, -1),
    ]

    def user(self):
        from .user import User
        u = User.find(self.user_id)
        return u

    def replys(self):
        from .reply import Reply
        rs = Reply.find_all(weibo_id=self.id, deleted=False)
        return rs