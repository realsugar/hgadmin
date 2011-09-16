from django.contrib import messages
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from projects.forms import ProjectForm
from projects.models import Project


def project_or_404(name):
    project = Project.get_by_name(name)
    if not project:
        raise Http404
    return project


def projects_list(request):
    projects = Project.all()
    return render_to_response('projects/list.html', {'projects': projects})


def project_details(request, name):
    project = project_or_404(name)
    return render_to_response('projects/details.html', {'project': project})


def project_add(request):
    if not request.POST:
        form = ProjectForm()
        return render_to_response('projects/add.html', {'form': form})
    return None


def project_edit(request, name):
    project = project_or_404(name)
    # TODO: implement me!
    return None


def project_delete(request, name):
    messages.error(request, "This feature is to be implemented.")
    return render_to_response('projects/delete.html',
                              context_instance=RequestContext(request))