from pathlib import Path

from poridhi_frame import PoridhiFrame
from poridhi_frame.common_handlers import CommonHandlers
from poridhi_frame.middlewares import ErrorHandlerMiddleware

cwd = Path(__file__).resolve().parent
app = PoridhiFrame(
    template_dir=f"{cwd}/templates",
    static_dir=f"{cwd}/static"
)
app.add_exception_handler(handler=CommonHandlers.generic_exception_handler)
exception_handler_middleware = ErrorHandlerMiddleware(
    app=app
)
