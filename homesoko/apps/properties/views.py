from django.views.generic import TemplateView, DetailView
from .models import Property
from .filters import PropertyFilter


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
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context_data = super(PropertyDetailView, self).get_context_data(**kwargs)
        sokoproperty = self.get_object()
        context_data['images'] = sokoproperty.images.values
        return context_data


class SalePropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(SalePropertiesView, self).get_context_data(**kwargs)
        context_data['properties'] = Property.sale.all()
        context_data['page_title'] = 'Property for sale'
        return context_data


class LettingPropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(LettingPropertiesView, self).get_context_data(**kwargs)
        context_data['properties'] = Property.letting.all()
        context_data['page_title'] = 'Property for letting'
        return context_data


class PropertyListView(TemplateView):
    pass
