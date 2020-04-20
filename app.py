from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login.html"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)


    @app.route("/login")
    def login():
        return "Login Page"

    # register admin page
    import admin as administrator
    admin = Admin(app, name="Spacedevs", template_mode="bootstrap3")
    administrator.init_app(admin)

    return app
