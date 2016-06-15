from django.conf.urls import patterns, url
from ltApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
