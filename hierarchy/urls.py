# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import render_teams, render_team, create_team, update_team, \
    TeamDetail, ProjectList, MemberList



urlpatterns = patterns('',

    url(r'^team/$', create_team, name='team'),
    url(r'^team/(?P<team>[\w|-]+)/$', TeamDetail.as_view(), name='team'),
    url(r'^teams/$', render_teams, name='teams'),
    url(r'^team/(?P<team>[\w|-]+)/settings/$', 'hierarchy.views.settings', name='team_settings'), 
    url(r'^team/(?P<team>[\w|-]+)/members/$', MemberList.as_view(), name='team_members'), 
    url(r'^team/(?P<team>[\w|-]+)/members/add/$', 'hierarchy.views.update_team', name='add_team_members'), 
    url(r'^team/(?P<team>[\w|-]+)/projects/$', ProjectList.as_view(), name='team_projects'), 

#    url(r'^team/(?P<team>[\w|-]+)/role/$', 'hierarchy.views.render_teams', name='team_role'), 

    
)
