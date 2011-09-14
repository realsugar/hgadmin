from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', developer_list, name="developers-list"),
    url(r'^add/$', developer_add, name="developers-add"),
    url(r'^edit/(?P<login>[\w\.\-_]+)/$', developer_edit, name="developers-edit"),
    url(r'^delete/(?P<login>[\w\.\-_]+)/$', developer_delete, name="developers-delete"),
)

  