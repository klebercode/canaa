# coding: utf-8
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import translation

from slim.helpers import get_language_from_request

from canaa.core.models import Enterprise, Banner


def enterprise_proc(request):
    enterprise = get_object_or_404(Enterprise, pk=1)
    return {
        'enterprise': enterprise,
    }


def back_proc(request):
    language = get_language_from_request(request)

    if language is not None:
        translation.activate(language)

    try:
        back = Banner.objects.filter(
            language=language, visible=True, type=1).order_by('?')[0]

    except Exception as e:
        raise Http404

    return {
        'bannerone': back,
    }
