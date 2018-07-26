from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@0.0.0.0/cric"
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS=False
print("init")
from app import views
