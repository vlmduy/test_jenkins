"""
src/controllers/user_controller.py: User Controller
Copyright 2017-2018 LinhHo Training.
"""

from flask import Blueprint, request, jsonify, abort
from src.models.user import User_Model
from src.daos.user_dao import insert_user_from_db, find_user_from_db, \
        get_user_by_id, remove_user_by_id, edit_user_by_id
from src.daos.login_dao import verify_token
from src.controllers.handler_error import error_handler, not_loggin
import db

user_api = Blueprint('user_api', __name__)


@user_api.route('/user', methods=['GET'])
def find_users():
    """
    API find user from user_dao
    :return: users
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

    with db.session() as session:
        _data = find_user_from_db(session)  # fetch all products on the table

        return jsonify(_data)


@user_api.route('/user/<user_id>', methods=['GET'])
def find_user_by_id(user_id):
    """
    API find user by user_id from user_dao
    :return: user
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

    with db.session() as session:
        _result = get_user_by_id(user_id, session)  # fetch all products on the table
        return jsonify(_result)


@user_api.route('/user/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    """
    API remove channel by channel_id from channel_dao
    :return: channel
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

    with db.session() as session:
        message = remove_user_by_id(session, user_id)
        return jsonify(message)



@user_api.route('/user', methods=['POST'])
def insert_users():
    """
    API insert user from user_dao
    :parameter: json
    :return: user
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception as ex:
        print ex
        return not_loggin()

    if not request.json:
        abort(400)
    else:
        try:
            id = None
            email = request.get_json()['email']
            first_name = request.get_json()['first_name']
            last_name = request.get_json()['last_name']
            password = request.get_json()['password']
            org_id = request.get_json()['org_id']
            feature_access = request.get_json()['feature_access']
            access_token = request.get_json()['access_token']
            should_reset_password = request.get_json()['should_reset_password']
            last_login_at = request.get_json()['last_login_at']
            created_at = None
            updated_at = None
            token_login_time = None
            password_hash = password
            password_salt = 'ddfsdsf'
        except Exception as ex:
            return error_handler(ex)

    user = User_Model(id,
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
                      token_login_time)

    with db.session() as session:
        # fetch pram from the request
        _result = insert_user_from_db(session, user)
        if _result['status'] == 'error':
            return error_handler(_result['message'])
        _user = _result['user']
        return jsonify(_user.serialize())


@user_api.route('/user/<user_id>', methods=['PUT'])
def edit_users(user_id):
    """
    API insert user from user_dao
    :parameter: json
    :return: user
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception as ex:
        print ex
        return not_loggin()

    if not request.json:
        abort(400)
    else:
        try:
            id = user_id
            email = request.get_json()['email']
            first_name = request.get_json()['first_name']
            last_name = request.get_json()['last_name']
            password = None
            org_id = request.get_json()['org_id']
            feature_access = request.get_json()['feature_access']
            access_token = None
            should_reset_password = request.get_json()['should_reset_password']
            last_login_at = None
            created_at = None
            updated_at = None
            token_login_time = None
            password_hash = password
            password_salt = 'ddfsdsf'
        except Exception as ex:
            return error_handler(ex)

    user = User_Model(id,
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
                      token_login_time)
    print 'QQQQQQQQ'

    print user.last_login_at
    with db.session() as session:
        # fetch pram from the request
        _result = edit_user_by_id(session, user)
        return jsonify(_result)
