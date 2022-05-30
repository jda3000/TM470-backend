import pprint
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class RegisterTests(APITestCase):

    def test_register_success(self):
        """ test post register a user success """

        url = reverse('register')

        data = {
            'username': 'james',
            'email': 'mrrewire@gmail.com',
            'password': 'superstrong12!!',
            'password_repeat': 'superstrong12!!'
        }

        response = self.client.post(url, data=data, format='json')
        # pprint.pprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_password_mismatch(self):
        """ test post register a user password mismatch """

        url = reverse('register')

        data = {
            'username': 'james',
            'email': 'mrrewire@gmail.com',
            'password': 'superstrong12!!',
            'password_repeat': 'superstrong11!!'
        }

        response = self.client.post(url, data=data, format='json')
        # pprint.pprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_email(self):
        """ test post register a user invalid email """

        url = reverse('register')

        data = {
            'username': 'james',
            'email': 'mrrewire@gmail',
            'password': 'superstrong12!!',
            'password_repeat': 'superstrong12!!'
        }

        response = self.client.post(url, data=data, format='json')
        # pprint.pprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_username(self):
        """ test post register a user invalid email """

        url = reverse('register')

        data = {
            'username': '',
            'email': 'mrrewire@gmail.com',
            'password': 'superstrong12!!',
            'password_repeat': 'superstrong12!!'
        }

        response = self.client.post(url, data=data, format='json')
        # pprint.pprint(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ForgottenPasswordTests(APITestCase):

    def create_user(self, email):
        """ creates a test user and return login tokens"""
        user = User.objects.create(
            username='test',
            email=email
        )
        user.set_password('test')
        user.save()
        return user



    def test_password_reset_success_valid_email(self):
        """ test post request password reset email with valid email """

        url = reverse('forgotten_password')

        # create user with email
        email = 'mrrewire@gmail.com'
        self.create_user(email)

        # password reset request form data
        data = {
            'email': email,
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_password_reset_success_invalid_email(self):
        """ test post request password reset email with invalid email """

        url = reverse('forgotten_password')

        # create user with email
        email = 'mrrewire@gmail.com'
        self.create_user(email)

        # password reset request form data
        data = {
            'email': 'jda3000@outlook.com',
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
