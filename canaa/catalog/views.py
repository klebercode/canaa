# coding: utf-8
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext

from canaa.context_processors import enterprise_proc, back_proc
from canaa.catalog.models import ProductGroup, Product, ProductInfo


def group(request):
    context = {}
    g_list = ProductGroup.objects.filter(visible=True)

    search = request.GET.get('search', '')
    if search:
        g_list = g_list.filter(Q(name__icontains=search) |
                               Q(description__icontains=search))

    paginator = Paginator(g_list, 6)

    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)

    context['groups'] = groups
    context['search'] = search

    return render(request, 'catalog/catalog_group.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def item(request, group):
    context = {}
    p_list = Product.objects.filter(product_group__slug=group,
                                    visible=True)

    search = request.GET.get('search', '')
    if search:
        p_list = p_list.filter(Q(name__icontains=search) |
                               Q(description__icontains=search))

    paginator = Paginator(p_list, 6)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context['products'] = products
    context['search'] = search
    # deixei o filtro slug para deixar o filtro menor
    context['infos'] = ProductInfo.objects.filter(product_group__slug=group,
                                                  visible=True)

    return render(request, 'catalog/catalog_item.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def detail(request, group, item):
    context = {}

    return render(request, 'catalog/catalog_detail.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))
