from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.user import User_Model

def getUsers(session):
    return session.query(User_Model).all()

def postUsers(session, User_Model):
    print(User_Model.email)
    try:
        session.add(User_Model)
        session.commit()
         #add prepared statment to opened session
        print('organization_model.name')
        return True
    except:
        print('name')
        return False
