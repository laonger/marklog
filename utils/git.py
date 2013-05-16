#!/usr/bin/python
# encoding: utf-8

import os
import file_system

last_commit = 'b8c4e2996f910192331eca04efaac1d924e12004'

# ::版本号::时间戳::短版本号::作者::note
COMMIT_INFO_CMD = 'cd articles && git pull && git log --name-only --pretty=format:aa--aa%n::%H::%ct::%h::%cn::%s%n====%n'

def new_commits():
    """# a: docstring
    args:
        :    ---    arg
    returns:
        0    ---    
    """
    output_obj = os.popen(COMMIT_INFO_CMD)
    output = output_obj.read()
    new_commit_str = output.split(last_commit)[0].rstrip('::')
    new_commit_list = [i.strip('\n') for i in new_commit_str.split('aa--aa') if i.startswith('\n::')]

    result = []
    for c in new_commit_list:
        info = commit_info(c)
        result.append(info)
    return result

def get_all_commit_info():
    """# get_all_conmit_info: docstring
    args:
        :    ---    arg
    returns:
        0    ---    
    """
    output_obj = os.popen(COMMIT_INFO_CMD)
    new_commit_str = output_obj.read()
    new_commit_list = [i.strip('\n') for i in new_commit_str.split('aa--aa') if i.startswith('\n::')]

    result = []
    for c in new_commit_list:
        info = commit_info(c)
        result.append(info)
    return result

def commit_info(commit_str):
    """# commit_info: docstring
    args:
        commit_str:    ---    arg
    returns:
        长版本号，时间戳，短版本号，作者，提交note，文章目录名
        ('3993a60f52c35ded2732fbf94fe2981e4d98cac7', '1368116966', '3993a60', 'la.onger', 'test\n', 'video_glass')
    """
    commit_str = commit_str.strip('aa--aa\n')
#    print '#'*36, commit_str
    info_str, file_str = commit_str.split('====')
    info_list = info_str.strip('::').split('::')

    file_list = file_str.strip('\n').split('\n')
    dir_name = file_list[0].split(os.path.sep)[0]

    info_list.append(dir_name)
    return tuple(info_list)

def get_commit_info(commit_version_long):
    """# get_co: docstring
    args:
        arg:    ---    arg
    returns:
        0    ---    
    """
    cmd = 'cd articles && git log --name-only --pretty=format:aa--aa%n::%H::%ct::%h::%cn::%s%n====%n ' + commit_version_long + ' ' + commit_version_long
    commit_str = os.popen(cmd).read()
    #print commit_str
    return commit_info(commit_str)

if __name__ == '__main__':
    #a()
    #print get_all_commit_info()
    print get_commit_info('b8c4e2996f910192331eca04efaac1d924e12004')
