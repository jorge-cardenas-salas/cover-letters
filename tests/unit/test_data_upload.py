from unittest import TestCase

from data_uploader.csv_parser import CsvParser


class TestDataUpload(TestCase):
    def test_basic_upload(self):
        parser = CsvParser()
        result = parser.upload("/app/tests/data/sampleUpload.csv")
        self.assertTrue(result)

    def test_partially_correct_data(self):
        with self.assertLogs() as check_log:
            parser = CsvParser()
            result = parser.upload("/app/tests/data/partiallyCorrectUpload.csv")
            self.assertFalse(result)
            log_text = str(check_log.output)
            self.assertIn("Error in Row 1: missing email", log_text)
            self.assertIn("Error in Row 3: skill level must be numeric", log_text)

    def test_invalid_format_data(self):
        with self.assertLogs() as check_log:
            parser = CsvParser()
            result = parser.upload("/app/tests/data/invalidFormatsUpload.csv")
            self.assertFalse(result)
            log_text = str(check_log.output)
            self.assertIn("Model error", log_text)
            self.assertIn("The email address is not valid", log_text)
            self.assertIn("Phone doesn't match expected pattern", log_text)
