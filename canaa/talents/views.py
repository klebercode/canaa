# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from canaa.context_processors import enterprise_proc, back_proc

from canaa.talents.forms import TalentForm

from canaa.talents.models import Talent, Page


def talent(request):
    context = {}
    context['talent'] = Page.objects.all()[:1]

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    context = {
        'form': TalentForm(),
    }
    context['page'] = Page.objects.all()[:1]

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
    context['page'] = Page.objects.all()[:1]

    if not form.is_valid():
        return render(request, 'talents/talent.html', context,
                      context_instance=RequestContext(request,
                                                      processors=[
                                                          enterprise_proc,
                                                          back_proc]
                                                      ))
    obj = form.save()
    return HttpResponseRedirect('/trabalhe-conosco/%d/' % obj.pk)


def detail(request, pk):
    talent = get_object_or_404(Talent, pk=pk)
    context = {
        'talent': talent,
    }
    context['page'] = Page.objects.all()[:1]

    return render(request, 'talents/talent_detail.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))
