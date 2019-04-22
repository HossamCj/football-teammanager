# Generated by Django 2.2 on 2019-04-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20190415_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='game_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position_in_field',
            field=models.CharField(choices=[('Goalkeeper', 'GoalKeeper'), ('Defender', 'Defender'), ('HalfDefender', 'HalfDefender'), ('Striker', 'Striker')], max_length=120),
        ),
    ]
