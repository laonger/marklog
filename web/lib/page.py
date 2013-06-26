#!/usr/bin/python
# encoding: utf-8


def replace(str, data):
    """# replace: docstring
    args:
        str, data:    ---    arg
    returns:
        0    ---    
    """
    for k, v in data.iteritems():
        str = str.replace('{$%s$}'%k, v)
    return str

