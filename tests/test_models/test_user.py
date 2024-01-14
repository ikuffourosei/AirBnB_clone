#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test Cases for the User class."""

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

    def test_user_instantiation(self):
        """Tests instantiation of User class."""

        value = User()
        self.assertEqual(str(type(value)), "<class 'models.user.User'>")
        self.assertIsInstance(value, User)
        self.assertTrue(issubclass(type(value), BaseModel))


if __name__ == "__main__":
    unittest.main()
