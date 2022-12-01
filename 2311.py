from bs4 import BeautifulSoup as BS
import requests
from fake_useragent import UserAgent

url = "https://assets.htmlacademy.ru/content/blog/1331/index.html?_ga=2.67928081.1266088690.1669870302-1378654872.1669870299"
ua = UserAgent()

response = requests.get(url, headers = {'User-Agent':ua.firefox})
bs = BS(response.text, 'lxml')
print(bs.prettify())
temp = bs.find_all('a')
#temp = bs.find_all('div', class_ = 'sites-embed-content-textbook')
#s = input()
for w in temp:
	#if w.text == s:
	print(w.get('href'))
