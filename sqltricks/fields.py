from config import db


class Field(dict):
    default = {}

    def __init__(self, name=None, *args, **kwargs):
        kwargs.update(self.default)
        kwargs['name'] = '`{}`'.format(name)
        super(Field, self).__init__(*args, **kwargs)

    @property
    def raw(self):
        output = [self['name'], self['type']]
        if 'primary_key' in self and self['primary_key']:
            output.append('PRIMARY KEY')
        if 'not_null' in self and self['not_null']:
            output.append('NOT NULL')
        return " ".join(output)


class CharField(Field):
    def __init__(self, num, name=None, *args, **kwargs):
        super(CharField, self).__init__(name=name, *args, **kwargs)
        self['type'] = self['type'] + "({})".format(num)


if db == 'sqlite':
    INT = type('INT', (Field,), {'default': {'type': 'INT'}})
    VARCHAR = type('VARCHAR', (CharField,), {'default': {'type': 'VARCHAR'}})
    FLOAT = type('FLOAT', (Field,), {'default': {'type': 'FLOAT'}})
    DATE = type('DATE', (Field,), {'default': {'type': 'DATE'}})
elif db == 'mysql':
    CHAR = type('CHAR', (dict,), {})
