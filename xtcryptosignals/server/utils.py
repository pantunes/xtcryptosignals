__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from functools import wraps
from flask import request
from xtcryptosignals.server.api.auth import service


def user_auth():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = request.headers['Authorization']
            except KeyError:
                raise ValueError('Invalid Token Session.', 400)
            auth = service.get_auth_with_token(token=token)
            return f(*args, **kwargs, auth=auth)
        return wrapper
    return decorator


def _sanitize_errors_mongoengine(errors):
    _errors = []
    for k, v in errors.to_dict().items():
        _errors.append("{} ({}).".format(v, k))
    return '\n'.join(_errors)


def _sanitize_errors_marshmallow(errors):
    _errors = []
    for k, v in errors.items():
        if k == '_schema':
            _errors += v
            continue
        for x in v:
            _errors.append("{} ({}).".format(x[:-1], k))
    return '\n'.join(_errors)


def validate_io(
        schema_in=None,
        schema_out=None,
        many_in=False,
        many_out=False,
        is_form=False
):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if schema_in:
                try:
                    if not is_form:
                        payload = request.get_json()
                    else:
                        payload = request.form
                except Exception:
                    return dict(error='Invalid JSON/Form payload.'), 402
                data, errors = schema_in().load(payload, many=many_in)
                if errors:
                    return dict(error=_sanitize_errors_marshmallow(errors)), 400
                kwargs.update(valid_data=data)
            try:
                data = f(*args, **kwargs)
            except ValueError as error:
                error, status = error.args
                return dict(error=error), status
            status = None
            if type(data) is tuple:
                data, status = data
            if schema_out:
                data, errors = schema_out().dump(data, many=many_out)
                if errors:
                    return dict(error=_sanitize_errors_marshmallow(errors)), 415
                errors = schema_out().validate(data, many=many_out)
                if errors:
                    return dict(error=_sanitize_errors_marshmallow(errors)), 416
            if data is None:
                data = dict(status='OK')
            return data, status or 200
        return wrapper
    return decorator
