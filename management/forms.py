__author__ = 'Rebeca'


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from hierarchy.models import Team
from basic.models import User
from models import Project, ProjectStatus, ProjectSkill,ProjectUser,CollegeProject,College,Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ('active',)


class ProjectForm(ModelForm):
    owner = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        teams = Team.objects.filter(users__user__in=[user.member.pk])
        print user, teams
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['owner'].choices = \
            [(user.username, None)] + [(team.name, team.logo, ) for team in teams]

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        owner = cleaned_data.get("owner")
        name = cleaned_data.get("name")
        team_queryset = Team.objects.filter(name=owner)

        if team_queryset.count():
            team = team_queryset[0]
            project_queryset = Project.objects.filter(
                name=name, 
                team__pk=team.pk)
            if project_queryset.count():
                message = u"A project named %s already exist for team %s" % (name, owner, )
                self.add_error('name', message)

        else:
            project_queryset = Project.objects.filter(
                name=name,
                users__user=User.objects.filter(
                    user__username=owner))
            if project_queryset.count():
                message = u"A project named %s already exist for %s" % (name, owner, )
                self.add_error('name', message)
        return cleaned_data

    class Meta:
        model = Project
        fields = ['name', 'description', 'access_level', 'owner', 'logo']



# class TestForm(forms.Form):
#     mychoicefield = forms.ChoiceField(choices=QS_CHOICES)

#     def __init__(self, *args, **kwargs):
        
#         self.fields['mychoicefield'].choices = \
#             list(self.fields['mychoicefield'].choices) + [('new stuff', 'new')]

#     def clean_mychoicefield(self):
#         data = self.cleaned_data.get('mychoicefield')
#         if data in QS_CHOICES:
#             try:
#                 data = MyModel.objects.get(id=data)
#             except MyModel.DoesNotExist:
#                 raise forms.ValidationError('foo')
#         return data