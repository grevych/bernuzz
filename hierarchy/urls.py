# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import render_teams, render_team, create_team



urlpatterns = patterns('',

    url(r'^team/$', create_team, name='team'),
    url(r'^team/(?P<team>[\w|-]+)/$', render_team, name='team'),
    url(r'^teams/$', render_teams, name='teams'),

    url(r'^team/(?P<team>[\w|-]+)/members/$', 'hierarchy.views.render_teams', name='team_members'), 
    url(r'^team/(?P<team>[\w|-]+)/projects/$', 'hierarchy.views.render_teams', name='team_projects'), 
    url(r'^team/(?P<team>[\w|-]+)/settings/$', 'hierarchy.views.render_teams', name='team_settings'), 

    url(r'^team/(?P<team>[\w|-]+)/role/$', 'hierarchy.views.render_teams', name='team_role'), 

    
)
