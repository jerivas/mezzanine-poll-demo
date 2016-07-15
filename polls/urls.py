#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<slug>[\w-]+)/vote/$', views.vote, name='vote'),
)
