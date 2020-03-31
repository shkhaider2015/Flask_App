from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os



app = Flask(__name__)

app.config['SECRET_KEY'] = 'f6cd85d264d6ceb0ad9a11d7be35a930'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# set up env for sending emails
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# private email and password
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
#initialized
mail = Mail(app)
 
from myApp.users.routes import users
from myApp.posts.routes import posts
from myApp.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)