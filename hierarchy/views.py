# -*- coding:utf-8 -*-

from django.shortcuts import render
from .models import Team
from .forms import TeamForm, TeamMemberForm, RoleForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def render_teams(request):
    template = "prototype/dashboard_teams.html"
    template_variables = dict()
    teams = Team.objects.all().filter(active=True)
    template_variables['group'] = teams
    template_variables['title'] = "Teams"
    return render(request, template, template_variables)


def login(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def create_team(request):
    template = "base.html"
    template_variables = dict()
    form = TeamForm()
    template_variables['title'] = "Team"
    template_variables['form'] = form
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/')
        else:
            #form error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def update_team(request, id_team):
    template = "base.html"
    template_variables = dict()
    team = Team.objects.all().filter(id=id_team)
    form = TeamForm(instance=team)
    template_variables['title'] = "Team"
    template_variables['form'] = form
    if request.method == 'POST':
        team = Team.objects.get(id=id_team)
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams/')
        else:
            #form error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def assign_to_team(request):
    template = "base.html"
    template_variables = dict()
    form = TeamMemberForm()
    team = Team.objects.all().filter(active=True)
    member = User.objects.all().filter(active=True)
    form.fields['']


def create_role(request):

