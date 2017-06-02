from flask import Flask, render_template, request, jsonify
from src.models.user import User_Model
from src.daos.user_dao import insert_user_from_db, find_user_from_db
from flask import Blueprint
import db

user_api = Blueprint('user_api', __name__)


@user_api.route('/users', methods=['GET'])
def find_users():
    """
    API find user from user_dao
    :return: user
    """
    with db.session() as session:
        user = find_user_from_db(session)  # fetch all products on the table
        data_all = [[product.id, product.email] for product in user]
        return jsonify(products=data_all)


@user_api.route('/users', methods=['POST'])
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
        password_hash = 'dsdf'
        password_salt = 'ddfsdsf'

        user = User_Model(id, email, first_name,
                          last_login_at,
                          password_hash,
                          password_salt,
                          org_id,
                          feature_access,
                          access_token,
                          should_reset_password,
                          last_login_at,
                          created_at,
                          updated_at)

        if insert_user_from_db(session, user):
            return jsonify(session=result)
        else:
            message = {
                  'message': 'fail',
            }
            resp = jsonify(message)
            return resp
