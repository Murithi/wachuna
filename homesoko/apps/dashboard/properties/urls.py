from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
    url(r'^$', PropertyListView.as_view(), name='dashboard.properties.property_list'),
    url(r'^new/$', PropertyCreateView.as_view(), name='dashboard.properties.property_new'),
    url(r'^images/(?P<pk>\d+)/$', PropertyImagesUploadView.as_view(), name='dashboard.properties.images_upload'),
    url(r'^images/delete/(?P<pk>\d+)/$', PropertyImagesUploadView.as_view(), name='dashboard.properties.images_delete'),
    url(r'^images/list/(?P<pk>\d+)/$', PropertyImagesListView.as_view(), name='dashboard.properties.images_view'),
    url(r'^edit/(?P<pk>\d+)/$', EditPropertyView.as_view(), name='dashboard.properties.property_edit'),
)
