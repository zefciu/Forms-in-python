fs = FieldSet(User)
fs.append(Field('repeat_password').label('Repeat password'))

def password_match(value, field):
    if value != field.parent.password.value:
        raise ValidationError('Passwords do not match')

fs.repeat_password.set(validate=password_match)
