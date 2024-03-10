#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Setting up the instance of the BaseModel for testing
        self.model = BaseModel()

    def test_init(self):
        # Testing initialization of BaseModel
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_to_dict(self):
        # Testing to_dict method of BaseModel
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()  # Running the unit tests
