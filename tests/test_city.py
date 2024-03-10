#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_init(self):
        self.assertIsInstance(self.city, City)

    def test_state_id(self):
        self.city.state_id = "1234"
        self.assertEqual(self.city.state_id, "1234")

    def test_name(self):
        self.city.name = "Test City"
        self.assertEqual(self.city.name, "Test City")


if __name__ == '__main__':
    unittest.main()
