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
        maxed = 100 if numerical > 100 else numerical
        return math.floor(maxed)
    except ValueError:
        return ''
