from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'get_news$', views.getNews, )
	]