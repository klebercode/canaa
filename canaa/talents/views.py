# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

# from canaa.context_processors import enterprise_proc, contact_proc
from canaa.talents.forms import TalentForm
from canaa.talents.models import Talent
# from canaa.core.models import Work


def talent(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    # work = get_object_or_404(Work, pk=1)
    context = {
        # 'work': work,
        'form': TalentForm(),
    }

    # return render(request, 'talents/talent.html', context, 
    #     context_instance=RequestContext(request, processors=[enterprise_proc, contact_proc]))
    return render(request, 'talents/talent.html', context)

def create(request):
    form = TalentForm(request.POST, request.FILES)
    # work = get_object_or_404(Work, pk=1)
    context = {
        # 'work': work,
        'form': form,
    }

    if not form.is_valid():
        # return render(request, 'talents/talent.html', context, 
        #     context_instance=RequestContext(request, processors=[enterprise_proc, contact_proc]))
        return render(request, 'talents/talent.html', context)

    obj = form.save()
    return HttpResponseRedirect('/trabalhe-conosco/%d/' % obj.pk)

def detail(request, pk):
    talent = get_object_or_404(Talent, pk=pk)
    # work = get_object_or_404(Work, pk=1)
    context = {
        # 'work': work,
        'talent': talent,
    }

    # return render(request, 'talents/talent_detail.html', context, 
    #     context_instance=RequestContext(request, processors=[enterprise_proc, contact_proc]))
    return render(request, 'talent/talent_detail.html')
