"""Tests of the sign up view."""
from django.test import TestCase
from django.urls import reverse
from microblogs.forms import LogInForm

class LogInViewTestCase(TestCase):
    """Unit tests of the log in view."""

    def setUp(self):
        self.url = reverse('log_in')

    def test_log_in_url(self):
        self.assertEqual(reverse('log_in'), '/log_in/')

    def test_get_log_in(self):
        url = reverse('log_in')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
