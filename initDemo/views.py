from django.shortcuts import render

from django.http import HttpResponse

#vue.js所需
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from django.views.generic import TemplateView

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
	def __str__(self):
		return '{"title": %s, "time": %s, "href": %s}' % (self.title, self.time, self.href) 

	def __dict__(self):
		dict = {}
		dict['title'] = self.title
		dict['time'] = self.time
		dict['href'] = self.href
		return dict

	def getTitle(self):
		return self.title
	def getTime(self):
		return self.time
	def getHref(self):
		return self.href

class UserEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, News):  
            return obj.__dict__()  
        return json.JSONEncoder.default(self, obj)


# Create your views here.
@require_http_methods(["GET"])
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
	
	response = {}
	response['list'] = json.dumps(news_list[0:10], cls=UserEncoder).encode('utf-8').decode('unicode_escape')

	return JsonResponse(response)
