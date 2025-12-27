import pytest

from poridhi_frame import PoridhiFrame


@pytest.fixture
def test_app() -> PoridhiFrame:
    return PoridhiFrame()
