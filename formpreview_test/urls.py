"""formpreview_test URL Configuration

"""
from django.conf.urls import patterns, url
from poolapp.apps.post import views
from .preview import GameFormPreview
from .forms import GameForm
from django import forms

urlpatterns = patterns('',
  url(r'^post/$', GameFormPreview(GameForm)),
  url(r'^post/submit$', views.form_upload, name='form_upload'),
)
