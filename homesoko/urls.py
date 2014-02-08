from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # Users
    #url(r'^properties/', include('homesoko.apps.properties.urls')),
    url(r'^dashboard/properties/', include('homesoko.apps.dashboard.properties.urls'))
)
