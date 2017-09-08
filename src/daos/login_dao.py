"""
src/daos/login_dao.py: Login Dao
Copyright 2017-2018 LinhHo Training.
"""

from datetime import datetime
import jwt
import pytz
from src.daos.user_dao import get_user_by_email, edit_use_by_email


def login_with_email(email, password, session):
    _user = get_user_by_email(email, session)

    result = {
        'message': None,
        'user_id': None,
        'status': False,
        'token': None
    }

    if not _user:
        result['message'] = 'user not exist'
        del result['user_id']
        del result['token']
    else:
        if _user.password_salt != password:
            result['message'] = 'password fail'
            del result['user_id']
            del result['token']
        else:
            result['user_id'] = _user.id
            result['token'] = jwt.encode({'exp': datetime.utcnow(), \
                'user': _user.serialize()}, \
                'secret', algorithm='HS256')
            result['status'] = True
            del result['message']

            _user.last_login_at = datetime.utcnow().replace(tzinfo=pytz.UTC)
            edit_use_by_email(session, _user)

    return result


def verify_token(token):
    # first try to authenticate by token
    _result = jwt.decode(token, 'secret', leeway=3600)
    return _result
