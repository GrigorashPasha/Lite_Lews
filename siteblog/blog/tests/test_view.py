from django.test import TestCase, Client
from django.urls import reverse

from blog.models import *


class HomePageTests(TestCase):

    def test_view_uses_correct_template_reg(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/register.html')

    def test_view_uses_correct_template_login(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/login.html')

    # def test_view_uses_correct_template_logout(self):
    #     response = self.client.get(reverse('logout'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/login.html')

    def test_view_uses_correct_template_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_view_uses_correct_template_by_category(self):
        response = self.client.get(reverse('category', args=['some-slug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_view_uses_correct_template_by_tag(self):
        response = self.client.get(reverse('tag', args=['some-slug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_view_uses_correct_template_post(self):
        response = self.client.get(reverse('post', args=['some-slug']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/single.html')

    # def test_view_uses_correct_template_search(self):
    #     response = self.client.get(reverse('search'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/search.html')
