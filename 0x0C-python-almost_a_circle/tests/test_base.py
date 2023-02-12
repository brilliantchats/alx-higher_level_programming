#!/usr/bin/python3
"""
Test for creation of Base object and assignment of id instance attr
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test creation of a Base object and assignment of id attr
    """
    def test_id(self):
        """Test that id of Base object is correct"""
        base_obj = Base()
        self.assertEqual(base_obj.id, 1)
    
    def test_id_true(self):
        """Test if id is a certain value"""
        obj = Base(12)
        self.assertTrue(obj.id == 12)

if __name__ == "__main__":
    unittest.main()
