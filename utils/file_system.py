#!/usr/bin/python
# encoding: utf-8

import os
import sys

reload(sys) 
sys.setdefaultencoding('utf8')

SEP = os.path.sep

BASE_ROOT = os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir + SEP

STATIC_PATH = BASE_ROOT + 'static' + os.sep

ARTICLE_PATH = BASE_ROOT + 'articles' + os.sep
ARTICLE_MAIN_FILE = 'main.mdown'
ARTICLE_PIC = 'pics'
ARTICLE_FILES = 'files'

CACHE_PATH = STATIC_PATH + 'cache' + os.sep
CACHE_SUM = BASE_ROOT + 'cache_sum.py'

def mkdir(path_str):
    """# mkdir: docstring
    args:
        path_st:    ---    arg
    returns:
        0    ---    
        1   目录已存在
    """
    if os.path.exists(path_str):
        return 1
    os.system('mkdir -p ' + path_str)

def ln(source_path, target_path):
    """# ln: docstring
    args:
        source_path, target_path:    ---    arg
    returns:
        0    ---    
    """
    os.symlink(source_path+'/', target_path)

def rm_dir(dir):
    """# rm_dir: docstring
    args:
        dir_path:    ---    arg
    returns:
        0    ---    
    """
    os.system('rm -rf ' + dir)
    
    
