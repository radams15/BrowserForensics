import sqlite3


class Extractor(object):

    def __init__(self): pass

    def history(self): pass

    @staticmethod
    def _sqlite3_load_table(file, table):
        db = sqlite3.connect(file)

        c = db.cursor()

        # Must use interpolation as it is not possible to use sqlite3
        # placeholders with table name.
        c.execute(f'SELECT * FROM {table}')

        out = c.fetchall()

        db.close()

        return out
