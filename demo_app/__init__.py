from pathlib import Path

from demo_app.middlewares import TokenMiddleware
from poridhiweb import PoridhiFrame
from poridhiweb.middlewares import (
    ErrorHandlerMiddleware,
    ExecutionTimeMiddleware,
    ReqResLoggingMiddleware
)
cwd = Path(__file__).resolve().parent
app = PoridhiFrame(
    template_dir=f"{cwd}/templates",
    static_dir=f"{cwd}/static"
)
app.add_middleware(TokenMiddleware)
app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(ExecutionTimeMiddleware)
app.add_middleware(ReqResLoggingMiddleware)
