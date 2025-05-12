import unittest
import csv
import json

class TestCSVtoJSON(unittest.TestCase):

    def test_csv_has_12_columns(self):
        with open('profiles1.csv', 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            self.assertEqual(len(header), 12, "CSV file does not have 12 columns")

    def test_csv_has_more_than_900_rows(self):
        with open('profiles1.csv', 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
            self.assertGreater(len(rows) -1, 900, "CSV file does not have more than 900 rows")

    def test_json_has_more_than_900_items(self):
        with open('data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            self.assertGreater(len(data), 900, "JSON file does not have more than 900 items")

    def test_json_properties_are_complete(self):
        expected_keys = [
            "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
        ]
        with open('data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for item in data:
                self.assertEqual(set(item.keys()), set(expected_keys), "JSON item does not have the expected properties")

    def test_intentional_fail(self):
        self.assertEqual(1, 2, "This test is intentionally designed to fail to verify CI/CD pipeline failure handling")

if __name__ == '__main__':
    unittest.main()