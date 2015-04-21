from django.shortcuts import render
from .models import Team
# Create your views here.


def dashboard_teams(request):
    template = "dashboard_teams.html"
    template_variables = dict()
    teams = Team.objects.all().filter(active=True)
    template_variables['group'] = teams
    template_variables['title'] = "Teams"
    return render(request, template, template_variables)