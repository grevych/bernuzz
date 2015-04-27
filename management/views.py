# -*- coding:utf-8 -*-

# import datetime as dt
# from django.shortcuts import render_to_response, render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.http import HttpResponseRedirect, Http404, HttpResponse
# from django.contrib.auth.models import User, Group
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login
# from django.template import RequestContext
# from django.contrib.auth import logout

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

#from books.models import Publisher


# Create your views here.



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

def default(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def profile(request):
    return HttpResponse("Hello, world. You're at the polls index.")





class ProjectList(LoginRequiredMixin, ListView):
    #paginate_by = 50
    context_object_name = 'projects'
    template_name = "management/projects.html"

    def get_queryset(self):
        # from basic.models import User
        # u = User()
        # u.user = self.request.user
        # u.save()
        # self.request.user.save()
        print self.request.user.u
        return self.request.user.u.projects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['r'] = range(0, 100)
        return context

