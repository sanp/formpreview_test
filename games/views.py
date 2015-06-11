from django.shortcuts import render
from .models import Game
from .forms import GameForm

def form_upload(request):
  if request.method == 'GET':
    form = GameForm()
  else:
    # A POST request: Handle Form Upload
    form = GameForm(request.POST) # Bind data from request.POST into a GameForm
    # If data is valid, proceeds to create a new game and redirect the user
    if form.is_valid():
      game = form.save()
      return render(request, 'games/success.html', {})
  return render(request, 'games/form_upload.html', {
    'form': form,
  })
