#-*- coding:utf-8 -*-

"""
download pic from baidu
~~~~~~~~~~~~~~~~~
just run `python picDownload.py` and input your word
"""

import os
import re
import requests
import urllib3

from mkdir import *


def dowmloadPic(url, keyword):

    print('找到关键词:的图片，现在开始下载图片...')
    try:
        http = urllib3.PoolManager()
        pic=http.request('GET', url)
    except http.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
    dirPath = os.path.dirname(os.path.realpath(__file__))
    imgsDirPath = str(dirPath) + '\pictrues\\meizi'
    mkdir(imgsDirPath)
    imgsDirPath = imgsDirPath + '\\' + keyword + '.jpg'
    print(imgsDirPath)
    print(type(imgsDirPath))
    # resolve the problem of encode, make sure that chinese name could be store
    fp = open(imgsDirPath, 'wb')
    fp.write(pic.data)
    fp.close()


if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://mm.chinasareview.com/wp-content/uploads/2014a/03/14/01.jpg'
    dowmloadPic(url, word)
