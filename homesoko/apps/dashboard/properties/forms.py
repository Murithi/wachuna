from django import forms
from django.conf import settings
from homesoko.apps.properties.models import SokoProperty


class SokoPropertyForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'required':'The name of the property is required'})
    price = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(choices=SokoProperty.PropertyTypeOptions.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=SokoProperty.CategoryOptions.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    bedrooms = forms.ChoiceField(choices=SokoProperty.BedroomOptions.choices)
    bathrooms = forms.ChoiceField(choices=SokoProperty.BathroomsOptions.choices)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}))
    structure_size = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lot_size = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    neighbourhood = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    feature = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.CharField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = SokoProperty
        exclude = ['author','updated_by']

    class Media:
        js = (settings.STATIC_URL + 'js/properties/add-remove-property-feature-field.js',
              )
