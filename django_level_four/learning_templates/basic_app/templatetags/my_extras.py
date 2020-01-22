from django import template

register = template.Library()
@register.filter(name='cut')  # using decorator
def cut(value, arg):
    return value.replace(arg,'')

#register.filter('cut', cut)  #simple way without using decorators
