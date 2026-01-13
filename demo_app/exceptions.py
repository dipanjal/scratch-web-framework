from http import HTTPStatus

from poridhiweb.exceptions import ResponseError


class ResourceNotFoundException(ResponseError):
    def __init__(self, message='Resource not found'):
        super().__init__(message, HTTPStatus.NOT_FOUND)


class UnauthorizedException(ResponseError):
    def __init__(self, message='You are not authorized to access this resource'):
        super().__init__(message, HTTPStatus.UNAUTHORIZED)
