# coding: utf-8
from django.contrib import admin

from canaa.blog.models import Blog, Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)


class PostAdmin(admin.ModelAdmin):
    list_filter = ('pub_date', 'created_by__username')
    list_display = ('pub_date', 'created_by', 'title')
    search_fields = ('pub_date', 'created_by__username',
                     'title', 'body')
    date_hierarchy = 'pub_date'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
