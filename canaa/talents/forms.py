# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from canaa.talents.models import Talent
from canaa.talents.models import SEX_CHOICES, FORMATION_CHOICES
from canaa.core.models import STATE_CHOICES


class TalentForm(forms.ModelForm):
    class Meta:
        model = Talent

    def send_mail(self):
        subject = u'Curriculo do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'phone': self.cleaned_data['phone'],
            'email': self.cleaned_data['email'],
        }

        email_to = 'talents@polpacanaa.com.br'
        
        message = render_to_string('talent_mail.txt', context)
        message_html = render_to_string('talent_mail.html', context)
        msg = EmailMultiAlternatives(subject, message, 
            'no-reply@polpacanaa.com.br', [email_to]) # ['kleberss@gmail.com'])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()