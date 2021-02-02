from flask import Flask
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app=Flask(__name__)
app.config['SECRET_KEY']='c04921879357e963347c30054535420e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


from app import routes