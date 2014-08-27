# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from canaa.context_processors import enterprise_proc
from canaa.talents.forms import TalentForm
from canaa.talents.models import Talent


def talent(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    context = {
        'form': TalentForm(),
    }

    return render(request, 'talents/talent.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def create(request):
    form = TalentForm(request.POST, request.FILES)
    context = {
        'form': form,
    }

    if not form.is_valid():
        return render(request, 'talents/talent.html', context,
                      context_instance=RequestContext(request,
                                                      processors=[enterprise_proc]
                                                      ))

    obj = form.save()
    return HttpResponseRedirect('/trabalhe-conosco/%d/' % obj.pk)


def detail(request, pk):
    talent = get_object_or_404(Talent, pk=pk)
    context = {
        'talent': talent,
    }

    return render(request, 'talents/talent_detail.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))
