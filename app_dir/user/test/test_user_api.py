from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

module = 'user_api'


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        # create user for force_authenticate
        user = User.objects.create_superuser(username='olivia', password='secret', email="admin@xple.com")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.instance_data = {
            "username": "James",
            'email': 'james@example.com',
            'password': '123sdfsdf3SDF##@!@!SD'
        }
        self.pk = None
        # create
        self.response = self.client.post(
            reverse(module + ':user-creator'),
            self.instance_data, format='json'
        )
        # self.api_list = self.client.get(reverse(module+':user-list'))

    def test_api_can_create_an_instance(self):
        """Test the api has instance creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data.get('username'), self.instance_data.get('username'))

        instance = User.objects.last()
        self.pk = instance.pk

        self.assertEqual(instance.username, 'James')
        api_update = self.client.put(
            reverse(module + ':user-updater', kwargs={'pk': self.pk}),
            self.instance_data,
        )
        self.assertEqual(api_update.data.get('username'), 'James')

    def test_api_list_with_parameters(self):
        self.api_list = self.client.get(reverse(module + ':user-list') + '?q=oli&page_size=10')
        self.assertEqual(self.api_list.status_code, status.HTTP_200_OK)

    def test_api_list_without_parameters(self):
        self.api_list = self.client.get(reverse(module + ':user-list'))
        self.assertEqual(self.api_list.status_code, status.HTTP_200_OK)


