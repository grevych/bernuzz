# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    #user dashboard
    url(r'^teams/$', 'hierarchy.views.render_teams', name='teams'),
    #creacion, edicicreatec de equipos
    url(r'^(?P<account>[\w|-]+)/team/$', 'hierarchy.views.create_team', name='team'),
    url(r'^(?P<account>[\w|-]+)/member/$', 'hierarchy.views.assign_to_team', name='team_member'),

    #creacion, edicion, etc de roles de equipo
    url(r'^(?P<account>[\w|-]+)/role/$', 'hierarchy.views.render_teams', name='team_role'),

    #url(r'^roles/$', 'hierarchy.views.render_roles', name='roles'),
    #url(r'^roles/new/$', 'hierarchy.views.create_role', name='create_role'),
    #url(r'^roles/update/(\d+)/$', 'hierarchy.views.update_role', name='update_role'),
    #url(r'^teams/new/$', 'hierarchy.views.create_team', name='create_team'),
    #url(r'^teams/update/(\d+)/$', 'hierarchy.views.update_team', name='update_team'),
)
