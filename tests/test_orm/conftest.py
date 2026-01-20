from poridhiweb.orm.sqlite.column import PrimaryKey, Column, ForeignKey
from poridhiweb.orm.sqlite.table import Table


class Author(Table):
    id = PrimaryKey()
    name = Column(str)
    age = Column(int)


class Book(Table):
    id = PrimaryKey()
    title = Column(str)
    published = Column(bool)
    author = ForeignKey(Author)
