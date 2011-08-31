from django.conf.urls.defaults import patterns, include, url
from views import *

urlpatterns = patterns('',
    (r'^developer/add/$', developer_add),
    (r'^developer/list/$', developer_list),
    (r'^developer/edit/(?P<login>[\w\.\-_]+)/$', developer_edit),
    (r'^developer/delete/(?P<login>[\w\.\-_]+)/$', developer_delete),
)
  