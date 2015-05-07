# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import logout, index, AccountSettingsList, ExploreList, AccountCreate


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^settings/$', AccountSettingsList.as_view(), name='settings'),
    #url(r'^(?P<account>[\w|-]+)/settings/$', 'management.views.default', name='account_settings'),

    url(r'^welcome/$', AccountCreate.as_view(), name='account'),
    url(r'^explore/$', ExploreList.as_view(), name='settings'),

)
