# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string


register = template.Library()


def reverse_admin(obj):
    return reverse('admin:{0}_{1}_change'.format(obj._meta.app_label, type(obj).__name__.lower()), args=[obj.id])


@register.simple_tag
def get_admin_url(obj, request, extra_css='margin-left:-25px;float:left;'):
    if not obj:
        return ''
    if request.user.is_authenticated():
        admin_url = reverse_admin(obj)
        return render_to_string('admin_url.html', {'url': admin_url, 'extra_css': extra_css})
    return ''
