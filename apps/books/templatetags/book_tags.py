import math
from django import template
register = template.Library()


@register.filter
def div(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        dec = value / arg
        numerical = dec * 100
        return math.floor(numerical)
    except ValueError:
        return ''
