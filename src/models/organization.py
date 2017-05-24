from flask import Flask, render_template, request, jsonify
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@192.168.210.84:5432/training'
db = SQLAlchemy(app)

class Organization_Model(db.Model):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    logo = Column(String(120), unique=True)
    details = Column(String(120), unique=True)
    primary_contact_email = Column(String(120), unique=True)
    status = Column(Boolean, unique=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now())


    def __init__(self, id, name, logo, details, primary_contact_email, status, created_at, updated_at):
    	self.id = id
        self.name = name
        self.logo = logo
        self.details = details
        self.primary_contact_email = primary_contact_email
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Name %r>' % self.name