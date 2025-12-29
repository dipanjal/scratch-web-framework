from poridhi_frame import PoridhiFrame
from poridhi_frame.middlewares import ErrorHandlerMiddleware

app = PoridhiFrame(template_dir="./demo_app/templates")
exception_handler_middleware = ErrorHandlerMiddleware(
    app=app
)
