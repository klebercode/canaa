# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from canaa.core.models import STATE_CHOICES


SEX_CHOICES = (
    ('Feminino', u'Feminino'),
    ('Masculino', u'Masculino'),
)


FORMATION_CHOICES = (
    ('EF', u'Ensino Fundamental'),
    ('EM', u'Ensino Médio'),
    ('ESC', u'Ensino Superior Completo'),
    ('ESI', u'Ensino Superior Incompleto'),
    ('PG', u'Pós Graduado'),
    ('M', u'Mestrado'),
    ('D', u'Doutorado'),
)


class Talent(models.Model):
    name = models.CharField(_(u'Nome'), max_length=150)
    address = models.CharField(_(u'Endereço'), max_length=200)
    number = models.CharField(_(u'Número'), max_length=10)
    complement = models.CharField(_(u'Complemento'), max_length=100, blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999', blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    country = models.CharField(_(u'País'), max_length=50)
    phone = models.CharField(_(u'Fone'), max_length=20, help_text='(99) 9999-9999')
    email = models.EmailField(_(u'Email'), unique=True)
    date_birth = models.DateField(_(u'Nascimento'))
    sex = models.CharField(_(u'Sexo'), max_length=10, choices=SEX_CHOICES)
    formation = models.CharField(_(u'Formação'), max_length=10, choices=FORMATION_CHOICES)
    qualification = models.TextField(_(u'Resumo da Qualificação'))
    experience = models.TextField(_(u'Experiência Profissional'))
    enterprise1 = models.CharField(_(u'Empresa 1'), max_length=100, blank=True, null=True)
    contact1 = models.CharField(_(u'Contato na Empresa 1'), max_length=150, blank=True, null=True)
    period1 = models.CharField(_(u'Período 1'), max_length=100, blank=True, null=True)
    post1 = models.CharField(_(u'Cargo 1'), max_length=100, blank=True, null=True)
    activies1 = models.TextField(_(u'Principais Atividades 1'), blank=True, null=True)
    enterprise2 = models.CharField(_(u'Empresa 2'), max_length=100, blank=True, null=True)
    contact2 = models.CharField(_(u'Contato na Empresa 2'), max_length=150, blank=True, null=True)
    period2 = models.CharField(_(u'Período 2'), max_length=100, blank=True, null=True)
    post2 = models.CharField(_(u'Cargo 2'), max_length=100, blank=True, null=True)
    activies2 = models.TextField(_(u'Principais Atividades 2'), blank=True, null=True)
    enterprise3 = models.CharField(_(u'Empresa 3'), max_length=100, blank=True, null=True)
    contact3 = models.CharField(_(u'Contato na Empresa 3'), max_length=150, blank=True, null=True)
    period3 = models.CharField(_(u'Período 3'), max_length=100, blank=True, null=True)
    post3 = models.CharField(_(u'Cargo 3'), max_length=100, blank=True, null=True)
    activies3 = models.TextField(_(u'Principais Atividades 3'), blank=True, null=True)
    courses = models.TextField(_(u'Cursos'), blank=True, null=True)
    referrals = models.TextField(_(u'Referências Pessoais'))
    attach = models.FileField(_(u'Arquivo'), upload_to=u'talents')

    def attach_link(self):
        if self.attach:
            return "<a href='%s'>Baixar</a>" % self.attach.url
        else:
            return "Nenhum arquivo encontrado"
    attach_link.allow_tags = True
    attach_link.short_description = "Arquivo"

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Talento')
        verbose_name_plural = _(u'Talentos')