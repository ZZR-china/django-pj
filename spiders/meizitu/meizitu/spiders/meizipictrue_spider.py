# encoding=utf-8
# # -*- coding: utf-8 -*-

import scrapy
import os

import sys
sys.path.insert(0, '../../libs')

from createFolder import create_folder

class MeizituSpider(scrapy.Spider):
    name = "meizipic"
    allowed_domains = ['mzitu.com']
    start_urls = [
       'http://i.meizitu.net/2018/09/01c01-1.jpg'
    #    'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536302980442&di=9f9833e4825d344575f4aa200b68b1f2&imgtype=0&src=http%3A%2F%2Fm.360buyimg.com%2Fn12%2Fjfs%2Ft2161%2F78%2F1747729168%2F80066%2F381f9f33%2F5672f5e9N7dfa5a0e.jpg%2521q70.jpg'
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        year = response.url.split("/")[-3]
        month = response.url.split("/")[-2]
        img_path = self.handleFolder(year, month)
        create_folder(img_path)
        filename = img_path + '\\meizi-%s.jpg' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def handleFolder(self, year, month):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_path = str(dir_path) + '\pictures\\' + year + '\\' + month
        return img_path

