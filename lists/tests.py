# vi lists/test.py
from django.test import TestCase
from django.urls import resolve
from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

'''
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
        self.assertEqual(1 + 1, 3)
'''

