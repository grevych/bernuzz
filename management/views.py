# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from models import Project
#from books.models import Publisher

# Create your views here.



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def default(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def profile(request):
    return HttpResponse("Hello, world. You're at the polls index.")





class ProjectList(LoginRequiredMixin, ListView):
    #paginate_by = 50
    context_object_name = 'user_projects'
    template_name = "management/projects.html"

    def get_queryset(self):
        # from basic.models import User
        # u = User()
        # u.user = self.request.user
        # u.save()
        # self.request.user.save()
        print self.request.user.member.projects.filter(project__active=True)
        return self.request.user.member.projects.filter(project__active=True)

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        user_teams = [team_member.team.pk for team_member in self.request.user.member.teams.all()]
        print 'DA: ', user_teams
        print self.request.user.username
        context['teams_projects'] = Project.objects.filter(team__in=user_teams).filter(active=True)
        print context['teams_projects']
        return context
