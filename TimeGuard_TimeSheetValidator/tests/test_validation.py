import unittest
from src.services.validation_service import validate_timesheet
from src.utils.csv_parser import parse_csv

class TestValidationService(unittest.TestCase):
    def test_validate_timesheet(self):
        timesheet = parse_csv('src/static/sample_timesheet.csv')
        report = validate_timesheet(timesheet)
        self.assertEqual(len(report), 3)  # Expect 3 validated entries
        self.assertTrue(report[0]['isValid'])  # 2025-08-01 should be valid (8 hours)
        self.assertFalse(report[1]['isValid'])  # 2025-08-02 should be invalid (4 hours)
        self.assertEqual(report[1]['discrepancy'], '')  # Should have event but wrong hours

if __name__ == '__main__':
    unittest.main()