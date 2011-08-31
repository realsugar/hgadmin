from django.core import validators
from django import forms
from hgmanager.validators import password_validator, login_validator


class DeveloperForm(forms.Form):
    validator_list = [validators.MinLengthValidator(4),
                        validators.MaxLengthValidator(32),
                        password_validator()]

    password = forms.CharField(max_length=32,
                            label = 'New Mercurial password',
                            widget = forms.PasswordInput(),
                            validators=validator_list)
    confirm = forms.CharField(max_length=32,
                            label = 'Confirm password',
                            widget = forms.PasswordInput(),
                            validators=validator_list)

    def clean(self):
        cleaned_data = self.cleaned_data
        new_password = cleaned_data.get('password')
        new_confirm = cleaned_data.get('confirm')

        if new_confirm != new_password:
            raise forms.ValidationError("Passwords does not match!")

        return cleaned_data


class DeveloperAddForm(DeveloperForm):
    login = forms.CharField(label='Mercurial login',
                        max_length=32,
                        validators=[login_validator()])

class DeveloperEditForm(DeveloperForm):
    pass