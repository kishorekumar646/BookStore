from django.test import TestCase, Client
from django.urls import reverse
from bookstore_backend.settings import BASE_URL

import pytest
import unittest

client = Client()

@pytest.mark.django_db
class test_TestURLs(unittest.TestCase):

    def test_RegistarationOnSubmit_ThenReturn_HTTP_406_NOT_ACCEPTABLE(self):
        url = BASE_URL + reverse("register")
        userData = {'first_name': '', 'last_name': '', 'phone_number': '',
                    'password1': '', 'password2': '', 'email': ''}

        response = client.post(path=url, data=userData, format='json')

        self.assertEqual(response.status_code, 406)