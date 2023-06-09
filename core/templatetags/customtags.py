from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='strtolist')
def strtolist(value):
    return value.split()
