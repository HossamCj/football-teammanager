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