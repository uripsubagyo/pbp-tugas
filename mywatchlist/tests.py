from django.test import TestCase, Client
from django.urls import resolve
from .views import show_mywatchlist

class mywatchTest(TestCase):
    def test_app_url(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_app_url_html(self):
        response = Client().get('/mywatchlist/html')
        self.assertEqual(response.status_code, 200)
    
    def test_app_url_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_app_url_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
