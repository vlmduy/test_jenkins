"""
src/models/user.py: User Mapping Object
Copyright 2017-2018 LinhHo Training.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, func, TIMESTAMP
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from src.config.config import SECRET_KEY
from db import Base


class User_Model(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    first_name = Column(String(120), unique=True)
    last_name = Column(String(120), unique=True)
    password_hash = Column(String(120), unique=True)
    password_salt = Column(String(120), unique=True)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    feature_access = Column(String(120), unique=True)
    access_token = Column(String(120), unique=True)
    should_reset_password = Column(Boolean, unique=True)
    last_login_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    token_login_time = Column(TIMESTAMP, nullable=False, server_default=func.now())

    def __init__(self,
                 id,
                 email,
                 first_name,
                 last_name,
                 password_hash,
                 password_salt,
                 org_id,
                 feature_access,
                 access_token,
                 should_reset_password,
                 last_login_at,
                 created_at,
                 updated_at,
                 token_login_time):
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
        self.token_login_time = token_login_time

    def serialize(self):
        return {
            'id': int(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'org_id': self.org_id,
            'feature_access': self.feature_access,
            'should_reset_password': self.should_reset_password,
            'last_login_at': str(self.last_login_at),
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def hash_password(self, password_salt):
        self.password_hash = pwd_context.encrypt(password_salt)

    def verify_password(self, password_salt):
        return pwd_context.verify(password_salt, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(_token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(_token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User_Model.query.get(data['id'])
        return user

    def __repr__(self):
        return '<E-mail %r>' % self.email
