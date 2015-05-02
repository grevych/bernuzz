# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import WorkflowCreate, WorkflowDetail, WorkflowList
from views import StageCreate, StageDetail, StageList
from views import TaskCreate, TaskDetail, TaskList


urlpatterns = patterns('',

    #user dashboard
    #url(r'^workflows/$', 'workflow.views.default', name='workflows'),
    url(r'^tasks/$', TaskList.as_view(), name='tasks'),

    #todos o solo mios (donde yo participo) tasks y workflows?
    #en teoria deben ser todos a los que tengo permiso, estoy involucrado, participo o soy encargado
    # url(r'^(?P<username>\w+)/(?P<project>\w+)/tasks/$', 'workflow.views.default', name='user_tasks'),
    # url(r'^(?P<username>\w+)/(?P<project>\w+)/workflows/$', 'workflow.views.default', name='user_workflows'),
    # url(r'^(?P<username>\w+)/(?P<project>\w+)/(?P<workflow>\w+)/$', 'workflow.views.default', name='workflow'),

    # url(r'^(?P<teamname>\w+)/(?P<project>\w+)/tasks/$', 'workflow.views.default', name='team_tasks'),
    # url(r'^(?P<teamname>\w+)/(?P<project>\w+)/workflows/$', 'workflow.views.default', name='team_workflows'),
    # url(r'^(?P<teamname>\w+)/(?P<project>\w+)/(?P<workflow>\w+)/$', 'workflow.views.default', name='workflow'),

    url(r'^project/(?P<project>[\w|-]+)/task/$', TaskCreate.as_view(), name='task'), #ajax? PODRIA SER
    url(r'^project/(?P<project>[\w|-]+)/task/(?P<task>[\w|-]+)/$', TaskDetail.as_view(), name='task'), #ajax? PODRIA SER
    url(r'^project/(?P<project>[\w|-]+)/tasks/$', TaskList.as_view(), name='tasks'), #ajax? PODRIA SER
    
    url(r'^project/(?P<project>[\w|-]+)/stage/$', StageCreate.as_view(), name='stage'), #ajax? PODRIA SER
    url(r'^project/(?P<project>[\w|-]+)/stage/(?P<stage>[\w|-]+)/$', StageDetail.as_view(), name='stage'), #ajax? PODRIA SER
    url(r'^project/(?P<project>[\w|-]+)/stages/$', StageList.as_view(), name='stages'), #ajax? PODRIA SER
    
    url(r'^project/(?P<project>[\w|-]+)/workflow/$', WorkflowCreate.as_view(), name='workflow'), #ajax? PODRIA SER
    url(r'^project/(?P<project>[\w|-]+)/workflow/(?P<workflow>[\w|-]+)/$', WorkflowDetail.as_view(), name='workflow'), #ajax? PODRIA SER
    url(r'^project/(?P<project>[\w|-]+)/workflows/$', WorkflowList.as_view(), name='workflows'), #ajax? PODRIA SER
)
