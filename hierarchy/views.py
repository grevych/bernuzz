# -*- coding:utf-8 -*-

from django.shortcuts import render
from .models import Team, Role
from management.models import Project
from .forms import TeamForm, TeamMemberForm, RoleForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def render_teams(request):
    template = "management/teams.html"
    template_variables = dict()
    teams = Team.objects.all().filter(active=True)
    template_variables['group'] = teams
    template_variables['title'] = "Teams"
    return render(request, template, template_variables)


def render_team(request, teamname):
    template = "management/team.html"
    template_variables = dict()
    team = Team.objects.all().filter(active=True, name=teamname)
    # projects = Project.object.all().filter(active=True, )
    template_variables['group'] = team
    template_variables['title'] = "Team"
    return render(request, template, template_variables)


def login(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def default(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def create_team(request):
    template = "form.html"
    template_variables = dict()
    form = TeamForm()
    template_variables['title'] = "Create Team"
    template_variables['form'] = form
    template_variables['url_name'] = "management:create_team"
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def update_team(request, id_team):
    template = "form.html"
    template_variables = dict()
    team = Team.objects.get(id=id_team)
    form = TeamForm(instance=team)
    template_variables['title'] = "Update Team"
    template_variables['form'] = form
    template_variables['id'] = id_team
    template_variables['url_name'] = "management:update_team"
    if request.method == 'POST':
        team = Team.objects.get(id=id_team)
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def render_team_members(request):
    print("Team members")


def assign_to_team(request):
    template = "form.html"
    template_variables = dict()
    form = TeamMemberForm()
    form.fields['team'].queryset = Team.objects.all().filter(active=True)
    form.fields['user'].queryset = User.objects.all().filter()
    template_variables['title'] = "Assign to team"
    template_variables['form'] = form
    template_variables['url_name'] = "management:assign_to_team"
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def render_roles(request):
    template = "roles.html"
    template_variables = dict()
    roles = Role.objects.all().filter(active=True)
    template_variables['group'] = roles
    template_variables['title'] = "Roles"
    return render(request, template, template_variables)


def create_role(request):
    template = "form.html"
    template_variables = dict()
    form = RoleForm()
    template_variables['title'] = "Create Role"
    template_variables['form'] = form
    template_variables['url_name'] = "hierarchy:create_role"
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/roles/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def update_role(request, id_role):
    template = "form.html"
    template_variables = dict()
    role = Role.objects.get(pk=id_role)
    form = RoleForm(instance=role)
    template_variables['title'] = "Update Role"
    template_variables['form'] = form
    template_variables['id'] = id_role
    template_variables['url_name'] = "hierarchy:update_role"
    if request.method == 'POST':
        role = Role.objects.get(pk=id_role)
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/roles/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)

