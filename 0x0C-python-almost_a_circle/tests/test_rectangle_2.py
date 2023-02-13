#!/usr/bin/python3
"""
Second sets of tests for Rectangle
"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Second sets of tests for Rectangle"""
    def test_area(self):
        """Test value of area"""
        rect1 = Rectangle(5, 6)
        self.assertEqual(rect1.area(), 30)

    def test_str(self):
        """Test str implementation of Rectangle object"""
        rect2 = Rectangle(4, 6, 2, 1, 12)
        self.assertTrue(print(rect2) == "[Rectangle] (12) 2/1 - 4/6")
