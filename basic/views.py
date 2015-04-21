# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from bernuzz.settings.private import SOCIAL_AUTH_GOOGLE_PLUS_KEY

# Create your views here.


def login(request):
    if request.method ==  'POST':
        return HttpResponse('HOLA')

    template_variables = {}
    template_variables['plus_id'] = SOCIAL_AUTH_GOOGLE_PLUS_KEY

    return render(request, 'login.html', template_variables)
