# coding: utf-8
from django.shortcuts import get_object_or_404
from canaa.core.models import Enterprise


def enterprise_proc(request):
    enterprise = get_object_or_404(Enterprise, pk=1)
    return {
        'enterprise': enterprise,
    }
