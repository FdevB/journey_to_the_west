from django import template

register = template.Library()

@register.filter(name='or_default')
def display_value_or_default(value, char):
    return value or char
