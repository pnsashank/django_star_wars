from django.test import TestCase, Client
from django.urls import reverse
from Planets.models import Planet
import json

class TestViews(TestCase):
    def test_project_Planets_GET_1(self):
        client=Client()
        response=client.get(reverse('home'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'Planets/home.html')

    def test_project_Planet_GET_2(self):
        client=Client()
        response=client.post(reverse('database'))

        self.assertEquals(response.status_code,200)

    def test_project_Planet_GET_3(self):
        client=Client()
        response=client.get(reverse('store'))
        self.assertEquals(response.status_code,200)

        
