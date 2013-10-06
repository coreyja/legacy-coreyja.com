from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="description_split")
@stringfilter
def desc_split_filter(value):
    output = '';

    values = value.split('\n')

    for v in values:
        if not v.strip():
            continue
        output += '<p class="desc">%s</p>' % v

    return  output