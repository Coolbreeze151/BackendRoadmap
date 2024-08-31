import unittest
import os

class TestFileIngestion(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.exists("data.csv"), "File does not exist")

    def test_file_not_empty(self):
        self.assertGreater(os.path.getsize("data.csv"), 0, "File is empty")

    def test_file_format(self):
        with open("data.csv", 'r') as file:
            header = file.readline().strip().split(',')
            expected_columns = ["id", "name"]
            self.assertEqual(header, expected_columns, "File format is incorrect")

if __name__ == "__main__":
    unittest.main()