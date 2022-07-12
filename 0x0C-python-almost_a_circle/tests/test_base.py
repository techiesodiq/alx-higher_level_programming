
"""
Test differents behaviors of the Base class
"""
import unittest
import pycodestyle
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A class to test Base Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """
        Test for positive Base Class id
        """
        base_instance = Base(110)
        self.assertEqual(base_instance.id, 110)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)

    def test_id_as_negative(self):
        """
        Test for negative Base Class id
        """
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

        # rect_data = re1.to_dictionary()
    def test_id_as_none(self):
        """
        Test for None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base("Ping Pong")
        self.assertEqual(base_instance.id, "Ping Pong")
        base_instance = Base("Tan gozu?")
        self.assertEqual(base_instance.id, "Tan gozu?")

    def test_to_json_string(self):
        """
        Test to_json_string method
        """
        rect_instance = Rectangle(10, 17, 2, 8, 70)
        # json_data = Base.to_json_string([rect_data])
        json_data = Base.to_json_string([rect_instance])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """
        Test for a empty data on to_json_string method
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)

    def test_instance(self):
        """
        self.assertEqual(json_data, "[]")
        Test Base Class instance
        """
        base_instance = Base()

