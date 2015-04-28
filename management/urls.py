# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import ProjectList


urlpatterns = patterns('',
    #user dashboard
    url(r'^projects/$', ProjectList.as_view(), name='projects'),
    url(r'^teams/$', 'hierarchy.views.render_teams', name='teams'),
    url(r'^teams/new/$', 'hierarchy.views.create_team', name='create_team'),
    url(r'^teams/update/(\d+)/$', 'hierarchy.views.update_team', name='update_team'),
    url(r'^teams/membership/$', 'hierarchy.views.assign_to_team', name='assign_to_team'),


    url(r'^(?P<username>[\w|-]+)/$', 'management.views.profile', name='profile'),
    url(r'^(?P<username>[\w|-]+)/settings/$', 'management.views.default', name='user_settings'),
    url(r'^(?P<username>[\w|-]+)/projects/$', 'management.views.default', name='user_projects'),
    url(r'^(?P<username>[\w|-]+)/(?P<project>[\w|-]+)/$', 'management.views.default', name='project'),
    url(r'^(?P<username>[\w|-]+)/(?P<project>[\w|-]+)/settings/$', 'management.views.default', name='project_settings'),

    url(r'^(?P<teamname>[\w|-]+)/$', 'hierarchy.views.render_team', name='team'),
    url(r'^(?P<teamname>[\w|-]+)/settings/$', 'management.views.default', name='team_settings'),
    url(r'^(?P<teamname>[\w|-]+)/projects/$', 'management.views.default', name='team_projects'),
    url(r'^(?P<teamname>[\w|-]+)/(?P<project>[\w|-]+)/$', 'management.views.default', name='project'),
    url(r'^(?P<teamname>[\w|-]+)/(?P<project>[\w|-]+)/settings/$', 'management.views.default', name='project_settings'),

)
