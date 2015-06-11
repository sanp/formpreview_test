# preview.py
from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from .models import Game
from .forms import GameForm

class GameFormPreview(FormPreview):

  form_template = 'games/form_upload.html'
  preview_template = 'games/preview.html'

  def done(self, request, cleaned_data):
    # Do something with the cleaned_data, then redirect
    # to a "success" page.
    return HttpResponseRedirect('/games/success')
