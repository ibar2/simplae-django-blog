import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def markdown(text):
    md.markdown(text, extensions=["markdown.extensions.fenced_code"])
