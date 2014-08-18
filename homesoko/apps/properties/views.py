from django.views.generic import TemplateView, DetailView
from .models import Property


class Homepage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context_data = super(Homepage, self).get_context_data(**kwargs)
        context_data['properties'] = Property.objects.all()
        return context_data


class PropertyDetailView(DetailView):
    template_name = 'property_detail.html'
    model = Property
    slug_url_kwarg = 'property_slug'
    slug_field = 'slug'



class SalePropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(SalePropertiesView, self).get_context_data(**kwargs)
        context_data['properties'] = Property.sale.all()
        return context_data


class LettingPropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(LettingPropertiesView, self).get_context_data(**kwargs)
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
