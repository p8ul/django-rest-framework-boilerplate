from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faker import Factory
from app_dir.factories import ModuleFactory, UserFactory

faker = Factory.create()


class ModuleApiTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.module = ModuleFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.namespace = 'module_api'
        self.body = {
            'name': faker.word(),
            'description': faker.text()
        }
        self.create_url = reverse(self.namespace + ':create')
        self.list_url = reverse(self.namespace + ':list')
        self.update_url = reverse(self.namespace + ':update', kwargs={'pk': self.module.id})

    def test_create_module_api(self):
        response = self.client.post(self.create_url, self.body, format='json')
        self.assertEqual(201, response.status_code)

    def test_list_modules_api_without_parameters(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.module)

    def test_listing_module_api_with_parameters(self):
        response = self.client.get(self.list_url + '?page_size=10&q=' + self.module.name)
        self.assertContains(response, self.module)

    def test_update_module_api(self):
        response = self.client.put(self.update_url, self.body)
        self.assertEqual(200, response.status_code)
