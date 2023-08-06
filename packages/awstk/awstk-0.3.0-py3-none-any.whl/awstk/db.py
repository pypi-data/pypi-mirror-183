from sqlitedict import SqliteDict
import os

_connection = None


def get_connection(tablename: str):
    global _connection
    if not _connection:
        _connection = SqliteDict(
            f"{os.path.expanduser('~')}/.awstk.db", tablename=tablename)
    return _connection
