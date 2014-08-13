from django.conf.urls import patterns, url
from .views import LettingProperties, SaleProperties, FilteredProperties

urlpatterns = patterns('',
                       #(r'contact-agent/$',agent_message),
                       url(r'list/$', FilteredProperties.as_view()),
                       url(r'list/for-sale/$', SaleProperties.as_view(), name='properties.list_sale'),
                       url(r'list/letting/$', LettingProperties.as_view(), name='properties.list_letting'),
                       url(r'listing/(?P<property_slug>[\w-]+)/$', LettingProperties.as_view()),
                       )
