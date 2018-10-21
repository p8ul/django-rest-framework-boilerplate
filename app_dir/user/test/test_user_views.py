from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from ...factories import UserFactory


class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

        self.namespace = 'user'
        self.url = reverse(self.namespace + ':index')

    def test_user_index_view(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
