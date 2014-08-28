# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext

from canaa.context_processors import enterprise_proc, back_proc

from canaa.blog.models import Post
from canaa.catalog.models import Product
from canaa.core.models import (Sale, Institutional, Seller, Step, Customer,
                               Banner)

from canaa.core.forms import ContactForm


def home(request):
    context = {}

    # banner secundario
    banner = Banner.objects.filter(visible=True, type=2).order_by('?')[0]
    # produtos
    products = Product.objects.filter(visible=True).order_by('?')[0:4]
    # blog
    posts = Post.objects.filter().order_by('?')[0:2]

    context['bannertwo'] = banner
    context['products'] = products
    context['posts'] = posts

    return render(request, 'home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def marketing(request):
    context = {}
    return render(request, 'home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def institutional(request):
    institutional = get_object_or_404(Institutional, area=1)
    mission = get_object_or_404(Institutional, area=2)
    context = {
        'institutional': institutional,
        'mission': mission,
    }
    context['steps'] = Step.objects.all()
    context['customers'] = Customer.objects.filter(visible=True)

    return render(request, 'institutional.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def sellers(request):
    sale = get_object_or_404(Sale, pk=1)
    context = {
        'sale': sale,
    }

    s_list = Seller.objects.filter(visible=True)

    search = request.GET.get('search', '')
    if search:
        s_list = s_list.filter(Q(name__icontains=search) |
                               Q(state__icontains=search))

    paginator = Paginator(s_list, 20)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context['sellers'] = posts
    context['search'] = search

    return render(request, 'sellers.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def contact(request):
    context = {}

    # contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['contact_success'] = True
    else:
        form = ContactForm()

    context['contact_form'] = form

    return render(request, 'contact.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))
