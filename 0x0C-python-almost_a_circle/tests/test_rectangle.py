#!/usr/bin/python3
"""
Test the Rectangle class and its methods
"""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Test Rectangle tests"""
    def test_rect_id(self):
        """Test if the id allocated is correct"""
        rect1 = Rectangle(10, 2, 3, 4, 11)
        self.assertEqual(rect1.id, 11)

    def test_rect_width(self):
        """Test width"""
        rect4 = Rectangle(3, 5)
        self.assertTrue(rect4.width == 3)
        rect5 = Rectangle(2, 3)
        self.assertFalse(rect5.width == 5)

    def test_rect_height(self):
        """Test height"""
        rect6 = Rectangle(4, 3)
        self.assertEqual(rect6.height, 3)

    def test_rect_x(self):
        """Test x"""
        rect7 = Rectangle(3, 5)
        self.assertTrue(rect7.x == 0)

    def test_rect_y(self):
        """Test y"""
        rect8 = Rectangle(4, 5, 2, 45)
        self.assertEqual(rect8.y, 45)

    def test_validate_width_type(self):
        """Validate width type"""
        with self.assertRaises(TypeError):
            rect9 = Rectangle("2", 4)

    def test_validate_width_value(self):
        """Validate width value"""
        with self.assertRaises(ValueError):
            rect10 = Rectangle(-2, 5)

    def test_validate_height_type(self):
        """Validate height type"""
        with self.assertRaises(TypeError):
            rect11 = Rectangle(7, "8")

    def test_validate_height_value(self):
        """Validate height value"""
        with self.assertRaises(ValueError):
            rect12 = Rectangle(7, -5)

    def test_validate_x_type(self):
        """Validate x type"""
        with self.assertRaises(TypeError):
            rect13 = Rectangle(2, 2, "5")

    def test_validate_x_value(self):
        """Validate x value"""
        with self.assertRaises(ValueError):
            rect14 = Rectangle(3, 3, -1)

    def test_validate_y_type(self):
        """Validate y type"""
        with self.assertRaises(TypeError):
            rect15 = Rectangle(1, 2, 4, "5")

    def test_validate_y_value(self):
        """Validate y value"""
        with self.assertRaises(ValueError):
            rect16 = Rectangle(2, 4, 5, -3)
