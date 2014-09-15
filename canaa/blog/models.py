# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

# from sorl.thumbnail import get_thumbnail
from PIL import Image as Img, ImageOps
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from tinymce import models as tinymce_models

from canaa.current_user import get_current_user


class Blog(models.Model):
    content = models.TextField(_(u'Conteúdo'))

    def __unicode__(self):
        return unicode(self.content)

    class Meta:
        verbose_name = _(u'Blog')
        verbose_name_plural = _(u'Blog')


class Post(models.Model):
    title = models.CharField(_(u'Título'), max_length=100)
    slug = models.SlugField(_(u'Título Slug'), max_length=100,
                            unique=True, editable=False)
    created_by = models.ForeignKey(User, verbose_name=u'Postado por',
                                   editable=False, default=get_current_user)
    pub_date = models.DateTimeField(_(u'Data'), auto_now_add=True)
    body = tinymce_models.HTMLField(verbose_name=u'Conteúdo')
    image = models.ImageField(_(u'Imagem'), upload_to=u'blog',
                              help_text='Tamanho Ideal 898x611 px')

    def admin_image(self):
        if self.image:
            return "<img src='%s' />" % self.image.url
        else:
            return "Nenhuma imagem encontrada"
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        # if self.image:
        #     self.image = get_thumbnail(self.image, '500x600', quality=99,
        #                                format='JPEG')

        if self.image:
            """ resize image """
            image = Img.open(StringIO.StringIO(self.image.read()))
            # .thumbnail = redimensiona proporcionalmente
            image.thumbnail((898, 611), Img.ANTIALIAS)
            # .resize = estica para o tamanho definido
            # image.resize((898, 611), Img.ANTIALIAS)
            # ImageOps.fit = corta a imagem sem esticar
            # ImageOps.fit(image, (898, 611), Img.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s"
                                              % self.image.name, 'image/jpeg',
                                              output.len, None)
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Post')
        verbose_name_plural = _(u'Posts')
        ordering = ['-pub_date']
