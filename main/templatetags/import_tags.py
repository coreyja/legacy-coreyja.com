from django import template
from django.utils.safestring import mark_safe
from coreyja import settings

register = template.Library()

@register.tag(name="import_compiled_js")
def import_compiled_js_tag(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)

    return CompiledJSNode(format_string[1:-1])


class CompiledJSNode(template.Node):
    def __init__(self, format_string):
        if settings.DEBUG:
            self.format_string = '%s.js' % format_string
        else:
            self.format_string = '%s.min.js' % format_string

    def render(self, context):

        return mark_safe('<script type="text/javascript" src="/static/js/compiled/%s"></script>' % self.format_string)


@register.tag(name="import_compiled_css")
def import_compiled_css_tag(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)

    return CompiledCSSNode(format_string[1:-1])


class CompiledCSSNode(template.Node):
    def __init__(self, format_string):
        if settings.DEBUG:
            self.format_string = '%s.css' % format_string
        else:
            self.format_string = '%s.min.css' % format_string

    def render(self, context):
        return mark_safe('<link href="/static/css/%s" rel="stylesheet">' % self.format_string)

