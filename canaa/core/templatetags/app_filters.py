# coding: utf-8
from django import template
from django.utils.translation import get_language
# from django.conf.global_settings import LANGUAGES

import re


register = template.Library()


@register.filter(name='strip_lang')
def strip_lang(path):
    pattern = '^(/%s)/' % get_language()
    match = re.search(pattern, path)
    if match is None:
        return path
    return path[match.end(1):]

    # l_path = path.split('/')
    # no_lang_path = path
    # codes = []
    # for code, name in LANGUAGES:
    #     codes.append(code)
    # if l_path[1] in codes:
    #     del l_path[1]
    #     no_lang_path = '/'.join(l_path)
    #     return no_lang_path
