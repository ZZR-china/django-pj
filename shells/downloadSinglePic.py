# -*- coding:utf-8 -*-


from createFolder import *
import urllib3
import os


def download(url, word):
    """
    download pic from baidu
    ~~~~~~~~~~~~~~~~~
    just run `python picDownload.py` and input your word
    """
    print('找到关键词:的图片，现在开始下载图片...')
    http = urllib3.PoolManager()
    pic = http.request('GET', url)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = str(dir_path) + '\pictures\\meizi'
    create_folder(img_path)
    img_path = img_path + '\\' + word + '.jpg'
    # resolve the problem of encode, make sure that chinese name could be store
    fp = open(img_path, 'wb')
    fp.write(pic.data)
    fp.close()


if __name__ == '__main__':
    word = input("Input key word: ")
    url = 'http://mm.chinasareview.com/wp-content/uploads/2014a/03/14/01.jpg'
    download(url, word)
