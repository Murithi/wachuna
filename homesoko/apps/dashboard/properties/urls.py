from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
    url(r'^$', PropertyListView.as_view(), name='properties.properties_list'),
    url(r'^new/$', PropertyCreateView.as_view(), name='properties.properties_create'),
    url(r'^upload-images/(?P<pk>\d+)/$', AddPropertyImages.as_view(), name='properties.upload_images'),
    url(r'^delete-images/(?P<pk>\d+)/$', AddPropertyImages.as_view(), name='upload-delete'),
    url(r'^view-images/(?P<pk>\d+)/$', PropertyImageListView.as_view(), name='view_images'),
    url(r'^edit/(?P<pk>\d+)/$', EditPropertyView.as_view(), name='properties.properties_edit'),
   )
