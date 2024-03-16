from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from usercore.models import User


class UserAPITests(APITestCase):

    def setUp(self):
        # Create a user in the test database
        User.objects.create(name="Test User", age=30)

    def test_get_users_list(self):
        """
        Ensure we can retrieve the list of users.
        """
        url = reverse("user-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only 1 user in test db

    def test_get_single_user(self):
        """
        Ensure we can retrieve a single user by ID.
        """
        user = User.objects.get(name="Test User")
        url = reverse("user-detail", args=[user.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test User")
        self.assertEqual(response.data["age"], 30)

    def test_create_user_(self):
        """
        Ensure we can create a user.
        """
        url = reverse("user-list")
        response = self.client.post(url, data={"name": "Anthony", "age": 2}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)  # Check if present, don't care about its value
        self.assertEqual(response.data["name"], response.data["name"])
        self.assertEqual(response.data["age"], response.data["age"])

    def test_delete_user_(self):
        """
        Ensure we can delete a user.
        """
        user = User.objects.get(name="Test User")
        url = reverse("user-detail", args=[user.id])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(name="Test User")
