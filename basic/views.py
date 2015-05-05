# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.generic import ListView
from django.db.models import Count

from bernuzz.settings.private import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
from management.models import Skill
from models import User

from cluster.methods.kmeans import Kmeans

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def index(request):
    template_variables = {}
    if not request.user.is_authenticated():
        #template_variables['thumbnails']
        template_variables['GOOGLE_OAUTH2_KEY'] = SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        return render(request, 'index.html', template_variables)
    #template_variables['']
    return render(request, 'home.html', template_variables)
    #if user.is_active():


def login(request):
    # if request.method ==  'POST':
    #     return HttpResponse('HOLA')
    template_variables = {}
    template_variables['plus_id'] = SOCIAL_AUTH_GOOGLE_PLUS_KEY
    return render(request, 'login_.html', template_variables)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


class AccountSettingsList(LoginRequiredMixin, ListView):
    pass


class ExploreList(LoginRequiredMixin, ListView):
    context_object_name = 'skills'
    template_name = 'basic/explore.html'

    def get(self, request, *args, **kwargs):
        skills = request.GET.getlist('skills[]', None)

        if not skills:
            return super(ExploreList, self).get(request, *args, **kwargs)
        
        skills = [int(skill) for skill in skills]
        users = User.objects.filter(projects__project__skills__skill__in=skills).annotate(total=Count('user'))
        skills_vector_lenght = Skill.objects.all().count()
        cluster_users = []

        for user in users:
            vector = [0] * skills_vector_lenght
            skill_queryset = Skill.objects.filter(projects__project__users__user__pk=user.pk).annotate(total=Count('name'))
            for skill in skill_queryset:
                vector[skill.pk - 1] = float(skill.total)
                print user.user.username, skill.name, skill.total
            cluster_users.append({'user': user, 'vector': vector})

        kmean = Kmeans(clusters=skills_vector_lenght, dataset=cluster_users)
        clusters = kmean.run()
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        
        def break_loops(clusters_as_param):
            for cluster in clusters_as_param.values():
                #print cluster
                for element in cluster.get('set'):
                    #print element.id, request.user.member
                    if element.id.pk == request.user.member.pk:
                        return cluster
            return None 

        context['cluster'] = break_loops(clusters)
        context['all_skills'] = Skill.objects.all()
        return self.render_to_response(context)


    def get_queryset(self):
        project_user_queryset = self.request.user.member.projects.select_related('skills').all()
        skills = set([(project_skill.skill.pk, project_skill.skill.name, ) for project_user in project_user_queryset for project_skill in project_user.project.skills.all()])
        return [{'pk': skill[0], 'name': skill[1]} for skill in skills]
    # def get_context_data(self, **kwargs):
    #     context = super(ExploreList, self).get_context_data(**kwargs)
    #     user_teams = [team_member.team.pk for team_member in self.request.user.member.teams.all()]
    #     print 'DA: ', user_teams
    #     print self.request.user.username
    #     context['teams_projects'] = Project.objects.filter(team__in=user_teams).filter(active=True)
    #     print context['teams_projects']
    #     return context


# todos los skills existentes para el count o su pk mas grande

# consuta para saber mis skills
# seleccion de skills
# obtencion de usuarios con esos skills
# para cada usuario
#     obtener todos sus skills
#     crear una lista de ceros del tamaño de la cantidad de skills
#     recorrer por proyecto
#         cada skill sumarle en posicion de su pk

















