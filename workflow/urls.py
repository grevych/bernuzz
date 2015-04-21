# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    #user dashboard
    url(r'^workflows/$', ),
    url(r'^tasks/$', ),

    url(r'^(?P<username>\w+)/(?P<project>\w+)/tasks/$', ),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/workflows/$', ),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<workflow>\w+)/$', ),

    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/tasks/$', ),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/workflows/$', ),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/(?P<workflow>\w+)/$', ),
)
