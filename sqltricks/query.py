# -*- coding: utf-8 -*-
import logging
from sqltricks.codition import *


class SELECT(object):
    SELECT = "SELECT"


class SelectTable(SELECT):
    """
    引用形式： CreateTable(runner=None)(Field,Field,Field)
    """
    TYPE = "TABLE"
    runner = None
    drop = None

    def __init__(self, name, *fields, **kwargs):
        self.name = name
        self.runner = kwargs.get('runner', None)
        self.drop = kwargs.get('drop', None)
        self.fields = ','.join(fields)

    def __call__(self, *args):
        _ = " ".join((self.SELECT, self.fields, 'FROM', "`{}`".format(self.name),
                      )) + " ".join([str(i) for i in args]) + ';'
        logging.debug(_)
        if callable(self.runner):
            self.runner(_)
            logging.info("Table jquery successfully")
        return _
