__author__ = 'duyviec'
from functools import wraps
from werkzeug.contrib import authdigest
import flask


class FlaskRealmDigestDB(authdigest.RealmDigestDB):
    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            request = flask.request
            if not self.isAuthenticated(request):
                return self.challenge()

            return f(*args, **kwargs)

        return decorated

authDB = FlaskRealmDigestDB('TestDigestAuthRealm')
authDB.add_user('admin', 'admin')