#!/usr/bin/python
# encoding: utf-8

import os
import time

import file_system
import git

from markdown import Markdown

md = Markdown()

ARTICLE_CACHE_TEMPLATE  = """
    <div id='tittle'><h1>{tittle}</h1></div>
    <p id='post_time'>{commit_time}</p>
    <div id='content'>{content}</div>
"""

def article_html(file_name, merge_data):
    """# make_info: docstring
    args:
        file_name:    ---    arg
    returns:
        0    ---    
    """
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    text = unicode(text, 'utf-8')
    html = md.convert(text)

    tittle, content = html.split('</h1>', 1)
    tittle = tittle.lstrip('<h1>')

    merge_data.update({
        'tittle': tittle,
        'content': content,
    })
    content = ARTICLE_CACHE_TEMPLATE.format(**merge_data)

    first_10 = text.replace('\r', '').strip('\n').split('\n')[:10]
    first_10_html = md.convert('\n'.join(first_10))
    first_10_html = first_10_html.split('</h1>', 1)[1]

    merge_data.update({
        'tittle': 'tittle--tittle',
        'content': first_10_html,
    })
    first_10_html = ARTICLE_CACHE_TEMPLATE.format(**merge_data)

    return {
        'article_html': content, 
        'first_10_html': first_10_html,
        'article_tittle': tittle,
    }

def get_cache_patch_from_hash(hash_str):
    """# get_patch_from_md5: 通过md5字符串得到路径
    args:
        md5_str:    ---    arg
    returns:
        0    ---    
    """
    path_str = file_system.CACHE_PATH + hash_str + os.sep
    return path_str

def cache_one(commit_info):
    """# cache_one: 一篇文章的缓存信息
    args:
        commit_info:    ---    arg
    returns:
        0    ---    
    """
    mark_down_file = file_system.ARTICLE_PATH + commit_info[5] + file_system.SEP + file_system.ARTICLE_MAIN_FILE

    article_key = commit_info[5]

    article_info = article_html(mark_down_file, 
        {
            'commit_time': time.ctime(float(commit_info[1])),
        }
    )

    cache = {
        'first_10_html': article_info['first_10_html'],
        'tittle': article_info['article_tittle'],
        'commit_time': commit_info[1],
        'article_short_version': commit_info[2],
        'article_key': article_key,
        'author_name': commit_info[3],
        'author': commit_info[3],
        'commit_note': commit_info[4],
        'origin_dir': commit_info[5],
    }

    article_cache_path = get_cache_patch_from_hash(article_key)
    mkdir_rc = file_system.mkdir(article_cache_path)
    if not mkdir_rc:
        file_system.ln(
            file_system.ARTICLE_PATH
                + cache['origin_dir']
                + file_system.SEP
                + file_system.ARTICLE_PIC
                + file_system.SEP
            , article_cache_path
                + file_system.ARTICLE_PIC)
        file_system.ln(
            file_system.ARTICLE_PATH
                + cache['origin_dir']
                + file_system.SEP
                + file_system.ARTICLE_FILES
                + file_system.SEP
            , article_cache_path
                + file_system.ARTICLE_FILES)
    html_cache_file = open(article_cache_path + 'html', 'w')
    html_cache_file.write(article_info['article_html'])
    html_cache_file.close()
    return cache

def cache_all():
    """# refresh_all: docstring
    args:
        :    ---    arg
    returns:
        0    ---    
    """
    file_system.rm_dir(file_system.CACHE_PATH)
    file_system.mkdir(file_system.CACHE_PATH)
    all_commit_info = git.get_all_commit_info()
    all_commit_info.reverse()
    result_dict = {}
    result_key_list = []
    for c_info in all_commit_info:
        cache = cache_one(c_info)
        result_dict[cache['article_key']] = cache
    cache_file = open(file_system.CACHE_SUM, 'w')
    cache_file.write('cache_sum = '+str(result_dict))

    cache_file.write('\n\n')

    result_key_list = result_dict.keys()
    result_key_list.sort(key=lambda x: float(result_dict[x]['commit_time']), reverse=True)
    cache_file.write('cache_key = '+str(result_key_list))

    cache_file.close()
    
if __name__ == '__main__':
    #print cache_one(git.get_commit_info('b8c4e2996f910192331eca04efaac1d924e12004'))
    cache_all()
