"""
app.py: App module
Copyright 2017-2018 LinhHo Training.
"""

from flask import Flask, request, jsonify
from src.controllers.organization_controller import organization_api
from src.controllers.channel_controller import channel_api
from src.controllers.user_controller import user_api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)

app.register_blueprint(channel_api)
app.register_blueprint(organization_api)
app.register_blueprint(user_api)


# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT')
#   return response


@app.route('/', methods = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT'])
# @cross_origin() 
def index():
    """
    API test
    :return: Hello World!
    """
    return 'Hello World!'


@app.errorhandler(404)
def not_found(error=None):
    """
    Handler error 404
    :return: Not Found url
    """
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(500)
def error_handler(error=None):
    """
    Handler error 500
    :return: Request Error url
    """
    message = {
        'status': 500,
        'message': error
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
