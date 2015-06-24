import views

from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^game/(?P<game_id>\d+)/$', views.game, name='game'),
)
