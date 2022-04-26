import datetime
from django.utils.timezone import make_aware

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.test import APITestCase

from beats.models.beat import Beat

User = get_user_model()


# tests designed for data security (confidentiality, integrity, and availability)
# TODO test anonymous user

class BeatTests(APITestCase):
    test_new_data = {
        'description': 'new test beat',
        'route': {
            'type': 'LineString',
            'coordinates': [(15.732421875, 8.5775756835938), (10.986328125, 3.3041381835938)]
        },
        'start_time': datetime.datetime.now(),
        'end_time': datetime.datetime.now()
    }

    def create_user(self):
        """ creates a test user and return login tokens"""
        user = User.objects.create(username='test')
        user.set_password('test')
        user.save()
        return user, self._login_credentials(user).access_token

    def _login_credentials(self, user):
        return RefreshToken.for_user(user)

    def test_get_beat_missing(self):
        """ test get a beat that does no exist """
        url = reverse(f'beats:beat_detail') + f'?id=1'
        user, access_token = self.create_user()
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_beat(self):
        """
        Ensure we can create a new beat object.
        """
        url = reverse('beats:beat_detail')
        user, access_token = self.create_user()

        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.post(url, self.test_new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_beat(self):
        """ test get a beat that exists"""
        user, access_token = self.create_user()

        beat = Beat.objects.create(
            user=user,
            description='test',
            start_time=make_aware(datetime.datetime.now()),
            end_time=make_aware(datetime.datetime.now())
        )

        url = reverse(f'beats:beat_detail') + f'?id={beat.id}'
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_beat_missing_description(self):
        """ Ensure no beat is created without missing route """
        url = reverse('beats:beat_detail')
        data = {
            'route': {
                'type': 'LineString',
                'coordinates': [(15.732421875, 8.5775756835938), (10.986328125, 3.3041381835938)]
            },
            'start_time': datetime.datetime.now(),
            'end_time': datetime.datetime.now()
        }
        user, access_token = self.create_user()
        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_beat(self):
        """ Ensure we can edit a Beat object """

        user, access_token = self.create_user()

        # create new Beat
        url = reverse('beats:beat_detail')

        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.post(url, self.test_new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # edit Beat
        data = {
            'id': response.data['id']
        }

        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_beat(self):
        user, access_token = self.create_user()

        # create new Beat
        url = reverse('beats:beat_detail')
        # initial number of Beat records in DB
        beat_initial_count = Beat.objects.all().count()

        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.post(url, self.test_new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # delete Beat
        url = reverse(f'beats:beat_detail') + f'?id={response.data["id"]}'

        self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(access_token))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # number of Beat record in DB after creating one and deleting one
        beat_after_count = Beat.objects.all().count()
        self.assertEqual(beat_initial_count, beat_after_count, 'Beat not deleted')
