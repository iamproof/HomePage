from django.conf.urls import patterns, url
from get_image import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	)