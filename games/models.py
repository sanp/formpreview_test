# models.py
from django.db import models
from django import forms

class Game(models.Model):

  # Game Choices
  FOOTBALL = 0
  BASKETBALL = 1
  TENNIS = 2
  OTHER = 3
  GAME_CHOICES = (
      (FOOTBALL, 'Football'),
      (BASKETBALL, 'Basketball'),
      (TENNIS, 'Tennis'),
      (OTHER, 'Other')
    )

  game_id = models.AutoField(primary_key=True)
  location = models.CharField(max_length=200, verbose_name="Location")
  game = models.IntegerField(choices=GAME_CHOICES, default=FOOTBALL)
  game_date = models.DateField(verbose_name='Game Date')
