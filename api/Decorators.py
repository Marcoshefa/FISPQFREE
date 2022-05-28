from functools import wraps
from flask import request

def validate_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = request.headers.get('token')
        if token != 'token123456':
            return 'Não permitido', 403

        return f(*args, **kwargs)
    return decorated_function