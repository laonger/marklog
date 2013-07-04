#!/usr/bin/python
# encoding: utf-8

import sys

reload(sys) 
sys.setdefaultencoding('utf8')

#sys.path.append('/home/longer/py_lib')

import md5

import web

from lib import cache
from lib import file_system
from lib import page

from markdown import Markdown
md = Markdown()

web.config.debug = True

urls = (
    "/(.*)/", 'SeeOther',   
    "/", "Index",
    "/article", "Article",
)

class SeeOther(object):
    def GET(self, path):
        """# GET: docstring
        args:
            path:    ---    arg
        returns:
            0    ---    
        """
        web.seeother("/"+path)

def result_html(file_name, css_file, data):
    """# make_html: docstring
    args:
        file_name, data:    ---    arg
    returns:
        0    ---    
    """
    content = web.template.frender('templates/%s'%file_name)
    c = content(data)
    web.header('Content-Type', 'text/html; charset=UTF-8')
    return web.template.frender('templates/common.html')({
        'content': c,
        'css_file': css_file if css_file else 'common.css',
    })

class Index(object):
    def GET(self):
        cache.auto_fresh()
        if 'cache_sum' in  sys.modules:
            del sys.modules['cache_sum']
        import cache_sum

        result = []
        for i in cache_sum.cache_key:
            info = cache_sum.cache_sum[i]
            result.append(info)
        
        return result_html(
            'index.html',
            'index.css',
            result
        )

class Article(object):
    def GET(self, ):
        params = web.input()
        article_key = params.a

        import cache_sum

        data = cache_sum.cache_sum[article_key]

        return result_html(
            'article.html',
            'article.css',
            {
                'article_data': data,
            }
        )

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
        
