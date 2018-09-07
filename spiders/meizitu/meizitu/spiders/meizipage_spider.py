# encoding=utf-8
# # -*- coding: utf-8 -*-

import scrapy


class MeiziPageSpider(scrapy.Spider):
    name = "meizipage"

    start_urls = [
       'http://www.mzitu.com/149209'
    ]

    def parse(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_img(img, query):
            return img.css(query).extract_first().strip()

        imgdata = response.css('div.main-image p a img')

        img = {
          'title': extract_with_img(imgdata, '::attr(alt)'),
          'src': extract_with_img(imgdata, '::attr(src)')
        }

        title = extract_with_css('div.content h2::text')

        yield {
            'title': title,
            'img': img
        }