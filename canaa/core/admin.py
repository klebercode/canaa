# coding: utf-8
from django.contrib import admin

from canaa.core.models import (Customer, Institutional, Step,
                               Enterprise, Sale, Seller, Banner)
from canaa.core.forms import (StepForm, BannerForm)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name',)
    search_fields = ('name',)


class InstitutionalAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)


class StepAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    form = StepForm


class BannerAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('title', 'back_image', 'type', 'visible',)
    search_fields = ('title', 'text', 'type', 'visible',)
    form = BannerForm


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ('name', 'description', 'address', 'number', 'complement',
                     'cep', 'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email')


class SaleAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'content',)
    search_fields = ('content',)


class SellerAdmin(admin.ModelAdmin):
    list_filter = ('visible',)
    list_display = ('name', 'phone', 'email', 'type', 'visible',)
    search_fields = ('name', 'phone', 'email', 'type', 'visible',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Institutional, InstitutionalAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Seller, SellerAdmin)
