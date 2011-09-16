from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.template.context import RequestContext
import developers
from models import Developer
from django.shortcuts import render_to_response
from django.contrib import messages
from forms import DeveloperEditForm, DeveloperAddForm


def back_to_developers_list():
    return HttpResponseRedirect(reverse(developers_list))


def developers_list(request):
    developers = Developer.all()
    return render_to_response('developers/list.html',
                              { 'developers': developers },
                              context_instance=RequestContext(request))


def developer_add(request):
    response = lambda form: render_to_response('developers/add.html', { 'form': form })

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

        return back_to_developers_list()

    # Form is not valid
    return response(form)


def developer_profile(request, login):
    developer = Developer.get_by_login(login)
    if not developer:
        raise Http404

    return render_to_response('developers/profile.html', {'developer': developer})


def developer_password(request, login):
    developer = Developer.get_by_login(login)
    if not developer:
        raise Http404

    response = lambda form, login: render_to_response('developers/password.html',
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

        return back_to_developers_list()

    # Form is not valid
    return response(form, login)


def developer_delete(request, login):
    messages.error(request, "This feature is to be implemented.")
    return render_to_response('developers/delete.html',
                              context_instance=RequestContext(request))