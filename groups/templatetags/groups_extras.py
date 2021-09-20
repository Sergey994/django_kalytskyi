from django import template

register = template.Library()


@register.filter
def get_name(data):
    return data.get('name')


@register.filter
def get_id(data):
    return data.get('id')


@register.filter
def get_type(data):
    return data.get('type')


@register.filter
def get_students(data):
    return data.get('students')
