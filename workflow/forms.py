# -*- coding:utf-8 -*-

from django.core.exceptions import ValidationError
from django.forms import ModelForm


from management.models import Project
from workflow.models import Process, Stage, Task



class ProcessForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        project = kwargs.pop('project')
        projects_processes = project.processes.filter(active=True)
        super(ProcessForm, self).__init__(*args, **kwargs)
        self.fields['parent_id'].choices = [('', '')] + \
            [(project_process.process.pk, project_process.process.name) for project_process in projects_processes]

    class Meta:
        model = Process
        fields = ['name', 'description', 'parent_id']


class StageForm(ModelForm):

    class Meta:
        model = Stage
        fields = ['name', 'description']


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['description', 'completed']

