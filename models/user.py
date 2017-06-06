from models.mongua import Mongua


class User(Mongua):
    __fields__=Mongua.__fields__ + [
        ('username', str, ''),
        ('password', str, ''),
        ('user_image', str, 'default.png'),
    ]

    @classmethod
    def validate_login(cls, form):
        u = User()
        u.username = form.get('username', '')
        u.password = form.get('password', '')
        user = User.find_by(username=u.username)
        if user is not None and u.password == user.password:
            return user
        else:
            return None

    @classmethod
    def validate_register(cls, form):
        username = form.get('username', 0)
        password = form.get('password', 0)
        print('form', form)
        print('username', username)
        print('password', password)
        if len(username) >= 2 and len(password) >= 2 and User.find_by(username=username)is None:
            u = User.new(form)
            return u
        else:
            return None
