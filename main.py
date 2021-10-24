from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
db.engine = db.create_engine(Config.SQLALCHEMY_DATABASE_URI.lower(), {})
# db.engine = db.engine_from_config("config.Config")
