from flask import Flask
from src.models.user import User_Model


def getUsers(session):
    return session.query(User_Model).all()


def postUsers(session, User_Model):
    print(User_Model.email)
    try:
        session.add(User_Model)
        session.commit()
        print('organization_model.name')
        return True
    except:
        print('name')
        return False
