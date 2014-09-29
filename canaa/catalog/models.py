# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField

try:
    from PIL import Image
except ImportError:
    import Image


PRODUCTINFO_CHOICES = (
    (1, _(u'Valor Energético')),
    (2, _(u'Carboidratos')),
    (3, _(u'Proteínas')),
    (3, _(u'Gorduras Totais')),
    (4, _(u'Gorduras Saturadas')),
    (5, _(u'Gorduras Trans')),
    (6, _(u'Fibra Alimentar')),
    (7, _(u'Sódio')),
    (8, _(u'Cálcio')),
    (9, _(u'Ferro')),
)


def get_display(key, list):
    """ Funcao que captura o label dos choices """
    d = dict(list)
    if key in d:
        return d[key]
    return None


class ProductGroup(models.Model):
    name = models.CharField(_(u'Nome'), max_length=50)
    slug = models.SlugField(_(u'Nome Slug'), max_length=50,
                            unique=True, editable=False)
    description = models.CharField(_(u'Descrição'), max_length=125)
    image = ImageField(_(u'Imagem'), upload_to='product_group',
                       help_text='Tamanho: 285x214 px (Ideal)')
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        self.slug = slugify(self.name)
        super(ProductGroup, self).save(*args, **kwargs)

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
        (width, height) = scale_dimensions(width, height, longest_side=285)

        size = (width, height)
        """ redimensiona esticando """
        # image = image.resize(size, Image.ANTIALIAS)
        """ redimensiona proporcionalmente """
        image.thumbnail(size, Image.ANTIALIAS)
        """ redimensiona cortando para encaixar no tamanho """
        # image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image.save(self.image.path, 'JPEG', quality=99)

    def get_absolute_url(self):
        return reverse('group:item', kwargs={"group": self.slug})

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Grupo de Produto')
        verbose_name_plural = _(u'Grupo de Produtos')
        ordering = ('name',)


class Product(models.Model):
    product_group = models.ForeignKey('ProductGroup',
                                      verbose_name=_(u'Grupo do Produto'))
    name = models.CharField(_(u'Nome'), max_length=120,
                            help_text='Nome do produto')
    slug = models.SlugField(_(u'Nome Slug'), max_length=50,
                            unique=True, editable=False)
    description = models.TextField(_(u'Descrição'), max_length=250,
                                   help_text='Descrição do produto')
    image = ImageField(_(u'Imagem'), upload_to=u'product',
                       help_text='Tamanho: 279x270 px (Ideal)')
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        self.slug = '%s-%s' % (self.pk, slugify(self.name))
        super(Product, self).save(*args, **kwargs)

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
        (width, height) = scale_dimensions(width, height, longest_side=285)

        size = (width, height)
        """ redimensiona esticando """
        # image = image.resize(size, Image.ANTIALIAS)
        """ redimensiona proporcionalmente """
        image.thumbnail(size, Image.ANTIALIAS)
        """ redimensiona cortando para encaixar no tamanho """
        # image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image.save(self.image.path, 'JPEG', quality=99)

    def get_absolute_url(self):
        return reverse('group:item',
                       kwargs={"group": slugify(self.product_group)})

    def __unicode__(self):
        return '%s - %s' % (unicode(self.product_group),
                            unicode(self.name))

    class Meta:
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'Produtos')
        ordering = ('name',)


class ProductInfo(models.Model):
    product_group = models.ForeignKey('ProductGroup',
                                      verbose_name=_(u'Grupo do Produto'),
                                      editable=False)
    product = models.ForeignKey('Product', verbose_name=_(u'Produto'))
    description = models.IntegerField(_(u'Descrição'),
                                      choices=PRODUCTINFO_CHOICES)
    amount = models.CharField(_(u'Quantidade'), max_length=30)
    value = models.CharField(_(u'Valor Diário'), max_length=2, default='**')
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    def save(self, *args, **kwargs):
        """
        funcao para salvar o grupo do produto.
        so para melhorar a velocidade da busca :P
        """
        p = Product.objects.get(pk=self.product_id)
        self.product_group = p.product_group
        super(ProductInfo, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(get_display(self.description, PRODUCTINFO_CHOICES))

    class Meta:
        verbose_name = _(u'Informação Nutricional')
        verbose_name_plural = _(u'Informações Nutricionais')
