from django.conf.urls import patterns, url
from ltApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login_user, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^dashboard/$', views.dashboard, name='dashboard'),
        url(r'^register/$', views.register, name='register'))