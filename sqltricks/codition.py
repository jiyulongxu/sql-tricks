# -*- coding: utf-8 -*-
import six


def convert(char):
    if isinstance(char, (six.binary_type, six.text_type)):
        return "\"{}\"".format(char)
    return six.text_type(char)


class Where(object):
    condition = {}

    def __init__(self, **kwargs):
        self.condition = kwargs

    def __str__(self):
        return " WHERE " + " AND ".join(["{}={}".format(k, convert(v)) for k, v in self.condition.items()])
