"""
src/controllers/user_controller.py: User Controller
Copyright 2017-2018 LinhHo Training.
"""

from flask import Blueprint, request, jsonify
from src.models.user import User_Model
from src.daos.user_dao import insert_user_from_db, find_user_from_db, get_user_by_id
import db

user_api = Blueprint('user_api', __name__)


@user_api.route('/user', methods=['GET'])
def find_users():
    """
    API find user from user_dao
    :return: users
    """
    with db.session() as session:
        user_data = find_user_from_db(session)  # fetch all products on the table
        data_all = [user.serialize() for user in user_data]
        return jsonify(data=data_all)


@user_api.route('/user/id/<user_id>', methods=['GET'])
def find_user_by_id(user_id):
    """
    API find user by user_id from user_dao
    :return: user
    """
    with db.session() as session:
        user_data = get_user_by_id(user_id, session)  # fetch all products on the table
        user = user_data.serialize()
        return jsonify(data=user)


@user_api.route('/user', methods=['POST'])
def insert_users():
    """
    API insert user from user_dao
    :parameter: json
    :return: user
    """
    with db.session() as session:
        # fetch pram from the request
        id = request.get_json()['id']
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
        password_hash = password
        password_salt = 'ddfsdsf'

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
                          updated_at)

        result = insert_user_from_db(session, user)
        return jsonify(result)
