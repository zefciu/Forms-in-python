class RegisterForm(Form):
    __validators__ = [('equals', 'password', 'repeat_password')]
    __reflect__ = ('eplasty', User)
    __frontend__ = 'dojo'
    login = {'label': 'Login'}
    hash = salt = None
    password = TextField(widgets=[PasswordInput], label='Hasło')
    repeat_password = TextField(widgets=[PasswordInput], label='Powtórz hasło')
    ok = HttpSubmit()
