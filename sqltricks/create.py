# -*- coding: utf-8 -*-
import logging
string = unicode


class Create(object):
    CREATE = "CREATE"


class CreateTable(Create):
    """
    引用形式： CreateTable(runner=None)(Field,Field,Field)
    """
    TYPE = "TABLE"
    runner = None

    def __init__(self, name, runner=None):
        self.name = name

    def __call__(self, *fields):
        SQL = " ".join((self.CREATE, self.TYPE, self.name,
                        "(\n" + ",\n".join([field.raw for field in fields]) + "\n)"
                        ))
        if callable(self.runner):
            self.runner(SQL)
        logging.info(SQL)
        return SQL
