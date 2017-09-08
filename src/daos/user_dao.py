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
    result = {
        'message': 'ok',
        'status': True,
        'data': None
    }
    try:
        data = session.query(User_Model).all()
        _data = []
        for user in data:
            _data.append(user.serialize())
        result['data'] = _data
        del result['message']
    except Exception as ex:
        result['status'] = False
        result['message'] = ex
        del result['data']
    return result


def insert_user_from_db(session, user_model):
    """
    Insert user into database
    :parameter: session, user
    :return: status
    """
    result = {
        'message': 'ok',
        'status': 'ok',
        'data': None
    }
    # check user already exist in database
    _user = get_user_by_email(user_model.email, session)
    if _user is None:
        try:
            session.add(user_model)
            session.commit()
            result['message'] = 'added new user success'
            result['status'] = 'ok'
            result['data'] = user_model
        except Exception as ex:
            print ex
            result['message'] = 'added new user fail'
            result['status'] = 'error'
    else:
        result['message'] = 'User already exists'
        result['status'] = 'error'
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
    result = {
        'message': 'ok',
        'data': None,
        'status': False
    }
    try:
        query = session.query(User_Model).filter(User_Model.id == user_id)
        user = query.one()
        result['data'] = user.serialize()
        result['status'] = True
        del result['message']
    except NoResultFound:
        result['message'] = 'user not exit'
        del result['user']
    return result


def get_user_by_email(user_email, session):
    """
    Get user by user_email
    :param user_email: user email
    :type user_email: string
    :param session: database connection session
    :type session:
    :rtype: <user object> or None
    """
    try:
        query = session.query(User_Model).filter(User_Model.email == user_email)
        user = query.one()
        return user
    except MultipleResultsFound:
        return query.first()
    except NoResultFound:
        return None


def get_user_by_token(user_token, session):
    """
    Get user by user_id
    :param user_id: user id
    :type user_id: integer
    :param session: database connection session
    :type session:
    :rtype: <user object> or None
    """

    try:
        query = session.query(User_Model).filter(User_Model.token == user_token)
        user = query.one()
        return user
    except MultipleResultsFound:
        return query.first()
    except NoResultFound:
        return None


def edit_use_by_email(session, user_model):
    """
    Edit user into database
    :parameter: session, user
    :return: status
    """
    # Check if channel already exist in database
    result = {
        'message': '',
        'data': None,
        'status': False
    }
    _user = get_user_by_email(user_email=user_model.email, session=session)
    if _user is None:
        result['message'] = 'User does not exist'
        del result['data']
    else:
        try:
            session.merge(user_model)
            session.commit()
            result['message'] = 'Edited User success'
            result['status'] = True
            result['data'] = user_model.serialize()
        except Exception as ex:
            print ex
            session.rollback()
            result['message'] = 'Edited User fail'
            del result['data']
    return result


def edit_user_by_id(session, user_model):
    """
    Edit user into database
    :parameter: session, user
    :return: status
    """
    # Check if channel already exist in database
    result = {
        'message': '',
        'data': None,
        'status': False
    }
    _user = _find_user_by_id(user_id=user_model.id, session=session)

    if _user is None:
        result['message'] = 'User does not exist'
        del result['data']
    else:
        try:
            user_model.last_login_at = _user.last_login_at
            user_model.access_token = _user.access_token
            user_model.created_at = _user.created_at
            user_model.updated_at = _user.updated_at
            user_model.token_login_time = _user.token_login_time
            user_model.password_hash = _user.password_hash
            user_model.password_salt = _user.password_salt
            session.merge(user_model)
            session.commit()
            result['message'] = 'Edited User success'
            result['status'] = True
            result['data'] = user_model.serialize()
        except Exception as ex:
            print ex
            session.rollback()
            result['message'] = 'Edited User fail'
            del result['data']
    return result


def remove_user_by_id(session, user_id):
    """
    Remove user in database
    :parameter: session, user
    :return: status
    """
    # Check if channel already exist in database
    result = {
        'message': '',
        'status': False
    }
    _user = _find_user_by_id(user_id=user_id, session=session)
    if _user is None:
        result['message'] = 'User does not exist'
    else:
        try:
            session.delete(_user)
            session.commit()
            result['message'] = 'Removed User success'
            result['status'] = True
        except Exception as ex:
            print ex
            session.rollback()
            result['message'] = 'Removed User fail'
    return result

def _find_user_by_id(user_id, session):
    try:
        query = session.query(User_Model).filter(User_Model.id == user_id)
        user = query.one()
        return user
    except MultipleResultsFound:
        return query.first()
    except NoResultFound:
        return None
