from enum import Enum

from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=120)
    details = models.TextField(max_length=4000)

    def __str__(self):
        return self.name


class Player(models.Model):
    striker = 'Striker'
    defender = 'Defender'
    halfdefender = 'HalfDefender'
    goalkeeper = 'Goalkeeper'
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    number = models.IntegerField()
    position_in_field = models.CharField(
        max_length=120, choices=(
            (goalkeeper, 'GoalKeeper'),
            (defender, 'Defender'),
            (halfdefender, 'HalfDefender'),
            (striker, 'Striker')
        )
    )
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.team)


class GameScore(models.Model):
    first_team = models.CharField(max_length=120)
    second_team = models.CharField(max_length=120)
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)

    def __str__(self):
        return '{} {} - {} {}'.format(self.first_team, self.first_team_score, self.second_team, self.second_team_score)