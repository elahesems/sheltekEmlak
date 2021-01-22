from django import template
register = template.Library()

@register.simple_tag()
def lastDayAdded(value):
    print(value)
    return True
