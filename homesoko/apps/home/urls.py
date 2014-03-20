from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'', Home.as_view(), name='home'),
)
