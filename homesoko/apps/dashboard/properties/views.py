import json
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from braces.views import LoginRequiredMixin
from homesoko.apps.properties.models import SokoProperty, PropertyImage, Features
from .forms import SokoPropertyForm
from .response import JSONResponse, response_mimetype
from .serialize import serialize


class PropertyCreateView(LoginRequiredMixin, CreateView):
    form_class = SokoPropertyForm
    model = SokoProperty
    template_name = 'property_form.html'
    success_url = reverse_lazy('properties.properties_list')

    def form_valid(self, form):
        soko_property = form.save()
        features = form.cleaned_data['features']
        for feature in features:
            soko_property.features.add(feature)
        return CreateView.form_valid(self, form)


class AddPropertyImages(CreateView):
    model = PropertyImage
    template_name = 'propertyimage_upload_form.html'

    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        print form.errors
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(AddPropertyImages, self).get_context_data(**kwargs)
        context['soko_property'] = SokoProperty.objects.get(id=self.kwargs['pk'])
        return context


class PropertyListView(LoginRequiredMixin, ListView):
    model = SokoProperty
    template_name = 'property_list.html'


class EditPropertyView(UpdateView):
    model = SokoProperty
    template_name = 'property_form.html'
    success_url = reverse_lazy('properties.properties_list')
    form_class = SokoPropertyForm

    def form_valid(self, form):
        soko_property = form.save()
        features = form.cleaned_data['features']
        soko_property.features.clear()
        for feature in features:
            soko_property.features.add(feature)
        return UpdateView.form_valid(self, form)


class PropertyImageListView(ListView):
    model = PropertyImage

    def render_to_response(self, context, **response_kwargs):
        files = [serialize(p) for p in self.get_queryset()]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def get_queryset(self):
        return PropertyImage.objects.filter(soko_property=self.kwargs['pk'])
