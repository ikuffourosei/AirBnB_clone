#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_amenity_instantiation(self):
        """Tests instantiation of Amenity class."""

        value = Amenity()
        self.assertEqual(str(type(value)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(value, Amenity)
        self.assertTrue(issubclass(type(value), BaseModel))

    def test_amenity_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        value = Amenity()
        for key, val in attributes.items():
            self.assertTrue(hasattr(value, key))
            self.assertEqual(type(getattr(value, key, None)), val)

if __name__ == "__main__":
    unittest.main()