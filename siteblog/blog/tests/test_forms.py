from django.test import TestCase
from blog.forms import UserLoginForm


class TestForm(TestCase):

    def test_login_form_valid_data(self):
        form = UserLoginForm(data={
            'username': 'admin',
            'password': 'admin'
        })

        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = UserLoginForm(data={})

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_register_form_valid_data(self):
        form = UserLoginForm(data={
            'username': 'Pavel',
            'password1': 'Soft12345',
            'password2': 'Soft12345',
            'email': 'Pavel@gmail.com'
        })

        self.assertTrue(form.is_valid())
