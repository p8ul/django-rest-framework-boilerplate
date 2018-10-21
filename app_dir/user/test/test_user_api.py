from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faker import Factory
from app_dir.factories import UserFactory

faker = Factory.create()


class UserTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.namespace = 'user_api'
        self.body = {
            'username': faker.first_name(),
            'email': faker.email(),
            'password': faker.password()
        }
        self.create_url = reverse(self.namespace + ':user-creator')
        self.list_url = reverse(self.namespace + ':user-list')
        self.update_url = reverse(self.namespace + ':user-updater', kwargs={'pk': self.user.id})

    def test_create_user_api(self):
        response = self.client.post(self.create_url, self.body, format='json')
        self.assertEqual(201, response.status_code)

    def test_listing_user_api_without_parameters(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.user)

    def test_listing_user_api_with_parameters(self):
        response = self.client.get(self.list_url + '?page_size=10&q=' + self.user.username)
        self.assertContains(response, self.user)

    def test_update_user_api(self):
        response = self.client.put(self.update_url, self.body, format='json')
        self.assertEqual(200, response.status_code)

