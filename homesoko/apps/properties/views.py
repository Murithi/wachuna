from django.views.generic import TemplateView
from .models import SokoProperty, PropertyFilter


class SaleProperties(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(SaleProperties, self).get_context_data(**kwargs)
        context_data['properties'] = SokoProperty.sale.all()
        return context_data


class LettingProperties(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(LettingProperties, self).get_context_data(**kwargs)
        context_data['properties'] = SokoProperty.letting.all()
        return context_data


class FilteredProperties(TemplateView):
    template_name = 'property_list.html'

    def get_context_data(self, **kwargs):
        context_data = super(PropertyFilter, self).get_context_data(**kwargs)
        context_data['properties'] = PropertyFilter(self.request.GET, queryset=SokoProperty.objects.all())
        return context_data
