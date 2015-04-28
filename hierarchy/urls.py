# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^roles/$', 'hierarchy.views.render_roles', name='roles'),
    url(r'^roles/new/$', 'hierarchy.views.create_role', name='create_role'),
    url(r'^roles/update/(\d+)/$', 'hierarchy.views.update_role', name='update_role'),

   # url(r'^(?P<username>\w+)/(?P<project>\w+)/roles/$', 'hierarchy.views.render_roles'),
  #  url(r'^(?P<teamname>\w+)/(?P<project>\w+)/roles/$', 'hierarchy.views.default'),
)
