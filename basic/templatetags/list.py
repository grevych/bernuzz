# -*- coding:utf-8 -*-

from django import template
register = template.Library()

@register.filter
def index_to_int(List, i):
    print List, i
    return int(List[int(i) - 1])

@register.filter
def index(List, i):
    print List, i
    return List[int(i) - 1]
