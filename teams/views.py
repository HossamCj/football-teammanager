from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import TeamForm, TeamModelForm, ScoreModelForm
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

    def get_context_data(self, **kwargs):
        context = super(GameScoreView, self).get_context_data(**kwargs)
        context['form'] = ScoreModelForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ScoreModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/scores/')



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
        form = TeamModelForm()
        context = {'form': form}
        return render(request, 'add_team.html', context)

    def post(self, request):
        form = TeamModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'add_team.html', context)

# class AddScoreView(View):
#     def get(self, request):
#         form = ScoreModelForm()
#         context = {'form': form}
#         return render(request, 'add_score.html', context)
#
#     def post(self, request):
#         form = ScoreModelForm()
#         if form.is_valid():
#             form.save()
#             return redirect('/scores')
#         else:
#             context = {'form': form}
#             return render(request, 'add_score.html', context)
