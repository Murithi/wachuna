from django.conf.urls import url, patterns
from .views import HomeDetail, HomeList

urlpatterns = patterns('',
                       #(r'contact-agent/$',agent_message),
                       (r'list/for-sale/$', HomeList.as_view()),
                       (r'list/letting/$', HomeList.as_view()),
                       (r'list/land/$', HomeList.as_view()),
                       (r'listing/(?P<property_slug>[\w-]+)/$', HomeDetail.as_view()),
                       )
