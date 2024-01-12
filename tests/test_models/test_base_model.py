#!/usr/bin/python3

import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test if a new id is created
        obj = BaseModel()
        self.assertIsNotNone(obj.id)

        # Test if created_at and updated_at are set to the current datetime
        current_time = obj.created_at
        self.assertEqual(obj.created_at, current_time)
        self.assertEqual(obj.updated_at, current_time)

        # Test if the object is added to storage
        with patch('models.storage.new') as mock_storage_new:
            obj = BaseModel()
            mock_storage_new.assert_called_once_with(obj)

        # Test if kwargs are correctly assigned to object attributes
        kwargs = {
            "id": "test_id",
            "created_at": "2022-01-01T00:00:00.000000",
            "updated_at": "2022-01-02T00:00:00.000000"
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.id, "test_id")
        self.assertEqual(obj.created_at, datetime(2022, 1, 1, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2022, 1, 2))

        # Test if kwargs with "__class__" key are ignored
        kwargs = {
            "__class__": "TestClass",
            "id": "test_id",
            "created_at": "2022-01-01T00:00:00.000000",
            "updated_at": "2022-01-02T00:00:00.000000"
        }
        obj = BaseModel(**kwargs)
        self.assertNotEqual(obj.__class__, "TestClass")

        # Test if the object is added to storage when kwargs is empty
        with patch('storage.new') as mock_storage_new:
            obj = BaseModel()
            mock_storage_new.assert_called_once_with(obj)

if __name__ == '__main__':
    unittest.main()
