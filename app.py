"""
app.py: App module
Copyright 2017-2018 LinhHo Training.
"""

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from src.controllers.organization_controller import organization_api
from src.controllers.channel_controller import channel_api
from src.controllers.user_controller import user_api
from src.controllers.login_controller import login_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(channel_api)
app.register_blueprint(organization_api)
app.register_blueprint(user_api)
app.register_blueprint(login_api)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hovietlinh17@gmail.com'
app.config['MAIL_PASSWORD'] = 'linh011193'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



print 'ssdsdsaasdad'

@app.route('/')
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

@app.route('/mail', methods=['POST'])
def mail_sent():
    """
    API login
    :return: users
    """
    if not request.json:
        abort(400)
    else:
        try:
            recipients = request.get_json(silent=True)['recipients']
            body = request.get_json(silent=True)['body']
        except Exception as ex:
            return error_handler(ex)
    msg = Message('Hello', sender = 'hovietlinh17@gmail.com', recipients = recipients)
    msg.body = body
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
