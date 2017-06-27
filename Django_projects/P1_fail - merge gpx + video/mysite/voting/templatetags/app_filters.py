from django.template.defaulttags import register
from django import template
import datetime

register = template.Library()

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key, "0")


@register.filter
def to_range(date):
    now = datetime.datetime.now(datetime.timezone.utc)
    delta = date - now
    str = "%s d, %s h %s min" %(delta.days, delta.seconds//3600, (delta.seconds//60)%60)
    return str

@register.filter
def set_duration(fin, debut):
    delta = fin - debut
    str = "%s d, %s h %s min" %(delta.days, delta.seconds//3600, (delta.seconds//60)%60)
    return str