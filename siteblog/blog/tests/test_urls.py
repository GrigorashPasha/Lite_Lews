from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import *


class TestUrls(SimpleTestCase):

    def test_urls_is_resolved_register(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, register)

    def test_urls_is_resolved_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_login)

    def test_urls_is_resolved_logout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_logout)

    def test_urls_is_resolved_add_news(self):
        url = reverse('add_news')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CreateNews)

    def test_urls_is_resolved_search(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Search)

    def test_urls_is_resolved_home(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_urls_is_resolved_category(self):
        url = reverse('category', args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, PostsByCategory)

    def test_urls_is_resolved_tag(self):
        url = reverse('tag', args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, PostsByTag)

    def test_urls_is_resolved_single(self):
        url = reverse('post', args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, GetPost)
