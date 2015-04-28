# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from bernuzz.settings.private import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY


def index(request):
    template_variables = {}
    if not request.user.is_authenticated():
        #template_variables['thumbnails']
        template_variables['GOOGLE_OAUTH2_KEY'] = SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        return render(request, 'index.html', template_variables)
    #template_variables['']
    return render(request, 'home.html', template_variables)

#if user.is_active():


def login(request):
    if request.method ==  'POST':
        return HttpResponse('HOLA')
    template_variables = {}
    template_variables['plus_id'] = SOCIAL_AUTH_GOOGLE_PLUS_KEY
    return render(request, 'login_.html', template_variables)
