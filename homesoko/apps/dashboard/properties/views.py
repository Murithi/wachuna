from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from braces.views import LoginRequiredMixin
from homesoko.apps.properties.models import SokoProperty
from .forms import SokoPropertyForm


class PropertyCreateView(LoginRequiredMixin, CreateView):
    form_class = SokoPropertyForm
    model = SokoProperty
    template_name = 'property_form.html'
    success_url = reverse_lazy('properties.properties_list')


class PropertyListView(LoginRequiredMixin, ListView):
    model = SokoProperty
    template_name = 'property_list.html'


class PropertyDeleteView(DeleteView):
    model = SokoProperty
    success_url = reverse_lazy('properties.properties_list')