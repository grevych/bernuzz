# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    #user dashboard
    url(r'^workflows/$', 'workflow.views.default', name='workflows'),
    url(r'^tasks/$', 'workflow.views.default', name='tasks'),

    #todos o solo mios (donde yo participo) tasks y workflows?
    #en teoria deben ser todos a los que tengo permiso, estoy involucrado, participo o soy encargado
    url(r'^(?P<username>\w+)/(?P<project>\w+)/tasks/$', 'workflow.views.default', name='user_tasks'),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/workflows/$', 'workflow.views.default', name='user_workflows'),
    url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<workflow>\w+)/$', 'workflow.views.default', name='workflow'),

    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/tasks/$', 'workflow.views.default', name='team_tasks'),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/workflows/$', 'workflow.views.default', name='team_workflows'),
    url(r'^(?P<teamname>\w+)/(?P<project>\w+)/(?P<workflow>\w+)/$', 'workflow.views.default', name='workflow'),
)
