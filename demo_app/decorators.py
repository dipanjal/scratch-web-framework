from webob.request import Request

from demo_app.constants import STATIC_TOKEN
from demo_app.exceptions import UnauthorizedException


def login_required(handler):
    def wrapped_handler(request: Request, *args, **kwargs):
        if not request.token or request.token != STATIC_TOKEN:
            raise UnauthorizedException()
        return handler(request, *args, **kwargs)

    return wrapped_handler
