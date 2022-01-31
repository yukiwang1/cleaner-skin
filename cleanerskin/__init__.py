import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from cleanerskin.config import Config

# EXTENSIONS:
app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URL")
db = SQLAlchemy(app)
# user auth
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail(app)

db.init_app(app)

# BLUEPRINTS
from cleanerskin.users.routes import users
from cleanerskin.main.routes import main
from cleanerskin.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(errors)
