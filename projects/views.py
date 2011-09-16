from django.contrib import messages
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from projects.forms import ProjectForm
from projects.models import Project


def project_list(request):
    projects = Project.all()
    return render_to_response('projects/list.html', {'projects': projects})

def project_add(request):
    if not request.POST:
        form = ProjectForm()
        return render_to_response('projects/add.html', {'form': form})
    return None

def project_edit(request, name):
    return None

def project_delete(request, name):
    messages.error(request, "This feature is to be implemented.")
    return render_to_response('projects/delete.html',
                              context_instance=RequestContext(request))