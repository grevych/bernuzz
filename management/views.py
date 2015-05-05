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
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.detail import SingleObjectMixin

from basic.models import User
from hierarchy.models import Team, TeamMember
from models import Project, Skill, ProjectUser
from forms import SkillForm, ProjectForm

# Create your views here.

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


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


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    fields = ['name', 'description', 'logo', 'access_level']
    template_name = 'management/project_create.html'

    def form_valid(self, form):
        self.success_url = reverse(
            'management:project', 
            kwargs={'project': form.cleaned_data.get('name')})
        print self.success_url

        response = super(ProjectCreate, self).form_valid(form)
        self.complete(form)
        return response

    # def form_invalid(self, form, *args, **kwargs):
    #     print super(ProjectCreate, self).form_invalid(form, *args, **kwargs)
    #     return super(ProjectCreate, self).form_invalid(form, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ProjectCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # def post(self, request, *args, **kwargs):
    #     return super(ProjectCreate, self).post(request, *args, **kwargs)

    def complete(self, form):
        owner = form.cleaned_data.get("owner")
        team_queryset = Team.objects.filter(name=owner)

        project = self.object

        if team_queryset.count():
            project.team = team_queryset[0]
            project.save()
        else:
            project_user = ProjectUser()
            project_user.project = project
            project_user.user = self.request.user.member
            project_user.save()


class ProjectDetail(LoginRequiredMixin, DetailView):
    context_object_name = 'project'
    model = Project
    template_name = 'management/project_announcements.html'
    slug_field = 'name'
    slug_url_kwarg = 'project'
    
    # def get_context_data(self, **kwargs):
    #     pass

    def get_queryset(self):
        name = self.kwargs.get(self.slug_url_kwarg, None)
        #slug_field = self.get_slug_field()
        #queryset = queryset.filter(**{slug_field: slug})
        project_queryset = self.request.user.member.projects.filter(project__active=True, project__name=name)

        if project_queryset.count():
            return Project.objects.filter(
                active=True, 
                users__user=User.objects.filter(
                    user=self.request.user))
        
        return Project.objects.filter(
            active=True, 
            team__in=[team_member.team.pk for team_member in self.request.user.member.teams.all()])


class ProjectSettingsList(LoginRequiredMixin, ListView):
    pass






