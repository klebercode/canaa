# coding: utf-8
#, get_object_or_404
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext
from django.utils import translation

from slim.helpers import get_language_from_request

from canaa.context_processors import enterprise_proc, back_proc
from canaa.blog.models import Blog, Post


def blog(request):
    language = get_language_from_request(request)

    results_kwargs = {}

    if language is not None:
        translation.activate(language)
        results_kwargs.update({'language': language})

    # blog = get_object_or_404(Blog, pk=1)
    blog = Blog.objects.all().prefetch_related(
        'translations').select_related('translation_of').get(language=language)

    context = {
        'blog': blog,
    }

    # posts_list = Post.objects.all()
    # posts_list = Post._default_manager.filter(**results_kwargs)
    posts_list = Post.objects.filter(**results_kwargs)

    search = request.GET.get('search', '')
    if search:
        posts_list = posts_list.filter(Q(title__icontains=search) |
                                       Q(created_by__username__contains=search)
                                       | Q(body__icontains=search))

    paginator = Paginator(posts_list, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context['posts'] = posts
    context['search'] = search

    return render(request, 'blog/blog_index.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))


def post(request, slug):
    # post = get_object_or_404(Post, slug=slug)
    language = get_language_from_request(request)

    if language is not None:
        translation.activate(language)

    try:
        # post = Post._default_manager.all().prefetch_related('translations') \
        #            .select_related('translation_of').get(slug=slug)
        post = Post.objects.all().prefetch_related(
            'translations').select_related('translation_of').get(slug=slug)

    except Exception as e:
        raise Http404

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_post.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))
