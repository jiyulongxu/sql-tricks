# -*- coding: utf-8 -*-
from __future__ import with_statement
from sqltricks.insert import *
from sqltricks.fields import *
import db
import logging

logging.getLogger().setLevel(logging.DEBUG)


def test_insert():
    assert InsertTable('test', runner=db.conn.execute)(
        name='name2',
        age=32,
        money=323.2
    ) == """INSERT INTO `test` (age,money,name) values(32, 323.2, "name2");"""

    db.conn.commit()


if __name__ == '__main__':
    test_insert()
