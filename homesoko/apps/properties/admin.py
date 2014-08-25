from django.contrib import admin
from .models import Property, City, Neighbourhood


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'category', 'city', 'neighbourhood')

admin.site.register(Property, PropertyAdmin)
admin.site.register(City)
admin.site.register(Neighbourhood)
