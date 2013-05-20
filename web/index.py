#!/usr/bin/python
# encoding: utf-8

import sys

reload(sys) 
sys.setdefaultencoding('utf8')

#sys.path.append('/home/longer/py_lib')

import md5

import web

from utils import cache
from utils import file_system

from markdown import Markdown
md = Markdown()

web.config.debug = True

urls = (
    "/(.*)/", 'SeeOther',   
    #"/pics/(.*)", 'Redirect',
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

def result_html(file_name, css_file, data):
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

    content = replace(content, data)

    web.header('Content-Type', 'text/html')
    return replace(common, {
        'content': content,
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
            first_10_html = info['first_10_html']
            first_10_html = first_10_html.replace(
                'tittle--tittle',
                '<a href="article?a=%s">%s</a>'%(
                    info['article_key'], info['tittle']
                )
            )
            result.append(
                '<div class="article_short">'+ first_10_html + '</div><div class="cutline"></div>'
            )
        
        return result_html(
            './templates/index.html',
            '',
            {
                'index_content': ''.join(result)
            }
        )

class Article(object):
    def GET(self, ):
        params = web.input()
        article_key = params.a

        f = open(file_system.CACHE_PATH + article_key + '/html', 'r')
        data = f.read()
        f.close()

        return result_html(
            './templates/article.html',
            'article.css',
            {
                'article': data,
            }
        )

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
        


