from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from games.models import Game
 
def index(request):
  game_list = Game.objects.order_by('game_id').values_list('game_id', flat=True).distinct()
  context = {'game_list': game_list}
  return render(request, 'view_games/index.html', context)

def game(request, game_id):
  game = Game.objects.filter(game_id=game_id).distinct()[0]
  context = {'game': game}
  return render(request, 'view_games/game.html', context)
