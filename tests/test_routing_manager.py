import pytest
from webob.response import Response

from poridhi_frame import PoridhiFrame


@pytest.fixture
def app() -> PoridhiFrame:
    return PoridhiFrame()


def test_basic_route_adding(app: PoridhiFrame):
    @app.route("/home")
    def home(req):
        return Response(
            text="Hello World"
        )


def test_duplicate_routing_exception(app: PoridhiFrame):
    @app.route("/test")
    def first(req):
        return Response(
            text="First Handler"
        )

    with pytest.raises(
        RuntimeError,
        match="Path: /test already bind to another handler"
    ):
        @app.route("/test")
        def second(req):
            return Response(
                text="Second Handler"
            )
