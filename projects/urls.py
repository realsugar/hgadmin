from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', projects_list, name="projects-list"),
    url(r'^details/(?P<name>[\w\.\-_]+)/$', project_details, name="project-details"),
    url(r'^add/$', project_add, name="project-add"),
    url(r'^edit/(?P<name>[\w\.\-_]+)/$', project_edit, name="project-edit"),
    url(r'^delete/(?P<name>[\w\.\-_]+)/$', project_delete, name="project-delete"),
)
  