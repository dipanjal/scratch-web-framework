import pytest
from webob.response import Response

from poridhi_frame.common_handlers import CommonHandlers
from poridhi_frame.exceptions import MethodNotAllowed
from poridhi_frame.middlewares import ErrorHandlerMiddleware
from tests.constants import BASE_URL
from tests.utils.test_framework import TestFrameworkBuilder


def test_client_can_send_requests(app, client):
    RESPONSE_TEXT = "Hello from test client"

    @app.route("/test")
    def test_handler(req):
        return Response(text=RESPONSE_TEXT)

    response = client.get(f"{BASE_URL}/test")
    assert response.text == RESPONSE_TEXT


@pytest.mark.parametrize(
    "name, exp_result",
    [
        pytest.param(
            "Alice", "Hello Alice", id="Alice",
        ),
        pytest.param(
            "Bob", "Hello Bob", id="Bob",
        ),
        pytest.param(
            "Charlie", "Hello Charlie", id="Charlie",
        )
    ]
)
def test_parameterized_route(app, client, name, exp_result):
    @app.route("/hello/{name}")
    def hello(req, name: str):
        return Response(text=f"Hello {name}")
    assert client.get(f"{BASE_URL}/hello/{name}").text == exp_result


def test_url_not_found(app, client):
    RESPONSE_TEXT = "Hello from test client"
    exp_response = {
        "message": f"Requested path: /hello does not exist"
    }

    @app.route("/test")
    def test_handler(req):
        return Response(text=RESPONSE_TEXT)

    response = client.get(f"{BASE_URL}/hello")
    assert response.status_code == 404
    assert response.json() == exp_response


def test_generic_exception_handler(app, client):
    app.add_exception_handler(handler=CommonHandlers.generic_exception_handler)
    msg = "A test exception"
    exp_response = {
        "message": f"Unhanded Exception Occurred: {msg}"
    }

    @app.route("/test")
    def test_handler(req):
        raise RuntimeError(msg)

    response = client.get(f"{BASE_URL}/test")
    assert response.status_code == 500
    assert response.json() == exp_response


def test_explicitly_registered_route(app, client):
    RESPONSE_TEXT = "Hello from test client"

    def test_handler(req):
        return Response(text=RESPONSE_TEXT)

    app.add_route("/test", test_handler)

    response = client.get(f"{BASE_URL}/test")
    assert response.text == RESPONSE_TEXT


def test_method_not_allowed_request():
    app = TestFrameworkBuilder().build()
    client = app.test_session()

    @app.route("/home", allowed_methods=["post"])
    def home(req):
        return Response("Hello")

    with pytest.raises(MethodNotAllowed):
        client.get(f"{BASE_URL}/home")


def test_method_not_allowed_request_handled():
    app = TestFrameworkBuilder().build()
    app.add_middleware(ErrorHandlerMiddleware)
    client = app.test_session()

    @app.route("/home", allowed_methods=["post"])
    def home(req):
        return Response("Hello")

    response = client.get(f"{BASE_URL}/home")
    response.status_code = 405

