import unittest
from src.utils.csv_parser import parse_csv

class TestCSVParser(unittest.TestCase):
    def test_parse_csv(self):
        result = parse_csv('src/static/sample_timesheet.csv')
        self.assertEqual(len(result), 3)  # Expect 3 entries
        self.assertEqual(result[0]['date'], '2025-08-01')  # Check first entry date
        self.assertEqual(float(result[0]['hours']), 8.0)  # Check first entry hours

if __name__ == '__main__':
    unittest.main()