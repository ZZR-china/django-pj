# encoding=utf-8
# # -*- coding: utf-8 -*-

import scrapy


class MeizituSpider(scrapy.Spider):
    name = "meizipic"

    start_urls = [
       'http://mm.chinasareview.com/wp-content/uploads/2017a/07/14/10.jpg'
    ]

    def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'meizi-%s.jpg' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
