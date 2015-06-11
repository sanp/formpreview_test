"""formpreview_test URL Configuration

"""
from django.conf.urls import patterns, url
from games import views
from games.preview import GameFormPreview
from games.forms import GameForm
from django import forms

urlpatterns = patterns('',
  url(r'^$', GameFormPreview(GameForm)),
  url(r'^/submit$', views.form_upload, name='form_upload'),
)
