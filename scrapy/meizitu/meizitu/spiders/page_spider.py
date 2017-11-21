# encoding=utf-8
# # -*- coding: utf-8 -*-

import scrapy


class MeizituSpider(scrapy.Spider):
    name = "page"

    start_urls = [
       'http://www.meizitu.com/'
    ]

    def parse(self, response):
        # follow pagination links
        for href in response.css('div#wp_page_numbers ul li a::attr(href)'):
            if href is not None:
                yield response.follow(href, self.meizi)

    def meizi(self, response):
        yield {
           'url': response.url
        }