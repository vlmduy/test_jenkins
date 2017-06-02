from flask import Flask, render_template, request, jsonify
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from organization import Organization_Model
from db import Base

class User_Model(Base):
    __tablename__ = 'users'
    id = Column(String(120), primary_key=True)
    email = Column(String(120), unique=True)
    first_name = Column(String(120), unique=True)
    last_name = Column(String(120), unique=True)
    password_hash = Column(String(120), unique=True)
    password_salt = Column(String(120), unique=True)
    org_id = Column(Integer, ForeignKey('organization.id'), nullable=False)
    feature_access = Column(String(120), unique=True)
    access_token = Column(String(120), unique=True)
    should_reset_password = Column(Boolean, unique=True)
    last_login_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    organization = relationship('Organization_Model')

    def __init__(self, id, email, first_name, last_name, password_hash, password_salt, org_id, feature_access, access_token, should_reset_password, last_login_at, created_at, updated_at):
    	self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = password_hash
        self.password_salt = password_salt
        self.org_id = org_id
        self.feature_access = feature_access
        self.access_token = access_token
        self.should_reset_password = should_reset_password
        self.last_login_at = last_login_at
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<E-mail %r>' % self.email