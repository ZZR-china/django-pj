from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp = urlopen('http://www.weather.com.cn/weather/101010100.shtml')
soup = BeautifulSoup(resp,'html.parser')
# tagToday = soup.find('p',class_ = "tem")
# try:
#     temperatureHigh = tagToday.span.string
# except AttributeError as e:
#     temperatureHigh = tagToday.find_next('p',class_="tem").span.string

# temperatureLow = tagToday.i.string
# weather = soup.find('p',class_="wea").string

# print('最低温度：' + temperatureLow)
# print('最高温度：' + temperatureHigh)
# print('天气：' + weather)
tagToday = soup.find_all('p',class_ = "tem")
print(tagToday)
for tag in tagToday:
    print(tag.span.string)
    pass