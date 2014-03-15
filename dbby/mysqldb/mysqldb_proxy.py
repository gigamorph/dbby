import types

import MySQLdb


class MySQLDBProxy:

    def __init__(self, host='', db='', user='', passwd='', debug=False):
        self.debug = debug

        if host != '' and db != '' and user != '' and passwd != '':
            self.connect(host, db, user, passwd)
        return

    def connect(self, host, db, user, passwd):
        self.db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db,
                                  charset='utf8')
        return

    def exec_query(self, query):
        c = self.db.cursor()
        c.execute(query)
        c.close()
        return

    def exec_query_with_cursor(self, query, cursor):
        cursor.execute(query)
        return cursor

    def exec_query_commit(self, query):
        self.exec_query(query)
        self.db.commit()
        return

    def fetchall(self, query):
        c = self.db.cursor()
        self.exec_query_with_cursor(query, c)
        rows = c.fetchall()
        c.close()
        return rows

    def fetchone(self, query):
        c = self.db.cursor()
        self.exec_query_with_cursor(query, c)
        row = c.fetchone()
        c.close()
        return row
