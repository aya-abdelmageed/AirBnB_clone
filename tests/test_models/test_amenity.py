#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenity1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity1.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity2 = Amenity()
        amenity3 = Amenity()
        self.assertNotEqual(amenity2.id, amenity3.id)

    def test_two_amenities_different_created_at(self):
        amenity2 = Amenity()
        sleep(0.05)
        amenity3 = Amenity()
        self.assertLess(amenity2.created_at, amenity3.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity2 = Amenity()
        sleep(0.05)
        amenity3 = Amenity()
        self.assertLess(amenity2.updated_at, amenity3.updated_at)

    def test_str_representation(self):
        dateTimev = datetime.today()
        dtRepr = repr(dateTimev)
        amenity1 = Amenity()
        amenity1.id = "123456"
        amenity1.created_at = amenity1.updated_at =dateTimev 
        amstr = amenity1.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dtRepr, amstr)
        self.assertIn("'updated_at': " + dtRepr, amstr)

    def test_args_unused(self):
        amenity1 = Amenity(None)
        self.assertNotIn(None, amenity1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dateTimev = datetime.today()
        dt_iso = dateTimev.isoformat()
        amenity1 = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity1.id, "345")
        self.assertEqual(amenity1.created_at, dateTimev)
        self.assertEqual(amenity1.updated_at, dateTimev)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amenity1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity1.updated_at
        amenity1.save()
        self.assertLess(first_updated_at, amenity1.updated_at)

    def test_two_saves(self):
        amenity1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity1.updated_at
        amenity1.save()
        second_updated_at = amenity1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity1.save()
        self.assertLess(second_updated_at, amenity1.updated_at)

    def test_save_with_arg(self):
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            amenity1.save(None)

    def test_save_updates_file(self):
        amenity1 = Amenity()
        amenity1.save()
        amid = "Amenity." + amenity1.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_testCorrect_keys(self):
        amenity1 = Amenity()
        self.assertIn("id", amenity1.to_dict())
        self.assertIn("created_at", amenity1.to_dict())
        self.assertIn("updated_at", amenity1.to_dict())
        self.assertIn("__class__", amenity1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity1 = Amenity()
        amenity1.middle_name = "Holberton"
        amenity1.my_number = 98
        self.assertEqual("Holberton", amenity1.middle_name)
        self.assertIn("my_number", amenity1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity1 = Amenity()
        am_dict = amenity1.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dateTimev = datetime.today()
        amenity1 = Amenity()
        amenity1.id = "123456"
        amenity1.created_at = amenity1.updated_at =dateTimev 
        obj = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dateTimev.isoformat(),
            'updated_at': dateTimev.isoformat(),
        }
        self.assertDictEqual(amenity1.to_dict(), obj)

    def test_contrast_to_dict_dunder_dict(self):
        amenity1 = Amenity()
        self.assertNotEqual(amenity1.to_dict(), amenity1.__dict__)

    def test_to_dict_with_arg(self):
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            amenity1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
