#!/usr/bin/python
# encoding: utf-8

import sys
#sys.path.append('/home/longer/py_lib')

import md5

import web

from utils import pages

from markdown import Markdown
md = Markdown()

web.config.debug = True

urls = (
    "/(.*)/", 'Redirect',   
    "/", "Article",
)

class Redirect(object):
    def GET(self, path):
        """# GET: docstring
        args:
            path:    ---    arg
        returns:
            0    ---    
        """
        web.seeother("/"+path)

class Index(object):
    def GET(self):

        return html%data

class Article(object):
    def GET(self, ):
        file = open('./articles/video_glass/main.mdown', 'r')
        text = file.read()
        file.close()
        text = unicode(text, 'utf-8')
        data = md.convert(text)
        return pages.make_html(
            './templates/article.html',
            'article.css',
            {
            'article': data,
            }
        )

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
        


