from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^edit/', views.edit, name='edit'),
    )