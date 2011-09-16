from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', developers_list, name="developers-list"),
    url(r'^profile/(?P<login>[\w\.\-_]+)/$', developer_profile, name="developer-profile"),
    url(r'^add/$', developer_add, name="developer-add"),
    url(r'^password/(?P<login>[\w\.\-_]+)/$', developer_password, name="developer-password"),
    url(r'^delete/(?P<login>[\w\.\-_]+)/$', developer_delete, name="developer-delete"),
)

  