import unittest
import sys

sys.path.append("..")

from src.street_normalizer import normalize_street_suffixes, normalize_unit_designators, normalize_street_abbreviations, remove_extra_chars, cleaner, city_cleaner, name_cleaner


class TestStreetNormalizer(unittest.TestCase):
    def test_normalize_street_suffixes(self):
        input_value = "1800 e keller drive apartment 1500"
        expected_output = "1800 E KELLER DR APARTMENT 1500"
        self.assertEqual(normalize_street_suffixes(input_value), expected_output)

    def test_normalize_unit_designators(self):
        input_value = "1800 e keller drive apartment 1500"
        expected_output = "1800 E KELLER DRIVE APT 1500"
        self.assertEqual(normalize_unit_designators(input_value), expected_output)

    def test_normalize_street_abbreviations(self):
        input_value = "1800 e keller avenida apt 100"
        expected_output = "1800 E KELLER AVE APT 100"
        self.assertEqual(normalize_street_abbreviations(input_value), expected_output)

    def test_remove_extra_chars(self):
        input_value = "THIS.  SHOULD,  BE;THE:ONLY-TEXT~HERE"
        expected_output = "THISSHOULDBETHEONLYTEXTHERE"
        self.assertEqual(remove_extra_chars(input_value), expected_output)

    def test_cleaner(self):
        input_value = "  1800 ~e keller avenida apartment 1300"
        expected_output = "1800 E KELLER AVE APT 1300"
        self.assertEqual(cleaner(input_value), expected_output)

    def test_city_cleaner(self):
        input_value_01 = "madison, wisconsin"
        input_value_02 = "madison, wi"
        input_value_03 = "madison"
        expected_result = "MADISON"
        self.assertEqual(city_cleaner(input_value_01), expected_result)
        self.assertEqual(city_cleaner(input_value_02), expected_result)
        self.assertEqual(city_cleaner(input_value_03), expected_result)

    def test_names(self):
        input_value = "Random Name LLC"
        expected_value = "RANDOM NAME"
        self.assertEqual(name_cleaner(input_value), expected_value)


if __name__ == "__main__":
    unittest.main()
