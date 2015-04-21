import datetime as dt
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth import logout

# Create your views here.


