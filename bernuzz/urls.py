# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bernuzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('basic.urls', namespace='basic')),
    url(r'', include('hierarchy.urls', namespace='hierarchy')),
    url(r'', include('management.urls', namespace='management')),
    url(r'', include('workflow.urls', namespace='workflow')),
#    url(r'^/$', '', name='dashboard'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)

# /username
# /username/project
#     announcements
# /username/project/settings
# /username/project/workflows
# /username/project/(workflow_hash)
# /username/project/tasks
# /username/project/settings
#     roles
# /username/settings

# /teamname
#     announcements

    
# /teamname/project
#     announcements
    
# /teamname/project/settings
# /teamname/project/workflows
# /teamname/project/(workflow_hash)
# /teamname/project/tasks
# /teamname/project/settings
#     roles
# /teamname/settings
#     roles