class Schema(colander.Schema):
    password = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=5),
        widget=deform.widget.CheckedPasswordWidget(size=20),
        description='Type your password and confirm it')
schema = Schema()
form = deform.Form(schema, buttons=('submit',)
