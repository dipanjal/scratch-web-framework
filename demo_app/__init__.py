from poridhi_frame import PoridhiFrame
from poridhi_frame.common_handlers import CommonHandlers
from poridhi_frame.middlewares import ErrorHandlerMiddleware

app = PoridhiFrame(template_dir="./demo_app/templates")
app.add_exception_handler(handler=CommonHandlers.generic_exception_handler)
exception_handler_middleware = ErrorHandlerMiddleware(
    app=app
)
