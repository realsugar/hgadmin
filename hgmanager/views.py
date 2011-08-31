from django.core import validators
from django.http import Http404, HttpResponseRedirect
from models import Developer
from django.shortcuts import render_to_response
from django import forms


class DeveloperEditForm(forms.Form):
    login = forms.CharField(required=False,
                            label='Mercurial login',
                            widget = forms.TextInput(attrs={'readonly':'readonly'}))

    validator_list= [validators.MinLengthValidator(4),
                      validators.MaxLengthValidator(32)]


    password = forms.CharField(max_length=32,
                            label = 'New Mercurial password',
                            widget = forms.PasswordInput(),
                            validators=validator_list)
    confirm = forms.CharField(max_length=32,
                            label = 'Confirm password',
                            widget= forms.PasswordInput(),
                            validators=validator_list)

    def clean(self):
        cleaned_data = self.cleaned_data
        new_password = cleaned_data.get('password')
        new_confirm = cleaned_data.get('confirm')

        if new_confirm != new_password:
            raise forms.ValidationError("Passwords does not match!")
        
        return cleaned_data
    

def developer_list(request):
    developers = Developer.all()
    return render_to_response('hgmanager/developer_list.html',
            { 'developers': developers })


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
        return HttpResponseRedirect('/developer/list')

    # Form is not valid
    return response(form, login)