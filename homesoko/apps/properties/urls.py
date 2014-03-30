from django.conf.urls import patterns
from .views import LettingProperties, SaleProperties, FilteredProperties

urlpatterns = patterns('',
                       #(r'contact-agent/$',agent_message),
                       (r'list/$', FilteredProperties.as_view()),
                       (r'list/for-sale/$', SaleProperties.as_view()),
                       (r'list/letting/$', LettingProperties.as_view()),
                       (r'listing/(?P<property_slug>[\w-]+)/$', LettingProperties.as_view()),
                       )
