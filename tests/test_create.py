# -*- coding: utf-8 -*-
from __future__ import with_statement
from sqltricks.create import *
from sqltricks.fields import *
import db
import logging

logging.getLogger().setLevel(logging.DEBUG)


def test_create():
    assert CreateTable('test', drop=True, runner=db.conn.execute)(
        VARCHAR(128, name='name', primary_key=True, not_null=True),
        INT(name='age', not_null=True),
        FLOAT(name='money'),
        DATE(name='update'),
    ) == """CREATE TABLE IF NOT EXISTS `test` (
`name` VARCHAR(128) PRIMARY KEY NOT NULL,
`age` INT NOT NULL,
`money` FLOAT,
`update` DATE
);"""


if __name__ == '__main__':
    test_create()
