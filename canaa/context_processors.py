# coding: utf-8
from django.shortcuts import get_object_or_404

from canaa.core.models import Enterprise, Banner


def enterprise_proc(request):
    enterprise = get_object_or_404(Enterprise, pk=1)
    return {
        'enterprise': enterprise,
    }


def back_proc(request):
    back = Banner.objects.filter(visible=True, type=1).order_by('?')[0]
    return {
        'bannerone': back,
    }
