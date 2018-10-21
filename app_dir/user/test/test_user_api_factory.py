from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from app_dir.factories import UserFactory


class UserTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.namespace = 'user_api'
        self.create_url = reverse(self.namespace + ':user-creator')
        self.list_url = reverse(self.namespace + ':user-list')
        self.update_url = reverse(self.namespace + ':user-updater')

    def test_list_factory(self):
        response = self.client.post(self.create_url, {}, format='json')
        self.assertEqual(400, response.status_code)

    def test_listing_created_user(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.user)
