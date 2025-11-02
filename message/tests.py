from http.client import responses
from django.urls import reverse

from django.test import SimpleTestCase

class MessagePageTests(SimpleTestCase):
    def test_url_exists_at_correct_loc(self):
        response = self.client.get("/message/")
        self.assertEqual(response.status_code,200)


    def test_url_available_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code,200)

    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_clint(self):
        response = self.client.get('/message/')
        self.assertContains(response,'<h2>این هدر سایت هست</h2>')