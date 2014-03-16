from django.test.testcases import TestCase
from django_dynamic_fixture import G
from homesoko.apps.properties.models import SokoProperty, City, Neighbourhood, Features
from homesoko.apps.dashboard.properties.forms import SokoPropertyForm


class PropertyCreateFormTests(TestCase):
    def test_property_create_form(self):
        city = G(City)
        neighbourhood = G(Neighbourhood)
        feature1 = G(Features)
        feature2 = G(Features)
        features = [feature1.id, feature2.id]
        data = {'name': 'Miotoni Apartment',
                'price': 82003000,
                'type': SokoProperty.PropertyTypeOptions.Apartment,
                'category': SokoProperty.CategoryOptions.Sale,
                'bedrooms': SokoProperty.BedroomOptions.Two,
                'bathrooms': SokoProperty.BathroomsOptions.OneAndHalf,
                'description': 'Spacious home in the cool of Karen',
                'structure_size': 1243,
                'lot_size': 123.34,
                'city': city.id,
                'neighbourhood': neighbourhood.id,
                'features': features
                }
        form = SokoPropertyForm(data, instance=None)
        self.assertTrue(form.is_valid())
