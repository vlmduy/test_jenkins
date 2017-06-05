"""
src/daos/user_dao.py: User Dao
Copyright 2017-2018 LinhHo Training.
"""

from src.models.user import User_Model
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def find_user_from_db(session):
    """
    Find user from database
    :parameter: session
    :return: user
    """
    return session.query(User_Model).all()


def insert_user_from_db(session, user_model):
    """
    Insert user into database
    :parameter: session, user
    :return: status
    """
    result = {
        'message': 'ok',
        'status': 'ok'
    }
    # check user already exist in database
    _user = get_user_by_id(user_model.id, session)
    if _user is None:
        try:
            session.add(user_model)
            session.commit()
            result['message'] = 'added new user success'
            result['status'] = 'ok'
        except Exception as ex:
            print ex
            result['message'] = 'added new user fail'
            result['status'] = 'fail'
    else:
        try:
            session.merge(user_model)
            session.commit()
            print "Merged user %s", user_model
            result['message'] = 'edited user success'
            result['status'] = 'ok'
        except Exception as ex:
            print "Error on merge user %s. Exception: %s", user_model, ex
            session.rollback()
            result['message'] = 'edited user fail'
            result['status'] = 'fail'
    return result


def get_user_by_id(user_id, session):
    """
    Get user by user_id
    :param user_id: user id
    :type user_id: integer
    :param session: database connection session
    :type session:
    :rtype: <user object> or None
    """
    try:
        query = session.query(User_Model).filter(User_Model.id == user_id)
        user = query.one()
        return user
    except MultipleResultsFound as ex:
        print "Multiple results found User.get_user_by_id %s", ex
        return query.first()
    except NoResultFound as ex:
        print "No result found User.get_user_by_id %s", ex
        return None
