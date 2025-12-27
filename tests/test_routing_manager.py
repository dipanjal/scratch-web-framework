import pytest
from webob.response import Response

from tests.conftest import TestFramework


def test_basic_route_adding(app: TestFramework):
    @app.route("/home")
    def home(req):
        return Response("Hello World!")


def test_route_overlap_throws_exception(app: TestFramework):
    @app.route("/test")
    def home(req, resp):
        return Response("First handler")

    # Test that duplicate route raises AssertionError
    with pytest.raises(RuntimeError):
        @app.route("/test")
        def home2(req, resp):
            return Response("Second handler")
