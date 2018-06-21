# -*- coding: utf-8 -*-

import markdown
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(value, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ], safe_mode=True, enable_attributes=False))