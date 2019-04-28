from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm

from .models import Team


class TeamForm(forms.Form):
    name = forms.CharField(label='Team name')
    details = forms.CharField(label='Team details')


class TeamModelForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))