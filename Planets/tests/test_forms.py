from django.test import SimpleTestCase
from Planets.forms import PlanetForm


class TestForms(SimpleTestCase):
    def test_valid_form_data(self):
        form=PlanetForm(data={
            'planet_name':'Test'
        })

        self.assertTrue(form.is_valid())

    def test_not_valid_form_data(self):
        form=PlanetForm(data={})

        self.assertFalse(form.is_valid())
