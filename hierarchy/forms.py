__author__ = 'Rebeca'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Team, TeamMember, Role


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ('active', )



class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        exclude = ('active', )


class RoleForm(ModelForm):
    class Meta:
        model = Role
        exclude = ('active',)