
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentTest(TestCase):
    def setUp(self):
        self.data = {
            'username': 'Peter',
            'email': 'peter@example.com'
        }
        self.instance = User(**self.data)

    def test_model_can_create_instance(self):
        """ Test if the model can create an instance."""
        old_count = User.objects.count()
        self.instance.save()
        new_count = User.objects.count()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(self.instance.username, self.data.get('username'))
