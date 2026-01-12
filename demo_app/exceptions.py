from poridhiweb.constants import HttpStatus
from poridhiweb.exceptions import ResponseError


class ResourceNotFoundException(ResponseError):
    def __init__(self, message='Resource not found'):
        super().__init__(message, HttpStatus.METHOD_NOT_ALLOWED)
