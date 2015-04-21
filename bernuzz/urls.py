from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       url(r'^static/media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       url(r'^teams/', 'hierarchy.views.dashboard_teams', name='team')
)
