from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.organization import Organization_Model
from src.controllers.test import account_api
from src.controllers.organization_controller import organization_api
from src.controllers.channel_controller import channel_api
from src.controllers.user_controller import user_api

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@192.168.210.84:5432/training'
# db = SQLAlchemy(app)

app.register_blueprint(account_api)
app.register_blueprint(organization_api)
app.register_blueprint(user_api)

@app.route('/')
def index():
    return 'Hello World!'

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(500)
def error_handler(error=None):
    message = {
            'status': 500,
            'message': 'Request Error: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()