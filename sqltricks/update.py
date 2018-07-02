# -*- coding: utf-8 -*-
import logging
from sqltricks.codition import convert


class Update(object):
    UPDATE = "UPDATE"


class UpdateTable(Update):
    TYPE = 'TABLE'

    runner = None
    drop = None

    def __init__(self, name, update_values, **kwargs):
        self.name = name
        self.runner = kwargs.get('runner', None)
        self.drop = kwargs.get('drop', None)
        self.update = " AND ".join(["{}={}".format(k, convert(v)) for k, v in update_values.items()])

    def __call__(self, *args):
        _ = " ".join((self.UPDATE, "`{}`".format(self.name), 'SET', self.update,
                      )) + " ".join([str(i) for i in args]) + ';'
        logging.debug(_)
        if callable(self.runner):
            self.runner(_)
            logging.info("Table UPDATE successfully")
        return _
