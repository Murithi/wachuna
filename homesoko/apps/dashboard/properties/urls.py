from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('',
    url(r'^$', PropertyListView.as_view(), name='dashboard_properties_list'),
    url(r'^new/$', PropertyCreateView.as_view(), name='dashboard_properties_create'),
    url(r'^images/(?P<pk>\d+)/$', AddPropertyImages.as_view(), name='upload_images'),
    url(r'^delete-images/(?P<pk>\d+)/$', AddPropertyImages.as_view(), name='upload-delete'),
    url(r'^view-images/(?P<pk>\d+)/$', PropertyImageListView.as_view(), name='view_images'),
    url(r'^edit/(?P<pk>\d+)/$', EditPropertyView.as_view(), name='dashboard_properties_edit'),
   )
