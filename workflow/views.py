# -*- coding:utf-8 -*-

from datetime import datetime

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView
from django.utils.translation import ugettext as _

from basic.models import User
from management.models import Project
from workflow.models import Process, ProjectProcess, Stage, Task

from forms import ProcessForm, StageForm, TaskForm



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class WorkflowCreate(LoginRequiredMixin, CreateView):
    model = Process
    form_class = ProcessForm
    fields = ['name', 'description', 'parent_id']
    template_name = 'workflow/workflow_create.html'

    def get(self, request, *args, **kwargs):
        project_name = kwargs.get('project', None)
        project_queryset = Project.objects.filter(
                active=True, 
                name=project_name,
                users__user=User.objects.filter(
                    user=self.request.user))

        if not project_queryset.count():
            project_queryset = Project.objects.filter(
                active=True,
                name=project_name,
                team__in=[team_member.team.pk for team_member in self.request.user.member.teams.all()])

            if not project_queryset.count():
                raise Http404(_("Project %(project_name)s not found for this account.")
                        % {'project_name': project_name})

        self.project = project_queryset.get()
        return super(WorkflowCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        project_name = kwargs.get('project', None)
        project_queryset = Project.objects.filter(
                active=True, 
                name=project_name,
                users__user=User.objects.filter(
                    user=self.request.user))

        if not project_queryset.count():
            project_queryset = Project.objects.filter(
                active=True,
                name=project_name,
                team__in=[team_member.team.pk for team_member in self.request.user.member.teams.all()])

            if not project_queryset.count():
                raise Http404(_("Project %(project_name)s not found for this account.")
                        % {'project_name': project_name})

        self.project = project_queryset.get()
        return super(WorkflowCreate, self).post(request, *args, **kwargs)        

    def form_valid(self, form):
        self.object = form.save()
        self.success_url = reverse(
            'workflow:workflow', 
            kwargs={
            'project': self.project.name,
            'workflow': self.object.pk})
        print self.success_url
        self.complete()
        return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form, *args, **kwargs):
    #     print super(ProjectCreate, self).form_invalid(form, *args, **kwargs)
    #     return super(ProjectCreate, self).form_invalid(form, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(WorkflowCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'project': self.project})
        return kwargs

    # def post(self, request, *args, **kwargs):
    #     return super(ProjectCreate, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(WorkflowCreate, self).get_context_data(**kwargs)
        #user_teams = [team_member.team.pk for team_member in self.request.user.member.teams.all()]
        context['project'] = self.project
        return context

    def complete(self):
        project_process = ProjectProcess()
        project_process.project = self.project
        project_process.process = self.object
        project_process.save()



class WorkflowDetail(LoginRequiredMixin, DetailView):
    pass


class WorkflowList(LoginRequiredMixin, ListView):
    #paginate_by = 50
    context_object_name = 'workflows'
    template_name = "workflow/project_workflows.html"
    project_name = None

    def get(self, request, *args, **kwargs):
        project_name = kwargs.get('project', None)
        project_queryset = Project.objects.filter(
                active=True, 
                name=project_name,
                users__user=User.objects.filter(
                    user=self.request.user))

        if not project_queryset.count():
            project_queryset = Project.objects.filter(
                active=True,
                name=project_name,
                team__in=[team_member.team.pk for team_member in self.request.user.member.teams.all()])

            if not project_queryset.count():
                raise Http404(_("Project %(project_name)s not found for this account.")
                        % {'project_name': project_name})

        self.project = project_queryset[0]
        return super(WorkflowList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Process.objects.select_related().filter(
            active=True, 
            projects__project=self.project)

    def get_context_data(self, **kwargs):
        context = super(WorkflowList, self).get_context_data(**kwargs)
        #user_teams = [team_member.team.pk for team_member in self.request.user.member.teams.all()]
        context['project'] = self.project
        print context
        return context


class StageCreate(LoginRequiredMixin, CreateView):
    model = Stage
    form_class = StageForm
    fields = ['name', 'description']
    template_name = 'workflow/project_workflow.html'

    def get(self, request, *args, **kwargs):
        project_name = kwargs.get('project', None)
        process_id = kwargs.get('workflow', None)
        project_queryset = Project.objects.filter(
                active=True, 
                name=project_name,
                users__user=User.objects.filter(
                    user=self.request.user))

        if not project_queryset.count():
            project_queryset = Project.objects.filter(
                active=True,
                name=project_name,
                team__in=[team_member.team.pk for team_member in self.request.user.member.teams.all()])

            if not project_queryset.count():
                raise Http404(_("Project %(project_name)s not found for this account.")
                        % {'project_name': project_name})

        self.project = project_queryset.get()
        process_queryset = self.project.processes.filter(process__pk=int(process_id))

        if not process_queryset.count():
            raise Http404(_("Workflow %(process_id)s not found for this project.")
                    % {'process_id': process_id})

        self.process = process_queryset.get().process
        return super(StageCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        project_name = kwargs.get('project', None)
        process_id = kwargs.get('workflow', None)
        project_queryset = Project.objects.filter(
                active=True, 
                name=project_name,
                users__user=User.objects.filter(
                    user=self.request.user))

        if not project_queryset.count():
            project_queryset = Project.objects.filter(
                active=True,
                name=project_name,
                team__in=[team_member.team.pk for team_member in self.request.user.member.teams.all()])

            if not project_queryset.count():
                raise Http404(_("Project %(project_name)s not found for this account.")
                        % {'project_name': project_name})

        self.project = project_queryset.get()
        process_queryset = self.project.processes.filter(process__pk=int(process_id))

        if not process_queryset.count():
            raise Http404(_("Workflow %(process_id)s not found for this project.")
                    % {'process_id': process_id})

        self.process = process_queryset.get().process
        return super(StageCreate, self).post(request, *args, **kwargs)     

    def get_form_kwargs(self):
        kwargs = super(StageCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'project': self.project})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = reverse(
            'workflow:workflow', 
            kwargs={
            'project': self.project.name,
            'workflow': self.process.pk})
        print self.success_url
        self.complete()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, *args, **kwargs):
        print 'WTF', form

        #print super(ProjectCreate, self).form_invalid(form, *args, **kwargs)
        #return super(ProjectCreate, self).form_invalid(form, *args, **kwargs)

    # def get_form_kwargs(self):
    #     kwargs = super(StageCreate, self).get_form_kwargs()
    #     kwargs.update({'user': self.request.user, 'project': self.project, 'process': self.process})
    #     return kwargs

    # def post(self, request, *args, **kwargs):
    #     return super(ProjectCreate, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StageCreate, self).get_context_data(**kwargs)
        #user_teams = [team_member.team.pk for team_member in self.request.user.member.teams.all()]
        context['project'] = self.project
        context['workflow'] = self.process
        return context

    def complete(self):
        self.object.process = self.process
        self.object.save()


class StageDetail(LoginRequiredMixin, DetailView):
    pass

class TaskCreate(LoginRequiredMixin, CreateView):
    pass

# class StageList(LoginRequiredMixin, ListView):
#     pass

@login_required
def task(request, project):
    stage_id = request.GET.get('stage', None)
    manager_id = request.GET.get('manager', None)
    date = request.GET.get('date', None)
    stage = Stage.objects.get(pk=int(stage_id)) 
    manager = User.objects.get(pk=int(manager_id))

    task = Task()
    task.description = request.GET.get('description', None)
    task.responsible = manager
    task.completed_by = None
    task.due_time = datetime.strptime(date, '%Y-%m-%d')
    task.stage = stage
    task.save()
    return HttpResponse('OK')

class TaskDetail(LoginRequiredMixin, DetailView):
    pass


class TaskList(LoginRequiredMixin, ListView):
    pass

@login_required
def check_task(request, project, task):
    task = Task.objects.get(pk=task)
    task.completed_by = request.user.member
    task.completed = True
    task.end_time = datetime.now()
    task.save()

    return HttpResponse('OK')
