from django.conf.urls.defaults import patterns, include, url
from views import *


# TODO: split urls
urlpatterns = patterns('',
    url(r'^$', index),
    (r'^developer/$', developer_list),
    (r'^developer/add/$', developer_add),
    (r'^developer/edit/(?P<login>[\w\.\-_]+)/$', developer_edit),
    (r'^developer/delete/(?P<login>[\w\.\-_]+)/$', developer_delete),
    (r'^project/$', project_list)
)
  