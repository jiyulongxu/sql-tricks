# -*- coding: utf-8 -*-
import logging


class Drop(object):
    Drop = "Drop"


class DropTable(Drop):
    TYPE = 'TABLE'

    def __init__(self, name, runner=None):
        self.name = name
        self.runner = runner

    def __call__(self):
        _ = " ".join((self.Drop, self.TYPE, "IF EXISTS", self.name)) + ';'
        logging.debug(_)
        if callable(self.runner):
            self.runner(_)
            logging.info("Table drop successfully")
        return _
