from webob.response import Response


def test_client_can_send_requests(app, client):
    RESPONSE_TEXT = "Hello from test client"

    @app.route("/test")
    def test_handler(req):
        return Response(
            text=RESPONSE_TEXT,
        )

    response = client.get("http://testserver/test")
    assert response.text == RESPONSE_TEXT


def test_parameterized_route(app, client):
    @app.route("/hello/{name}")
    def hello(req, name: str):
        return Response(f"Hello {name}")

    # Test multiple parameter values
    assert client.get("http://testserver/hello/Alice").text == "Hello Alice"
    assert client.get("http://testserver/hello/Bob").text == "Hello Bob"
    assert client.get("http://testserver/hello/Charlie").text == "Hello Charlie"


def test_default_404_response(client):
    response = client.get("http://testserver/nonexistent")
    expected: dict = {'message': 'Requested path: /nonexistent does not exist'}

    assert response.status_code == 404
    assert response.json() == expected
