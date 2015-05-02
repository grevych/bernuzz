# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import logout, index, AccountSettingsList


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^settings/$', AccountSettingsList.as_view(), name='settings'),
    #url(r'^(?P<account>[\w|-]+)/settings/$', 'management.views.default', name='account_settings'),

)
