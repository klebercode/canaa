# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext_lazy as _

from canaa.core.models import Step, Banner


SUBJECT_CHOICES = (
    (_(u'--- Escolha um assunto ---'), _(u'--- Escolha um assunto ---')),
    (_(u'Dúvida'), _(u'Dúvida')),
    (_(u'Elogio'), _(u'Elogio')),
    (_(u'SAC'), _(u'SAC')),
    (_(u'Informação'), _(u'Informação')),
    (_(u'Reclamação'), _(u'Reclamação')),
    (_(u'Venda'), _(u'Venda')),
)


class ContactForm(forms.Form):
    name = forms.CharField(label=_(u'Nome'),
                           widget=forms.TextInput(attrs={'class':
                                                  'span12'}))
    email = forms.EmailField(label=_(u'E-mail'),
                             widget=forms.EmailInput(attrs={'class':
                                                     'span12'}))
    subject = forms.ChoiceField(label=_(u'Assunto'), choices=SUBJECT_CHOICES,
                                widget=forms.Select(attrs={'class':
                                                    'span12'}))
    message = forms.CharField(label=_(u'Mensagem'),
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
                                         'maxlength': 255}))

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
