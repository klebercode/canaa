from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'canaa.core.views.home', name='home'),
    url(r'^institucional/', 'canaa.core.views.institutional',
        name='institutional'),
    # url(r'^produtos/', 'canaa.core.views.products', name='products'),
    url(r'^representantes/', 'canaa.core.views.sellers', name='sellers'),
    url(r'^marketing/', 'canaa.core.views.marketing', name='marketing'),
    url(r'^contato/', 'canaa.core.views.contact', name='contact'),

    url(r'^trabalhe-conosco/', include('canaa.talents.urls')),
    url(r'^mais-saude/', include('canaa.blog.urls', namespace='blog')),
    url(r'^produtos/', include('canaa.catalog.urls', namespace='group')),

    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
