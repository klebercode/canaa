# coding: utf-8
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext
from django.utils import translation

from slim.helpers import get_language_from_request

from canaa.context_processors import enterprise_proc, back_proc

from canaa.blog.models import Post
from canaa.catalog.models import Product
from canaa.core.models import (Sale, Institutional, Seller, Step, Customer,
                               Banner)

from canaa.core.forms import ContactForm


def home(request):
    context = {}

    language = get_language_from_request(request)

    if language is not None:
        translation.activate(language)

    try:
        # banner secundario
        banner = Banner.objects.filter(
            language=language, visible=True, type=2).order_by('?')[0]
        # produtos
        products = Product.objects.filter(
            language=language, visible=True).order_by('?')[0:4]
        # blog
        posts = Post.objects.filter(language=language).order_by('?')[0:2]

    except Exception as e:
        raise Http404

    # redirecionar para mesma pagina na internacionalizacao
    # next = strip_lang(request.path)
    # context['next'] = next

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
    language = get_language_from_request(request)

    if language is not None:
        translation.activate(language)

    try:
        institutional = Institutional.objects.filter(
            language=language, area=1)[0]
        mission = Institutional.objects.filter(
            language=language, area=2)[0]
        step = Step.objects.filter(language=language)
        customer = Customer.objects.filter(visible=True)

    except Exception as e:
        raise Http404

    context = {
        'institutional': institutional,
        'mission': mission,
        'steps': step,
        'customers': customer,
    }

    return render(request, 'institutional.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def sellers(request):
    language = get_language_from_request(request)

    if language is not None:
        translation.activate(language)

    try:
        sale = Sale.objects.filter(language=language)[0]
        # sale = get_object_or_404(Sale, pk=1)
        s_list = Seller.objects.filter(visible=True)

    except Exception as e:
        raise Http404

    context = {
        'sale': sale,
    }

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
