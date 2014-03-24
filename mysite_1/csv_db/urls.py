from django.conf.urls import patterns, url
from csv_db import views
	
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^csv_file/', views.csv_file, name='csv_file'),
    url(r'^(?P<order_item>[\w\-]+)/$', views.order, name='order'),
)