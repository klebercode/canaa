# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import TabularInline

from canaa.catalog.models import ProductGroup, Product, ProductInfo


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class ProductInfoInline(TabularInline):
    model = ProductInfo
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('product_group',)
    list_display = ('name', 'product_group')
    search_fields = ('name', 'product_group')
    inlines = [ProductInfoInline]


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Product, ProductAdmin)
