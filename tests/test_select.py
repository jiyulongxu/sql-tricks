# -*- coding: utf-8 -*-
from __future__ import with_statement
from sqltricks.query import *
from sqltricks.fields import *
import db
import logging

logging.getLogger().setLevel(logging.DEBUG)


def test_select():

    def query(sql):
        c = db.conn.cursor()
        cursor = c.execute(sql)
        for row in cursor:
            print(row)

    assert SelectTable('test', '*', runner=query)(
        Where(name='namxce')
    ) == 'SELECT * FROM `test` WHERE name="namxce";'



if __name__ == '__main__':
    test_select()
