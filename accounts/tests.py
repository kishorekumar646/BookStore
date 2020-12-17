from django.test import TestCase, Client
from django.urls import reverse
from bookstore_backend.settings import BASE_URL

import pytest
import unittest

client = Client()


class test_TestURLs(unittest.TestCase):

    def test_RegisterView(self):
        url = BASE_URL + reverse("register")
        userData = {'first_name': '', 'last_name': '', 'phone_number': '',
                    'password1': '', 'password2': '', 'email': ''}

        response = client.post(path=url, data=userData, format='json')

        self.assertEqual(response.status_code, 406)
