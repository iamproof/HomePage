from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite_1.views.home', name='home'),
    url(r'^auth/', include('auth.urls', namespace="auth")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^news/', include('news.urls', namespace="news")),
    url(r'^get_image/', include('get_image.urls', namespace="get_image")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^polls/', include('polls.urls', namespace="polls")), # instance namespace polls
    url(r'^flash_message/', include('flash_message.urls', namespace="flash_message")),
    url(r'^csv_db/', include('csv_db.urls', namespace="csv_db")),
    url(r'^admin/', include(admin.site.urls)),

)
