# coding: utf-8
from django import forms

from canaa.catalog.models import ProductGroup


class ProductGroupForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'cols': 60, 'rows': 6,
                                         'maxlength': 125}))

    class Meta:
        model = ProductGroup
