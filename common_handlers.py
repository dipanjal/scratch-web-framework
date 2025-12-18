from constants import HttpStatus
from helpers import json_response
from webob import Request, Response

import logging

logger = logging.getLogger(__name__)


class CommonHandlers:
    @staticmethod
    def generic_exception_handler(request: Request, excp: Exception) -> Response:
        logger.exception(excp)
        response = {
            "message": f"Unhanded Exception Occurred: {str(excp)}"
        }
        return Response(
            json_body=response,
            status=HttpStatus.INTERNAL_SERVER_ERROR
        )

    @staticmethod
    def url_not_found_handler(request: Request) -> Response:
        response = {
            "message": f"Requested path: {request.path} does not exist"
        }
        return Response(
            json_body=response,
            status=HttpStatus.NOT_FOUND
        )
