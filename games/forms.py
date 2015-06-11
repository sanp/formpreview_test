# forms.py
from django import forms
from django.forms import ModelForm 
from .models import Game

class GameForm(ModelForm):
  class Meta:
    model = Game
    fields = (
      'location',
      'game',
      'game_date'
    )
