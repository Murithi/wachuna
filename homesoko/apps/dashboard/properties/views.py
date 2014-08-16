from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from braces.views import LoginRequiredMixin
from homesoko.apps.properties.models import Property, PropertyImage
from homesoko.apps.utils.djupload.views import UploadView, UploadListView, UploadDeleteView
from .forms import SokoPropertyForm


class PropertyCreateView(LoginRequiredMixin, CreateView):
    form_class = SokoPropertyForm
    model = Property
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('dashboard_properties_list')

    def form_valid(self, form):
        soko_property = form.save()
        features = form.cleaned_data['features']
        for feature in features:
            soko_property.features.add(feature)
        return CreateView.form_valid(self, form)


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'properties/dashboard_property_list.html'


class EditPropertyView(LoginRequiredMixin, UpdateView):
    model = Property
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('dashboard_properties_list')
    form_class = SokoPropertyForm

    def form_valid(self, form):
        soko_property = form.save()
        features = form.cleaned_data['features']
        soko_property.features.clear()
        for feature in features:
            soko_property.features.add(feature)
        return UpdateView.form_valid(self, form)


class PropertyImagesUploadView(LoginRequiredMixin, UploadView):
    model = PropertyImage
    delete_url = 'dashboard.properties.images_delete'

    def get_context_data(self, **kwargs):
        context = super(PropertyImagesUploadView, self).get_context_data(**kwargs)
        context['property'] = Property.objects.get(id=int(self.kwargs['pk']))
        return context


class PropertyImagesListView(LoginRequiredMixin, UploadListView):
    model = PropertyImage
    delete_url = 'dashboard.properties.images_delete'

    def get_queryset(self):
        return PropertyImage.objects.filter(property=self.kwargs['pk'])


class PropertyImagesDeleteView(LoginRequiredMixin, UploadDeleteView):
    model = PropertyImage


