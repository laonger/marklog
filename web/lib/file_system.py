#!/usr/bin/python
# encoding: utf-8

import os
import sys

from settings import *

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
    os.symlink(source_path, target_path)

def rm_dir(dir):
    """# rm_dir: docstring
    args:
        dir_path:    ---    arg
    returns:
        0    ---    
    """
    os.system('rm -rf ' + dir)
    
    
