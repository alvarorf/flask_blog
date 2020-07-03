from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '172213268cb8712da87df60b8c51bc42059dba741570741ab4d02cda24bf56f4b5e9250f2776e24a4d44af5d074588fcffb2f6e3be83962f8af248357c5fb8f1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flaskblog import routes