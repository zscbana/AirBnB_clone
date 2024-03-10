#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_init(self):
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        self.user.email = "test@example.com"
        self.user.password = "test_password"
        self.user.first_name = "Test"
        self.user.last_name = "User"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "test_password")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")


if __name__ == '__main__':
    unittest.main()
