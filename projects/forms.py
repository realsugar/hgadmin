from django.core import validators
from django import forms
from developers.models import Developer


class ProjectForm(forms.Form):
    ARCHIVE_CHOICES = (
        ('zip', 'zip'),
        ('gz', 'gz'),
        ('bz2', 'bz2'),
    )

    name = forms.CharField(label='Id',
                        max_length=32,
                        validators=[])

    description = forms.Textarea()

    contact = forms.CharField(label='Contact',
                        max_length=64,
                        validators=[])

    allow_archive = forms.MultipleChoiceField(choices=ARCHIVE_CHOICES,
                                              label="Allow archive",
                                              required=False)

    developer_choices = []
    developers = Developer.all()
    for developer in developers:
        developer_choices.append((developer.login(), developer.login()))

    allow_push = forms.MultipleChoiceField(choices=developer_choices,
                                           label='Allow push')

    allow_read = forms.MultipleChoiceField(choices=developer_choices,
                                           label='Allow read')

    def clean(self):
        cleaned_data = self.cleaned_data
        #new_password = cleaned_data.get('password')
        #new_confirm = cleaned_data.get('confirm')

        #if new_confirm != new_password:
        #    raise forms.ValidationError("Passwords does not match!")

        return cleaned_data


