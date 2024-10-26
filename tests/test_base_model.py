#!/usr/bin/python3

import unittest
import datetime
import uuid
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Create an instance of BaseModel for testing."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if an instance of BaseModel is created with correct attributes."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save_method(self):
        """Test if `save` method updates `updated_at` attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_str_method(self):
        """Test if `__str__` method returns the correct format."""
        expected_str = f"{self.model.__class__.__name__} {self.model.id} {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_to_dict_method(self):
        """Test if `to_dict` method returns a correct dictionary representation."""
        model_dict = self.model.to_dict()
        
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIn("id", model_dict)
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertIn("created_at", model_dict)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
