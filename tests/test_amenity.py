#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_init(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_name(self):
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
