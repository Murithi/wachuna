from django import forms
from django.conf import settings
from homesoko.apps.properties.models import SokoProperty, City, Neighbourhood, Features
from django_select2.fields import HeavyModelSelect2MultipleChoiceField
from django_select2.widgets import Select2MultipleWidget
from multiuploader.forms import MultiuploaderField


class SokoPropertyForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'required':'The name of the property is required'})
    price = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(choices=SokoProperty.PropertyTypeOptions.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=SokoProperty.CategoryOptions.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    bedrooms = forms.ChoiceField(choices=SokoProperty.BedroomOptions.choices, required=False)
    bathrooms = forms.ChoiceField(choices=SokoProperty.BathroomsOptions.choices, required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}))
    structure_size = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lot_size = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    neighbourhood = forms.ModelChoiceField(queryset=Neighbourhood.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    features = HeavyModelSelect2MultipleChoiceField(
                            label='Features',
                            required=False,
                            queryset=Features.objects.all(),  # Correct filter will be added by the view, since it depends on the request
                            # This will be dynamically changed to a HeavySelect2MultipleWidget in the view, because doing it here causes cyclic imports
                            widget=Select2MultipleWidget(select2_options={
                                'width': '32em',
                                'class': 'form-control'
                            }))

    def __init__(self, *args, **kwargs):
        super(SokoPropertyForm, self).__init__(*args, **kwargs)
        if kwargs['instance']:
            self.fields['features'].initial = kwargs['instance'].features.all()

    class Meta:
        model = SokoProperty
        exclude = ['author', 'updated_by']

    class Media:
        js = (settings.STATIC_URL + 'js/properties/jquery.duplicate.min.js',
              )
