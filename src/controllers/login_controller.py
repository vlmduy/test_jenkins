from flask import Blueprint, request, jsonify, abort
from src.daos.login_dao import login_with_email
from src.controllers.handler_error import error_handler
import db

login_api = Blueprint('login_api', __name__)


@login_api.route('/login', methods=['POST'])
def login_users():
    """
    API login
    :return: users
    """
    if not request.json:
        abort(400)
    else:
        try:
            email = request.get_json(silent=True)['email']
            password = request.get_json(silent=True)['password']
        except Exception as ex:
            return error_handler(ex)
    with db.session() as session:
        result = login_with_email(email, password, session)
        return jsonify(result)
