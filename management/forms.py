__author__ = 'Rebeca'


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Project, ProjectStatus, ProjectPrivacy, ProjectSkill,ProjectUser,CollegeProject,College,Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ('active',)