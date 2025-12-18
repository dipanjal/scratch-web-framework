from webob import Request, Response

from poridhi_frame.routing_manager import RouteManager


class PoridhiFrame:
    def __init__(self):
        self.routing_manager = RouteManager()

    def __call__(self, environ, start_response):
        http_request = Request(environ)
        response: Response = self.routing_manager.dispatch(http_request)
        return response(environ, start_response)

    def route(self, path: str):
        def decorator(handler):
            self.routing_manager.register(path, handler)
            return handler
        return decorator
