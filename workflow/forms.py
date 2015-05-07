# -*- coding:utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import ModelForm


from management.models import Project
from workflow.models import Process, Stage, Task



class ProcessForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        project = kwargs.pop('project')
        project_processes = project.processes.filter(active=True)
        project_members = project.team.users.filter(active=True)
        super(ProcessForm, self).__init__(*args, **kwargs)
        self.fields['parent_id'].choices = [('', '')] + \
            [(project_process.process.pk, project_process.process.name) for project_process in project_processes]
        self.fields['responsible'].choices = [(project_member.user.user.pk, project_member.user.user.username, ) 
            for project_member in project_members] if project_members.count() else [(user.user.pk, user.user.username, )]

    class Meta:
        model = Process
        fields = ['name', 'description', 'parent_id', 'responsible']


class StageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        project = kwargs.pop('project')
        project_members = project.team.users.filter(active=True)
        super(StageForm, self).__init__(*args, **kwargs)
        self.fields['responsible'].choices = [(project_member.user.user.pk, project_member.user.user.username, ) 
            for project_member in project_members] if project_members.count() else [(user.user.pk, user.user.username, )]

    class Meta:
        model = Stage
        fields = ['name', 'description', 'responsible']


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['description', 'completed', 'responsible']

