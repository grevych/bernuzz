# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def default(request):
    return HttpResponse("Hello, world. You're at the polls index.")

