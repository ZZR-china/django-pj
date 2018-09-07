## lean:

  https://docs.scrapy.org/en/latest/intro/tutorial.html

## command-line

  **check all spider**
	
	scrapy list

	scrapy shell "http://www.meizitu.com"

	title = response.css("div.title")

	or

	title = response.xpath("//title")
  
  urls = title.extract_first().xpath("//a/@href")


## scrapy将爬虫数据保存为json
	
scrapey crawl huxiu -o name.json