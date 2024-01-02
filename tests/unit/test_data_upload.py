from typing import List
from unittest import TestCase
from unittest.mock import patch

from common.database.daos.dao import Dao
from common.database.table_models.table_row_models import UserTableRow
from data_uploader.csv_parser import CsvParser


def mock_dao_return_values() -> List[UserTableRow]:
    usr1 = UserTableRow()
    usr1.id = 1
    usr2 = UserTableRow()
    usr2.id = 2
    return [usr1, usr2]


class TestDataUpload(TestCase):
    @patch.object(Dao, "merge_users", return_value=mock_dao_return_values())
    def test_basic_upload(self, *args):
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

    @patch.object(Dao, "merge_users", return_value=mock_dao_return_values())
    def test_invalid_format_data(self, *args):
        with self.assertLogs() as check_log:
            parser = CsvParser()
            result = parser.upload("/app/tests/data/invalidFormatsUpload.csv")
            self.assertFalse(result)
            log_text = str(check_log.output)
            self.assertIn("Model error", log_text)
            self.assertIn("The email address is not valid", log_text)
            self.assertIn("Phone doesn't match expected pattern", log_text)
