# coding: utf-8
"""teste"""

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext

# from fipel.context_processors import enterprise_proc, contact_proc
# from fipel.revenue.models import *FIELDNAME = models.SmallIntegerField()


def blog(request):
    """blog"""
    context = {}

    # posts_list = Post.objects.all()

    # search = request.GET.get('search', '')
    # if search:
    #     posts_list = posts_list.filter(
    #         Q(title__icontains=search) \
    #         | Q(created_by__username__contains=search) \
    #         | Q(pub_date__icontains=search) \
    #         | Q(body__icontains=search))

    # paginator = Paginator(posts_list, 20)

    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)

    # context['posts'] = posts
    # context['search'] = search

    # return render(request, 'blog/blog.html', context,
    #     context_instance=RequestContext(request,
    #                                     processors=[enterprise_proc,
    #                                     contact_proc]))
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    """post"""
    # post = get_object_or_404(Post, slug=slug)
    # context = {
    #     'post': post,
    # }

    # return render(request, 'blog/post.html', context,
    #     context_instance=RequestContext(request,
    #                                     processors=[enterprise_proc,
    #                                     contact_proc]))
    context = {}
    return render(request, 'blog/post.html', context)
