#!/usr/bin/python
# encoding: utf-8


def replace(source_text, values):
    """# replace: docstring
    args:
        source_text, values:    ---    arg
    returns:
        0    ---    
    """
    return 


def make_html(file_name, css_file, data):
    """# make_html: docstring
    args:
        file_name, data:    ---    arg
    returns:
        0    ---    
    """
    common_template = open('./templates/common.html', 'r')
    common = unicode(common_template.read(), 'utf-8')
    common_template.close()

    template = open(file_name, 'r')
    content = unicode(template.read(), 'utf-8')
    template.close()

    content = content.format(**data)

    return common.format(**{
        'content': content,
        'css_file': css_file,
    })
    
    
