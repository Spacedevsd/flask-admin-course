from flask_admin.contrib.sqla import ModelView
from flask import redirect
from wtforms.fields import PasswordField
from werkzeug.security import generate_password_hash
from flask_login import current_user

from models import User, Task, Profile
from app import db


class UserView(ModelView):
    column_editable_list = ('name', 'email', 'profile'  )
    form_edit_rules = {'name', 'email', 'tasks', 'profile'}
    column_searchable_list = ['email']
    edit_modal = True

    form_extra_fields = {
        "password": PasswordField("Password"),
    }

    inline_models = [Profile]

    column_filters = ['name', 'profile']

    column_exclude_list = ('password', )
    column_list = ["name", "email", "profile"]

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(form.password.data)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect("/login")

    
def init_app(admin):
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Task, db.session))
