#!/usr/bin/python3

import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_init(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_reload(self):
        self.storage.reload()
        self.assertIsNotNone(self.storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
