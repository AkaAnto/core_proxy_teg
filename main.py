from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
db.create_engine(Config.SQLALCHEMY_DATABASE_URI)