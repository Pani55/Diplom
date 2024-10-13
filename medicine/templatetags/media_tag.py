from django import template

register = template.Library()


@register.filter()
def media_tag(path):
    return f"/media/{path}"
