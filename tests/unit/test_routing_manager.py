import pytest

from poridhi_frame import PoridhiFrame


def test_basic_route_adding(test_app: PoridhiFrame):
    @test_app.route("/home")
    def home(req, resp):
        resp.text = "Hello World"


def test_route_overlap_throws_exception(test_app: PoridhiFrame):
    @test_app.route("/test")
    def home(req, resp):
        resp.text = "First handler"

    # Test that duplicate route raises AssertionError
    with pytest.raises(RuntimeError):
        @test_app.route("/test")
        def home2(req, resp):
            resp.text = "Second handler"
