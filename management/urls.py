# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import ProjectList



urlpatterns = patterns('',

    #user dashboard
    url(r'^projects/$', ProjectList.as_view(), name='projects'),
    url(r'^teams/$', 'management.views.default', name='teams'),

    url(r'^(?P<username>[\w|-]+)/$', 'management.views.profile', name='profile'),
    url(r'^(?P<username>[\w|-]+)/settings/$', 'management.views.default', name='user_settings'),
    url(r'^(?P<username>[\w|-]+)/projects/$', 'management.views.default', name='user_projects'),
    url(r'^(?P<username>[\w|-]+)/(?P<project>[\w|-]+)/$', 'management.views.default', name='project'),
    url(r'^(?P<username>[\w|-]+)/(?P<project>[\w|-]+)/settings/$', 'management.views.default', name='project_settings'),

    url(r'^(?P<teamname>[\w|-]+)/$', 'management.views.default', name='team'),
    url(r'^(?P<teamname>[\w|-]+)/settings/$', 'management.views.default', name='team_settings'),
    url(r'^(?P<teamname>[\w|-]+)/projects/$', 'management.views.default', name='team_projects'),
    url(r'^(?P<teamname>[\w|-]+)/(?P<project>[\w|-]+)/$', 'management.views.default', name='project'),
    url(r'^(?P<teamname>[\w|-]+)/(?P<project>[\w|-]+)/settings/$', 'management.views.default', name='project_settings'),

)
