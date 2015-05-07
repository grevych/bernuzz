# -*- coding:utf-8 -*-

from django.shortcuts import render
from .models import Team, Role, TeamMember
from management.models import Project
from .forms import TeamForm, TeamMemberForm, RoleForm
from basic.models import User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def delete(model):
    model.active = False
    model.save()


def render_teams(request):
    template = "management/teams.html"
    template_variables = dict()
    teams = TeamMember.objects.all().filter(active=True, user=request.user)
    teams_membership = TeamMember.objects.all().filter(active=True, team = teams)
    print teams_membership
    template_variables['group'] = teams
    template_variables['title'] = "Teams"
    return render(request, template, template_variables)


def render_team(request, teamname):
    template = "management/team.html"
    template_variables = dict()
    team = Team.objects.all().filter(active=True, name=teamname)
    template_variables['group'] = team
    template_variables['title'] = "Team"
    return render(request, template, template_variables)


def get_team_members(request, team):
    team_members = TeamMember.objects.all().filter(team__name=team)
  #  users = User.objects.all().filter(user=team_members.user)
    print team_members
    return team_members
    #regresa error
    

def create_team(request):
    template = "hierarchy/team_create.html"
    template_variables = dict()
    form = TeamForm
    template_variables['title'] = "Create Team"
    template_variables['form'] = form
    template_variables['user'] = request.user
    template_variables['url_name'] = "hierarchy:team"
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():                
            new_team = form.save()
            team = Team.objects.get(name=new_team.name)
            team_member = TeamMember(user=user, team= team)
            team_member.save()
            return HttpResponseRedirect('/teams/')
        else:
            form_error = forms
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)


def update_team(request, team):
    template = "hierarchy/team_profile.html"
    template_variables = dict()
    team = Team.objects.get(name=team)
    form = TeamForm(instance=team)
    template_variables['title'] = "Update Team"
    template_variables['form'] = form
    template_variables['url_name'] = "hierarchy:team_profile"
    template_variables['users'] = User.objects.all().filter(active=True)
    template_variables['members'] = TeamMember.objects.all().filter(active=True, team=team)
    template_variables['projects'] = Project.objects.all().filter(active=True, team=team)
    if request.method == 'POST':
        team = Team.objects.get(id=team.id)
        form = TeamForm(request.POST, request.FILES, instance=team)
        if 'add_member' in request.POST:
            print request.POST['team_member']
            user = User.objects.get(user__username=request.POST['team_member'])
            team_member = TeamMember(user=user, team= team)
            team_member.save()
            url = '/team/' + team.name
            return HttpResponseRedirect(url)
        elif 'delete':
            delete(team)
            return HttpResponseRedirect('/teams/')
        else:
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


def settings(request, team):
    template = "hierarchy/team_settings.html"
    template_variables = dict()
    form = RoleForm()
    template_variables['form'] = form
    team = Team.objects.get(name=team)
    template_variables['team'] = team
    template_variables['roles'] = Role.objects.all().filter(active=True, team=team)
    template_variables['form'] = form
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.team = team
            new_form.save()
            url = '/team/' + team.name + '/settings'
            return HttpResponseRedirect(url)
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
        elif 'delete':
            delete(team)
            return HttpResponseRedirect('/teams/')
        else:
            form_error = form
            template_variables['form'] = form_error
            return render(request, template, template_variables)
    return render(request, template, template_variables)

