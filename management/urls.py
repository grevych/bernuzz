# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    #user dashboard
    url(r'^projects/$', 'basic.views.login'),
    url(r'^teams/$', ),

    url(r'^(?P<username>\w+)/$', 'management.views.profile'),
    url(r'^(?P<username>\w+)/settings/$', 'management.views.'),
    url(r'^(?P<username>\w+)/projects/$', ),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/$', ),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/settings/$', ),

    url(r'^(?P<teamname>\w+)/$', ),
    url(r'^(?P<teamname>\w+)/settings/$', ),
    url(r'^(?P<teamname>\w+)/projects/$', ),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/$', ),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/settings/$', ),

)
