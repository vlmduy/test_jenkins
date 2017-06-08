"""
app.py: App module
Copyright 2017-2018 LinhHo Training.
"""

from flask import Flask, request, jsonify, redirect, url_for
from src.controllers.organization_controller import organization_api
from src.controllers.channel_controller import channel_api
from src.controllers.user_controller import user_api
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import db
from src.daos.user_dao import check_user_login, get_user_by_email

login_manager = LoginManager()
app = Flask(__name__)
app.secret_key = 'fuck'
login_manager.init_app(app)

app.register_blueprint(channel_api)
app.register_blueprint(organization_api)
app.register_blueprint(user_api)

@app.route('/')
# @authDB.requires_auth
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
        'message': 'Request Error: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''
    else:
        email = request.form['email']
        password = request.form['pw']
        with db.session() as session:
            logged_in_user = check_user_login(session, email, password)
            if logged_in_user:
                tmp_user = AuthenUser()
                tmp_user.id = logged_in_user.email
                login_user(tmp_user)
                return redirect(url_for('protected'))
            return 'Bad login'

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

class AuthenUser(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    with db.session() as session:
        tmp = get_user_by_email(session, email)
        if not tmp:
            return

        user = AuthenUser()
        user.id = email
        return user


@login_manager.request_loader
def request_loader(request):
    with db.session() as session:
        email = request.form.get('email')
        tmp = get_user_by_email(session, email)
        if not tmp:
            return

        user = AuthenUser()
        user.id = email

        # DO NOT ever store passwords in plaintext and always compare password
        # hashes using constant-time comparison!
        tmp = check_user_login(session, email, request.form['pw'])
        user.is_authenticated = True if tmp is not None else False

        return user
if __name__ == '__main__':
    app.debug = True
    app.run()
