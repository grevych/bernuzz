# -*- encoding:utf-8 -*-

from django.conf.urls import patterns, include, url

from views import ProjectList, ProjectCreate, ProjectDetail, ProjectSettingsList




urlpatterns = patterns('',

    url(r'^project/$', ProjectCreate.as_view(), name='project'),
    url(r'^project/(?P<project>[\w|-]+)/$', ProjectDetail.as_view(), name='project'),
    url(r'^projects/$', ProjectList.as_view(), name='projects'),

    url(r'^project/(?P<project>[\w|-]+)/settings/$', ProjectSettingsList.as_view(), name='settings'), #ajax? PODRIA SER
    #url(r'^(?P<account>[\w|-]+)/(?P<project>[\w|-]+)/settings/$', 'management.views.default', name='project_settings'),



    #url(r'^(?P<account>[\w|-]+)/$', AccountProfile.as_view(), name='profile'), # perfil publico de usuario o equipo
    #url(r'^(?P<account>[\w|-]+)/(?P<project>[\w|-]+)/$', ProjectProfile.as_view(), name='project'), #perfil publico de proyecto
    #url(r'^(?P<account>[\w|-]+)/projects/$', 'management.views.default', name='account_projects'), #ajax?

)



#cambiar a profile el nombre de usuario nuevo

#PERFILES PUBLICOS
    #->proyecto
    #->usuario
    #->equipo

#equipos y proyectos van a tener como principal en publico, anuncios públicos y logs publicos
    #y aqui a la vez, opciones para ver cosas del perfil
        #proyectos
            #-> anuncios
            #-> logs
            #-> workflows
            #-> colaboradores
            #-> estado actual del proyecto
            #-> privacidad
            #-> skills
            #-> fecha de inicio de proyecto

        #equipos
            #->anuncios
            #->miembros
            #->proyectos
            #->instituciones
            #->¿¿¿skils???


#usuario
    #->proyectos
    #->equipos
    #->skills
    #->instituciones
    #->fecha de ingreso a bernuzz
    #->pefiles parecidos
    #->¿¿¿participaciones actuales a proyectos, estilo github???



#WORKSPACES PRIVADOS
    #dashboard de usuario
        #usuario va a tener TL de todas las cosas que han sucedido en sus proyectos, equipos y equipos y proyectos que sigue
            #esto como dashboard al ingresar a su perfil, privado
        #acceso rapido a proyectos
        #acceso rapido a equipos
        #acceso rapido a explore
        #workflows de toooodo al momento -> mucho poder de computo
        #TASKS GENERALES DE TODO LO QUE TIENE PENDIENTE O HA TERMINADO RECIENTEMENTE
        #settings de cuenta
        #creacion rapida de proyectos
        #creacion rapida de equipos
        # **ISSUES SON COMO TASKS :P

    #perfil privado de proyecto
        #settings
            #colaboradores
            #privacidad
            #skills
            #permisos
        #workflows
        #tasks
        #anuncios

    #perfil privado de equipo
        #settings
            #miembros
            #roles
            #privacidad
            #skills
            #estadisticas... ???

        #workflows del equipo -> INNECESARIO CREO YO
        #tasks de todos los pendientes de los proyectos involucrados del equipo -> INNECESARIO

        #proyectos
        #anuncios



