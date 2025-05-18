import unittest
import csv
import json
import os

class TestCSVtoJSON(unittest.TestCase):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(BASE_DIR, 'profiles1.csv')
    json_path = os.path.join(BASE_DIR, 'data.json')

    def test_csv_has_12_columns(self):
        with open(self.csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            self.assertEqual(len(header), 12, "CSV file does not have 12 columns")

    def test_csv_has_more_than_900_rows(self):
        with open(self.csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
            self.assertGreater(len(rows) - 1, 900, "CSV file does not have more than 900 rows")

    def test_json_has_more_than_900_items(self):
        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            self.assertGreater(len(data), 900, "JSON file does not have more than 900 items")

    def test_json_properties_are_complete(self):
        expected_keys = [
            "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
        ]
        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for item in data:
                self.assertEqual(set(item.keys()), set(expected_keys), "JSON item does not have the expected properties")

    def test_simple_addition(self):
        self.assertEqual(1 + 1, 2, "This test is intentionally designed to always pass to verify CI/CD pipeline success handling")

    def test_intentional_fail(self):
        self.assertEqual(1, 2, "This test is intentionally designed to fail to verify CI/CD pipeline failure handling")

if __name__ == '__main__':
    unittest.main()
