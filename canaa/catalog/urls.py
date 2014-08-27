# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('canaa.catalog.views',
    url(r'^$', 'group', name='group'),
    url(r'^(?P<group>[\w\-]+)/$', 'item', name='item'),
    url(r'^(?P<group>[\w\-]+)/(?P<item>[\w\-]+)/$', 'detail', name='detail'),
)
