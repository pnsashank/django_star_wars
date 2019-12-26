import httpretty
import requests
from django.test import TestCase

class TestSwapiService(TestCase):
    @httpretty.activate
    def test_check_swapi_get(self):
        httpretty.register_uri(
            httpretty.GET,
            "http://swapi.co/api/planets/?search=xvyoop",
            body='{"count": 0,"next": null,"previous": null,"results": []}'
            )
        response = requests.get('http://swapi.co/api/planets/?search=xvyoop')
        self.assertEqual(response.json(),{"count": 0,"next": None,"previous": None,"results": []})
