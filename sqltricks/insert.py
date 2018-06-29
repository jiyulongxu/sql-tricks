# -*- coding: utf-8 -*-
import logging
import json


class INSERT(object):
    INSERT = "INSERT INTO"


class InsertTable(INSERT):
    """
    引用形式： CreateTable(runner=None)(Field,Field,Field)
    """
    runner = None
    drop = None

    def __init__(self, name, drop=False, runner=None):
        self.name = name
        self.runner = runner
        self.drop = drop

    def __call__(self, **data):
        names, values = [i for i in zip(*data.items())]
        _ = " ".join((self.INSERT, "`{}`".format(self.name),
                      "(" + ",".join([name for name in names]) + ")",
                      "values({})".format(json.dumps(values)[1:-1])
                      )) + ';'
        logging.debug(_)
        if callable(self.runner):
            self.runner(_)
            logging.info("Table insert successfully")
        return _
