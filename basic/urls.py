# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'basic.views.index'),

)
