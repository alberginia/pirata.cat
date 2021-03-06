import os
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import redirect_to
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = patterns('',
    # hardcoded redirections, these go to external sites
#    url(r'^ca/bloc/$', redirect_to, { 'url': '/lalala' }),
    url(r'^favicon.ico$', redirect_to, { 'url': '/media/img/favicon.ico' }),

    url(r'^contacte/', 'apps.contact.views.message_form'),
    url(r'^afiliacio/', 'apps.contact.views.interested_form'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    )
