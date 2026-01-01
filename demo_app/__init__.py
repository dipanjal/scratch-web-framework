from pathlib import Path

from poridhi_frame import PoridhiFrame
from poridhi_frame.middlewares import ErrorHandlerMiddleware

cwd = Path(__file__).resolve().parent
app = PoridhiFrame(
    template_dir=f"{cwd}/templates",
    static_dir=f"{cwd}/static"
)
app.add_middleware(ErrorHandlerMiddleware)
