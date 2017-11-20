# encoding=utf-8
# # -*- coding: utf-8 -*-

import scrapy


class MeizituSpider(scrapy.Spider):
    name = "meizitu"

    start_urls = [
       'http://www.meizitu.com/'
    ]

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.postContent a::attr(href)'):
            yield response.follow(href, self.parse_meizi)

        # follow pagination links
        for href in response.css('div#wp_page_numbers ul li a::attr(href)'):
            if href is not None:
               yield response.follow(href, self.parse)

    def parse_meizi(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_img(img, query):
            return img.css(query).extract_first().strip()

        imgslist = []

        for img in response.css('div.postContent div#picture p img'):
            item = {
                'title': extract_with_img(img, '::attr(alt)'),
                'src': extract_with_img(img, '::attr(src)')
            }
            imgslist.append(item)

        day = extract_with_css('div.day::text')
        month_Year = extract_with_css('div.month_Year::text')
        month_Year = month_Year.split('\u00a0')
        month = month_Year[0]
        year = month_Year[1]
        time = year + '-' + month + '-' + day

        title = extract_with_css('div.metaRight h2 a::text')

        yield {
            'time': time,
            'year': year,
            'month': month,
            'day': day,
            'title': title,
            'tags': extract_with_css('div.metaRight p::text'),
            'imgslist': imgslist
        }