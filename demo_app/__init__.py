from poridhi_frame import PoridhiFrame
from poridhi_frame.middlewares import ErrorHandlerMiddleware

app = PoridhiFrame()
exception_handler_middleware = ErrorHandlerMiddleware(
    app=app
)
