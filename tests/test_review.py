#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_init(self):
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "This is a test review."

        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")
        self.assertEqual(self.review.text, "This is a test review.")


if __name__ == '__main__':
    unittest.main()
