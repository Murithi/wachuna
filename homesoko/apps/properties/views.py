from django.views.generic import TemplateView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        if kwargs['type']:
            properties_list = Property.sale.filter(property_type=kwargs['type'])
        else:
            properties_list = Property.sale.all()

        # Pagination
        paginator = Paginator(properties_list, 24)  # Show 25 properties per page
        page = self.request.GET.get('page')
        try:
            context_data['properties'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            context_data['properties'] = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context_data['properties'] = paginator.page(paginator.num_pages)

        context_data['page_title'] = 'Property for letting'
        context_data['page_title'] = 'Properties for sale'
        return context_data


class LettingPropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(LettingPropertiesView, self).get_context_data(**kwargs)
        if kwargs['type']:
            properties_list = Property.letting.filter(property_type=kwargs['type'])
        else:
            properties_list = Property.letting.all()

        # Pagination
        paginator = Paginator(properties_list, 24)  # Show 25 properties per page
        page = self.request.GET.get('page')
        try:
            context_data['properties'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            context_data['properties'] = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context_data['properties'] = paginator.page(paginator.num_pages)

        context_data['page_title'] = 'Properties for letting'
        return context_data


class CityPropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(CityPropertiesView, self).get_context_data(**kwargs)
        city = kwargs['city']
        queryset = Property.objects.filter(city__name=city)
        if kwargs['type']:
            properties_list = queryset.filter(property_type=kwargs['type'])
        else:
            properties_list = queryset

        # Pagination
        paginator = Paginator(properties_list, 24)  # Show 25 properties per page
        page = self.request.GET.get('page')
        try:
            context_data['properties'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            context_data['properties'] = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context_data['properties'] = paginator.page(paginator.num_pages)

        context_data['page_title'] = 'Properteis in ' + city
        return context_data


class NeighbourhoodPropertiesView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(NeighbourhoodPropertiesView, self).get_context_data(**kwargs)
        neighbourhood = kwargs['neighbourhood']
        queryset = Property.objects.filter(neighbourhood__name=neighbourhood)
        if kwargs['type']:
            properties_list = queryset.filter(property_type=kwargs['type'])
        else:
            properties_list = queryset

        # Pagination
        paginator = Paginator(properties_list, 24)  # Show 25 properties per page
        page = self.request.GET.get('page')
        try:
            context_data['properties'] = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            context_data['properties'] = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context_data['properties'] = paginator.page(paginator.num_pages)

        context_data['page_title'] = 'Properties in ' + neighbourhood
        return context_data


class PropertyListView(TemplateView):
    template_name = "property_list.html"

    def get_context_data(self, **kwargs):
        context_data = super(PropertyListView, self).get_context_data(**kwargs)
        context_data['properties'] = PropertyFilter(self.request.GET, queryset=Property.objects.all())
        context_data['page_title'] = 'Property List'
        return context_data

