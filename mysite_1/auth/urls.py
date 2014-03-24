from django.conf.urls import patterns, url
from auth import views



urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^logged_in/', views.logged_in, name='logged_in'),
	url(r'^logged_out/', views.logged_out, name='logged_out'),
	url(r'^invalid/', views.invalid, name='invalid'),
	url(r'^disabled/', views.disabled, name='disabled'),
	url(r'^registration/', views.registration, name='registration'),
	url(r'^confirmation/', views.confirmation, name='confirmation'),
	)
