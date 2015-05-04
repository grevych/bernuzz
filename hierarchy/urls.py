# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import render_teams, render_team, create_team, update_team



urlpatterns = patterns('',

    url(r'^team/$', create_team, name='team'),
    url(r'^team/(?P<team>[\w|-]+)/$', update_team, name='team_profile'),
    url(r'^teams/$', render_teams, name='teams'),
    url(r'^team/(?P<team>[\w|-]+)/settings/$', 'hierarchy.views.settings', name='team_settings'), 
    url(r'^team/(?P<team>[\w|-]+)/members/$', 'hierarchy.views.get_team_members', name='team_members'), 
    url(r'^team/(?P<team>[\w|-]+)/projects/$', 'hierarchy.views.render_teams', name='team_projects'), 

#    url(r'^team/(?P<team>[\w|-]+)/role/$', 'hierarchy.views.render_teams', name='team_role'), 

    
)
