# coding: utf-8
from django.contrib import admin

from slim.admin import SlimAdmin

from canaa.blog.models import Blog, Post


class BlogAdmin(SlimAdmin):
    list_display = ('content',)
    search_fields = ('content',)

    collapse_slim_fieldset = False

    fieldsets = (
        (None, {
            'fields': ('content',)
        }),
    )


class PostAdmin(SlimAdmin):
    list_filter = ('pub_date', 'created_by__username')
    list_display = ('title', 'pub_date', 'created_by')
    search_fields = ('pub_date', 'created_by__username',
                     'title', 'body')
    date_hierarchy = 'pub_date'

    collapse_slim_fieldset = False

    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'image')
        }),
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
