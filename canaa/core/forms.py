# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from canaa.core.models import Step, Banner


class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nome',
                           widget=forms.TextInput(attrs={'class':
                                                  'span12'}))
    email = forms.EmailField(label=u'E-mail',
                             widget=forms.EmailInput(attrs={'class':
                                                     'span12'}))
    message = forms.CharField(label=u'Mensagem',
                              widget=forms.Textarea(attrs={'class':
                                                    'span12',
                                                    'rows': 6}))

    def send_mail(self):
        subject = u'Contato do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = render_to_string('contact_mail.txt', context)
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     'no-reply@canaa.ind.br',
                                     ['contato@canaa.ind.br'])
                                     # ['kleberr@msn.com'])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()


class StepForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'cols': 60, 'rows': 6,
                                         'maxlength': 240}))

    class Meta:
        model = Step


class BannerForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(
                            attrs={'cols': 60, 'rows': 6, 'maxlength': 50}))
    text = forms.CharField(widget=forms.Textarea(
                           attrs={'cols': 60, 'rows': 6, 'maxlength': 100}),
                           required=False)

    class Meta:
        model = Banner
