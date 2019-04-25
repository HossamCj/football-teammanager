from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import TeamForm, TeamModelForm
from .models import Team, GameScore, Player


def home(request):
    all_teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': all_teams})


class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'


class GameScoreView(ListView):
    model = GameScore
    template_name = 'scores_list.html'
    context_object_name = 'scores'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_objects_name = 'team'
    slug_field = 'name'


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player_detail.html'
    contexT_object_name = 'player'
    slug_field = 'name'


class AddTeamView(View):
    def get(self, request):
        form = TeamForm()
        context = {'form': form}
        return render(request, 'add_team.html', context)

    def post(self, request):
        form = TeamModelForm()
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form, 'error_msg': 'This team is already exist!'}
            return render(request, 'add_team.html', context)