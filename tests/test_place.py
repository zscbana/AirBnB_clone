#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_init(self):
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "Test Place"
        self.place.description = "This is a test place."
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 3
        self.place.price_by_night = 100
        self.place.latitude = 12.34
        self.place.longitude = 56.78
        self.place.amenity_ids = ["9", "10"]

        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.description, "This is a test place.")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 3)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 12.34)
        self.assertEqual(self.place.longitude, 56.78)
        self.assertEqual(self.place.amenity_ids, ["9", "10"])


if __name__ == '__main__':
    unittest.main()
