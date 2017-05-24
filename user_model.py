from flask import Flask, render_template, request, jsonify
from sqlalchemy import Column, Integer, String
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@192.168.210.84:5432/training'
db = SQLAlchemy(app)

class User_Model(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email