import os
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from cms.sitemaps import CMSSitemap
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^partitpirata/', include('partitpirata.foo.urls')),
    url(r'^contacte/', 'apps.contact.views.message_form'),
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
