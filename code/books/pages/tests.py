# pages/tests.py
from django.test import TestCase
from django.urls import reverse
from .views import HomePageView

class HomepageTests(TestCase):
    def test_homepage(self):
        """Test that the homepage returns a 200 status code and uses the correct template."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')