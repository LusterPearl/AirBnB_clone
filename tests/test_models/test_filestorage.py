#!/usr/bin/python3
""" Testing the function of FileStorage regarding save and reload objects. """

import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ To test the functionality of the FileStorage """

    def setUp(self):
        """ Create a new object and setup """
        self.storage = storage
        self.storage.reload()

    def tearDown(self):
        """ Teardown a new object """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_reload_objects(self):
        """ Create a new object and save it """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        """ Ensure the object is in storage """
        all_objs = self.storage.all()
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, all_objs)

        """ Ensure the object is in the JSON file """
        with open("file.json", "r", encoding="utf-8") as file:
            json_data = file.read()
            self.assertIn(key, json_data)

        """ Create a new storage instance and reload """
        new_storage = storage
        new_storage.reload()

        """ Ensure the object is reloaded """
        reloaded_obj = new_storage.all().get(key)
        self.assertIsNotNone(reloaded_obj)
        self.assertEqual(reloaded_obj.name, "My_First_Model")
        self.assertEqual(reloaded_obj.my_number, 89)


if __name__ == '__main__':
    unittest.main()
