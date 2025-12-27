from webob import Response


def test_class_based_handler_get(app, client):
    response_text = "This is a GET request"

    @app.route("/books")
    class BookResource:
        def get(self, req):
            return Response(
                text=response_text
            )

    response = client.get("http://testserver/books")
    assert response.text == response_text


def test_class_based_handler_post(app, client):
    response_text = "This is a POST request"

    @app.route("/books")
    class BookResource:
        def post(self, req):
            return Response(
                text=response_text
            )

    response = client.post("http://testserver/books")
    assert response.text == response_text


def test_class_based_handler_not_allowed_method(app, client):
    expected_response = {
        "message": f"GET request is not allowed for /books",
    }

    @app.route("/books")
    class BookResource:
        def post(self, req):
            return Response(
                text="Only POST allowed"
            )

    response = client.get("http://testserver/books")
    assert response.json() == expected_response
