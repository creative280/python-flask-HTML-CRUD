from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z15467*/'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from routes.contacts import contacts
app.register_blueprint(contacts)
