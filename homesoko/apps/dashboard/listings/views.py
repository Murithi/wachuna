from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from homesoko.apps.properties.models import Property, PropertyImage
from homesoko.apps.utils.djupload.views import UploadView, UploadListView, UploadDeleteView
from homesoko.apps.utils.views_utils import require_own_agency
from .forms import PropertyForm, AddPropertyFeaturesForm
from .tables import PropertyTable


class PropertyCreateView(CreateView):
    form_class = PropertyForm
    model = Property
    template_name = 'listings/listing_form.html'
    success_url = reverse_lazy('listings.property_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PropertyCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.agency = self.request.user
        return super(PropertyCreateView, self).form_valid(form)


class PropertyListView(ListView):
    model = Property
    template_name = 'listings/listing_list.html'

    @require_own_agency
    def dispatch(self, *args, **kwargs):
        self.get_object_agency()
        return super(PropertyListView, self).dispatch(*args, **kwargs)

    def get_object_agency(self):
        return self.request.user

    def get_queryset(self):
        user = self.request.user
        if not user.is_staff:
            return Property.objects.filter(agency=user)
        return Property.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PropertyListView, self).get_context_data(**kwargs)
        context['table'] = PropertyTable(self.get_queryset())
        return context


class EditPropertyView(UpdateView):
    model = Property
    template_name = 'listings/listing_form.html'
    success_url = reverse_lazy('listings.listing_list')
    form_class = PropertyForm

    @require_own_agency
    def dispatch(self, *args, **kwargs):
        self.get_object_agency()
        return super(EditPropertyView, self).dispatch(*args, **kwargs)

    def get_object_agency(self):
        return self.get_object().agency

    def form_valid(self, form):
        form.instance.agency = self.request.user
        return super(EditPropertyView, self).form_valid(form)


class PropertyImagesUploadView(UploadView):
    model = PropertyImage
    delete_url = 'listings.images_delete'
    template_name = 'listings/propertyimage_form.html'

    @require_own_agency
    def dispatch(self, *args, **kwargs):
        self.get_object_agency()
        return super(PropertyImagesUploadView, self).dispatch(*args, **kwargs)

    def get_object_agency(self):
        return self.get_object().agency

    def get_object(self):
        return Property.objects.get(id=int(self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super(PropertyImagesUploadView, self).get_context_data(**kwargs)
        context['property'] = self.get_object()
        return context


class PropertyImagesListView(UploadListView):
    model = PropertyImage
    delete_url = 'listings.images_delete'

    @require_own_agency
    def dispatch(self, *args, **kwargs):
        self.get_object_agency()
        return super(PropertyImagesListView, self).dispatch(*args, **kwargs)

    def get_object_agency(self):
        return self.get_object().agency

    def get_object(self):
        return Property.objects.get(id=int(self.kwargs['pk']))

    def get_queryset(self):
        return PropertyImage.objects.filter(property=self.get_object(), deleted=False)


class PropertyImagesDeleteView(UploadDeleteView):
    model = PropertyImage

    @require_own_agency
    def dispatch(self, *args, **kwargs):
        self.get_object_agency()
        return super(PropertyImagesDeleteView, self).dispatch(*args, **kwargs)

    def get_object_agency(self):
        return self.get_object().property.agency

    def get_object(self):
        return PropertyImage.objects.get(id=int(self.kwargs['pk']))


class AddPropertyFeaturesView(View):
    template_name = 'listings/listing_features.html'
    form_class = AddPropertyFeaturesForm
    initial = {'key': 'value'}

    @require_own_agency
    def dispatch(self, *args, **kwargs):
        self.get_object_agency()
        return super(AddPropertyFeaturesView, self).dispatch(*args, **kwargs)

    def get_object_agency(self):
        return self.get_object().agency

    def get_object(self):
        return Property.objects.get(id=int(self.kwargs['pk']))

    def get(self, request, *args, **kwargs):
        sokoproperty = self.get_object()
        current_features = sokoproperty.features.all()
        context = {'property': sokoproperty, 'form': self.form_class(initial=self.initial), 'current_features': current_features}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        sokoproperty = self.get_object()
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
            messages.success(request, 'Property features have been updated successfully.')
            return HttpResponseRedirect(reverse('listings.listing_features', args=[sokoproperty.id]))

        return render(request, self.template_name, {'form': form, 'property': sokoproperty})


