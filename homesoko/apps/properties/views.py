from django.views.generic import TemplateView
from .models import Property, PropertyFilter


class Homepage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context_data = super(Homepage, self).get_context_data(**kwargs)
        context_data['properties'] = Property.objects.all()
        return context_data


class SaleProperties(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(SaleProperties, self).get_context_data(**kwargs)
        context_data['properties'] = Property.sale.all()
        return context_data


class LettingProperties(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(LettingProperties, self).get_context_data(**kwargs)
        context_data['properties'] = Property.letting.all()
        return context_data


class FilteredProperties(TemplateView):
    template_name = 'property_list.html'
'''
    def get_context_data(self, **kwargs):
        context_data = super(FilteredProperties, self).get_context_data(**kwargs)
        context_data['properties'] = FilteredProperties(self.request.GET, queryset=SokoProperty.objects.all())
        return context_data
'''
