# -*- coding:utf-8 -*-

# import datetime as dt
# from django.shortcuts import render_to_response, render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.http import HttpResponseRedirect, Http404, HttpResponse
# from django.contrib.auth.models import User, Group
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login
# from django.template import RequestContext
# from django.contrib.auth import logout

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from models import Project, Skill
from forms import SkillForm

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


def render_skills(request, teamname):
    template = "roles.html"
    template_variables = dict()
    skills = Skill.objects.all().filter(active=True, name=teamname)
    template_variables['group'] = skills
    template_variables['title'] = "Skills"
    return render(request, template, template_variables)


def create_skill(request):
    template = "form.html"
    template_variables = dict()
    form = SkillForm()
    template_variables['title'] = "Create Skill"
    template_variables['form'] = form
    template_variables['url_name'] = "hierarchy:create_skill"
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/skills/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


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

