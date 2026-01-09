import inspect
from typing import Optional, Any

from webob.response import Response

from poridhi_frame.constants import HttpStatus, ContentType


class RouteDefinition:
    def __init__(
        self,
        handler,
        allowed_methods: Optional[list[str]] = None,
        kwargs: Optional[dict[str, Any]]=None
    ):
        self.handler = handler
        self.allowed_methods = allowed_methods or ["GET", "POST", "PUT", "PATCH", "DELETE"]
        self.kwargs = kwargs or {}

    def is_valid_method(self, method: str) -> bool:
        return method in self.allowed_methods

    def add_kwargs(self, kwargs: dict):
        self.kwargs.update(kwargs)

    def is_class_based_handler(self):
        return inspect.isclass(self.handler)


class TextResponse(Response):
    def __init__(self, content: str, status: str = HttpStatus.OK, **kwargs):
        super().__init__(text=content, status=status, content_type=ContentType.TEXT, **kwargs)


class JSONResponse(Response):
    def __init__(self, content: dict | Any, status: str = HttpStatus.OK, **kwargs):
        if not isinstance(content, dict):
            content = content.__dict__

        super().__init__(json=content, status=status, content_type=ContentType.JSON, **kwargs)


class HTMLResponse(Response):
    def __init__(self, content: str, status: str = HttpStatus.OK, **kwargs):
        super().__init__(body=content, status=status, content_type=ContentType.HTML, **kwargs)
