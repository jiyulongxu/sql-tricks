# -*- coding: utf-8 -*-
import sqlite3
import logging

conn = sqlite3.connect('db.sqlite')


def table_create(query):
    conn.execute(query)

