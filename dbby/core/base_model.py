from .text import quote_if_str


class BaseModel(object):

    TABLE_NAME = ''

    FIELDS = []

    def __init__(self, **kwds):
        for k, v in kwds.iteritems():
            setattr(self, k, v)

    def __setattr__(self, name, value):
        if name in self.FIELDS:
            super(BaseModel, self).__setattr__(name, value)
        else:
            raise KeyError('Invalid sites column: %s' % name)

    def effective_fields_values(self):
        fields = []
        values = []
        for k in self.FIELDS:
            value = getattr(self, k, None)
            if value != None:
                fields.append(k)
                values.append(quote_if_str(value))
        return fields, values
