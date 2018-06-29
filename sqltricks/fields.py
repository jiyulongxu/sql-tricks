from config import db


class Field(dict):
    default = {}

    def __init__(self, *args, **kwargs):
        kwargs.update(self.default)
        super(Field, self).__init__(*args, **kwargs)

    @property
    def raw(self):
        return self['name']+" "+self['type']

if db == 'sqlite':
    INT = type('INT', (Field,), {'default': {'type': 'INT'}})
elif db == 'mysql':
    CHAR = type('CHAR', (dict,), {})
