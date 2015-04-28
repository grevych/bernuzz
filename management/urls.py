# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import ProjectList


urlpatterns = patterns('',
    #user dashboard
    url(r'^projects/$', ProjectList.as_view(), name='projects'),

    url(r'^(?P<account>[\w|-]+)/$', 'management.views.profile', name='profile'),
    url(r'^(?P<account>[\w|-]+)/settings/$', 'management.views.default', name='account_settings'),
    url(r'^(?P<account>[\w|-]+)/projects/$', 'management.views.default', name='account_projects'),
    url(r'^(?P<account>[\w|-]+)/(?P<project>[\w|-]+)/$', 'management.views.default', name='project'),
    url(r'^(?P<account>[\w|-]+)/(?P<project>[\w|-]+)/settings/$', 'management.views.default', name='project_settings'),
)
