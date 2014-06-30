# coding: utf-8 
from django.conf.urls import patterns, url

from canaa.talents.views import *

urlpatterns = patterns('canaa.talents.views',
    url(r'^$', 'talent', name='talent'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)