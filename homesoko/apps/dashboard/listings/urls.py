from django.conf.urls import url, patterns
from .views import PropertyListView, PropertyCreateView, AddPropertyFeaturesView, PropertyImagesDeleteView, PropertyImagesListView, \
    PropertyImagesUploadView, EditPropertyView


urlpatterns = patterns('',
    url(r'^$', PropertyListView.as_view(), name='listings.property_list'),
    url(r'^new/$', PropertyCreateView.as_view(), name='listings.property_new'),
    url(r'^features/(?P<pk>\d+)/$', AddPropertyFeaturesView.as_view(), name='listings.listing_features'),
    url(r'^images/(?P<pk>\d+)/$', PropertyImagesUploadView.as_view(), name='listings.images_upload'),
    url(r'^images/delete/(?P<pk>\d+)/$', PropertyImagesDeleteView.as_view(), name='listings.images_delete'),
    url(r'^images/list/(?P<pk>\d+)/$', PropertyImagesListView.as_view(), name='listings.images_view'),
    url(r'^edit/(?P<pk>\d+)/$', EditPropertyView.as_view(), name='listings.property_edit'),
)
