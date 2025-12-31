from pathlib import Path

import pytest

from poridhi_frame.common_handlers import CommonHandlers
from tests.utils.temp_file_builder import TempFileBuilder
from tests.utils.test_framework import TestFramework


@pytest.fixture
def app() -> TestFramework:
    cwd = Path(__file__).resolve().parent
    app = TestFramework(template_dir=f"{cwd}/templates")
    app.add_exception_handler(handler=CommonHandlers.generic_exception_handler)
    return app


@pytest.fixture
def client(app: TestFramework):
    return app.test_session()


@pytest.fixture
def temp_file_builder(tmpdir_factory) -> TempFileBuilder:
    return TempFileBuilder(tmpdir_factory, root_dir="static")
