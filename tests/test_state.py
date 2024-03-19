#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_init(self):
        self.assertIsInstance(self.state, State)

    def test_name(self):
        self.state.name = "Test State"
        self.assertEqual(self.state.name, "Test State")


if __name__ == '__main__':
    unittest.main()
