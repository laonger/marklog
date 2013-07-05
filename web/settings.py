#!/usr/bin/python
# encoding: utf-8

import os
import sys

reload(sys) 
sys.setdefaultencoding('utf8')

SEP = os.path.sep

BASE_ROOT = os.path.dirname(os.path.abspath(__file__)) + SEP

STATIC_PATH = BASE_ROOT + 'static' + SEP

ARTICLE_PATH = BASE_ROOT + 'articles' + SEP
ARTICLE_MAIN_FILE = 'main.mdown'
ARTICLE_PIC = 'pics'
ARTICLE_FILES = 'files'

CACHE_URL = 'static' + SEP + 'cache' + SEP
CACHE_PATH = STATIC_PATH + 'cache' + SEP
CACHE_MARK_FILE = CACHE_PATH + 'cache_mark'
CACHE_SUM = BASE_ROOT + 'cache_sum.py'
