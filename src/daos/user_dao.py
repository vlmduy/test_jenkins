from flask import Flask
from src.models.user import User_Model


def find_user_from_db(session):
    """
    Find user from database
    :parameter: session
    :return: user
    """
    return session.query(User_Model).all()


def insert_user_from_db(session, User_Model):
    """
    Insert user into database
    :parameter: session, user
    :return: status
    """
    print(User_Model.email)
    try:
        session.add(User_Model)
        session.commit()
        return True
    except:
        print('name')
        return False
