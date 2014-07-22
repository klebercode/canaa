# coding: utf-8
"""teste"""

from django.shortcuts import render


def group(request):
    """product"""
    context = {}

    return render(request, 'catalog/group.html', context)


def item(request, group):
    """item"""

    context = {}
    return render(request, 'catalog/item.html', context)


def detail(request, group, item):
    """detail"""

    context = {}
    return render(request, 'catalog/detail.html', context)
