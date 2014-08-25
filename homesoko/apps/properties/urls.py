from django.conf.urls import patterns, url
from .views import LettingPropertiesView, SalePropertiesView, PropertyDetailView

urlpatterns = patterns('',
                       #(r'contact-agent/$',agent_message),
                       #url(r'list/$', FilteredProperties.as_view()),
                       url(r'list/for-sale/$', SalePropertiesView.as_view(), name='properties.list_sale'),
                       url(r'list/letting/$', LettingPropertiesView.as_view(), name='properties.list_letting'),
                       url(r'listing/(?P<property_slug>[\w-]+)/$', PropertyDetailView.as_view(), name='properties.listing'),
                       )
