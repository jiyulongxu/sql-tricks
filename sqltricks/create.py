# -*- coding: utf-8 -*-
import logging
from sqltricks.drop import DropTable


class Create(object):
    CREATE = "CREATE"


class CreateTable(Create):
    """
    引用形式： CreateTable(runner=None)(Field,Field,Field)
    """
    TYPE = "TABLE"
    runner = None
    drop = None

    def __init__(self, name, drop=False, runner=None):
        self.name = name
        self.runner = runner
        self.drop = drop

    def __call__(self, *fields):
        _ = " ".join((self.CREATE, self.TYPE, "IF NOT EXISTS", "`{}`".format(self.name),
                      "(\n" + ",\n".join([field.raw for field in fields]) + "\n)"
                      )) + ';'
        if self.drop:
            DropTable(self.name, runner=self.runner)()
        logging.debug('\n'+_)
        if callable(self.runner):
            self.runner(_)
            logging.info("Table created successfully")
        return _
