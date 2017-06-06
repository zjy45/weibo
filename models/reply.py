from models.mongua import Mongua


class Reply(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('content', str, ''),
        ('user_id', int, -1),
        ('weibo_id', int, -1),
    ]

    def user(self):
        from .user import User
        u = User.find(self.user_id)
        return u
