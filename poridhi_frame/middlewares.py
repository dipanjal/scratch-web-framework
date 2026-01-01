from typing import TYPE_CHECKING

from webob import Request
from webob.response import Response

from poridhi_frame.common_handlers import CommonHandlers

if TYPE_CHECKING:
    from poridhi_frame.framework import PoridhiFrame


class Middleware:
    def __init__(self, app: "PoridhiFrame"):
        self.app = app

    def __call__(self, environ, start_response):
        http_request = Request(environ)
        response = self.handle_request(http_request)
        return response(environ, start_response)

    def add(self, middleware_cls) -> None:
        self.app = middleware_cls(app=self.app)

    def process_request(self, req: Request) -> None:
        pass

    def process_response(self, req: Request, resp: Response) -> None:
        pass

    def handle_request(self, request: Request) -> Response:
        self.process_request(request)
        response = self.app.handle_request(request)
        self.process_response(request, response)
        return response


class ErrorHandlerMiddleware(Middleware):
    def handle_request(self, request: Request) -> Response:
        try:
            return super().handle_request(request)
        except Exception as e:
            return CommonHandlers.generic_exception_handler(request, e)
