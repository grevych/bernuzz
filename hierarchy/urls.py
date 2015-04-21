# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    url(r'^(?P<username>\w+)/(?P<project>\w+)/roles/$', 'hierarchy.views.'),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/roles/$', ),
)
