# coding: utf-8
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# from forms import *

def home(request):
    context = {}

    # if request.method == 'POST':
    #     contact_form = ContactForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.send_mail()
    #         context['contact_success'] = True
    # else:
    #     contact_form = ContactForm()

    # context['contact_form'] = contact_form

    return render(request, 'home.html', context)


def institutional(request):
    context = {}

    return render(request, 'institutional.html', context)


def products(request):
    context = {}

    return render(request, 'products.html', context)


def sellers(request):
    context = {}

    return render(request, 'sellers.html', context)


def marketing(request):
    context = {}

    return render(request, 'marketing.html', context)


def talents(request):
    context = {}

    return render(request, 'talents.html', context)


def contact(request):
    context = {}

    return render(request, 'contact.html', context)