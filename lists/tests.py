from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', request = request)
        self.assertEqual(
            self.remove_csrf_line(response.content.decode()),
            self.remove_csrf_line(expected_html)
        )

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            "home.html", 
            {'new_item_text': 'A new list item'},
            request = request
        )
        self.assertEqual(
            self.remove_csrf_line(response.content.decode()),
            self.remove_csrf_line(expected_html)
        )
        
    def remove_csrf_line(self, rawText):
        textLines = rawText.splitlines()
        result = ""
        for line in textLines:
            if ('name=\'csrfmiddlewaretoken\'' in line):
                continue
            else:
                result += line
                result += '\n'
        return result
    