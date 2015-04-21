# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bernuzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('basic.urls')),
    url(r'', include('hierarchy.urls')),
    url(r'^projects/', 'basic.views.login'),
    # url(r'^teams/', ),
    # url(r'^workflows/', ),
    # url(r'^tasks/', ),




    # url(r'(?P<username>\w+)/', ),
    # url(r'(?P<teamname>\w+)/', ),
    # url(r'', ),
    # url(r'', ),
    # url(r'', ),

    url('', include('social.apps.django_app.urls', namespace='social')),


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




    url(r'^admin/', include(admin.site.urls)),
)
