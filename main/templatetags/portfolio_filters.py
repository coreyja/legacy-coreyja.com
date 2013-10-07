from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="description_split")
@stringfilter
def desc_split_filter(value, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    output = '';

    values = value.split('\n')

    for v in values:
        if not v.strip():
            continue
        output += '<p class="desc">%s</p>' % esc(v)

    return  mark_safe(output)