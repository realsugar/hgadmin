from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', project_list, name="projects-list"),
    url(r'^add/$', project_add, name="projects-add"),
    url(r'^edit/(?P<name>[\w\.\-_]+)/$', project_edit, name="projects-edit"),
    url(r'^delete/(?P<name>[\w\.\-_]+)/$', project_delete, name="projects-delete"),
)
  