from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_hompage_contains_correct_html(self):
       self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Shoud not')
    
    def test_homepage_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )