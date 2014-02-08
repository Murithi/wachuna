from .views import *
from django.conf.urls import *

urlpatterns = patterns('',
    # Add a new property
    url(r'^new/$', PropertyCreateView.as_view(), name='properties.properties_create'),
    # List properties
    url(r'^$', PropertyListView.as_view(), name='properties.properties_list'),
   )