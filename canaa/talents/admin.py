# coding: utf-8
from django.contrib import admin

from slim.admin import SlimAdmin

from canaa.talents.models import Talent, Page


class PageAdmin(SlimAdmin):
    list_display = ('admin_image', 'content')
    search_fields = ('content',)

    collapse_slim_fieldset = False

    fieldsets = (
        (None, {
            'fields': ('content', 'image')
        }),
    )


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

    # collapse_slim_fieldset = False

    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'name', 'address', 'number', 'complement', 'cep', 'district',
    #             'city', 'state', 'country', 'phone', 'email', 'date_birth',
    #             'sex', 'formation', 'qualification', 'experience',
    #             'enterprise1', 'contact1', 'period1', 'post1', 'activies1',
    #             'enterprise2', 'contact2', 'period2', 'post2', 'activies2',
    #             'enterprise3', 'contact3', 'period3', 'post3', 'activies3',
    #             'courses', 'referrals', 'attach',
    #         )
    #     }),
    # )


admin.site.register(Page, PageAdmin)
admin.site.register(Talent, TalentAdmin)
