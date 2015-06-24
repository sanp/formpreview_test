"""formpreview_test URL Configuration

"""
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^post_games', include('games.urls')),
    url(r'^view_games/', include('view_games.urls')),
)
