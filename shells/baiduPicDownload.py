# -*- coding:utf-8 -*-


import os
import re
import requests

import sys
sys.path.insert(0, '../libs')

from createFolder import create_folder


def dowmload_pic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 0
    print('找到关键词:'+keyword+'的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_path = str(dir_path) + '\pictures\\' + keyword
        create_folder(img_path)
        img_path = img_path + '\\' + keyword + '_' + str(i) + '.jpg'
        print(img_path)
        # resolve the problem of encode, make sure that chinese name could be
        # store
        fp = open(img_path, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + \
        word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmload_pic(result.text, word)
