from django.conf.urls import patterns, include, url
from homesoko.apps.properties.views import Homepage
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Homepage.as_view(), name='home'),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^properties/', include('homesoko.apps.properties.urls')),
    url(r'^dashboard/listings/', include('homesoko.apps.dashboard.listings.urls')),
    #url(r'^accounts/', include('userena.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^users/', include('homesoko.apps.users.urls')),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^zoner/', include('homesoko.apps.zoner.urls')),
)

import os
urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
