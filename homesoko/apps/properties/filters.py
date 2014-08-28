import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):

    class Meta:
        model = Property
        fields = ['bedrooms', 'bathrooms', 'city', 'neighbourhood', 'category']