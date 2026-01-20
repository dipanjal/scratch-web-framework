from typing import TYPE_CHECKING

from poridhiweb.orm.sqlite.sql_types import SQL_TYPE_MAP, SQLType

if TYPE_CHECKING:
    from poridhiweb.orm.sqlite.table import Table

class Column:
    def __init__(self, column_type):
        self.type = column_type

    @property
    def sql_type(self) -> SQLType:
        return SQL_TYPE_MAP[self.type]


class PrimaryKey(Column):
    def __init__(self, column_type=int, auto_increment=True):
        self.auto_increment = auto_increment
        super().__init__(column_type)


class ForeignKey(Column):
    def __init__(self, table: type["Table"], column_type=int):
        self.table = table
        super().__init__(column_type)
