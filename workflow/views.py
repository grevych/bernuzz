# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class WorkflowCreate(LoginRequiredMixin, CreateView):
    pass


class WorkflowDetail(LoginRequiredMixin, DetailView):
    pass


class WorkflowList(LoginRequiredMixin, ListView):
    pass


class StageCreate(LoginRequiredMixin, CreateView):
    pass


class StageDetail(LoginRequiredMixin, DetailView):
    pass


class StageList(LoginRequiredMixin, ListView):
    pass


class TaskCreate(LoginRequiredMixin, CreateView):
    pass


class TaskDetail(LoginRequiredMixin, DetailView):
    pass


class TaskList(LoginRequiredMixin, ListView):
    pass

