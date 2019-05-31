from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm

from .models import Team, GameScore


class TeamForm(forms.Form):
    name = forms.CharField()
    details = forms.CharField()


class TeamModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Add Team'))


    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'name':'Team Name',
            'details': 'Team Details'
        }

        error_messages = {
            'name': {
                'unique': 'This team is exist, sorry try another one!',
            }
        }


class ScoreModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScoreModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Add Score'))

    class Meta:
        model = GameScore
        exclude = ['game_date']

        labels = {
            'first_team_relation': 'First Team',
            'second_team_relation': 'Second Team',
            'first_team_score': 'First Team Score',
            'second_team_score': 'Second Team Score'
        }