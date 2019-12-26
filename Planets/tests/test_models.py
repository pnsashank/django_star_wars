from django.test import TestCase
from Planets.models import Planet

class TestModels(TestCase):
    def setUp(self):
        planet_details=Planet.objects.create(planet_name='Test',rotation_period=34,orbital_period=21,gravity="1 standard")
        planet_details.save()
    def test_text(self):
        planet=Planet.objects.get(planet_name='Test')
        planet_rotation_period=planet.rotation_period
        self.assertEquals(planet_rotation_period,"34")
