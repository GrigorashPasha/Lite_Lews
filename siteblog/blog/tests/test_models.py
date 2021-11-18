from django.test import TestCase
from blog.models import *


class TestModel(TestCase):

    def SetUp(self):
        self.category1 = Category.objects.create(
            title='Photo',
            slug='photo'
        )

        self.post1 = Post.objects.create(
            title='News1',
            slug='news1',
            author='Pavel',
            content='blablabla',
            category='IT',
            tags='Python',
        )

    def test_assign_category(self):
        self.assertEquals(self.category1.title, 'Photo')

    def test_assign_post(self):
        self.assertEquals(self.post1.title, 'News1')

