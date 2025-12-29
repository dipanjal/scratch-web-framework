from jinja2 import Environment, FileSystemLoader
from webob import Request, Response

from poridhi_frame.routing_manager import RouteManager
import os


class PoridhiFrame:
    def __init__(self, template_dir: str = "templates"):
        self.routing_manager = RouteManager()

        # Initialize Jinja2 environment
        self.templates_env = Environment(
            loader=FileSystemLoader(os.path.abspath(template_dir))
        )

    def __call__(self, environ, start_response):
        http_request = Request(environ)
        response: Response = self.routing_manager.dispatch(http_request)
        return response(environ, start_response)

    def add_route(self, path: str, handler: callable) -> None:
        """
        Django style explicit route registration.
        :param path:
        :param handler:
        :return:
        """
        self.routing_manager.register(path, handler)

    def route(self, path: str):
        def decorator(handler):
            self.add_route(path, handler)
            return handler
        return decorator

    def template(self, template_name: str, context: dict) -> str:
        if context is None:
            context = {}

        return self.templates_env.get_template(template_name).render(**context)
