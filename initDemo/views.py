from django.shortcuts import render

from django.http import HttpResponse

#爬虫所需
import requests
from bs4 import BeautifulSoup
url = 'http://news.sina.com.cn/china/'
res = requests.get(url)
res.encoding = 'UTF-8'
soup = BeautifulSoup(res.text, 'html.parser') # 使用剖析器为html.parser

class News:
	def __init__(self, title, time, href):
		self.title   = title
		self.time    = time
		self.href    = href

	def getTitle(self):
		return self.title
	def getTime(self):
		return self.time
	def getHref(self):
		return self.href


# Create your views here.
def getNews(request):
	news_list = []
	for news in soup.select('.news-item'):
		h2 = news.select('h2')    
		if len(h2) > 0:
			time = news.select('.time')[0].text
			title = h2[0].text
			href = h2[0].select('a')[0]['href']
			obj = News(title, time, href)
			news_list.append(obj)
	return render(request, 'initShow.html', {'news_list':news_list})

