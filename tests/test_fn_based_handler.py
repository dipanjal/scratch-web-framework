from webob.response import Response

from tests.constants import BASE_URL


def test_client_can_send_requests(app, client):
    RESPONSE_TEXT = "Hello from test client"

    @app.route("/test")
    def test_handler(req):
        return Response(text=RESPONSE_TEXT)

    response = client.get(f"{BASE_URL}/test")
    assert response.text == RESPONSE_TEXT


def test_parameterized_route(app, client):
    @app.route("/hello/{name}")
    def hello(req, name: str):
        return Response(text=f"Hello {name}")

    # Test multiple parameter values
    assert client.get("http://testserver/hello/Alice").text == "Hello Alice"
    assert client.get("http://testserver/hello/Bob").text == "Hello Bob"
    assert client.get("http://testserver/hello/Charlie").text == "Hello Charlie"
