from django import template
from user_agents import parse
from django.urls import reverse
import os

register = template.Library()

@register.filter(name = 'list_filter')
def list_filter(value):
    return list(range(value))

@register.filter(name = 'split')
def split(value, key):
    return value.split(key)

@register.filter(name = 'get_dict_item')
def get_dict_item(value, key):
    return value[key]

@register.filter(name = 'get_list_item')
def get_list_item(value, key):
    return value[key]

@register.filter(name = 'get_base_name')
def get_base_name(value):
    return os.path.basename(value)

@register.filter(name = 'parse_user_agent')
def parse_user_agent(value):
    result = parse(value)
    return {
        'browser': {
            'family': result.browser.family,
            'version': result.browser.version_string
        },
        'os': {
            'family': result.os.family,
            'version': result.os.version_string
        },
        'device': {
            'family': result.device.family,
            'brand': result.device.brand,
            'model': result.device.model
        }
    }

@register.filter(name = 'clean_image_url')
def clean_image_url(value):
    value = "/".join(str(value).split('/')[1:])
    return f"/{value}"