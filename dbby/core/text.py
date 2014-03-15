def quote_if_str(value):
    if (type(value) is types.StringType or
        type(value) is types.UnicodeType):

        return "'%s'" % value
    else:
        return value
