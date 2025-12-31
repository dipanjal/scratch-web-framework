import os
from pathlib import Path

import pytest

from poridhi_frame import PoridhiFrame
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter

from poridhi_frame.middlewares import ErrorHandlerMiddleware
from tests.constants import BASE_URL


class TestFramework(PoridhiFrame):
    def test_session(self, base_url=BASE_URL):
        session = RequestsSession()
        session.mount(
            prefix=base_url,
            adapter=RequestsWSGIAdapter(
                app=ErrorHandlerMiddleware(app=self)
            )
        )
        return session


@pytest.fixture
def app() -> TestFramework:
    cwd = Path(__file__).resolve().parent
    return TestFramework(template_dir=f"{cwd}/templates")


@pytest.fixture
def client(app: TestFramework):
    return app.test_session()

