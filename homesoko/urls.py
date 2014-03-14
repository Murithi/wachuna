from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/properties/', include('homesoko.apps.dashboard.properties.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'^select2/', include('django_select2.urls')),
)

import os
urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
