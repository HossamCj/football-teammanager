from django.shortcuts import render
from django.views.generic import ListView, DetailView
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