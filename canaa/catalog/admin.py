# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import TabularInline

from slim.admin import SlimAdmin

from canaa.catalog.models import ProductGroup, Product, ProductInfo
from canaa.catalog.forms import ProductGroupForm


class ProductGroupAdmin(SlimAdmin):
    list_filter = ('visible',)
    list_display = ('name', 'description', 'visible')
    search_fields = ('name', 'description')

    form = ProductGroupForm

    collapse_slim_fieldset = False

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'image', 'visible')
        }),
    )


class ProductInfoInline(TabularInline):
    model = ProductInfo
    extra = 1


class ProductAdmin(SlimAdmin):
    list_filter = ('product_group', 'visible')
    list_display = ('name', 'product_group', 'visible')
    search_fields = ('name', 'product_group')

    inlines = [ProductInfoInline]

    collapse_slim_fieldset = False

    fieldsets = (
        (None, {
            'fields': (
                'product_group', 'name', 'description', 'image', 'visible'
            )
        }),
    )


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Product, ProductAdmin)
