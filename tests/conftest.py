import pytest

from poridhi_frame import PoridhiFrame
from requests import Session as RequestSession
from wsgiadapter import WSGIAdapter as RequestWSGIAdapter


class TestFramework(PoridhiFrame):
    def test_session(self, base_url="http://testserver") -> RequestSession:
        session = RequestSession()
        session.mount(prefix=base_url, adapter=RequestWSGIAdapter(self))
        return session


@pytest.fixture
def app() -> TestFramework:
    return TestFramework()


@pytest.fixture
def client(app) -> RequestSession:
    return app.test_session()
