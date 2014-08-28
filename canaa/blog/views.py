# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template import RequestContext

from canaa.context_processors import enterprise_proc, back_proc
from canaa.blog.models import Blog, Post


def blog(request):
    blog = get_object_or_404(Blog, pk=1)
    context = {
        'blog': blog,
    }

    posts_list = Post.objects.all()

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
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }

    return render(request, 'blog/blog_post.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc,
                                                              back_proc]
                                                  ))
