# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


from sorl.thumbnail import ImageField
from tinymce import models as tinymce_models
from slim import LanguageField, Slim
# from slim.models.decorators import auto_prepend_language

try:
    from PIL import Image
except ImportError:
    import Image

from canaa.current_user import get_current_user


class Blog(models.Model, Slim):
    content = models.TextField(_(u'Conteúdo'))
    language = LanguageField()

    def __unicode__(self):
        return unicode(self.content)

    class Meta:
        verbose_name = _(u'Blog')
        verbose_name_plural = _(u'Blog')


class Post(models.Model, Slim):
    title = models.CharField(_(u'Título'), max_length=100)
    slug = models.SlugField(_(u'Título Slug'), max_length=100,
                            unique=True, editable=False)
    created_by = models.ForeignKey(User, verbose_name=u'Postado por',
                                   editable=False, default=get_current_user)
    pub_date = models.DateTimeField(_(u'Data'), auto_now_add=True)
    body = tinymce_models.HTMLField(verbose_name=u'Conteúdo')
    image = ImageField(_(u'Imagem'), upload_to=u'blog',
                       help_text='Tamanho Ideal 898x611 px')
    language = LanguageField()

    def admin_image(self):
        if self.image:
            return "<img src='%s' />" % self.image.url
        else:
            return "Nenhuma imagem encontrada"
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

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
        (width, height) = scale_dimensions(width, height, longest_side=900)

        size = (width, height)
        """ redimensiona esticando """
        # image = image.resize(size, Image.ANTIALIAS)
        """ redimensiona proporcionalmente """
        image.thumbnail(size, Image.ANTIALIAS)
        """ redimensiona cortando para encaixar no tamanho """
        # image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image.save(self.image.path, 'JPEG', quality=99)

    # @auto_prepend_language
    def get_absolute_url(self):
        return reverse('blog:post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Post')
        verbose_name_plural = _(u'Posts')
        ordering = ['-pub_date']
