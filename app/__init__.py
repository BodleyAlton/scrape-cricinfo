from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://altonbodley@127.0.0.1/cric"
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS=False
from app import views
