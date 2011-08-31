from django.http import Http404, HttpResponseRedirect
from django.template.context import RequestContext
from models import Developer
from django.shortcuts import render_to_response
from django.contrib import messages
from hgmanager.forms import DeveloperEditForm, DeveloperAddForm

#
# Developer CRUD
#

def developer_add(request):
    response = lambda form: render_to_response('hgmanager/developer_add.html', { 'form': form })

    if not request.POST:
        form = DeveloperAddForm()
        return response(form)

    # Validating form and saving developer
    form = DeveloperAddForm(request.POST)
    if form.is_valid():
        developer = Developer()
        developer.set_login(form.cleaned_data['login'])
        developer.set_password(form.cleaned_data['password'])
        developer.save()

        messages.success(request, 'Developer %s was added successfully.' % developer.login())
        return HttpResponseRedirect('/developer/list')

    # Form is not valid
    return response(form)

    
def developer_list(request):
    developers = Developer.all()
    return render_to_response('hgmanager/developer_list.html',
                              { 'developers': developers },
                              context_instance=RequestContext(request))


def developer_edit(request, login):
    developer = Developer.get_by_login(login)
    if not developer:
        return Http404

    response = lambda form, login: render_to_response('hgmanager/developer_edit.html',
        { 'form' : form, 'login': login })

    if not request.POST:
        form = DeveloperEditForm(initial={ 'login' : login })
        return response(form, login)

    # Validating form and saving developer
    form = DeveloperEditForm(request.POST)
    if form.is_valid():
        developer.set_password(form.cleaned_data['password'])
        developer.save()

        messages.success(request, 'Password updated for %s.' % login)
        return HttpResponseRedirect('/developer/list')

    # Form is not valid
    return response(form, login)


def developer_delete(request, login):
    messages.error(request, "This feature is to be implemented.")
    return render_to_response('hgmanager/developer_delete.html',
                              context_instance=RequestContext(request))