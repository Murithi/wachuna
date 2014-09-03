from decimal import Decimal
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View
from braces.views import LoginRequiredMixin
from homesoko.apps.properties.models import Property, PropertyImage
from homesoko.apps.utils.djupload.views import UploadView, UploadListView, UploadDeleteView
from .forms import PropertyForm, AddPropertyFeaturesForm
from .tables import PropertyTable


class PropertyCreateView(LoginRequiredMixin, CreateView):
    form_class = PropertyForm
    model = Property
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('dashboard.properties.property_list')


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'properties/dashboard_property_list.html'

    def get_queryset(self):
        return Property.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PropertyListView, self).get_context_data(**kwargs)
        context['table'] = PropertyTable(Property.objects.all())
        return context


class EditPropertyView(LoginRequiredMixin, UpdateView):
    model = Property
    template_name = 'properties/property_form.html'
    success_url = reverse_lazy('dashboard.properties.property_list')
    form_class = PropertyForm


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
        return PropertyImage.objects.filter(property=self.kwargs['pk'], deleted=False)


class PropertyImagesDeleteView(LoginRequiredMixin, UploadDeleteView):
    model = PropertyImage


class AddPropertyFeaturesView(View):
    template_name = 'properties/property_add_features.html'
    form_class = AddPropertyFeaturesForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        sokoproperty = Property.objects.get(id=int(kwargs['pk']))
        current_features = sokoproperty.features.all()
        context = {'form': self.form_class(initial=self.initial), 'current_features': current_features}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        sokoproperty = Property.objects.get(id=int(kwargs['pk']))
        if form.is_valid():

            features = request.POST.getlist('features')
            current_features = [str(feature.id) for feature in sokoproperty.features.all()]

            # Add new features
            for feature in features:
                if feature not in current_features:
                    sokoproperty.features.add(feature)
            # Remove other features
            if current_features:
                for feature in current_features:
                    if feature not in features:
                        sokoproperty.features.remove(feature)
            # if images have been added redirect to list else to the images page
            if sokoproperty.images.all():
                return HttpResponseRedirect(reverse('dashboard.properties.property_list'))
            else:
                return HttpResponseRedirect(reverse('dashboard.properties.images_upload', kwargs={'pk': sokoproperty.id}))

        return render(request, self.template_name, {'form': form})

