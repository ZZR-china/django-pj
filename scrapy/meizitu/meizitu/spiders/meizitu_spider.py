import scrapy


class MeizituSpider(scrapy.Spider):
    name = "meizity"

    def start_requests(self):
        urls = [
            'http://www.meizitu.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'files/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
