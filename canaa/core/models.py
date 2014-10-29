# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps


STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)

ICON_CHOICES = (
    ('icon-leaf', _(u'Meio Ambiente')),
    ('icon-group', _(u'Funcionários')),
    ('icon-globe', _(u'Sociedade')),
)

INSTITUTIONAL_CHOICES = (
    (1, _(u'Institucional')),
    (2, _(u'Nossa Missão')),
)

SELLER_CHOICE = (
    # (1, _(u'Distribuidor')),
    (2, _(u'Representante')),
)

BANNER_CHOICES = (
    (1, _(u'Principal')),
    (2, _(u'Secundário')),
)


class Customer(models.Model):
    name = models.CharField(_(u'Nome'), max_length=50)
    image = models.ImageField(_(u'Logo'), upload_to='customer')
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    def admin_image(self):
        return '<img src="%s" width="150" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u'Logo'

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')
        ordering = ['name']


class Institutional(models.Model):
    area = models.IntegerField(_(u'Área'), choices=INSTITUTIONAL_CHOICES,
                               help_text='Área no menu institucional')
    content = models.TextField(_(u'Conteúdo'), help_text='Conteúdo a ser \
                               exibido no institucional.')
    image = models.ImageField(_(u'Imagem'), upload_to='institutional')

    def admin_image(self):
        return '<img src="%s" width="150" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u'Imagem'

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = _(u'Institucional')
        verbose_name_plural = _(u'Institucional')


class Step(models.Model):
    icon = models.CharField(_(u'Ícone'), max_length=20, choices=ICON_CHOICES)
    title = models.CharField(_(u'Título'), max_length=20)
    description = models.CharField(_(u'Descrição'), max_length=250)
    order = models.IntegerField(_(u'Ordem'), default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u'Proposta de Valor')
        verbose_name_plural = _(u'Propostas de Valor')
        ordering = ('order',)


class Banner(models.Model):
    type = models.IntegerField(_(u'Banner'), choices=BANNER_CHOICES, default=1)
    image = models.ImageField(_(u'Imagem'), upload_to=u'banner',
                              help_text='Tamanho: 1920x2977 px',
                              blank=True, null=True)
    title = models.CharField(_(u'Título'), max_length=50,
                             help_text='O título aparece com fontes maiores \
                             no site')
    text = models.CharField(_(u'Texto'), max_length=100,
                            help_text='O texto aparece com fontes menores \
                            no site',
                            blank=True, null=True)
    label = models.CharField(_(u'Texto do botão'), max_length=40,
                             help_text='Ex: Conheça nossa empresa')
    link = models.CharField(_(u'Link do botão'), max_length=200,
                            help_text='Ex: intitucional ou \
                            mais-saude/acerola-magica')
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    def back_image(self):
        if self.image:
            return '<img src="%s" width="200" />' % self.image.url
        else:
            return u'Banner secundário não tem imagem'
    back_image.allow_tags = True
    back_image.short_description = u'Imagem'

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Banner')
        verbose_name_plural = _(u'Banners')


class Enterprise(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    description = models.CharField(_(u'Descrição'), max_length=100,
                                   blank=True, null=True)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20,
                            help_text='99.999.999/9999-99')
    address = models.CharField(_(u'Endereço'), max_length=200)
    number = models.CharField(_(u'Número'), max_length=10)
    complement = models.CharField(_(u'Complemento'), max_length=100)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999',
                           blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    country = models.CharField(_(u'País'), max_length=50)
    phone1 = models.CharField(_(u'Fone 1'), max_length=20,
                              help_text='(99) 9999-9999')
    phone2 = models.CharField(_(u'Fone 2'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    phone3 = models.CharField(_(u'Fone 3 (Fax)'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    email = models.EmailField(_(u'Email'))

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Empresa')
        verbose_name_plural = _(u'Empresa')


class Sale(models.Model):
    content = models.TextField(_(u'Descrição'))
    image = models.ImageField(_(u'Banner'), upload_to='sale')

    def admin_image(self):
        return '<img src="%s" width="300" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u'Banner'

    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        super(Sale, self).save(*args, **kwargs)

        image = Image.open(self.image)

        def scale_dimensions(width, height, longest_side):
            if width > height:
                if width > longest_side:
                    ratio = longest_side*1./width
                    return (int(width*ratio), int(height*ratio))
                elif height > longest_side:
                    ratio = longest_side*1./height
                    return (int(width*ratio), int(height*ratio))
            return (width, height)

        (width, height) = image.size
        (width, height) = scale_dimensions(width, height, longest_side=902)

        size = (902, 355)
        """ redimensiona esticando """
        # image = image.resize(size, Image.ANTIALIAS)
        """ redimensiona proporcionalmente """
        image.thumbnail(size, Image.ANTIALIAS)
        """ redimensiona cortando para encaixar no tamanho """
        # image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image.save(self.image.path, 'JPEG', quality=99)

    def __unicode__(self):
        return unicode(self.content)

    class Meta:
        verbose_name = _(u'Venda')
        verbose_name_plural = _(u'Venda')


class Seller(models.Model):
    type = models.IntegerField(_(u'Tipo'), choices=SELLER_CHOICE,
                               editable=False)
    name = models.CharField(_(u'Nome'), max_length=150, unique=True)
    slug = models.SlugField(_(u'Nome Slug'), max_length=150,
                            unique=True, editable=False)
    phone = models.CharField(_(u'Fone'), max_length=20,
                             help_text='(99) 9999-9999')
    email = models.EmailField(_(u'Email'))
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    def save(self, *args, **kwargs):
        self.type = 2
        self.slug = slugify(self.name)
        super(Seller, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Representante e Distribuidor')
        verbose_name_plural = _(u'Representantes e Distribuidores')
        ordering = ('name', 'state', 'type')
