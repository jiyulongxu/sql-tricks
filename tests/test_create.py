# -*- coding: utf-8 -*-
from __future__ import with_statement
import unittest
from sqltricks.create import *
from sqltricks.fields import *


def test_welcome():
    assert CreateTable('test')(
        INT(name='name'),
        INT(name='age'),
    ) == \
"""CREATE TABLE test (
name INT,
age INT
)"""



if __name__ == '__main__':
    test_welcome()
