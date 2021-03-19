# vi lists/test.py
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page
import re

class HomePageTest(TestCase):
    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = self.remove_csrf(render_to_string(
            'home.html'
        ))
        response_decode = self.remove_csrf(response.content.decode())
        self.assertEqual(response_decode, expected_html)

        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        # self.assertIn('신규 작업 아이템', response.content.decode())

        response_decode = self.remove_csrf(response.content.decode())
        expected_html = self.remove_csrf(render_to_string(
            'home.html',
            {'new_item_text':'신규 작업 아이템'}
        ))
        self.assertEqual(response_decode, expected_html)



