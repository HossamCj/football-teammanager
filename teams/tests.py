from django.test import TestCase

from .models import Team


class ModelsTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='my team', details='test team')
        self.assertEqual(team.name, 'my team')

class ViewTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='my team', details='test team')
        self.team1 = Team.objects.create(name='First team', details='This is the first team')
        self.team2 = Team.objects.create(name='Second team', details='This is the second team')

    def test_teams_list_view(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.team1, response.context['teams'])
        self.assertIn(self.team2, response.context['teams'])
        self.assertTemplateUsed(response, 'team_list.html')
        self.assertContains(response, self.team1)
        self.assertTemplateUsed(response, 'team_list.html')
        self.assertContains(response, self.team1)

    def test_team_detail_view(self):
        response = self.client.get('/team/my team/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.team, response.context['team'])