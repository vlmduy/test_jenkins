"""
src/controllers/handler_error.py: handler error
Copyright 2017-2018 LinhHo Training.
"""

from flask import jsonify, Blueprint

handler_api = Blueprint('handler_api', __name__)


@handler_api.errorhandler(500)
def error_handler(error):
    """
    Handler error 500
    :return: Request Error url
    """
    _error = str(error)
    message = {
        'status': 500,
        'message': _error
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp


@handler_api.errorhandler(403)
def error_loggin():
    """
    Handler error 500
    :return: Request Error url
    """
    message = {
        'status': 403,
        'message': 'login fail'
    }
    resp = jsonify(message)
    resp.status_code = 403

    return resp


@handler_api.errorhandler(401)
def not_loggin():
    """
    Handler error 500
    :return: Request Error url
    """
    message = {
        'status': 401,
        'message': 'not loggin'
    }
    resp = jsonify(message)
    resp.status_code = 401

    return resp
