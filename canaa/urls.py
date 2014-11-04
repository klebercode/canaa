from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'canaa.core.views.home', name='home'),
    url(_(r'^institucional/'), 'canaa.core.views.institutional',
        name='institutional'),
    # url(r'^produtos/', 'canaa.core.views.products', name='products'),
    url(_(r'^representantes/'), 'canaa.core.views.sellers', name='sellers'),
    url(_(r'^marketing/'), 'canaa.core.views.marketing', name='marketing'),
    url(_(r'^contato/'), 'canaa.core.views.contact', name='contact'),

    url(_(r'^trabalhe-conosco/'), include('canaa.talents.urls')),
    url(_(r'^mais-saude/'), include('canaa.blog.urls', namespace='blog')),
    url(_(r'^produtos/'), include('canaa.catalog.urls', namespace='group')),

    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls')),
    )
