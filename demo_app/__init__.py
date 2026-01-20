from pathlib import Path

from demo_app.middlewares import TokenMiddleware
from demo_app.models.book import Book
from poridhiweb import PoridhiFrame
from poridhiweb.middlewares import (
    ErrorHandlerMiddleware,
    ExecutionTimeMiddleware,
    ReqResLoggingMiddleware
)
from poridhiweb.orm.db_factory import DatabaseFactory, Dialect

cwd = Path(__file__).resolve().parent
app = PoridhiFrame(
    template_dir=f"{cwd}/templates",
    static_dir=f"{cwd}/static"
)
app.add_middleware(TokenMiddleware)
app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(ExecutionTimeMiddleware)
app.add_middleware(ReqResLoggingMiddleware)

db = DatabaseFactory(dialect=Dialect.SQLITE).get_connection("./myapp.db")
db.create(Book)
