# -*- coding:utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import ModelForm


from management.models import Project
from workflow.models import Process, Stage, Task
from django.db.models import ObjectDoesNotExist



class ProcessForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        project = kwargs.pop('project')
        project_processes = project.processes.filter(active=True)
        project_members = []
        try:
            if project.team:
                project_members = project.team.users.filter(active=True)
        except ObjectDoesNotExist:
            pass

        super(ProcessForm, self).__init__(*args, **kwargs)
        print project_members
        print user
        self.fields['parent_id'].choices = [('', '')] + \
            [(project_process.process.pk, project_process.process.name) for project_process in project_processes]
        self.fields['responsible'].choices = [(project_member.user.user.pk, project_member.user.user.username, ) 
            for project_member in project_members] if project_members and project_members.count() else [(user.member.pk, user.username, )]
        print self.fields['responsible'].choices

    class Meta:
        model = Process
        fields = ['name', 'description', 'parent_id', 'responsible']


class StageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        project = kwargs.pop('project')
        project_members = []
        try:
            if project.team:
                project_members = project.team.users.filter(active=True)
        except ObjectDoesNotExist:
            pass
        super(StageForm, self).__init__(*args, **kwargs)
        self.fields['responsible'].choices = [(project_member.user.user.pk, project_member.user.user.username, ) 
            for project_member in project_members] if project_members and project_members.count() else [(user.member.pk, user.username, )]

    class Meta:
        model = Stage
        fields = ['name', 'description', 'responsible']


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['description', 'completed', 'responsible']

