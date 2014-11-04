# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from slim.helpers import get_language_from_request

from canaa.context_processors import enterprise_proc, back_proc
from canaa.talents.forms import TalentForm
from canaa.talents.models import Talent, Page


def talent(request):
    context = {}

    language = get_language_from_request(request)

    results_kwargs = {}

    if language is not None:
        translation.activate(language)
        results_kwargs.update({'language': language})

    # context['talent'] = Page.objects.all()[:1]
    context['talent'] = Page.objects.filter(**results_kwargs)

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    context = {
        'form': TalentForm(),
    }

    language = get_language_from_request(request)

    results_kwargs = {}

    if language is not None:
        translation.activate(language)
        results_kwargs.update({'language': language})

    # context['page'] = Page.objects.all()[:1]
    context['page'] = Page.objects.filter(**results_kwargs)[:1]

    return render(request, 'talents/talent.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def create(request):
    form = TalentForm(request.POST, request.FILES)
    context = {
        'form': form,
    }

    language = get_language_from_request(request)

    results_kwargs = {}

    if language is not None:
        translation.activate(language)
        results_kwargs.update({'language': language})

    # context['page'] = Page.objects.all()[:1]
    context['page'] = Page.objects.filter(**results_kwargs)[:1]

    if not form.is_valid():
        return render(request, 'talents/talent.html', context,
                      context_instance=RequestContext(request,
                                                      processors=[
                                                          enterprise_proc,
                                                          back_proc]
                                                      ))
    obj = form.save()
    return HttpResponseRedirect(_('/trabalhe-conosco/%d/') % obj.pk)


def detail(request, pk):
    talent = get_object_or_404(Talent, pk=pk)
    context = {
        'talent': talent,
    }

    language = get_language_from_request(request)

    results_kwargs = {}

    if language is not None:
        translation.activate(language)
        results_kwargs.update({'language': language})

    # context['page'] = Page.objects.all()[:1]
    context['page'] = Page.objects.filter(**results_kwargs)[:1]

    return render(request, 'talents/talent_detail.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))
