# coding: utf-8 
from django.conf.urls import patterns, url

from canaa.blog.views import *


urlpatterns = patterns('canaa.blog.views',
    url(r'^$', 'blog', name='blog'),
    url(r'^(?P<slug>[\w\-]+)/$', 'post', name='post'),
)