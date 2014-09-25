# coding: utf-8
from django.contrib import admin
from canaa.talents.models import Talent, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'content')
    search_fields = ('content',)


class TalentAdmin(admin.ModelAdmin):
    list_filter = ('state', 'city', 'sex', 'formation',)
    list_display = ('name', 'phone', 'email', 'attach_link',)
    search_fields = ('name', 'address', 'number', 'complement', 'cep',
                     'district', 'city', 'country', 'phone', 'email',
                     'date_birth', 'sex', 'formation', 'qualification',
                     'experience', 'enterprise1', 'contact1', 'period1',
                     'activies1', 'enterprise2', 'contact2', 'period2',
                     'activies2', 'enterprise3', 'contact3', 'period3',
                     'activies3', 'courses', 'referrals', 'attach_link')
    date_hierarchy = 'date_birth'


admin.site.register(Page, PageAdmin)
admin.site.register(Talent, TalentAdmin)
