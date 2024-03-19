#!/usr/bin/python3

import unittest
from unittest.mock import patch
import io
import sys
import os
import models
from models.base_model import BaseModel
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            new_id = fake_out.getvalue().strip()
            new_model = models.storage.all()["BaseModel." + new_id]
            self.assertIsInstance(new_model, BaseModel)

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            new_id = fake_out.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(new_id))
            output = fake_out.getvalue().strip()
            self.assertIn("[BaseModel]", output)

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            new_id = fake_out.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(new_id))
            obj_dict = models.storage.all()
            self.assertNotIn("BaseModel." + new_id, obj_dict)

    def test_all(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create State")
            self.console.onecmd("all")
            output = fake_out.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)
            self.assertIn("State", output)

    def test_count(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "3")

    def test_update(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            new_id = fake_out.getvalue().strip()
            self.console.onecmd("update BaseModel {}name'test'".format(new_id))
            obj_dict = models.storage.all()["BaseModel." + new_id]
            self.assertEqual(obj_dict.name, "test")

    def test_quit(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_prompt(self):
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_emptyline(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.assertFalse(self.console.onecmd(""))

    def test_invalid_command(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.onecmd("invalid")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: invalid")


if __name__ == '__main__':
    unittest.main()
