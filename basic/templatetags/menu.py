# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def active_item(context, request, domain):
    return 'visible' if request.path == reverse(domain) else ''
