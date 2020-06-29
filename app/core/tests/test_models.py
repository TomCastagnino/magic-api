from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@castagnino.dev'
        password = 'testing321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@CASTAGNINO.DEV'
        user = get_user_model().objects.create_user(email, 'testing321')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testing321')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'testsuper@castagnino.dev', 
            'testing321'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)